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
# Date      Author      Comments
# 04/18/16   Deepak     Initial development.
#

from PiStorms import PiStorms
import LegoDevices
psm = PiStorms()

m = ["EV3TouchSensor-Demo", "Connect EV3 Touch sensor",
 "to BAS1, and Press OK to continue"]
psm.screen.askQuestion(m,["OK"])

#
# we are attaching a TouchSensor to Port BAS1
# Initialize the variable for the sensor
#
# touchSensor = LegoDevices.NXTTouchSensor("BAS1")
touchSensor = LegoDevices.EV3TouchSensor("BAS1")

doExit = False
old_touch = True
touch = True

old_touch_count = 0
touch_count = 0

psm.screen.termPrintAt(7, "Touch screen to reset Count")
psm.screen.termPrintAt(8, "Press GO to stop program")
#main loop
while(not doExit):
    #save the previous touch value
    old_touch = touch
    #
    # read from NXT Touch Sensor
    #
    touch = touchSensor.isPressed()

    #
    # Also count the number of times it was touched.
    #
    old_touch_count = touch_count
    touch_count = touchSensor.getBumpCount()

    # print value only if it was changed.
    if (old_touch != touch) or (old_touch_count != touch_count):
        msg = "Sensor Touched:  " + str(touch)
        msg2 = "Touch Count: " + str(touch_count)

        psm.screen.termPrintAt(2, "")
        psm.screen.termPrintAt(3, msg)
        psm.screen.termPrintAt(4, msg2)


    elif(psm.screen.isTouched()):
        #
        # check if screen touched.
        #
        # if scren was touched, reset BAS1 touch count
        touchSensor.resetBumpCount()


    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintAt(8, "Exiting to menu")
        doExit = True
