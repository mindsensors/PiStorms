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

m = ["NXTLightSensor-Demo", "Connect NXT Light sensor to BAS1",
 "and Press OK to continue.",
 "Then move sensor at different lights",
 "",
 "Press Go to terminate"]
psm.screen.askQuestion(m,["OK"])

doExit = False
old_lightValue = True
lightValue = True
reflectiveMode = True

#main loop
while(not doExit):
    #save the previous value
    old_lightValue = lightValue
    #
    # read from NXT Light Sensor
    #
    lightValue = psm.BAS1.lightSensorNXT(reflectiveMode)

    if ( reflectiveMode == True ):
        msg2 = " (reflective)"
    else:
        msg2 = " (ambient)"

    msg = "Light Value:  " + str(lightValue) + msg2

    # print value only if it was changed.
    if (old_lightValue != lightValue):
        psm.screen.clearScreen()
        psm.screen.drawAutoText(msg, 15, 164, fill=(255, 255, 255), size = 18)
        psm.screen.drawAutoText("Touch screen to change mode", 15, 182, fill=(255, 255, 255), size = 18)
        psm.screen.drawAutoText("  between ambient/reflected", 15, 200, fill=(255, 255, 255), size = 18)

    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        doExit = True

    #
    # check if screen touched.
    #
    if(psm.screen.isTouched()):
        # if scren was touched,
        if ( reflectiveMode == False):
            reflectiveMode = True
        else:
            reflectiveMode = False
