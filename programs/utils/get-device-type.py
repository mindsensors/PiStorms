#!/usr/bin/env python3
#
# Copyright (c) 2016 mindsensors.com
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
# 05/02/16  deepak      Initial development
#
# we could also do this instead:
# i2cdump -y -r 0x00-0x04 1 0x1a | grep "^00:" | cut -c 56-60
#

from PiStormsCom import PiStormsCom
comm = PiStormsCom()

import configparser
config = configparser.RawConfigParser()
config.read("/usr/local/mindsensors/conf/msdev.cfg")

if "GRX" in comm.GetDeviceFeatures().upper():
    config.set('msdev', 'device', 'PiStorms-GRX')
else:
    config.set('msdev', 'device', 'PiStorms')

with open("/usr/local/mindsensors/conf/msdev.cfg", 'w') as configfile:
    config.write(configfile)
