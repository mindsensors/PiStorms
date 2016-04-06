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

import os,sys,inspect,time,thread
import socket,fcntl,struct,ms_explorerlib    

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms

print "running program"
psm = PiStorms()
psm.screen.termPrintln("Connect your I2C device to BAS1")
psm.screen.termPrintln("and click Explore")
psm.screen.drawButton(75, 95, width = 85, height = 40, text="Explore", display=False)
psm.screen.drawButton(175, 95, width = 60, height = 40, text="Exit", display=True)

exit = False
lastled = 0

def explore():
    time.sleep(3)
    addr = 0x00     # DO NOT change this address!!!
    i2c = ms_explorerlib.Explorer(addr)
    found = i2c.ping(0x00)  
    # Checks for connection on all I2C addresses until connection is found
    count = 0 
    while found == -1:     
        if (addr < 0xef):
            addr = addr + 1
            count = count + 1
            if (addr != 0x34 and addr != 0x35 and addr != 0x36 and addr != 0x37):
                i2c = ms_explorerlib.Explorer(addr)
                found = i2c.ping(0x00)
            if (count > 2000):
                found = 5
        else:
            addr = 0x00   
    if (found == 5):
        psm.screen.termPrintAt(5, "No Device found!")
        psm.screen.termPrintAt(6, "Click Exit to return to main menu")
    else:
        psm.screen.termPrintAt(5, "7 bit address: " + str(hex(addr/2)))      
        psm.screen.termPrintAt(6, "8 bit address: " + str(hex(addr)))         
        psm.screen.termPrintAt(7, "FW Version: " + i2c.GetFirmwareVersion()[:5])
        psm.screen.termPrintAt(8, "Vendor ID: " + i2c.GetVendorName())
        device = i2c.GetDeviceId()
        pos = device.find('\0') 
        psm.screen.termPrintAt(9, "Device ID: " + i2c.GetDeviceId()[:pos])

while(not exit):
    explorer = psm.screen.checkButton(75, 95,width=85,height=40)
    bye = psm.screen.checkButton(175, 95,width=60,height=40)
    if(explorer == True):
        psm.screen.termPrintAt(5, "")
        psm.screen.termPrintAt(6, "")
        psm.screen.termPrintAt(7, "")
        psm.screen.termPrintAt(8, "")
        psm.screen.termPrintAt(9, "")
        psm.screen.termPrintAt(5, "Searching for i2c device...")        
        psm.BAS1.activateCustomSensorI2C()
        explore()
    if(bye == True):
        psm.screen.termPrintAt(5, "Exiting to menu")
        exit = True
    time.sleep(.1)