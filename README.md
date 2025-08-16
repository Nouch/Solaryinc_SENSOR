# Solaryinc_SENSOR

A lightweight Linux tray application displaying system sensor temperatures using OpenLinkHub and its tray. Updates every 5 seconds from a local server.

## Features

- Shows CPU, GPU, and storage temperatures in a tray icon
- Automatic updates every 5 seconds
- Works with OpenLinkHub and its tray
- Minimal dependencies

## Requirements

- Python 3
- Pip packages (install in a virtual environment):

```bash
pip install requests beautifulsoup4 pillow
```
    GTK 3 and AppIndicator3 (Linux)

Installation

    Clone this repository:
```bash
git clone https://github.com/yourusername/Solaryinc_Sensors.git
```
    Move it to a system-wide folder (requires sudo):
```bash
sudo mv Solaryinc_Sensors /opt/solaryinc_sensors
cd /opt/solaryinc_sensors
```
    Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
    Make sure your ICON_PATH in the script points to /opt/solaryinc_sensors/solaryinc_icon.png.

    Test the script:
```bash
./venv/bin/python Solaryinc_Sensors_tray.py
```
Systemd Service (Auto-start)

    Create a service file /etc/systemd/system/solaryinc_sensors.service:

```ini
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

Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable solaryinc_sensors.service
sudo systemctl start solaryinc_sensors.service
```
Check status:

systemctl status solaryinc_sensors.service
