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

import os,sys,inspect,time,thread
import socket,fcntl,struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
    
    

from PiStorms import PiStorms
print "running psm-info.py"
psm = PiStorms()

print " Version : "+ str(psm.GetFirmwareVersion() )[:5]
print " Vendor  : "+ str(psm.GetVendorName() )
print " Device : "+ str(psm.GetDeviceId() )
print " HostName :     "   + socket.gethostname()
   
try:
    print " eth0 :     "   + get_ip_address('eth0')
except:
    print " eth0 : not present"
try:    
    print " wlan0 :    "+ get_ip_address('wlan0')
except:
    print " wlan0 : not present"
   
