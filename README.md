# OLED IP Display for Raspberry Pi

Simple project to show the IP of a Raspberry Pi on an OLED screen (SSD1306).

## Setup / Installation

Ensure I2C is enabled on the Raspberry Pi. This can be done through the `raspi-config` tool, and it can be enabled with a command that's included in the block below.

Wire up your OLED display to the I2C pins on the Raspberry Pi. The default pins are GPIO 2 (pin 3)(SDA) and GPIO 3 (pin 5)(SCL), and power to Pin1 for 3v3 and pin 9 for ground. [See this diagram for pinout https://pinout.xyz/pinout/i2c](https://pinout.xyz/pinout/i2c)

Then run the following commands:

```bash
# Ensure Git is installed
sudo apt-get install git

# Clone Repo
git clone https://github.com/boristsr/rpi-oled-ip-display
cd rpi-oled-ip-display

# Ensure Python3 is installed
sudo apt-get install python3-pip python3

# Enable I2C
sudo raspi-config nonint do_i2c 0

# Run Setup Script
chmod +x setup.sh
sudo ./setup.sh

# Finally, Reboot RPi
sudo reboot
```
