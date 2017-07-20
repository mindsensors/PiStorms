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

import sys

from mindsensors_i2c import mindsensors_i2c

from PiStorms import PiStorms
psm = PiStorms("Explorer")

psm.BAS1.activateCustomSensorI2C()
psm.BAS2.activateCustomSensorI2C()

i2c_all = []
for addr in range(0x00,0x34,2) + range(0x38,0xEF,2):
    i2c_all.append(mindsensors_i2c(addr>>1))

def ping(i2c):
    return i2c.readByte(0x00) != None

def mainLoop()
    found = filter(ping, i2c_all)

    psm.screen.terminalBuffer = [""]*20
    psm.screen.terminalBuffer[0] = "Found {} I2C device{}." \
            .format(len(found), "s" if len(found) != 1 else "")
    psm.screen.terminalBuffer[8] = "Press GO to quit"

    if len(found) > 1:
        for i,dev in enumerate(found):
            psm.screen.terminalBuffer[i+2] = "0x{:02X}: {}" \
                    .format(dev.address*2, dev.GetDeviceId().rstrip("\0"))
        psm.screen.refresh()
    elif len(found) == 1:
        dev = found[0]
        psm.screen.terminalBuffer[2] = "7 bit address: 0x{:02X}".format(dev.address*2)
        psm.screen.terminalBuffer[3] = "8 bit address: 0x{:02X}".format(dev.address)
        psm.screen.terminalBuffer[4] = "FW Version: {}".format(dev.GetFirmwareVersion().rstrip("\0"))
        psm.screen.terminalBuffer[5] = "Vendor ID: {}".format(dev.GetVendorName().rstrip("\0"))
        psm.screen.terminalBuffer[6] = "Device ID: {}".format(dev.GetDeviceId().rstrip("\0"))
        psm.screen.refresh()
    else:
        psm.screen.terminalBuffer[2] = "Connect an I2C sensor to either"
        psm.screen.terminalBuffer[3] = "sensor port on bank A."
        psm.screen.terminalBuffer[5] = "Searching..."
        psm.screen.refresh()
        psm.screen.drawAutoText("(here) -->", 235, 110, fill=(0,200,0), display=False)
        psm.screen.drawAutoText("(here) -->", 235,  36, fill=(0,200,0))

psm.untilKeyPress(mainLoop)
