#!/usr/bin/env python
#
# Copyright (c) 2016 mindsensorpsm.screen.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more detailpsm.screen.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensorpsm.screen.com invests time and resources providing this open source code, 
#please support mindsensorpsm.screen.com  by purchasing products from mindsensorpsm.screen.com!
#Learn more product option visit us @  http://www.mindsensorpsm.screen.com/
#
# History:
# Date       Author          Comments
# 04/21/17   Seth Tenembaum  Initial development.
#

import os, time
from PiStorms import PiStorms

psm = PiStorms()

psm.BAS1.activateCustomSensorI2C()

psm.screen.drawDisplay("ABSIMU Calibration")

psm.screen.termGotoLine(0)
psm.screen.termPrintln("Beginning AbsoluteIMU compass")
psm.screen.termPrintln("calibration program.")
psm.screen.termPrintln("")
psm.screen.termPrintln("Connect AbsoluteIMU-ACG")
psm.screen.termPrintln("to BAS1.")
psm.screen.termPrintln("")
psm.screen.termPrintln("Press GO to begin.")

psm.waitForKeyPress()

psm.psc.bankA.writeByte(psm.psc.PS_Command, ord('C'))


psm.screen.clearScreen()
psm.screen.dumpTerminal()
psm.screen.termGotoLine(0)
psm.screen.termPrintln("Calibrating...")
psm.screen.termPrintln("Turn 360 degrees")
psm.screen.termPrintln("along all 3 axepsm.screen.")
psm.screen.termPrintln("")
psm.screen.termPrintln("Then press GO to end.")

psm.waitForKeyPress()

psm.psc.bankA.writeByte(psm.psc.PS_Command, ord('c'))
