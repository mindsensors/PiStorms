#!/usr/bin/env python
#
# Copyright (c) 2015 mindsensors.com
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
#
# History:
# Date        Author      Comments
#  04-12-16   Deepak      Troubleshooting program

import time
import Image
import ImageDraw
import ImageFont
import Adafruit_ILI9341 as TFT
import Adafruit_GPIO.SPI as SPI

print "Beginning PiStorms screen test"
disp = TFT.ILI9341(24, rst=25, spi=SPI.SpiDev(0,0,max_speed_hz=64000000))
disp.begin()
disp.clear()

image = disp.buffer
text = "PiStorms screen test"
fill = (255,255,255)
angle = 90
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 20)
draw = ImageDraw.Draw(image)
width, height = draw.textsize(text, font=font)
textimage = Image.new('RGBA', (width, height), (0,0,0,0))
textdraw = ImageDraw.Draw(textimage)
textdraw.text((0,0), text, font=font, fill=fill)
rotated = textimage.rotate(angle, expand=1)
position = (120,100)
image.paste(rotated, position, rotated)
disp.display()
time.sleep(2)

print "Exiting PiStorms screen test"
