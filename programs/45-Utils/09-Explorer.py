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

class STATE:
    INIT = 0
    FOUND = 1
    SEARCHING = 2
state = STATE.INIT

i2c_all = []
for addr in range(0x00,0x34,2) + range(0x38,0xEF,2):
    i2c_all.append(mindsensors_i2c(addr>>1))

def ping(i2c):
    return i2c.readByte(0x00) != None
def println(text="", text2=""):
    psm.screen.termPrintln("{} {}".format(text, text2.rstrip("\0")), display=False)
def draw():
    psm.screen.termPrintAt(8, "Press GO to quit.", display=False)  
    psm.screen.refresh()
    #psm.screen.drawDisplay("Explorer")

while not psm.isKeyPressed():
    found = []
    for i2c in i2c_all:
        if ping(i2c):
            found.append(i2c)

    #if len(found) == 0: continue
    i2c = None
    if len(found) > 0: i2c = found[0]
    if i2c and state != STATE.FOUND:
        psm.screen.dumpTerminal()
        println("I2C device found!")
        println("")
        println("7 bit address:", hex(i2c.address*2))
        println("8 bit address:", hex(i2c.address))
        println("FW Version:",    i2c.GetFirmwareVersion())
        println("Vendor ID:",     i2c.GetVendorName())
        println("Device ID:",     i2c.GetDeviceId())
        draw()
        state = STATE.FOUND
    elif not i2c and state != STATE.SEARCHING:
        psm.screen.dumpTerminal()
        println("Connect your I2C device to BAS1")
        println("")
        println("Searching...")
        draw()
        psm.screen.drawAutoText("(here) -->", 235, 110)
        state = STATE.SEARCHING
