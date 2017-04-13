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
# Date      Author      Comments
# Mar 2017  Deepak      Initial Authoring

from mindsensors_i2c import mindsensors_i2c
from mindsensorsUI import mindsensorsUI
import time, math
import sys,os
import ctypes
import random
import json # for new touchscreen functionality

## GRXCom: this class provides communication functions for PiStorms-GRX.
# do not use this class directly in user programs, instead use functions provided by LegoDevices or MsDevices class.
class GRXCom(object):

    GRX_A_ADDRESS = 0x34
    GRX_B_ADDRESS = 0x36
    
    A1 = 0
    A2 = 1
    A3 = 2
    D1 = 3
    D2 = 4
    NONE = 0
    S1 = 1
    S2 = 2
    S3 = 3

    _NONE = 0
    _ANIN = 1
    _DO   = 2
    _DI   = 3
    _I2C  = 4
    _TAC2X = 5
    _SERIAL = 6

    HIGH = 1
    LOW = 0

    # Registers
    GRX_BattV = 0x6E
    GRX_Servo_Base = 0x42
    GRX_LED_Base  =  0xB6
    GRX_SA1_Base = 0x48
    GRX_SA2_Base = 0x5E
    GRX_SA3_Base = 0x74
    GRX_SD1_Base = 0x8A
    GRX_SD2_Base = 0xA0
    GRX_KEY1_Count = 0xBA

    # ???
    GRX_KEY_Press = 0xB9

    # Registers
    GRX_Command = 0x41
    
    #Supported I2C commands
    R = 0x52
    S = 0x53
    a = 0x61
    b = 0x62
    c = 0x63
    A = 0x41
    B = 0x42
    C = 0x43
    H = 0x48
    E = 0x45
    t = 0x74
    T = 0x54
    w = 0x77
    l = 0x6C
    
    
    bankA = mindsensors_i2c(GRX_A_ADDRESS >> 1)
    bankB = mindsensors_i2c(GRX_B_ADDRESS >> 1)
    
    def __init__(self):
        try:
            self.bankA.readByte(self.GRX_BattV)
        except:
            print "could not connect to pistorms-grx"
        else:
            self.bankA.writeByte(self.GRX_Command,self.R)
            self.bankB.writeByte(self.GRX_Command,self.R)
        
        self.ts_cal = None # signified firmware version older than V2.10, use old touchscreen methods
        if self.GetFirmwareVersion() >= 'V2.10':
            # read touchscreen calibration values from cache file
            try:
                self.ts_cal = json.load(open('/tmp/ps_ts_cal', 'r'))
            except IOError:
                print 'Touchscreen Error: Failed to read touchscreen calibration values in PiStormsCom.py'
        
    def Shutdown(self):
        self.bankA.writeByte(self.GRX_Command,self.H)
        
    def command(self, cmd, bank):
        if(bank == 1):
            self.bankA.writeByte(self.GRX_Command,cmd)
        elif(bank == 2):
            self.bankB.writeByte(self.GRX_Command,cmd)
            
    def battVoltage(self):
        try:
            return self.bankA.readByte(self.GRX_BattV)*.040
        except:
            return 0
    ##  Read the firmware version of the i2c device
    
    def GetFirmwareVersion(self):
        try:
            ver = self.bankA.readString(0x00, 8)
            return ver
        except:
            return "ReadErr"

    ##  Read the vendor name of the i2c device
    def GetVendorName(self):
        try:
            vendor = self.bankA.readString(0x08, 8)
            return vendor
        except:
            return "ReadErr"

    ##  Read the i2c device id
    def GetDeviceId(self):
        try:
            device = self.bankA.readString(0x10, 8)
            return device    
        except:
            return "ReadErr"

    ##  Read the features from device
    def GetDeviceFeatures(self):
        try:
            features = self.bankA.readString(0x18, 8)
            return features    
        except:
            return "ReadErr"
        
    def led(self,lednum,red,green,blue):
        try:
            if(lednum == 1):
                array = [red, green, blue]
                self.bankA.writeArray(self.GRX_LED_Base, array)
            if(lednum == 2):
                array = [red, green, blue]
                self.bankB.writeArray(self.GRX_LED_Base, array)

        except AttributeError:
            pass
        time.sleep(.001)

    def isKeyPressed(self):
        x = 0
        try:
            x = self.bankA.readByte(self.GRX_KEY_Press)
            return int(0x01&x)
        except:
            return 0

    def getKeyPressValue(self):
        try:
            if self.ts_cal == None:
                return (self.bankA.readByte(self.GRX_KEY_Press))
            
            # if self.ts_cal doesn't exist because it failed to load touchscreen calibration values in __init__, the surrounding try/except block here will handle returning 0 as the default/error value
            x1 = self.ts_cal['x1']
            y1 = self.ts_cal['y1']
            x2 = self.ts_cal['x2']
            y2 = self.ts_cal['y2']
            x3 = self.ts_cal['x3']
            y3 = self.ts_cal['y3']
            x4 = self.ts_cal['x4']
            y4 = self.ts_cal['y4']
            
            x = self.bankA.readInteger(0xE7) # current x
            # x1 and x2 are the left-most calibration points. We want to take whichever value is furthest right, to give the maximum touch area for the software buttons that make sense. x4 is the right-top calibration point. If x4 > x1 then 0 is towards the left so the the greater value of x1 and x2 will be the rightmost. If not, then high numbers are towards the left so we the lesser value of x1 and x2 will be rightmost.
            # We don't take a calibration point in the left gutter, so we have to assume 200 is the greatest reasonable width of this area. If the current touched x point is right of the border, then it is on the touchscreen so return 0 (because none of the software buttons are being pressed). If the value is between the border and 200 points left of that, continue on as the touch point is in the software button area, If the value is further than 200 points left of the border, it is likely an erroneous error caused by the touchscreen not being touched.
            if x4 > x1: # lower values left
                xborder = max(x1, x2) # where the touchscreen ends and the software buttons begin
                if not xborder+100 > x > xborder-200:
                    return 0
            else: # greater values left
                xborder = min(x1, x2)
                if not xborder-100 < x < xborder+200:
                    return 0
            
            y = self.bankA.readInteger(0xE9) # current y
            # the lower and greater of the two left-most y calibration values
            # TODO: does this assume the screen is not flipped vertically? Be sure to test this
            ymin = min(y1, y2)
            ymax = max(y1, y2)
            yQuarter = (ymax-ymin)/4 # a quarter of the distance between the two y extremes
            
            if y < ymin + 0 * yQuarter:
                return 0 # too low
            if y < ymin + 1 * yQuarter:
                return 8
            if y < ymin + 2 * yQuarter:
                return 16
            if y < ymin + 3 * yQuarter:
                return 24
            if y < ymin + 4 * yQuarter:
                return 40
            if y >= ymin + 4 * yQuarter:
                return 0 # too high
            
            return 0 # some other weird error occured, execution should not reach this point
        except:
            return 0

    def getKeyPressCount(self):
        try:
            return(self.bankA.readByte(self.GRX_KEY1_Count))
        except:
            return 0

    def resetKeyPressCount(self):
        try:
            self.bankA.writeByte(self.GRX_KEY1_Count,0)
        except:
            pass

    def ping(self):
        self.bankA.readByte(0x00)


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
# TODO: Add encoder support
class RCServo(GRXCom):

    ## Initialize an RC servo object.
    #  @param port Must be a valid port, one of [BAM1, BAM2, BAM3, BBM1, BBM2, BBM3].
    #              The first two characters are "BA" or "BB", for "Bank A" or "Bank B".
    #              The third character is 'M' for "Motor". The fourth character
    #              is the pin number. See the RCServo class documentation for details.
    #  @ param neutralPoint You may specify the neutral point of this servo.
    #                       The default is 1500, but as a result of the manufacturing
    #                       process for these servos each has a slightly different
    #                       neutral point. For example, if your continuous rotation
    #                       servo continues to spin when you call setNeutral, it likely
    #                       has the wrong neutral point set. You can update this
    #                       at any time with setNeutralPoint(self, neutralPoint).
    def __init__(self, port=None, neutralPoint=1500):
        if port == None:
            raise TypeError('You must specify a port as an argument')

        try:
            if not len(port) == 4:
                raise TypeError()
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
