import time
import datetime
import signal
import sys

import board
import busio

from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)


import socket
def get_ip():
    # From here: https://stackoverflow.com/a/28950776
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


print(get_ip())

keep_updating = True

def interrupt_handler(signum, frame):
    global keep_updating
    print(f'Handling signal {signum} ({signal.Signals(signum).name}).')

    keep_updating = False

    oled.fill(0)
    #oled.show()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw the current time
    time_string = datetime.datetime.now().strftime("%I:%M%p")

    # Load default font.
    font = ImageFont.load_default()

    draw.text(
        (0,0),
        time_string,
        font=font,
        fill=255,
    )

    status_string = "Shutting Down...."

    draw.text(
        (0,20),
        status_string,
        font=font,
        fill=255,
    )

    oled.image(image)
    oled.show()


    # do whatever...
    #time.sleep(1)
    #sys.exit(0)



def display_loop():
    global keep_updating
    while keep_updating:
        # Clear display.
        oled.fill(0)
        #oled.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (oled.width, oled.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw the current time
        time_string = datetime.datetime.now().strftime("%I:%M%p")

        # Load default font.
        font = ImageFont.load_default()

        draw.text(
            (0,0),
            time_string,
            font=font,
            fill=255,
        )

        draw.text(
            (0,20),
            get_ip(),
            font=font,
            fill=255,
        )

        oled.image(image)
        oled.show()

        time.sleep(1)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, interrupt_handler)
    signal.signal(signal.SIGTERM, interrupt_handler)

    display_loop()

    time.sleep(2)