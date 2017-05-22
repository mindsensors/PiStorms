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
# 04/18/16  Deepak      Initial development.
# 05/10/16  Michael     Support for 3 modes 
#


import time
from PiStorms import PiStorms
psm = PiStorms()

m = ["EV3ColorSensor-Demo", "Connect EV3 Color sensor to BAS1",
 "and Press OK to continue.", 
 "Then move colored objects in front",
 "of Color sensor"]
psm.screen.askQuestion(m,["OK"])

doExit = False
old_colorValue = True
colorValue = True
count = 0

#main loop
while(not doExit):
    #save the previous value
    old_colorValue = colorValue
    #
    # read from EV3 Color Sensor
    #
    if (count == 1):
        colorValue = psm.BAS1.ambientLightSensorEV3()
        msg = "Light Seen:  " + str(colorValue) + " (ambient)"
    elif (count == 0):
        colorValue = psm.BAS1.reflectedLightSensorEV3()
        msg = "Light Seen:  " + str(colorValue) + " (reflected)"
    else:   
        colorValue = psm.BAS1.colorSensorEV3()
        msg = "Color Seen:  " + str(colorValue) + " (color)"

    # print value only if it was changed.
    if (old_colorValue != colorValue):
        psm.screen.clearScreen()
        psm.screen.drawAutoText(msg, 15, 164, fill=(255, 255, 255), size = 18) 
        psm.screen.drawAutoText("Touch screen to change mode", 15, 182, fill=(255, 255, 255), size = 18) 
        psm.screen.drawAutoText("between reflected/ambient/color", 15, 200, fill=(255, 255, 255), size = 18) 
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
        # if screen was touched, 
        # reset BAS1 touch count
        count = count + 1
        if ( count > 2):
            count = 0
        time.sleep(.5)
