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
import configparser
import time


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

        if port == "BBD2" and type == GRXCom.TYPE.ENCODER:
            raise ValueError("BBD2 does not support encoders at this time. Please use BBD1, BAD1 or BAD2.")

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
#  in the form "BAS1" for Bank A Servo 1. Looking at the top of the device
#  with the screen facing you, the ports are, from left to right:
#  > BBS1, BBS2, BBS3, BAS3, BAS2, BAS1
#  The signal pin should be facing away from you (closer to the Raspberry Pi)
#  and the ground pin should be closer to you, towards the front of the device
#  with the screen. Of course this leaves the voltage pin in the center.
#  This class supports both regular servos and continuous rotation servos.
class RCServo():

    ## Initialize an RC servo object.
    #  @param port Must be a valid port, one of [BAS1, BAS2, BAS3, BBS1, BBS2, BBS3].
    #              The first two characters are "BA" or "BB", for "Bank A" or "Bank B".
    #              The third character is 'S' for "Servo". The fourth character
    #              is the pin number. See the RCServo class documentation for details.
    #  @param neutralPoint You may specify the neutral point of this servo.
    #                      The default is 1500, but as a result of the manufacturing
    #                      process for these servos each has a slightly different
    #                      neutral point. For example, if your continuous rotation
    #                      servo continues to spin when you call setNeutral, it likely
    #                      has the wrong neutral point set. You can update this at any
    #                      time with setNeutralPoint(self, neutralPoint).
    #                      If you have ran 45-Utils/03-FindNeutralPoint.py, this
    #                      configuration will be loaded automatically. Make sure the port
    #                      is the same as when you configured it.
    def __init__(self, port=None, neutralPoint=None):
        if port == None or port[2]!="S":
            raise TypeError("You must specify a port as an argument." \
                    " Please do so in the form B?S# where ? is A or B" \
                    " for the bank letter (which half of the PiStorms)," \
                    " and # is the servo number: 1, 2 or 3." \
                    " For example: BBS3 is Bank B, Motor 3.")
        if neutralPoint == None:
            config = configparser.RawConfigParser()
            config.read("/usr/local/mindsensors/conf/msdev.cfg")
            if config.has_section('neutralpoint') and config.has_option('neutralpoint', port.upper()):
                neutralPoint = config.get('neutralpoint', port.upper())
            else:
                neutralPoint = 1500

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
    #  @param port Must be a valid port, one of [BAS1, BAS2, BAS3, BBS1, BBS2, BBS3].
    #              The first two characters are "BA" or "BB", for "Bank A" or "Bank B".
    #              The third character is 'S' for "Servo". The fourth character
    #              is the pin number. See the RCServo class documentation for details.
    #  @param encoder You may associate an encoder with this servo by specifying
    #                 the digital port it is connected to.
    #  @param neutralPoint You may specify the neutral point of this servo.
    #                      The default is 1500, but as a result of the manufacturing
    #                      process for these servos each has a slightly different
    #                      neutral point. For example, if your continuous rotation
    #                      servo continues to spin when you call setNeutral, it likely
    #                      has the wrong neutral point set. You can update this at any
    #                      time with setNeutralPoint(self, neutralPoint).
    #                      If you have ran 45-Utils/03-FindNeutralPoint.py, this
    #                      configuration will be loaded automatically. Make sure the port
    #                      is the same as when you configured it.
    def __init__(self, port=None, encoder=None, neutralPoint=None):
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

    ## Set the position which this servo should target. It will try to move
    #  until it knows from the encoder that it's in the right place.
    #  @param degrees Where the servo should target. This is in degrees
    #         and may be between negative two billion and positive two billion.
    def setTarget(self, degrees):
        # divide by 5 to convert to 1/72ths
        value = degrees/5
        if value.bit_length() > 64:
            raise ValueError("Encoder target must fit in a signed long data type.")
        self.comm.setEncoderTarget(value)

    ## Read the current position of this servo according to the encoder.
    def readEncoder(self):
        # multiply by 5 to convert back to 1/360ths, degrees
        return self.comm.readEncoderValue()*5


## PiStorms_GRX: This class provides functions for the PiStorms-GRX.
#  GrovePort, RCServo, and RCServoEncoder are all separate classes and should be initialized as needed.
class PiStorms_GRX():

    ## Create an object which represents the PiStorms-GRX
    #  @param name The display title that will appear at the top of the LCD touchscreen.
    #  @param rotation The rotation of the LCD touchscreen.
    #  @remark
    #  There is no need to use this function directly. To initialize the PiStorms_GRX class in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  @endcode
    def __init__(self, name="PiStorms_GRX", rotation=3):
        self.screen = mindsensorsUI(name, rotation)
        self.resetKeyPressCount()

    ## Send a command to the PiStorms
    #  @param cmd The command byte to send. This should be a value of GRXCom.COMMAND.
    #  @note The command will be sent to bank A. This will be important for operations such as resetting the encoder values.
    #  @remark
    #  You shouldn't need to use this method directly in your programs, but if you do:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  from PiStormsCom_GRX import GRXCom
    #  ...
    #  PiStorms_GRX.command(GRXCom.COMMAND.SHUTDOWN)
    #  @endcode
    @classmethod
    def command(self, cmd):
        if cmd not in range(256):
            raise ValueError("Command must be an integer between 0 and 255 (hint: try using a constant from GRXCom.COMMAND).")
        GRXCom.I2C.A.writeByte(GRXCom.REGISTER.COMMAND, cmd)

    ## Shutdown the Raspberry Pi
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  psm.Shutdown()
    #  @endcode
    @classmethod
    def shutdown(self):
        GRXCom.I2C.A.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.SHUTDOWN)

    ## Returns the input battery voltage
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  volts = psm.batteryVoltage()
    #  if(volts > 6):
    #      # do some task
    #  @endcode
    @classmethod
    def batteryVoltage(self):
        return GRXCom.I2C.A.readByte(GRXCom.REGISTER.BATTERY_VOLTAGE) * 0.04

    ## Returns the PiStorms firmware version
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  fwVersion = psm.getFirmwareVersion()
    #  print str(fwVersion)
    #  @endcode
    @classmethod
    def getFirmwareVersion(self):
        return GRXCom.I2C.A.readString(GRXCom.REGISTER.FIRMWARE_VERSION, 8).rstrip(chr(0x00))

    ## Returns the PiStorms vendor name
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  venName = psm.getVendorName()
    #  print str(venName)
    #  @endcode
    @classmethod
    def getVendorName(self):
        return GRXCom.I2C.A.readString(GRXCom.REGISTER.VENDOR_NAME, 8).rstrip(chr(0x00))

    ## Returns the PiStorms model name
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  model = psm.getDeviceModel()
    #  print str(model)
    #  @endcode
    @classmethod
    def getDeviceModel(self):
        return GRXCom.I2C.A.readString(GRXCom.REGISTER.DEVICE_MODEL, 8).rstrip(chr(0x00))

    ## Returns the PiStorms feature (read from bank A) (ex: "GRX-A")
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  feature = psm.getDeviceModel()
    #  print str(feature)
    #  @endcode
    @classmethod
    def getDeviceFeatures(self):
        return GRXCom.I2C.A.readString(GRXCom.REGISTER.FEATURE, 8).rstrip(chr(0x00))

    ## Writes to the specified RGB LED
    #  @param lednum The number to specify the LED (1 for BankA, 2 for BankB).
    #  @param red The red value to write to the specified LED (0-255).
    #  @param green The green value to write to the specified LED (0-255).
    #  @param blue The blue value to write to the specified LED (0-255).
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  psm.led(1,255,0,0)
    #  @endcode
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

    ## Wait until the GO button is pressed
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  psm.screen.termPrintln("Press GO to continue...")
    #  psm.waitForKeyPress()
    #  @endcode
    @classmethod
    def waitForKeyPress(self):
        self.untilKeyPress(time.sleep, 0.01)

    ## Repeat an action until the GO button is pressed
    #  @param func The function to be called repeatedly
    #  @param args Positional arguments to be passed to func
    #  @param kwargs Keyword arguments to be passed to func
    #  @warning Beware of scope issues! In Python, functions introduce a new scope.
    #  You might have to use the keyword "global" to achieve your intended behavior.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #
    #  def mainLoop():
    #      psm.screen.termPrintln(psm.battVoltage())
    #
    #  psm.untilKeyPress(mainLoop)
    #  @endcode
    @classmethod
    def untilKeyPress(self, func, *args, **kwargs):
        initialKeyPressCount = self.getKeyPressCount()
        while self.getKeyPressCount() == initialKeyPressCount:
            func(*args, **kwargs)

    ## Repeat an action until the GO button is pressed or the touchscreen is touched
    #  @param func The function to be called repeatedly
    #  @param args Positional arguments to be passed to func
    #  @param kwargs Keyword arguments to be passed to func
    #  @warning Beware of scope issues! In Python, functions introduce a new scope.
    #  You might have to use the keyword "global" to achieve your intended behavior.
    #  @note This is not a class method because it needs self.screen, an instance attribute
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #
    #  def mainLoop():
    #      psm.screen.termPrintln(psm.battVoltage())
    #
    #  psm.untilKeyPressOrTouch(mainLoop)
    #  @endcode
    def untilKeyPressOrTouch(self, func, *args, **kwargs):
        initialKeyPressCount = self.getKeyPressCount()
        while self.getKeyPressCount() == initialKeyPressCount and not self.screen.isTouched():
            func(*args, **kwargs)

    ## Repeat an action until the touchscreen is touched
    #  @param func The function to be called repeatedly
    #  @param args Positional arguments to be passed to func
    #  @param kwargs Keyword arguments to be passed to func
    #  @warning Beware of scope issues! In Python, functions introduce a new scope.
    #  You might have to use the keyword "global" to achieve your intended behavior.
    #  @note This is not a class method because it needs self.screen, an instance attribute
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #
    #  def mainLoop():
    #      psm.screen.termPrintln(psm.battVoltage())
    #
    #  psm.untilTouch(mainLoop)
    #  @endcode
    def untilTouch(self, func, *args, **kwargs):
        while not self.screen.isTouched():
            func(*args, **kwargs)

    ## Check if any function button is pressed
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  key = psm.getKeyValue()
    #  if(key == 0):
    #      # no function button is pressed
    #  @endcode
    @classmethod
    def getKeyPressValue(self): # F1-4
        return {0:0, 8:1, 16:2, 24:3, 40:4}[GRXCom.getKeyPressValue()]

    ## Check if F1 function button is pressed
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  if psm.isF1Pressed():
    #      # F1 is pressed, do some task
    #  @endcode
    @classmethod
    def isF1Pressed(self):
        return (GRXCom.getKeyPressValue() == 8)

    ## Check if F2 function button is pressed
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  if psm.isF1Pressed():
    #      # F2 is pressed, do some task
    #  @endcode
    @classmethod
    def isF2Pressed(self):
        return (GRXCom.getKeyPressValue() == 16)

    ## Check if F3 function button is pressed
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  if psm.isF1Pressed():
    #      # F3 is pressed, do some task
    #  @endcode
    @classmethod
    def isF3Pressed(self):
        return (GRXCom.getKeyPressValue() == 24)

    ## Check if F4 function button is pressed
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  if psm.isF1Pressed():
    #      # F4 is pressed, do some task
    #  @endcode
    @classmethod
    def isF4Pressed(self):
        return (GRXCom.getKeyPressValue() == 40)

    ## Returns the number of times the GO button has been pressed
    #  @see untilKeyPress
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  initialKeyPressCount = psm.getKeyPressCount()
    #  ...
    #  if(psm.getKeyPressCount() != initialKeyPressCount):
    #      # the GO button has been pressed at least once (or reset)
    #  @endcode
    @classmethod
    def getKeyPressCount(self):
        return GRXCom.I2C.A.readByte(GRXCom.REGISTER.GO_PRESS_COUNT)

    ## Resets the GO button press count to 0
    #  @see untilKeyPress
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms_GRX import PiStorms_GRX
    #  ...
    #  psm = PiStorms_GRX()
    #  psm.resetKeyPressCount()
    #  ...
    #  if(psm.getKeyPressCount() != 0):
    #      # the GO button has been pressed at least once
    #  @endcode
    @classmethod
    def resetKeyPressCount(self):
        GRXCom.I2C.A.writeByte(GRXCom.REGISTER.GO_PRESS_COUNT, 0)

    ### @cond Doxygen_ignore_this
    ## Pings the PiStorms for reliable I2C communication
    @classmethod
    def ping(self):
        GRXCom.ping()
    ### @endcond
