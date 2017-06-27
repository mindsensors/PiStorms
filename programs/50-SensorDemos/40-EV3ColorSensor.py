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
# Date       Author      Comments
# 07/11/16   Yug Rao     Initial development.
#
import time
from LegoDevices import *
from PiStorms import PiStorms
psm = PiStorms()

m = ["EV3ColorSensor-Demo", "Connect EV3 Color sensor to BAS1",
 "and Press OK to continue.",
 "Then move colored objects in front",
 "of Color sensor"]
psm.screen.askQuestion(m,["OK"])

doExit = False
oldValue = True
value = True
count = 0
#
# Instantiate EV3 color sensor object
#
colorSensor = EV3ColorSensor("BAS1")
psm.screen.termPrintAt(7, "Touch screen to change mode")
psm.screen.termPrintAt(8, "between reflected/ambient/color")
psm.screen.termPrintAt(9, "Press Go to stop program")
change = 1
while(not doExit):
    oldValue = value
    if change == 1: #setMode only if the screen mode changed
        mode = "Light Value"
        unit = ""
        if (count == 0):
            colorSensor.setMode(PS_SENSOR_MODE_EV3_COLOR_REFLECTED)
            unit = "(reflected)"
        elif (count == 1):
            colorSensor.setMode(PS_SENSOR_MODE_EV3_COLOR_AMBIENT)
            unit = "(ambient)"
        elif (count == 2):
            colorSensor.setMode(PS_SENSOR_MODE_EV3_COLOR_COLOR)
            mode = "Color"
        time.sleep(.2)
    else:
        value = colorSensor.getValue()
        if (count == 2): #Convert number color output to correspond to its color word
            colors = ["None", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
            value = colors[value]
        msg = mode+":  " + str(value)+" "+unit


    if (oldValue != value):
        psm.screen.termPrintAt(4, msg)
    if(psm.isKeyPressed() == True):
        psm.screen.clearScreen()
        colorSensor = EV3ColorSensor("BAS1", 9) #Turn off detecting
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        doExit = True
    change = 0
    if(psm.screen.isTouched()): #Change mode if screen is tapped
        count = count + 1
        if ( count > 2):
            count = 0
        psm.screen.termPrintAt(4, "Switching...")
        change = 1
        time.sleep(.5)
