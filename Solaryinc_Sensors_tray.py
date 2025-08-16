#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GLib
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

# URL du serveur local
URL = "http://127.0.0.1:27003/"
# Identifiant de l'indicateur
APPINDICATOR_ID = 'Solaryinc_Temp'
# Chemin vers l'icône dans un dossier système
ICON_PATH = '/opt/solaryinc_sensors/solaryinc_icon.png'

# Liste des capteurs à surveiller
SENSOR_IDS = {
    "CPU": "cpu_temp",
    "GPU": "gpu_temp_0",
    "M480": "storage_temp-hwmon1",
    "WD": "storage_temp-hwmon2"
}

def get_temperatures():
    """Récupère les températures depuis le serveur local"""
    try:
        r = requests.get(URL, timeout=2)
        soup = BeautifulSoup(r.text, "html.parser")
        temps = {}
        for label, sensor_id in SENSOR_IDS.items():
            element = soup.find(id=sensor_id)
            temps[label] = element.text.strip() if element else "N/A"
        return temps
    except Exception as e:
        return {"Erreur": str(e)}

def create_menu():
    """Crée le menu avec un item pour chaque température et un pour quitter"""
    menu = Gtk.Menu()
    menu_items = []

    for label in SENSOR_IDS.keys():
        item = Gtk.MenuItem(label=f"{label}: ...")
        item.set_sensitive(False)  # pas cliquable
        item.show()
        menu.append(item)
        menu_items.append(item)

    quit_item = Gtk.MenuItem(label="Quitter")
    quit_item.connect("activate", lambda _: Gtk.main_quit())
    quit_item.show()
    menu.append(quit_item)

    return menu, menu_items

def update_menu(indicator, menu_items):
    """Met à jour les libellés du menu avec les températures"""
    temps = get_temperatures()
    for key, item in zip(temps.keys(), menu_items):
        item.set_label(f"{key}: {temps[key]}")
    # Mettre à jour le label de l'indicateur (texte à côté de l'icône)
    indicator.set_label("TEMP", "")
    return True  # continue le timer

def main():
    indicator = AppIndicator3.Indicator.new(
        APPINDICATOR_ID,
        ICON_PATH,
        AppIndicator3.IndicatorCategory.SYSTEM_SERVICES
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    indicator.set_title("Solaryinc_Temp")

    menu, menu_items = create_menu()
    indicator.set_menu(menu)

    GLib.timeout_add_seconds(5, update_menu, indicator, menu_items)

    Gtk.main()

if __name__ == "__main__":
    main()
