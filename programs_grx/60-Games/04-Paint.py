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

from PiStorms_GRX import PiStorms_GRX
psm = PiStorms_GRX()

color = (255, 255, 255)

while True:
    if psm.isKeyPressed():
        break

    if psm.isF1Pressed():
        color = (255, 0, 0)
    if psm.isF2Pressed():
        color = (255, 255, 0)
    if psm.isF3Pressed():
        color = (0, 255, 0)
    if psm.isF4Pressed():
        color = (0, 0, 255)

    if psm.screen.isTouched():
        x = psm.screen.TS_To_ImageCoords_X(psm.screen.x, psm.screen.y)
        y = psm.screen.TS_To_ImageCoords_Y(psm.screen.x, psm.screen.y)
        psm.screen.fillRect(x-1, y-1, 2, 2, fill=color)
