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
#mindsensors.com invests time and resources providing this open source code,
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date       Author          Comments
# 01/02/17   Roman Bohuk     Initial development.
#

from PiStorms import PiStorms
import MsDevices
import os, inspect
import time


psm = PiStorms()
# Attaching a SumoEyes sensor to Port BAS1
se_sensor = MsDevices.SumoEyes(psm.BAS1)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Ask the user to connect the sensor to BAS1
m = ["SumoEyes Demo", "Connect SumoEyes sensor to BAS1,",
"and press OK to continue, then"," ",
"Press GO to stop the program", "Tap the screen to switch mode"]
psm.screen.showMessage(m)


x = 10
y = 10
w = 250
h = 181
psm.screen.fillBmp(x,y,w,h, path=currentdir+'/'+'SumoEyes-view-None.png', display = True)

# Current mode
mode = se_sensor.LONG_RANGE
psm.screen.termPrintAt(8,"Mode: LONG_RANGE")
psm.screen.termPrintAt(9,"Press GO to stop")

def mainLoop():
    #psm.screen.termPrintAt(6, "SumoEyes: " + se_sensor.detectObstactleZone(True))
    z = se_sensor.detectObstactleZone(True)
    psm.screen.fillBmp(x,y,w,h, path=currentdir+'/'+'SumoEyes-view-'+z+'.png', display = True)
    # Code to change the mode
    if psm.screen.checkButton(0, 0, 320, 320):
        if mode == se_sensor.LONG_RANGE:
            mode = se_sensor.SHORT_RANGE
            psm.screen.termPrintAt(8, "Mode: SHORT_RANGE")
        else:
            mode = se_sensor.LONG_RANGE
            psm.screen.termPrintAt(8, "Mode: LONG_RANGE")
        se_sensor.setRange(mode)

psm.untilKeyPress(mainLoop)
psm.screen.termPrintAt(9, "Exiting program")
