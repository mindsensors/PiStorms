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
import time

print "running program"

psm = PiStorms()
# Attaching a SumoEyes sensor to Port BAS1
se_sensor = MsDevices.SumoEyes(psm.BAS1)

# Ask the user to connect the sensor to BAS1
question = ["SumoEyes Demo", "Connect SumoEyes sensor to BAS1,",
"and press OK to continue"]
psm.screen.askQuestion(question,["OK"])


psm.screen.termPrintln("SumoEyes readout (from BAS1):")
psm.screen.termPrintln("Press GO to stop the program")
psm.screen.termPrintln(" ")
psm.screen.termPrintln("Tap the screen to switch mode")
psm.screen.termPrintln(" ")

# Current mode
mode = se_sensor.LONG_RANGE
psm.screen.termPrintAt(5,"Mode: LONG_RANGE")

# Main loop
exit = False
while not exit:
    psm.screen.termPrintAt(6, "SumoEyes: " + se_sensor.detectObstactleZone(True))
    # Code to change the mode
    if psm.screen.checkButton(0, 0, 320, 320):
        if mode == se_sensor.LONG_RANGE:
            mode = se_sensor.SHORT_RANGE
            psm.screen.termPrintAt(5, "Mode: SHORT_RANGE")
        else:
            mode = se_sensor.LONG_RANGE
            psm.screen.termPrintAt(5, "Mode: LONG_RANGE")
        se_sensor.setRange(mode)
    
    # Code to exit the program
    if psm.isKeyPressed():
        psm.screen.termPrintAt(8, "Exiting program")
        exit = True
        
