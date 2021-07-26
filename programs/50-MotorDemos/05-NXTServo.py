#!/usr/bin/env python3
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
#
# History:
# Date      Author          Comments
# 05/02/17  Seth Tenembaum  Initial development.
#

from PiStorms import PiStorms
from mindsensors import NXTSERVO
import time

psm = PiStorms()
psm.BAS1.activateCustomSensorI2C()

nxt_servo = NXTSERVO()

m = ["NXTServo Example",
     "Connect NXTServo to BAS1.",
     "Connect a servo to SV1.",
     "Connect power to the NXTServo.",
     "Tap OK or press GO to continue."]
psm.screen.showMessage(m)

# Set servo SV1 to position 100
nxt_servo.setPosition(1, 100)
psm.screen.showMessage(["NXTServo Example", "Servo 1 should be at position 100."])

nxt_servo.setPosition(1, 200)
psm.screen.showMessage(["NXTServo Example", "Servo 1 should be at position 200."])
