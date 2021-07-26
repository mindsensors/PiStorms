#!/usr/bin/env python3
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
psm = PiStorms()

m = ["EV3Ultrasonic-Demo", "Connect EV3 Ultrasonic sensor",
 "to BAS1, and Press OK to continue"]
psm.screen.askQuestion(m,["OK"])

doExit = False
oldValue = True
value = True
count = 0
#
# Instantiate ultrasonic object
#
ultrasonic = EV3UltrasonicSensor("BAS1")
psm.screen.termPrintAt(7, "Touch screen to change mode")
psm.screen.termPrintAt(8, "between Dist IN/ Dist CM/ Detect")
psm.screen.termPrintAt(9, "Press Go to stop program")
change = 1

while(not doExit):
    oldValue = value
    if change == 1: #setMode only if the screen mode changed
        mode = "Distance"
        unit = ""
        if (count == 0):
            ultrasonic.setMode(PS_SENSOR_MODE_EV3_ULTRASONIC_DIST_IN)
            unit = "in"
        elif (count == 1):
            ultrasonic.setMode(PS_SENSOR_MODE_EV3_ULTRASONIC_DIST_CM)
            unit = "cm"
        elif (count == 2):
            ultrasonic.setMode(PS_SENSOR_MODE_EV3_ULTRASONIC_DETECT)
            mode = "Detect"
        time.sleep(.2)
    else:
        if ((count==0)or(count==1)):
            value = ultrasonic.getDistance()
            value = float(value)/10
            if (value == 100.3)or(value == 255):
                value = "---"
        else:
            value = ultrasonic.detect()
        msg = mode + ":  " + str(value)+" "+unit


    if (oldValue != value):
        psm.screen.termPrintAt(4, msg)
    if(psm.isKeyPressed() == True):
        psm.screen.clearScreen()
        ultrasonic = EV3UltrasonicSensor("BAS1", 9) #Turn off detecting
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
