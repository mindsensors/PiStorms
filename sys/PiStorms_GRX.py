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
import struct
from functools import partial


## This class provides functions for digital Grove sensors.
#  This class has derived classes for each sensor.
#  @remark There is no need to use this class directly in your program.
class GroveDigitalPort():
    def __init__(self, port, initType=GRXCom.TYPE.DIGITAL_INPUT):
        bank = port[1]
        if bank == "A":
            i2c = GRXCom.I2C.A
        elif bank == "B":
            i2c = GRXCom.I2C.B
        else:
            raise ValueError("Invalid bank (must be A or B).")

        if port[2]=="A":
            addresses = GRXCom.ANALOG
        elif port[2]=="D":
            addresses = GRXCom.DIGITAL
        else:
            raise ValueError("Invalid port type (must be A for analog or D for digital).")

        number = int(port[3]) - 1
        # not catching an IndexError here because -1 should not be valid
        if number not in range(len(addresses)):
            raise ValueError("Invalid port number (must be 1, 2, or 3 for analog; or 1 or 2 for digital).")

        address = addresses[number]
        self.comm = GRXCom(i2c, address)
        if initType:
            self.setType(initType)

    def setType(self, newType, mode=0):
        if newType not in GRXCom.TYPE_SUPPORT.DIGITAL:
            raise TypeError("This port does not support that type.")
        self.comm.setType(newType, mode)

    def readValue(self):
        return self.comm.digitalRead()


## This class provides functions for analog Grove sensors.
#  This class has derived classes for each sensor.
#  @remark There is no need to use this class directly in your program.
class GroveAnalogPort(GroveDigitalPort):
    def __init__(self, port):
        GroveDigitalPort.__init__(self, port)
        self.setType(GRXCom.TYPE.ANALOG_INPUT)

    def setType(self, newType, mode=0):
        if newType not in GRXCom.TYPE_SUPPORT.ANALOG:
            raise TypeError("This port does not support that type.")
        self.comm.setType(newType, mode)

    def readValue(self):
        return self.comm.analogRead()


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
class RCServo(GRXCom):

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
            raise TypeError("You must specify a port as an argument")

        try:
            if not len(port) == 4:
                raise TypeError("Incorrect port format")
            if port[:2] == "BA":
                bank = self.bankA
            elif port[:2] == "BB":
                bank = self.bankB
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

        self.sendDataArray = lambda dataArray: bank.writeArray(self.GRX_Servo_Base+(pinNum-1)*2, dataArray)
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
class RCServoEncoder(RCServo, GroveDigitalPort):
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
        if port[3] not in ["1", "2"]:
            raise ValueError("The servo associated with this encoder must be on servo port 1 or 2, not 3.")
        if port[2] != "D":
            raise ValueError("The encoder must be on digital port 1 or 2.")

        RCServo.__init__(self, port, neutralPoint)
        GroveDigitalPort.__init__(self, port, initType=None):
        self.setType(GRXCom.TYPE.ENCODER, mode=int(encoder[3]))

    def setTarget(self, value):
        self.setEncoderTarget(value)

    def readEncoder(self):
        return self.readEncoderValue()


class PiStorms_GRX:

    def __init__(self, name = "PiStorms_GRX", rotation = 3 ):
        self.screen = mindsensorsUI(name, rotation)
        self.psc = GRXCom()

    def command (self, cmd, bank):
        self.psc.command(cmd, bank)

    def Shutdown(self):
        self.psc.Shutdown()

    def battVoltage(self):
        return self.psc.battVoltage()

    def GetFirmwareVersion(self):
        return self.psc.GetFirmwareVersion()

    def GetVendorName(self):
        return self.psc.GetVendorName()

    def GetDeviceId(self):
        return self.psc.GetDeviceId()

    def led(self,lednum,red,green,blue):
        return self.psc.led(lednum,red,green,blue)

    def isKeyPressed(self):
        return self.psc.isKeyPressed()

    def getKeyPressValue(self):
        return self.psc.getKeyPressValue()

    def isF1Pressed(self):
        return (self.psc.getKeyPressValue() == 8)

    def isF2Pressed(self):
        return (self.psc.getKeyPressValue() == 16)

    def isF3Pressed(self):
        return (self.psc.getKeyPressValue() == 24)

    def isF4Pressed(self):
        return (self.psc.getKeyPressValue() == 40)
    
    def getKeyPressCount(self):
        return self.psc.getKeyPressCount()
    
    def resetKeyPressCount(self):
        self.psc.resetKeyPressCount()
    
    def ping(self):
        self.psc.ping()
