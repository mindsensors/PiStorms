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
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
# History:
# Date      Author      Comments
#  Oct 2015  Nitin     Initial Authoring 
# Oct 2016   Deepak    support for graceful shutdown.

from mindsensors_i2c import mindsensors_i2c
import sys,os,time

lckfile = '/tmp/.psm_shutdown.lck'

print "starting..."
driver = mindsensors_i2c( 0x34 >> 1)
count = 0
while (True):
    time.sleep(0.4)
    try :
        keypress = driver.readByte(0xdB)
        #print keypress
        if keypress == 253:
            #print "sudo halt -p"
            try:
                os.remove(lckfile)
            except OSError:
                pass
            f = open(lckfile, 'w')
            f.write("go_pressed")
            f.close()
            os.system("sudo shutdown -h now")
            quit()
    except:
        #print " read failed"
        count = count + 1


