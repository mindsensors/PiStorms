#!/usr/bin/env python
#
# Copyright (c) 2017 mindsensors.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code,
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/

# Displays mindsensors.com logo only using Adafruit libraries.
# If I2c isn't working, this will still be able to display the image (over SPI).

from Adafruit_ILI9341 import ILI9341 as TFT
from Adafruit_GPIO import SPI
import Image

disp = TFT(24, rst=25, spi=SPI.SpiDev(0,0,max_speed_hz=64000000))
disp.display(Image.open("/usr/local/mindsensors/images/ms-logo-w320-h240.png").rotate(90))
