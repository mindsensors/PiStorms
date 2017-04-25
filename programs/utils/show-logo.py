# Displays mindsensors.com logo only using Adafruit libraries.
# If I2c isn't working, this will still be able to display the image (over SPI).

from Adafruit_ILI9341 import ILI9341 as TFT
from Adafruit_GPIO import SPI
import Image

disp = TFT(24, rst=25, spi=SPI.SpiDev(0,0,max_speed_hz=64000000))
disp.display(Image.open("/usr/local/mindsensors/images/ms-logo-w320-h240.png").rotate(90))
