# Solaryinc_SENSOR
<img width="393" height="252" alt="image" src="https://github.com/user-attachments/assets/7ba6656a-436a-4368-b807-47c5a0dc1cf3" />

Solaryinc_SENSOR est une application légère pour Linux qui affiche les températures des capteurs système (CPU, GPU, stockage) dans la barre de notification (tray).  
Elle utilise [OpenLinkHub](https://github.com/jurkovic-nikola/OpenLinkHub) pour récupérer les données et met à jour toutes les 5 secondes.  
Compatible avec le [OpenLinkHubtray](https://github.com/jurkovic-nikola/openlinkhub-tray).

---

## 🚀 Fonctionnalités

- Affiche les températures CPU, GPU et stockage dans la barre de notification
- Mise à jour automatique toutes les 5 secondes

---

## 🛠️ Prérequis

- **Python 3**
- Paquets système Linux : GTK 3 et AppIndicator3  
  *(exemple pour Debian/Ubuntu :)*

```bash
sudo apt install libgtk-3-dev gir1.2-appindicator3-0.1 python3-venv python3-pip
```

Paquets Python (via pip) :

```bash
pip install requests beautifulsoup4 pillow
```

---

## 💾 Installation

Cloner le dépôt :

```bash
git clone https://github.com/yourusername/Solaryinc_Sensors.git
```

Déplacer le dossier dans un emplacement système (requiert sudo) :

```bash
sudo mv Solaryinc_Sensors /opt/solaryinc_sensors
cd /opt/solaryinc_sensors
```

Créer un environnement virtuel Python et installer les dépendances :

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Vérifier que ICON_PATH dans le script pointe vers :

```bash
/opt/solaryinc_sensors/solaryinc_icon.png
```

Tester le script :

```bash
./venv/bin/python Solaryinc_Sensors_tray.py
```

---

## ⚙️ Auto-démarrage avec systemd

Créer le fichier de service :

```bash
sudo nano /etc/systemd/system/solaryinc_sensors.service
```

Coller le contenu suivant dans le fichier :

```bash
[Unit]
Description=Solaryinc Sensors Tray
After=network.target

[Service]
Type=simple
ExecStart=/opt/solaryinc_sensors/venv/bin/python /opt/solaryinc_sensors/Solaryinc_Sensors_tray.py
Restart=on-failure

[Install]
WantedBy=default.target
```

Activer et démarrer le service :

```bash
sudo systemctl daemon-reload
sudo systemctl enable solaryinc_sensors.service
sudo systemctl start solaryinc_sensors.service
```

Vérifier le statut :

```bash
systemctl status solaryinc_sensors.service
```

---

## 🔧 Débogage

Si l’icône ne s’affiche pas ou si le service ne démarre pas, vérifier les logs :

```bash
journalctl -u solaryinc_sensors.service -f
```
