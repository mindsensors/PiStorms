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

from PiStorms import PiStorms
import time
from mindsensors import EV3SensAdapt

psm = PiStorms()

m = ["EV3 SensorMux demo", "Connect EV3 Sensor Mux to BAS1",
 "and attach a EV3 Touch Sensor",
 "to channel C1 of your Mux",
 "and Press OK to continue"]
psm.screen.askQuestion(m,["OK"])

# the Mux is an i2c device, so activate the i2c line on that port.
psm.BAS1.activateCustomSensorI2C()


# create our mux object for Channel C1
#Channel addresses as follows:
#Channel 1: 0xA0
#Channel 2: 0xA2
#Channel 3: 0xA4
muxC1=EV3SensAdapt(0xA0)

doExit = False
psm.screen.termPrintAt(8, "Press GO button to exit")
while (not doExit):
    try:
        # check for touch
        x = muxC1.isTouchedEV3()
        psm.screen.termPrintAt(6,"Touch value: "+ str(x))
    except:
        #
        # error could happen if the mux is missing
        #
        psm.screen.termPrintAt(6,"read error")

    time.sleep(.1)    
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintAt(6, "Exiting to menu")
        time.sleep(0.2) 
        doExit = True 
