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

import time
from PiStorms_GRX import PiStorms_GRX, RCServo, GrovePort
from PiStormsCom_GRX import GRXCom

psm = PiStorms_GRX()

leftServo = RCServo("BBS1", 1690)
rightServo = RCServo("BAS1", 1350)

leftEncoder = GrovePort("BBD1", type=GRXCom.TYPE.ENCODER) # no mode, not associated with any servo
rightEncoder = GrovePort("BAD2", type=GRXCom.TYPE.ENCODER)

GRXCom.I2C.A.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.RESET_ENCODERS)
GRXCom.I2C.B.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.RESET_ENCODERS)

for i in range(200):
    try:
        leftEncoderValue = -1*leftEncoder.comm.readEncoderValue()
        rightEncoderValue = rightEncoder.comm.readEncoderValue()

        print "{:6d} {:6d}".format(leftEncoderValue, rightEncoderValue)
        if leftEncoderValue < rightEncoderValue:
            leftServo.setSpeed(30)
            rightServo.setSpeed(50)
        else:
            leftServo.setSpeed(50)
            rightServo.setSpeed(30)
    except TypeError: pass # I2C failure

leftServo.stop()
rightServo.stop()
