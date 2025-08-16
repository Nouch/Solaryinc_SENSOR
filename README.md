# Solaryinc_SENSOR

A lightweight Linux tray application displaying system sensor temperatures using **[OpenLinkHub](https://github.com/jurkovic-nikola/OpenLinkHub)** and its **[tray](https://github.com/jurkovic-nikola/openlinkhub-tray)**. Updates every 5 seconds from a local server.

## Features

- Shows CPU, GPU, and storage temperatures in a tray icon
- Automatic updates every 5 seconds
- Works with **OpenLinkHub** and its tray
- Minimal dependencies

## Requirements

- Python 3
- Pip packages (install in a virtual environment):
  ```bash
  pip install requests beautifulsoup4 pillow

    GTK 3 and AppIndicator3 (Linux)

Installation

    Clone this repository:

git clone https://github.com/yourusername/Solaryinc_Sensors.git
cd Solaryinc_Sensors

Create a virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Make sure your ICON_PATH in the script points to your icon file.

Test the script:

    ./venv/bin/python Solaryinc_Sensors_tray.py

Systemd Service (Auto-start)

    Create a service file /etc/systemd/system/solaryinc_sensors.service:

```ini
[Unit]
Description=Solaryinc Sensors Tray
After=network.target

[Service]
Type=simple
User=nouch
ExecStart=/home/nouch/Ubuntu_APP/venv/bin/python /home/nouch/Ubuntu_APP/Solaryinc_Sensors_tray.py
Restart=on-failure

[Install]
WantedBy=default.target
```

Enable and start the service:

sudo systemctl daemon-reload
sudo systemctl enable solaryinc_sensors.service
sudo systemctl start solaryinc_sensors.service

Check status:

systemctl status solaryinc_sensors.service
