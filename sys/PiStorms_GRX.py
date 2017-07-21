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

from PiStormsCom_GRX import GRXCom
from mindsensorsUI import mindsensorsUI
import struct,functools


## This class provides functions for Grove sensors.
#  This class has derived classes for each sensor.
#  @remark There is no need to use this class directly in your program.
class GrovePort():
    def __init__(self, port=None, type=GRXCom.TYPE.ANALOG_INPUT, mode=0):
        if port == None:
            raise TypeError("You must specify a port as an argument." \
                    " Please do so in the form B?$# where ? is A or B" \
                    " for the bank letter (which half of the PiStorms)," \
                    " $ is A or D for the port type (analog or digital)," \
                    " and # is the port number." \
                    " For example: BAA2 is Bank A, Analog port 2.")

        bank = port[:2]
        if bank == "BA":
            i2c = GRXCom.I2C.A
        elif bank == "BB":
            i2c = GRXCom.I2C.B
        else:
            raise ValueError("Invalid bank (must be A or B).")

        if port[2]=="A":
            addresses = GRXCom.ANALOG
            typeSupport = GRXCom.TYPE_SUPPORT.ANALOG
        elif port[2]=="D":
            addresses = GRXCom.DIGITAL
            typeSupport = GRXCom.TYPE_SUPPORT.DIGITAL
        else:
            raise ValueError("Invalid port type (must be A for analog or D for digital).")
        if type not in typeSupport:
            raise TypeError("This port does not support that type.")

        number = int(port[3]) - 1
        # not catching an IndexError here because -1 should not be valid
        if number not in range(len(addresses)):
            raise ValueError("Invalid port number (must be 1, 2, or 3 for analog; or 1 or 2 for digital).")

        if mode not in range(256):
            raise ValueError("Sensor port mode must be an integer between 0 and 255.")

        address = addresses[number]
        self.comm = GRXCom(i2c, address)
        self.comm.setType(type, mode)

        if type == GRXCom.TYPE.DIGITAL_INPUT:
            self.readValue = self.comm.digitalRead
        elif type == GRXCom.TYPE.ANALOG_INPUT:
            self.readValue = self.comm.analogRead
        elif type == GRXCom.TYPE.DIGITAL_OUTPUT:
            self.writeValue = self.comm.digitalWrite
        elif type == GRXCom.TYPE.ENCODER:
            self.readValue = self.comm.readEncoderValue


## This class provides functions for controlling a servo connected to
#  the PiStorms-GRX. It has six servo pins at the top of the device. There are
#  three on Bank A and three on Bank B. The pins on the outside, closer to
#  the edge of the device, are numbered 1. The next pins inward are pin 2,
#  and the pins closest to the center are pin 3. The ports are represented
#  in the form "BAM1" for Bank A Motor 1. Looking at the top of the device
#  with the screen facing you, the ports are, from left to right:
#  BBM1, BBM2, BBM3, BAM3, BAM2, BAM1.
#  The signal pin should be facing away from you (closer to the Raspberry Pi)
#  and the ground pin should be closer to you, towards the front of the device
#  with the screen. Of course this leaves the voltage pin in the center.
#  This class supports both regular servos and continuous rotation servos.
class RCServo():

    ## Initialize an RC servo object.
    #  @param port Must be a valid port, one of [BAM1, BAM2, BAM3, BBM1, BBM2, BBM3].
    #              The first two characters are "BA" or "BB", for "Bank A" or "Bank B".
    #              The third character is 'M' for "Motor". The fourth character
    #              is the pin number. See the RCServo class documentation for details.
    #  @param neutralPoint You may specify the neutral point of this servo.
    #                      The default is 1500, but as a result of the manufacturing
    #                      process for these servos each has a slightly different
    #                      neutral point. For example, if your continuous rotation
    #                      servo continues to spin when you call stop or setNeutral,
    #                      it likely has the wrong neutral point set. You can update
    #                      this at any time with setNeutralPoint(self, neutralPoint).
    def __init__(self, port=None, neutralPoint=1500):
        if port == None:
            raise TypeError("You must specify a port as an argument." \
                    " Please do so in the form B?M# where ? is A or B" \
                    " for the bank letter (which half of the PiStorms)," \
                    " and # is the servo number: 1, 2 or 3." \
                    " For example: BBM3 is Bank B, Motor 3.")

        try:
            if not len(port) == 4:
                raise TypeError("Incorrect port format")
            if port[:2] == "BA":
                bank = GRXCom.I2C.A
            elif port[:2] == "BB":
                bank = GRXCom.I2C.B
            else:
                raise ValueError("Invalid bank letter")
        except TypeError:
            raise TypeError("Port argument is invalid. Please see this class's documentation.")

        try:
            pinNum = int(port[-1])
        except ValueError:
            raise ValueError("Servo number must be an integer: 1, 2, or 3")
        if not 1 <= pinNum <= 3:
            raise ValueError("Servo number must be 1, 2, or 3")

        self.sendDataArray = lambda dataArray: bank.writeArray(GRXCom.SERVO[pinNum-1], dataArray)
        self.setNeutralPoint(neutralPoint)
        self.setNeutral()
        # useful properties for user access, not necessary for this class's functions
        #self.pos has already been set to neutralPoint
        self.speed = 0
        self.bankAddr = bank.address
        self.pinNum = pinNum

    ## Sets the pulse being send to this servo.
    #  @param pulse A number of microseconds for the pulse length.
    #  @remark There is no need to use this method directly in your program.
    def setPulse(self, pulse):
        try:
            pulse = int(pulse)
        except ValueError:
            raise ValueError("Servo pulse must be an integer in the range 500-2500")
        if not (500 <= pulse <= 2500  or pulse==0):
            raise ValueError("Servo pulse must be in the range 500 through 2500")
        self.sendDataArray([pulse%256, pulse/256])

    ## Use this method to set the position of regular servos.
    #  @param newPos A position between 0.0 and 180.0, with 90.0 being
    #                the nominal center value.
    def setPos(self, newPos):
        try:
            newPos = float(newPos)
        except ValueError:
            raise ValueError("Servo position must be a decimal in the range 0.0 - 180.0")
        if not 0.0 <= newPos <= 180.0:
            raise ValueError("Servo position must be in the range 0.0 through 180.0")
        self.setPulse((newPos/90.0 - 1) * self.range + self.neutralPoint)
        self.pos = newPos

    ## Use this method to set the speed of continuous rotation servos.
    #  @param speed A decimal between -100 and 100 for what speed this servos
    #               should run at.
    def setSpeed(self, speed):
        try:
            speed = float(speed)
        except ValueError:
            raise ValueError("Servo speed must be a decimal between -100 and 100")
        if not -100.0 <= speed <= 100.0:
            raise ValueError("Servo speed must be between -100 and 100")
        self.setPulse(speed/100.0 * self.range + self.neutralPoint)
        self.speed = speed

    ## Update the neutral point of this servo.
    #  @param neutralPoint The new neutral point of this servo. As with setPos(self, newPos),
    #                      this number must be between 500 and 2500.
    ## @note This does <b>not</b> call self.setNeutral(self) after the neutral point is set.
    def setNeutralPoint(self, neutralPoint):
        try:
            neutralPoint = int(neutralPoint)
        except ValueError:
            raise ValueError("Servo neutral point must be an integer in the range 500-2500")
        if not 500 <= neutralPoint <= 2500:
            raise ValueError("Servo neutral point must be in the range 500 through 2500")

        self.neutralPoint = neutralPoint
        margin = 150 # don't try to set speed too close to the extremes
        # here min is used to find the smaller range: neutral to min or neutral to max (max to neutral)
        self.range = min(self.neutralPoint-(500+margin), (2500-margin)-self.neutralPoint)

    ## Return this servo to the neutral position. For a regular servo it will go
    #  to the center, and a continuous rotation servo will stop rotating.
    def setNeutral(self):
        self.setPulse(self.neutralPoint)

    ## Stop sending a signal altogether to this servo.
    def stop(self):
        self.setPulse(0)


## This class provides functions for controlling a servo and encoder connected to
#  the PiStorms-GRX.
class RCServoEncoder(RCServo, GrovePort):
    ## Initialize an RC servo object with an associated encoder.
    #  @param encoder You may associate an encoder with this servo by specifying
    #                 the digital port it is connected to.
    def __init__(self, port=None, neutralPoint=1500, encoder=None):
        if port == None:
            raise TypeError("You must specify a port as an argument")
        if encoder == None:
            raise TypeError("You must specify an encoder as an argument. If you do not wish to use an "
                            "encoder with this servo, please use the RCServo class instead.")

        if encoder[1] != port[1]:
            raise ValueError("The encoder must be on the same bank as the servo it is associated with.")
        #if port[3] not in ["1", "2"]:
        #    raise ValueError("The servo associated with this encoder must be on servo port 1 or 2, not 3.")
        if encoder[2] != "D":
            raise ValueError("The encoder must be on digital port 1 or 2.")

        RCServo.__init__(self, port, neutralPoint)
        GrovePort.__init__(self, encoder, type=GRXCom.TYPE.ENCODER, mode=int(encoder[3]))

    def setTarget(self, value):
        if value.bit_length() > 64:
            raise ValueError("Encoder target must fit in a signed long data type.")
        self.comm.setEncoderTarget(value)

    def readEncoder(self):
        return self.comm.readEncoderValue()


class PiStorms_GRX():

    def __init__(self, name="PiStorms_GRX", rotation=3):
        self.screen = mindsensorsUI(name, rotation)

    # note the command will be sent to bank A. This will be important for operations such as resetting the encoder values.
    @classmethod
    def command(self, cmd):
        if cmd not in range(256):
            raise ValueError("Command must be an integer between 0 and 255 (hint: try using a constant from GRXCom.COMMAND).")
        GRXCom.I2C.A.writeByte(GRXCom.REGISTER.COMMAND, cmd)

    @classmethod
    def shutdown(self):
        GRXCom.I2C.A.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.SHUTDOWN)

    @classmethod
    def batteryVoltage(self):
        return GRXCom.I2C.A.readByte(GRXCom.REGISTER.BATTERY_VOLTAGE) * 0.04

    @classmethod
    def getFirmwareVersion(self):
        return GRXCom.I2C.A.readString(GRXCom.REGISTER.FIRMWARE_VERSION, 8)

    @classmethod
    def getVendorName(self):
        return GRXCom.I2C.A.readString(GRXCom.REGISTER.VENDOR_NAME, 8)

    @classmethod
    def getDeviceModel(self):
        return GRXCom.I2C.A.readString(GRXCom.REGISTER.DEVICE_MODEL, 8)

    @classmethod
    def getDeviceFeatures(self):
        return GRXCom.I2C.A.readString(GRXCom.REGISTER.FEATURE, 8)

    @classmethod
    def led(self, lednum, red, green, blue):
        for color in [red, green, blue]:
            if color not in range(256):
                raise ValueError("LED color intensities must be an integer between 0 and 255.")
        if lednum == 1:
            comm = GRXCom.I2C.A
        elif lednum == 2:
            comm = GRXCom.I2C.B
        else:
            raise ValueError("Invalid LED number (must be 1 or 2 for bank A or B).")
        comm.writeArray(GRXCom.REGISTER.LED, [red, green, blue])

    @classmethod
    def isKeyPressed(self):
        return GRXCom.I2C.A.readByte(GRXCom.REGISTER.GO_BUTTON_STATE) % 2 == 1

    @classmethod
    def waitForKeyPress(self):
        self.untilKeyPress(functools.partial(time.sleep, 0.01))

    @classmethod
    def untilKeyPress(self, func):
        initialKeyPressCount = self.getKeyPressCount()
        while self.getKeyPressCount() == initialKeyPressCount:
            func()

    @classmethod
    def getKeyPressValue(self): # F1-4
        return {0: 0, 8: 1, 16: 2, 24: 3, 40: 4}[GRXCom.getKeyPressValue()]

    @classmethod
    def isF1Pressed(self):
        return (GRXCom.getKeyPressValue() == 8)

    @classmethod
    def isF2Pressed(self):
        return (GRXCom.getKeyPressValue() == 16)

    @classmethod
    def isF3Pressed(self):
        return (GRXCom.getKeyPressValue() == 24)

    @classmethod
    def isF4Pressed(self):
        return (GRXCom.getKeyPressValue() == 40)

    @classmethod
    def getKeyPressCount(self):
        return GRXCom.I2C.A.readByte(GRXCom.REGISTER.GO_PRESS_COUNT)

    @classmethod
    def resetKeyPressCount(self):
        GRXCom.I2C.A.writeByte(GRXCom.REGISTER.GO_PRESS_COUNT, 0)

    @classmethod
    def ping(self):
        GRXCom.ping()
