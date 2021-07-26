#!/usr/bin/env python3
#
# Copyright (c) 2016 mindsensors.com
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
# May 2016  Deepak      Initial authoring
# July 2016  Yug      Added OO functions.
# Mar 2017 Deepak     Removed COM class and PSMotor class

from mindsensors_i2c import mindsensors_i2c
from PiStormsCom import PiStormsCom
import time, math
import sys,os
import ctypes
import random

PS_SENSOR_MODE_EV3_COLOR_REFLECTED = 0
PS_SENSOR_MODE_EV3_COLOR_AMBIENT = 1
PS_SENSOR_MODE_EV3_COLOR_COLOR = 2
PS_SENSOR_MODE_EV3_GYRO_ANGLE =  0
PS_SENSOR_MODE_EV3_GYRO_RATE = 1
PS_SENSOR_MODE_EV3_ULTRASONIC_DIST_CM = 0
PS_SENSOR_MODE_EV3_ULTRASONIC_DIST_IN = 1
PS_SENSOR_MODE_EV3_ULTRASONIC_DETECT = 2
PS_SENSOR_MODE_EV3_IR_PROXIMITY = 0
PS_SENSOR_MODE_EV3_IR_CHANNEL = 1
PS_SENSOR_MODE_EV3_IR_REMOTE = 2
PS_SENSOR_MODE_NXT_LIGHT_REFLECTED = 0
PS_SENSOR_MODE_NXT_LIGHT_AMBIENT = 0
PS_SENSOR_MODE_NXT_COLOR_COLOR = 0

PS_SENSOR_TYPE_COLORFULL = 13
PS_SENSOR_TYPE_COLORRED = 14
PS_SENSOR_TYPE_COLORGREEN = 15
PS_SENSOR_TYPE_COLORBLUE = 16
PS_SENSOR_TYPE_COLORNONE = 17

## LegoSensor: This class provides functions for LEGOSensors
# This class will have derived classes for each sensor.
#  @remark
# There is no need to use this class directly in your program.
#

class LegoSensor(PiStormsCom):


    def __init__(self, port):
        if ( port == "BAS1" ):
            self.bank = self.bankA
            self.sensornum = 1
        elif ( port == "BAS2" ):
            self.bank = self.bankA
            self.sensornum = 2
        elif ( port == "BBS1" ):
            self.bank = self.bankB
            self.sensornum = 1
        elif ( port == "BBS2" ):
            self.bank = self.bankB
            self.sensornum = 2
        else:
            print ("no such port???")
        self.type = self.PS_SENSOR_TYPE_NONE
        self.EV3Cache = [ 0, [0]*16, 0, 0, [0]*32 ] # ready, ID[16], mode, length, data[32]

    ##
    #  Set the sensor type
    #  This function is called by the constructor of each sensor's class
    #  User programs don't need to call this function.
    #
    def setType(self, type):
        if(type != self.type):
            self.type = type
            if(self.sensornum == 1):
                self.bank.writeByte(self.PS_S1_Mode,type)
            if(self.sensornum == 2):
                self.bank.writeByte(self.PS_S2_Mode,type)
            if(self.type != self.PS_SENSOR_TYPE_CUSTOM):
                time.sleep(1)

    def getType(self):
        return self.type

    def setMode(self, mode):
        if(self.sensornum == 1):
            self.bank.writeByte(PiStormsCom.PS_S1EV_Mode,mode)
        if(self.sensornum == 2):
            self.bank.writeByte(PiStormsCom.PS_S2EV_Mode,mode)

    ##
    #  Retrieve the UART data buffer.
    #  This function is called internally when the UART data is needed.
    #  User programs don't need to call this function.
    #
    def retrieveUARTData(self):
        if(self.sensornum == 1):
            self.EV3Cache[0] = self.bank.readByte(PiStormsCom.PS_S1EV_Ready)
            self.EV3Cache[1] = self.bank.readArray(PiStormsCom.PS_S1EV_SensorID,16)
            self.EV3Cache[2] = self.bank.readByte(PiStormsCom.PS_S1EV_Mode)
            self.EV3Cache[3] = self.bank.readByte(PiStormsCom.PS_S1EV_Length)
            self.EV3Cache[4] = self.bank.readArray(PiStormsCom.PS_S1EV_Data,32)
        if(self.sensornum == 2):
            self.EV3Cache[0] = self.bank.readByte(PiStormsCom.PS_S2EV_Ready)
            self.EV3Cache[1] = self.bank.readArray(PiStormsCom.PS_S2EV_SensorID,16)
            self.EV3Cache[2] = self.bank.readByte(PiStormsCom.PS_S2EV_Mode)
            self.EV3Cache[3] = self.bank.readByte(PiStormsCom.PS_S2EV_Length)
            self.EV3Cache[4] = self.bank.readArray(PiStormsCom.PS_S2EV_Data,32)

    def readNXT(self):
        if(self.sensornum == 1):
            return self.bank.readInt(PiStormsCom.PS_S1AN_Read)
        if(self.sensornum == 2):
            return self.bank.readInt(PiStormsCom.PS_S2AN_Read)

## This class implements NXT Touch Sensor
# @code
# import LegoDevices
# # initialize a Touch sensor connected to BAS1
# touchSensor = LegoDevices.EV3TouchSensor("BAS1")
# # check if touched.
# touch = touchSensor.isPressed()
#  if(touch == True ):
#      # do some task
# @endcode
class NXTTouchSensor(LegoSensor):

    def __init__(self, port):
        super(self.__class__,self).__init__(port)
        self.setType(self.PS_SENSOR_TYPE_SWITCH)

    ## check if the sensor is touched,
    # @returns
    # True if it is touched.
    # @code
    # #
    # # create instance of touch sensor on port BAS1
    # touchSensor = LegoDevices.NXTTouchSensor("BAS1")
    # # read from NXT Touch Sensor
    # touch = touchSensor.isPressed()
    # # if touched, do something
    # if (touch == True):
    #     # do something
    # @endcode
    def isPressed(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data) == 1
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data) == 1

    ## With PiStorms it is possible to count how many times the sensor was touched.
    # This count is maintained since the PiStorms was powered on.
    # You can reset this count with resetBumpCount()
    # @returns
    # count of touches since last reset (or power on)
    #
    # @code
    # # Create an instance
    # touchSensor = LegoDevices.NXTTouchSensor("BAS1")
    #
    # # read the number of touches.
    # n = touchSensor.getBumpCount()
    #
    # if ( n > max_allowed):
    #     # do something
    #
    # @endcode
    def getBumpCount(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data+1)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data+1)

    ## With PiStorms it is possible to count how many times the sensor was touched.
    # This count is maintained since the PiStorms was powered on.
    # You can reset this count with resetBumpCount()
    def resetBumpCount(self):
        if(self.sensornum == 1):
            self.bank.writeByte(PiStormsCom.PS_S1EV_Data+1,0)
        if(self.sensornum == 2):
            self.bank.writeByte(PiStormsCom.PS_S2EV_Data+1,0)

class EV3TouchSensor(LegoSensor):

    def __init__(self, port):
        super(self.__class__,self).__init__(port)
        self.setType(self.PS_SENSOR_TYPE_EV3_SWITCH)

    ## check if the sensor is touched,
    # @returns
    # True if it is touched.
    # @code
    # #
    # # create instance of touch sensor on port BAS1
    # touchSensor = LegoDevices.NXTTouchSensor("BAS1")
    # # read from NXT Touch Sensor
    # touch = touchSensor.isPressed()
    # # if touched, do something
    # if (touch == True):
    #     # do something
    # @endcode
    def isPressed(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data) == 1
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data) == 1

    ## With PiStorms it is possible to count how many times the sensor was touched.
    # This count is maintained since the PiStorms was powered on.
    # You can reset this count with resetBumpCount()
    # @returns
    # count of touches since last reset (or power on)
    #
    # @code
    # # Create an instance
    # touchSensor = LegoDevices.EV3TouchSensor("BAS1")
    #
    # # read the number of touches.
    # n = touchSensor.getBumpCount()
    #
    # if ( n > max_allowed):
    #     # do something
    #
    # @endcode
    def getBumpCount(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data+1)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data+1)

    ## With PiStorms it is possible to count how many times the sensor was touched.
    # This count is maintained since the PiStorms was powered on.
    # You can reset this count with resetBumpCount()
    def resetBumpCount(self):
        if(self.sensornum == 1):
            self.bank.writeByte(PiStormsCom.PS_S1EV_Data+1,0)
        if(self.sensornum == 2):
            self.bank.writeByte(PiStormsCom.PS_S2EV_Data+1,0)


class NXTLightSensor(LegoSensor):
    def __init__(self, port, mode = PS_SENSOR_MODE_NXT_LIGHT_REFLECTED): #mode can be PS_SENSOR_MODE_NXT_LIGHT_[AMBIENT, REFLECTED]
        super(self.__class__,self).__init__(port)
        if mode==PS_SENSOR_MODE_NXT_LIGHT_AMBIENT:
            self.setType(self.PS_SENSOR_TYPE_LIGHT_AMBIENT)
        else:
            self.setType(self.PS_SENSOR_TYPE_LIGHT_REFLECTED)
        self.mode = mode
        self.setMode(mode)
    ## Read color value from the sensor
    def getValue(self):
        if(self.sensornum == 1):
            return self.bank.readInteger(PiStormsCom.PS_S1AN_Read)
        if(self.sensornum == 2):
            return self.bank.readInteger(PiStormsCom.PS_S2AN_Read)

class NXTColorSensor(LegoSensor):
    def __init__(self, port, mode = PS_SENSOR_TYPE_COLORFULL): #mode can be PS_SENSOR_MODE_NXT_COLOR_COLOR
        super(self.__class__,self).__init__(port)
        self.setType(13)
        self.mode = mode
        self.setMode(mode)
    ## read raw value from the sensor
    def rawValue(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1AN_Read)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2AN_Read)
    ## read color value from the sensor
    def getColor(self): #test
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1AN_Read)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2AN_Read)

    #def colorSensorNXT(self):#test
    #    if(self.sensornum == 1):
    #        return self.bank.readByte(PiStormsCom.PS_S1AN_Read)
    #    if(self.sensornum == 2):
    #        return self.bank.readByte(PiStormsCom.PS_S2AN_Read)

class EV3ColorSensor(LegoSensor):
    def __init__(self, port, mode = PS_SENSOR_MODE_EV3_COLOR_REFLECTED): #mode can be PS_SENSOR_MODE_EV3_COLOR_[AMBIENT, REFLECTED, COLOR]
        super(self.__class__,self).__init__(port)
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.mode = mode
        self.setMode(mode)
    ## Read value from the color sensor
    def getValue(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data)

class EV3GyroSensor(LegoSensor):
    def __init__(self, port, mode=PS_SENSOR_MODE_EV3_GYRO_ANGLE): #mode can be PS_SENSOR_MODE_EV3_GYRO_[ANGLE, RATE]
        super(self.__class__,self).__init__(port)
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.mode = mode
        self.setMode(mode)
    # read the raw value from the sensor.
    def rawValue(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data)
    # read value from the sensor (signed integer).
    def readValue(self):
        if(self.sensornum == 1):
            return self.bank.readIntegerSigned(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readIntegerSigned(PiStormsCom.PS_S2EV_Data)

class EV3UltrasonicSensor(LegoSensor):
    def __init__(self, port, mode=PS_SENSOR_MODE_EV3_ULTRASONIC_DIST_CM): #mode can be PS_SENSOR_MODE_EV3_ULTRASONIC_[DETECT, DIST_CM, DIST_IN]
        super(self.__class__,self).__init__(port)
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.mode = mode
        self.setMode(mode)
    def getDistance(self):
        if(self.sensornum == 1):
            return self.bank.readInteger(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readInteger(PiStormsCom.PS_S2EV_Data)
    def detect(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data) == 1
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data) == 1

class EV3InfraredSensor(LegoSensor):
    def __init__(self, port, mode=PS_SENSOR_MODE_EV3_IR_PROXIMITY): #mode can be PS_SENSOR_MODE_EV3_IR_[CHANNEL, PROXIMITY, REMOTE]
        super(self.__class__,self).__init__(port)
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.mode = mode
        self.setMode(mode)
    def readProximity(self):#unit?
        if(self.sensornum == 1):
            return self.bank.readInteger(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readInteger(PiStormsCom.PS_S2EV_Data)
    def readRaw(self):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data)
    def readChannelHeading(self,channel):
        if(self.sensornum == 1):
            return self.bank.readByteSigned(PiStormsCom.PS_S1EV_Data + ((channel-1)*2))
        if(self.sensornum == 2):
            return self.bank.readByteSigned(PiStormsCom.PS_S2EV_Data + ((channel-1)*2))
    def readChannelProximity(self,channel):
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data + (((channel-1)*2)+1))
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data + (((channel-1)*2)+1))
    def readRemote(self,channel):
        if(self.sensornum == 1):
            remote = self.bank.readByte(PiStormsCom.PS_S1EV_Data + (channel-1))
        if(self.sensornum == 2):
            remote = self.bank.readByte(PiStormsCom.PS_S2EV_Data + (channel-1))
        L = 999
        R = 999
        if(remote == 0 or remote == 3 or remote == 4):
            L=0
        if(remote == 1 or remote == 5 or remote == 6):
            L=1
        if(remote == 2 or remote == 7 or remote == 8):
            L=-1

        if(remote == 0 or remote == 1 or remote == 2):
            R=0
        if(remote == 3 or remote == 7 or remote == 5):
            R=1
        if(remote == 4 or remote == 6 or remote == 8):
            R=-1
        return (L, R)
