#!/usr/bin/env python
#
# Copyright (c) 2016 mindsensors.com
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
# mindsensors.com invests time and resources providing this open source code,
# please support mindsensors.com  by purchasing products from mindsensors.com!
# Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date          Author          Comments
# March 2016    Roman Bohuk     Initial Authoring
# July 2017     Seth Tenembaum  Update for GRX

import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

import time, socket
from PiStorms_GRX import PiStorms_GRX
psm = PiStorms_GRX()

def checkInternet():
    try:
        socket.setdefaulttimeout(5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except:
        return False

psm.screen.drawAutoText("Testing internet connection", 20, 30, fill=(255,255,255), size=23, display=False)
psm.screen.fillRect(20, 80, 320, 240, fill=(0,0,0), display=False)
psm.screen.fillBmp(110, 110, 100, 100, path=currentdir+'/'+'load.png', display=False)
psm.screen.disp.display()
#time.sleep(1)

c = checkInternet()
color = (0,255,0) if c else (255,0,0)
message1 = "You are connected" if c else "You are not connected"
image = "wifi_green.png" if c else "x_red.png"

psm.screen.clearScreen(display=False)
psm.screen.drawAutoText(message1, 35, 20, fill=color, size=25, display=False)
psm.screen.drawAutoText("to the internet!", 35, 50, fill=color, size=25, display=False)
psm.screen.fillBmp(120, 85, 80, 80, path=currentdir+'/'+image, display=False)

psm.screen.drawButton(35, 170, width=250, height=40, text="Continue", display=False)
psm.screen.disp.display()

psm.untilKeyPressOrTouch(time.sleep, 0.01)
