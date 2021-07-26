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
psm = PiStorms()

m = ["NXTTouchSensor-Demo", "Connect NXT Touch sensor",
 "to BAS1, and Press OK to continue"]
psm.screen.askQuestion(m,["OK"])

doExit = False
old_touch = True
touch = True

old_touch_count = 0
touch_count = 0

#main loop
while(not doExit):
    #save the previous touch value
    old_touch = touch
    #
    # read from NXT Touch Sensor
    #
    touch = psm.BAS1.isTouchedNXT()

    #
    # Also count the number of times it was touched.
    #
    old_touch_count = touch_count
    touch_count = psm.BAS1.numTouchesNXT()

    # print value only if it was changed.
    if (old_touch != touch) or (old_touch_count != touch_count):
        msg = "Sensor Touched:  " + str(touch)
        msg2 = "Touch Count: " + str(touch_count)

        psm.screen.termPrintAt(2, "")
        psm.screen.termPrintAt(3, msg)
        psm.screen.termPrintAt(4, msg2)

        psm.screen.termPrintAt(7, "Touch screen to reset Count")
        psm.screen.termPrintAt(8, "Press GO to stop program")

    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintAt(8, "Exiting to menu")
        doExit = True

    #
    # check if screen touched.
    #
    if(psm.screen.isTouched()):
        # if scren was touched,
        # reset BAS1 touch count
        psm.BAS1.resetTouchesNXT()
