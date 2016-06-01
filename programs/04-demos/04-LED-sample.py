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
# July 2015  Henry     Initial Authoring from SensorShield import SensorShield

import os,sys,inspect,time,thread

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms
print "running program"
psm = PiStorms()

m = ["LED-sample", "This feature is not yet",
 "implemented on the PiStorms.",
 "   ",
 "Click OK to exit."]
psm.screen.askQuestion(m,["OK"])

#psm.screen.termPrintln("LED blinking program")
#psm.screen.termPrintln("Hold screen to exit")

d1 = 0.1
d2 = 0.1
exit = False
psm.screen.termPrintAt(8, "Press Go button to exit")
oldKeyPressCount = psm.getKeyPressCount()
while(not exit):
    
    psm.led(2,0,255,0)
    time.sleep(d1)
    psm.led(1,0,255,0)
    time.sleep(d2)
    psm.led(2,255,0,0)
    time.sleep(d1)
    psm.led(1,255,0,0)
    time.sleep(d2)
    psm.led(2,0,0,255)
    time.sleep(d1)
    psm.led(1,0,0,255)
    time.sleep(d2)

    newKeyPressCount = psm.getKeyPressCount()
    if ( newKeyPressCount > oldKeyPressCount ):
        psm.screen.termPrintln("")
        psm.screen.termPrintAt(8, "Exiting to menu")
        time.sleep(1)
        psm.led(1,0,0,0)
        psm.led(2,0,0,0)
        time.sleep(1)
        exit = True
        
