#!/bin/bash

apt-get install -y python3-dev

# Copy the files to the correct location
mkdir /usr/local/bin/rpi-oled-ip-display
cp display_ip.py /usr/local/bin/rpi-oled-ip-display/
cp display_ip.sh /usr/local/bin/rpi-oled-ip-display/

pushd /usr/local/bin/rpi-oled-ip-display
# Create the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Make script executable
chmod +x display_ip.sh

# Set permissions on the files
chmod 744 display_ip.py
chmod 744 display_ip.sh
popd

# Ensure all requirements are installed
pip install -r requirements.txt

# exit the virtual environment
deactivate

# Copy the service file to the correct location and set permissions
cp rpi-oled-ip-display.service /etc/systemd/system/
chmod 664 /etc/systemd/system/rpi-oled-ip-display.service

# Reload the daemons and Enable the service
systemctl daemon-reload
systemctl enable rpi-oled-ip-display.service
