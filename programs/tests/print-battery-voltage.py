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
# Date        Author      Comments
#  04-11-16   Deepak      Troubleshooting program

import time

from PiStorms import PiStorms
print ""
print "Running program 5 times, press Ctrl-C to terminate"
print ""
psm = PiStorms()

exit = False
a = 0
while(a < 5):
    voltVal = psm.battVoltage()
    print "PiStorms voltage: " + str(voltVal)
    time.sleep(2)
    a = a + 1
