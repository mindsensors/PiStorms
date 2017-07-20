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


import os,sys,inspect,time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PiStorms import PiStorms

psm = PiStorms()
psm.screen.termPrintAt(2, "PiStorms ")
psm.screen.termPrintAt(3, "GO button test:")

print "Running Button Test"
print "press anywhere in PiStorms Screen to exit"
psm.screen.termPrintAt(8, "Touch Display to Exit")
psm.screen.termPrintln(" ")

def mainLoop()
    psm.screen.termPrintAt(5, "GO Button is = " +str(psm.isKeyPressed()))
    psm.screen.termPrintAt(6, "Press Count = " +str(psm.getKeyPressCount()))

psm.untilKeyPress(mainLoop)

psm.screen.termPrintln(" ")
psm.screen.termPrintln("Exiting .....")
