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
# 04/21/17   Seth Tenembaum  Initial development.
#

import os, time
from mindsensorsUI import mindsensorsUI
from mindsensors_i2c import mindsensors_i2c
from PiStormsCom import PiStormsCom
from PiStormsCom import PSSensor


s = mindsensorsUI() # screen
psc = PiStormsCom()
i2c = mindsensors_i2c(0x22 >> 1)

PSSensor(psc.bankA, 1).activateCustomSensorI2C()

s.drawDisplay("ABSIMU Calibration")

s.termGotoLine(0)
s.termPrintln("Beginning AbsoluteIMU compass")
s.termPrintln("calibration program.")
s.termPrintln("")
s.termPrintln("Connect AbsoluteIMU-ACG")
s.termPrintln("to BAS1.")
s.termPrintln("")
s.termReplaceLastLine("Press GO to begin.")

startKeyPressCount = psc.getKeyPressCount()
while psc.getKeyPressCount() == startKeyPressCount: time.sleep(0.1)

i2c.writeByte(psc.PS_Command, ord('C'))


s.clearScreen()
s.dumpTerminal()
s.termGotoLine(0)
s.termPrintln("Calibrating...")
s.termPrintln("Turn 360 degrees")
s.termPrintln("along all 3 axes.")
s.termPrintln("")
s.termReplaceLastLine("Then press GO to end.")

startKeyPressCount = psc.getKeyPressCount()
while psc.getKeyPressCount() == startKeyPressCount: time.sleep(0.1)

i2c.writeByte(psc.PS_Command, ord('c'))

