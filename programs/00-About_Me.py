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
import socket,fcntl,struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
    
    

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms
print "running program"
psm = PiStorms()

psm.screen.termPrintln("                     About Me")
psm.screen.termPrintln(" ")

exit = False
lastled = 0
psm.screen.termPrintAt(2," Version : "+ str(psm.GetFirmwareVersion() )[:5])
psm.screen.termPrintAt(3," Vendor  : "+ str(psm.GetVendorName() ))
psm.screen.termPrintAt(4," Device : "+ str(psm.GetDeviceId() ))
psm.screen.termPrintAt(6," HostName :     "   + socket.gethostname() )
while(not exit):
   
    try:
        psm.screen.termPrintAt(7," eth0 :     "   + get_ip_address('eth0'))
    except:
        psm.screen.termPrintAt(7," eth0 : not present")
    try:    
        psm.screen.termPrintAt(8," wlan0 :    "+ get_ip_address('wlan0'))
    except:
        psm.screen.termPrintAt(8," wlan0 : not present")
   
    if(psm.screen.checkButton(0,0,320,320)):
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        exit = True
