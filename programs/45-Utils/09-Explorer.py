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
import sys

from mindsensors_i2c import mindsensors_i2c

from PiStorms import PiStorms
psm = PiStorms("Explorer")

psm.BAS1.activateCustomSensorI2C()
psm.BAS2.activateCustomSensorI2C()
psm.BBS1.activateCustomSensorI2C()
psm.BBS2.activateCustomSensorI2C()

i2c_all = []
for addr in range(0x00,0x34,2) + range(0x38,0xEF,2):
    i2c_all.append(mindsensors_i2c(addr>>1))

def ping(i2c):
    return i2c.readByte(0x00) != None
def println(text="", text2=""):
    psm.screen.termPrintln("{} {}".format(text, text2.rstrip("\0")), display=False)

while not psm.isKeyPressed():
    found = []
    for i2c in i2c_all:
        if ping(i2c):
            found.append(i2c)

    psm.screen.dumpTerminal(display=False)
    println("Found {} I2C device{}.".format(len(found), "s" if len(found) != 1 else ""))
    println("")
    
    if len(found):
        println("7 bit address:", hex(found[0].address*2))
        println("8 bit address:", hex(found[0].address))
        println("FW Version:",    found[0].GetFirmwareVersion())
        println("Vendor ID:",     found[0].GetVendorName())
        println("Device ID:",     found[0].GetDeviceId())
    else:
        println("Connect an I2C sensor to any")
        println("sensor port.")
        println("")
        println("Searching...")
    psm.screen.termPrintAt(8, "Press GO to quit.", display=False)  
    psm.screen.refresh()
