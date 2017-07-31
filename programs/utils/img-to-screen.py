#!/usr/bin/env python
#
# Copyright (c) 2017 mindsensors.com
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

from mindsensorsUI import mindsensorsUI
import sys

X = int(sys.argv[1])
Y = int(sys.argv[2])
W = int(sys.argv[3])
H = int(sys.argv[4])
IMAGE = str(sys.argv[5])

screen = mindsensorsUI("PiStorms",3)
screen.fillBmp(X, Y, W, H, path = IMAGE)
