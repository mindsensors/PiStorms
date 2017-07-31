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

# SETUP PiStorms and joystick

from PiStorms import PiStorms
# initialize PiStorms object
psm = PiStorms()

m = ["Instructions",
     "Use the left and right joysticks",
     "to move the left and right motors.",
     "Press GO to Exit."]
psm.screen.showMessage(m)

import pygame
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# LOOP while GO is not pressed
while not psm.isKeyPressed():
    # let Pygame update, check the joystick, etc.
    pygame.event.pump()
    # moves right motor foward and backwards with joystick value
    # the joystick returns -1 to 1, but the motor needs -100 to 100
    psm.BAM1.setSpeed(joystick.get_axis(1) * 100)
    # moves left motor foward and backwards with joystick value
    psm.BAM2.setSpeed(joystick.get_axis(4) * 100)
