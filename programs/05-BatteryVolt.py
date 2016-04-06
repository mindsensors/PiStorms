#!/usr/bin/env python
#
# Copyright (c) 2015 mindsensors.com
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
#  July 2015  Henry     Initial Authoring from SensorShield import SensorShield

import os,sys,inspect,time,thread

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms
print "running program"
psm = PiStorms()

psm.screen.termPrintln("Battery Voltage")
psm.screen.termPrintln(" ")

psm.BBS1.resetTouchesEV3()
exit = False
lastled = 0
while(not exit):
    voltVal = psm.battVoltage()
    psm.screen.termReplaceLastLine(str(voltVal) + "V")
	
    if(voltVal >= 8and lastled != 1):
        psm.led(1,0,255,0)
        psm.led(2,0,255,0)
        lastled = 1
    if(voltVal < 8 and voltVal > 6 and lastled != 2):
        psm.led(1,0,255,0)
        psm.led(2,0,255,0)
        lastled = 2
    if(voltVal <= 6 and lastled != 3):
        psm.led(1,255,0,0)
        psm.led(2,255,0,0)
        lastled = 3
    if(psm.screen.checkButton(0,0,320,320)):
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        psm.led(1,0,0,0)
        psm.led(2,0,0,0)
        exit = True
		