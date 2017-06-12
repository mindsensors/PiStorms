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
# Oct 2015  Michael     Initial Authoring
# Jun 2017  Seth        Simplification

import time
import ms_explorerlib

from PiStorms import PiStorms
psm = PiStorms()

psm.BAS1.activateCustomSensorI2C()

class STATE:
    INIT = 0
    FOUND = 1
    SEARCHING = 2
state = STATE.INIT

while not psm.isKeyPressed():
    for addr in range(0x00,0x34) + range(0x38,0xEF):
        i2c = ms_explorerlib.Explorer(addr)
        if i2c.ping(0x00) != -1: break

    if i2c.ping(0x00) != -1 and state != STATE.FOUND:
        psm.screen.dumpTerminal()
        psm.screen.termPrintln("I2C device found!")
        psm.screen.termPrintln("")
        psm.screen.termPrintln("7 bit address: " + str(hex(addr/2)))
        psm.screen.termPrintln("8 bit address: " + str(hex(addr)))
        psm.screen.termPrintln("FW Version: " + i2c.GetFirmwareVersion()[:5])
        psm.screen.termPrintln("Vendor ID: " + i2c.GetVendorName())
        psm.screen.termPrintln("Device ID: " + i2c.GetDeviceId().rstrip("\0"))
        psm.screen.termPrintAt(8, "(hold GO for a moment to quit)")
        state = STATE.FOUND
    elif i2c.ping(0x00) == -1 and state != STATE.SEARCHING:
        psm.screen.dumpTerminal()
        psm.screen.termPrintln("Connect your I2C device to BAS1")
        psm.screen.drawAutoText("(here) -->", 235, 110)
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Searching...")
        psm.screen.termPrintAt(8, "(hold GO for a moment to quit)")
        state = STATE.SEARCHING
