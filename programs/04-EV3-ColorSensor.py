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
# Date      Author      Comments
# 04/18/16   Deepak     Initial development.
#

from PiStorms import PiStorms
print "running program"
psm = PiStorms()

m = ["EV3ColorSensor-Demo", "Connect EV3 Color sensor to BAS1",
 "and Press OK to continue.", 
 "Then move colored objects in front",
 "of Color sensor"]
psm.screen.askQuestion(m,["OK"])

doExit = False
old_colorValue = True
colorValue = True
ambientMode = False

#main loop
while(not doExit):
    #save the previous value
    old_colorValue = colorValue
    #
    # read from EV3 Color Sensor
    #
    if ( ambientMode == True):
        colorValue = psm.BAS1.ambientLightSensorEV3()
        msg = "Color Seen:  " + str(colorValue) + " (ambient)"
    else:
        colorValue = psm.BAS1.colorSensorEV3()
        msg = "Color Seen:  " + str(colorValue) + " (reflected)"

    # print value only if it was changed.
    if (old_colorValue != colorValue):
        psm.screen.clearScreen()
        psm.screen.drawAutoText(msg, 15, 164, fill=(255, 255, 255), size = 18) 
        psm.screen.drawAutoText("Touch screen to change mode", 15, 182, fill=(255, 255, 255), size = 18) 
        psm.screen.drawAutoText("between ambient/reflected", 15, 200, fill=(255, 255, 255), size = 18) 
        psm.screen.drawAutoText("Press Go to stop program", 15, 218, fill=(255, 255, 255), size = 18) 
    
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        doExit = True 

    #
    # check if screen touched.
    #
    if(psm.screen.checkButton(0,0,320,320)):
        # if scren was touched, 
        # reset BAS1 touch count
        if ( ambientMode == False):
            ambientMode = True
        else:
            ambientMode = False


