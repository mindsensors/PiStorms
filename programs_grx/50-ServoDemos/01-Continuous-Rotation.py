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
from PiStorms_GRX import RCServo

psm = PiStorms_GRX()
servo = RCServo("BAS1")

m = ["Grove Continous Rotation Servo Demo",
     "Please connect a continuous rotation RC servo to port BAS1 (Bank A, Servo 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

m[1] = "If your servo is spinning right now, please run 45-Utils/03-FindNeutralPoint."
psm.screen.showMessage(m, wrapText=True)

servo.setSpeed(100)
m[1] = "Speed: 100"
psm.screen.showMessage(m, wrapText=True)

servo.setSpeed(-100)
m[1] = "Speed: -100"
psm.screen.showMessage(m, wrapText=True)

servo.stop()
m[1] = "Stopped"
psm.screen.showMessage(m, wrapText=True)
