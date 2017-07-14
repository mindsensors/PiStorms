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
from PiStorms import PiStorms
from LegoDevices import *
import time
psm = PiStorms()

m = ["EV3InfraredSensor-Demo", "Connect EV3 IR sensor",
 "to BAS1, and Press OK to continue"]
psm.screen.showMessage(m)

oldValue = True
value = True
count = 0
#
# Instantiate IR object
#
IR = EV3InfraredSensor("BAS1")
psm.screen.termPrintAt(7, "Touch screen to change mode")
psm.screen.termPrintAt(8, "Press Go to stop program")
change = 1


def mainLoop():
    oldValue = value
    if change == 1: #setMode only if the screen mode changed
        msg0 = ""
        if (count == 0):
            IR.setMode(PS_SENSOR_MODE_EV3_IR_PROXIMITY)
            mode = "Proximity"
        elif (count == 1):
            IR.setMode(PS_SENSOR_MODE_EV3_IR_CHANNEL)
        elif (count == 2):
            IR.setMode(PS_SENSOR_MODE_EV3_IR_REMOTE)
            mode = "Remote"
        time.sleep(.2)
    else:
        if (count == 0):
            value = IR.readProximity()
        elif (count == 1):
            psm.screen.termPrintAt(2, "Remember to switch to Channel 1")
            value = IR.readChannelHeading(1)
            mode = "Heading"
            msg0 = mode+":  " + str(value)
            value = IR.readChannelProximity(1)
            mode = "Proximity"
        elif (count == 2):
            psm.screen.termPrintAt(2, "Remember to switch to Channel 1")
            value = IR.readRemote(1)
            #Output is in array (L, R), where L is the left stick and R is the right stick
            #1 is up, 0 is nothing, and -1 is down

        msg = mode+":  " + str(value)

    if (oldValue != value):
        psm.screen.termPrintAt(3, msg0)
        psm.screen.termPrintAt(4, msg)
    change = 0
    if(psm.screen.isTouched()): #Change mode if screen is tapped
        count = count + 1
        if ( count > 2):
            count = 0
        psm.screen.clearScreen()
        psm.screen.termPrintAt(4, "Switching...")
        psm.screen.termPrintAt(7, "Touch screen to change mode")
        psm.screen.termPrintAt(8, "Press Go to stop program")
        change = 1
        time.sleep(.5)

psm.untilKeyPress(mainLoop)

psm.screen.clearScreen()
IR = EV3InfraredSensor("BAS1", 9) #Turn off detecting
psm.screen.termPrintln("")
psm.screen.termPrintln("Exiting to menu")
