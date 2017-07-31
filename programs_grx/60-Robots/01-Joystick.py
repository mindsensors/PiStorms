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

from PiStorms_GRX import RCServo
l = RCServo("BAS1", 1300)
r = RCServo("BAS2", 1690)

import pygame, sys
try:
    pygame.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except:
    psm.screen.showMessage("Please connect a joystick and try again.")
    sys.exit(0)

import time
while not psm.isKeyPressed() and not joystick.get_button(16):
    pygame.event.pump()
    l.setSpeed(joystick.get_axis(1)*-40)
    r.setSpeed(joystick.get_axis(3)*-100)
    time.sleep(0.05)

l.stop()
r.stop()
