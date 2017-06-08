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
# Date       Author          Comments
# June 2017  Seth Tenembaum  Initial Authoring

from mindsensors_i2c import mindsensors_i2c


## GRXCom: this class provides communication functions for PiStorms-GRX.
#  Do not use this class directly in user programs.
class GRXCom():
    class I2C:
        A = mindsensors_i2c(0x34 >> 1)
        B = mindsensors_i2c(0x36 >> 1)
    class TYPE:
        NONE = 0
        ANALOG_INPUT = 1
        DIGITAL_OUTPUT = 2
        DIGITAL_INPUT = 3
        I2C = 4
        ENCODER = 5
        SERIAL = 6
#    class TYPE_SUPPORT:
#        ALL = [GRXCom.TYPE.NONE, GRXCom.TYPE.DIGITAL_OUTPUT, GRXCom.TYPE.DIGITAL_INPUT, GRXCom.TYPE.I2C]
#        ANALOG = ALL + [GRXCom.TYPE.ANALOG_INPUT]
#        DIGITAL = ALL + [GRXCom.TYPE.ENCODER]
#        # note: SERIAL is only supported on A1 and A2
    SERVO   = [0x42+i*0x02 for i in range(3)]
    ANALOG  = [0x48+i*0x16 for i in range(3)]
    DIGITAL = [0x8A+i*0x16 for i in range(2)]
    class OFFSET:
        TYPE = 0
        MODE = 1
        RATE = 2
        GO = 3
        DATA = 4
        ENCODER_VALUE = 4
        ENCODER_TARGET = 8

    def __init__(self, i2c, address):
        self.i2c = i2c
        self.address = address

    def setType(self, newType, mode=0):
        self.i2c.writeByte(self.address, newType)
        self.i2c.writeByte(self.address+1, mode)

    def digitalRead(self):
        return self.i2c.readByte(self.address + self.OFFSET.DATA)

    def analogRead(self):
        return self.i2c.readInteger(self.address + self.OFFSET.DATA)

    def readEncoderValue(self):
        return self.i2c.readLongSigned(self.address + self.OFFSET.ENCODER_VALUE)

    def setEncoderTarget(self, target):
        return self.i2c.writeLongSigned(self.address + self.OFFSET.ENCODER_TARGET, target)

class TYPE_SUPPORT:
    ALL = [GRXCom.TYPE.NONE, GRXCom.TYPE.DIGITAL_OUTPUT, GRXCom.TYPE.DIGITAL_INPUT, GRXCom.TYPE.I2C]
    ANALOG = ALL + [GRXCom.TYPE.ANALOG_INPUT]
    DIGITAL = ALL + [GRXCom.TYPE.ENCODER]
    # note: SERIAL is only supported on A1 and A2
GRXCom.TYPE_SUPPORT = TYPE_SUPPORT
del TYPE_SUPPORT

