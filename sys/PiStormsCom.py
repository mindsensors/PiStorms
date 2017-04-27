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
#  July 2015  Henry     Initial Authoring 

from mindsensors_i2c import mindsensors_i2c
import time, math
import sys,os
import ctypes
import random
import json # for new touchscreen functionality

class PSSensor():

    PS_SENSOR_TYPE_NONE = 0
    PS_SENSOR_TYPE_SWITCH = 1
    PS_SENSOR_TYPE_ANALOG = 2
    PS_SENSOR_TYPE_LIGHT_ACTIVE = 3
    PS_SENSOR_TYPE_LIGHT_INACTIVE = 4
    PS_SENSOR_TYPE_SOUND_DB = 5
    PS_SENSOR_TYPE_SOUND_DBA = 6
    PS_SENSOR_TYPE_LOWSPEED_9V = 7
    PS_SENSOR_TYPE_LOWSPEED = 8
    PS_SENSOR_TYPE_CUSTOM = 9
    PS_SENSOR_TYPE_COLORFULL = 13
    PS_SENSOR_TYPE_COLORRED = 14
    PS_SENSOR_TYPE_COLORGREEN = 15
    PS_SENSOR_TYPE_COLORBLUE = 16
    PS_SENSOR_TYPE_COLORNONE = 17
    PS_SENSOR_TYPE_EV3_SWITCH = 18
    PS_SENSOR_TYPE_EV3 = 19
    
    
    PS_EV3CACHE_READY = 0
    PS_EV3CACHE_ID = 1
    PS_EV3CACHE_READY = 2
    PS_EV3CACHE_READY = 3
    PS_EV3CACHE_READY = 4
    
    
    
    sensornum = 0
    def __init__(self,bank,num):
        self.bank = bank
        self.sensornum = num
        self.type = self.PS_SENSOR_TYPE_NONE
        self.EV3Cache = [ 0, [0]*16, 0, 0, [0]*32 ] # ready, ID[16], mode, length, data[32]
    def setType(self,type):
        if(type != self.type):
            self.type = type
            if(self.sensornum == 1):
                self.bank.writeByte(PiStormsCom.PS_S1_Mode,type)
            if(self.sensornum == 2):
                self.bank.writeByte(PiStormsCom.PS_S2_Mode,type)
            if(self.type != self.PS_SENSOR_TYPE_CUSTOM):
                time.sleep(1)
    def getType(self):
        return self.type
    def EV3Retrieve(self):
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
    def isTouchedEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3_SWITCH)
        #self.EV3Retrieve()
        #return self.EV3Cache[4][0] == 1
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data) == 1
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data) == 1     
    def numTouchesEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3_SWITCH)
        #self.EV3Retrieve()
        #return self.EV3Cache[4][1]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data+1)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data+1)
    def resetTouchesEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3_SWITCH)
        if(self.sensornum == 1):
            self.bank.writeByte(PiStormsCom.PS_S1EV_Data + 1,0)
        if(self.sensornum == 2):
            self.bank.writeByte(PiStormsCom.PS_S2EV_Data + 1,0)
    def setModeEV3(self, mode):
        if(self.sensornum == 1):
            self.bank.writeByte(PiStormsCom.PS_S1EV_Mode,mode)
        if(self.sensornum == 2):
            self.bank.writeByte(PiStormsCom.PS_S2EV_Mode,mode)
    def distanceIREV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #raw1 = self.EV3Cache[4][0]
        #raw2 = self.EV3Cache[4][1]
        #return ctypes.c_short(raw1 | (raw2*256)).value
        if(self.sensornum == 1):
            return self.bank.readInteger(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readInteger(PiStormsCom.PS_S2EV_Data)
    def rawIREV3(self,mode):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(mode)
        #self.EV3Retrieve()
        #return self.EV3Cache[4]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data) 
    def headingIREV3(self,channel):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(1)
        #return ctypes.c_byte(self.rawIREV3(1)[(channel-1)*2]).value
        if(self.sensornum == 1):
            return self.bank.readByteSigned(PiStormsCom.PS_S1EV_Data + ((channel-1)*2))
        if(self.sensornum == 2):
            return self.bank.readByteSigned(PiStormsCom.PS_S2EV_Data + ((channel-1)*2))
    def distanceRemoteIREV3(self,channel):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(1)
        #return ctypes.c_byte(self.rawIREV3(1)[((channel-1)*2)+1]).value
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data + (((channel-1)*2)+1))
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data + (((channel-1)*2)+1))
    def remoteLeft(self,channel):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(2)
        #remote = self.rawIREV3(2)[channel-1]
        if(self.sensornum == 1):
            remote = self.bank.readByte(PiStormsCom.PS_S1EV_Data + (channel-1))
        if(self.sensornum == 2):
            remote = self.bank.readByte(PiStormsCom.PS_S2EV_Data + (channel-1))
        if(remote == 0 or remote == 3 or remote == 4):
            return 0
        if(remote == 1 or remote == 5 or remote == 6):
            return 1
        if(remote == 2 or remote == 7 or remote == 8):
            return -1
    def remoteRight(self,channel):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(2)
        #remote = self.rawIREV3(2)[channel-1]
        if(self.sensornum == 1):
            remote = self.bank.readByte(PiStormsCom.PS_S1EV_Data + (channel-1))
        if(self.sensornum == 2):
            remote = self.bank.readByte(PiStormsCom.PS_S2EV_Data + (channel-1))
        if(remote == 0 or remote == 1 or remote == 2):
            return 0
        if(remote == 3 or remote == 7 or remote == 5):
            return 1
        if(remote == 4 or remote == 6 or remote == 8):
            return -1
    def distanceUSEV3cm(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #raw1 = self.EV3Cache[4][0]
        #raw2 = self.EV3Cache[4][1]
        #return ctypes.c_short(raw1 | (raw2*256)).value
        if(self.sensornum == 1):
            return self.bank.readInteger(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readInteger(PiStormsCom.PS_S2EV_Data)
    def distanceUSEV3in(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(1)
        #self.EV3Retrieve()
        #raw1 = self.EV3Cache[4][0]
        #raw2 = self.EV3Cache[4][1]
        #return ctypes.c_short(raw1 | (raw2*256)).value
        if(self.sensornum == 1):
            return self.bank.readInteger(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readInteger(PiStormsCom.PS_S2EV_Data)
    def presenceUSEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(2)
        #self.EV3Retrieve()
        #return self.EV3Cache[4][0] == 1
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data) == 1
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data) == 1
    def rawGyro(self, mode):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(mode)
        #self.EV3Retrieve()
        #return self.EV3Cache[4]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data)
    def gyroAngleEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(0)
        #raw = self.rawGyro(0)
        #raw1 = raw[0]
        #raw2 = raw[1]
        #return ctypes.c_short(raw1 | (raw2*256)).value
        if(self.sensornum == 1):
            return self.bank.readIntegerSigned(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readIntegerSigned(PiStormsCom.PS_S2EV_Data)
    def gyroRateEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(1)
        #raw = self.rawGyro(1)
        #raw1 = raw[0]
        #raw2 = raw[1]
        #return ctypes.c_short(raw1 | (raw2*256)).value
        if(self.sensornum == 1):
            return self.bank.readIntegerSigned(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readIntegerSigned(PiStormsCom.PS_S2EV_Data)
    def reflectedLightSensorEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #return self.EV3Cache[4][0]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data)
    def ambientLightSensorEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(1)
        #self.EV3Retrieve()
        #return self.EV3Cache[4][0]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data)
    PS_SENSOR_COLOR_NONE = 0
    PS_SENSOR_COLOR_BLACK = 1
    PS_SENSOR_COLOR_BLUE = 2
    PS_SENSOR_COLOR_GREEN = 3
    PS_SENSOR_COLOR_YELLOW = 4
    PS_SENSOR_COLOR_RED = 5
    PS_SENSOR_COLOR_WHITE = 6
    PS_SENSOR_COLOR_BROWN = 7
    def colorSensorEV3(self):
        self.setType(self.PS_SENSOR_TYPE_EV3)
        self.setModeEV3(2)
        #self.EV3Retrieve()
        #return self.EV3Cache[4][0]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data)
    def readNXT(self):
        if(self.sensornum == 1):
            return self.bank.readInt(PiStormsCom.PS_S1EV_Ready)
        if(self.sensornum == 2):
            return self.bank.readInt(PiStormsCom.PS_S2EV_Ready)
    def isTouchedNXT(self):
        self.setType(self.PS_SENSOR_TYPE_SWITCH)
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #return self.EV3Cache[4][0] == 1
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data) == 1
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data) == 1
    def numTouchesNXT(self):
        self.setType(self.PS_SENSOR_TYPE_SWITCH)
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #return self.EV3Cache[4][1]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Data + 1)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Data + 1)
    def resetTouchesNXT(self):
        if(self.sensornum == 1):
            self.bank.writeByte(PiStormsCom.PS_S1EV_Data+1,0)
        if(self.sensornum == 2):
            self.bank.writeByte(PiStormsCom.PS_S2EV_Data+1,0)
    def lightSensorNXT(self, active=True):
        if(active):
            self.setType(self.PS_SENSOR_TYPE_LIGHT_ACTIVE)
        else:
            self.setType(self.PS_SENSOR_TYPE_LIGHT_INACTIVE)
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #return (self.EV3Cache[1][0]<<8 ) +self.EV3Cache[0]
        if(self.sensornum == 1):
            return self.bank.readInteger(PiStormsCom.PS_S1EV_Ready)
        if(self.sensornum == 2):
            return self.bank.readInteger(PiStormsCom.PS_S2EV_Ready)
        
    def SumoEyes(self, long = True):
        self.SE_None = 0
        self.SE_Front = 1
        self.SE_Left = 2
        self.SE_Right = 3
        if(long):
            self.setType(self.PS_SENSOR_TYPE_LIGHT_INACTIVE)
        else:
            self.setType(self.PS_SENSOR_TYPE_LIGHT_ACTIVE) 
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #if  self.SumoEyesisNear(465, 30,(self.EV3Cache[1][0]<<8 ) +self.EV3Cache[0]   ):
        if(self.sensornum == 1):
            if(self.SumoEyesisNear(465, 30, (self.bank.readInteger(PiStormsCom.PS_S1EV_Ready)))):
                return self.SE_Front
        #if  self.SumoEyesisNear(800, 30, (self.EV3Cache[1][0]<<8 ) +self.EV3Cache[0]  ):
            elif(self.SumoEyesisNear(800, 30, (self.bank.readInteger(PiStormsCom.PS_S1EV_Ready)))):
                return self.SE_Left
        #if  self.SumoEyesisNear(555, 30, (self.EV3Cache[1][0]<<8 ) +self.EV3Cache[0]  ):
            elif(self.SumoEyesisNear(555, 30, (self.bank.readInteger(PiStormsCom.PS_S1EV_Ready)))):
                return self.SE_Right
            else:
                return self.SE_None 
        if(self.sensornum == 2):
            if(self.SumoEyesisNear(465, 30, (self.bank.readInteger(PiStormsCom.PS_S2EV_Ready)))):
                return self.SE_Front
        #if  self.SumoEyesisNear(800, 30, (self.EV3Cache[1][0]<<8 ) +self.EV3Cache[0]  ):
            elif(self.SumoEyesisNear(800, 30, (self.bank.readInteger(PiStormsCom.PS_S2EV_Ready)))):
                return self.SE_Left
        #if  self.SumoEyesisNear(555, 30, (self.EV3Cache[1][0]<<8 ) +self.EV3Cache[0]  ):
            elif(self.SumoEyesisNear(555, 30, (self.bank.readInteger(PiStormsCom.PS_S2EV_Ready)))):
                return self.SE_Right
            else:
                return self.SE_None                  
        
    def SumoEyesisNear(self,reference, delta, comet):
        if (comet > (reference - delta)) and (comet < (reference + delta)):
            return True
        else:
            return False        
        
    def colorSensorRawNXT(self, smode = 13):
        self.setType(smode)
        self.setModeEV3(0)
        self.EV3Retrieve()
        return self.EV3Cache[0:1] + self.EV3Cache[1]
    def colorSensorNXT(self, smode = 13):
        self.setType(smode)
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #return self.EV3Cache[0]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Ready)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Ready)
    def colorSensorNoneNXT(self):
        return self.colorSensorRawNXT(self.PS_SENSOR_TYPE_COLORNONE)[0]
    def colorSensorRedNXT(self):
        return self.colorSensorRawNXT(self.PS_SENSOR_TYPE_COLORRED)[0]
    def colorSensorGreenNXT(self):
        return self.colorSensorRawNXT(self.PS_SENSOR_TYPE_COLORGREEN)[0]
    def colorSensorBlueNXT(self):
        return self.colorSensorRawNXT(self.PS_SENSOR_TYPE_COLORBLUE)[0]
    def analogSensor(self): #untested
        self.setType(self.PS_SENSOR_TYPE_ANALOG)
        self.setModeEV3(0)
        #self.EV3Retrieve()
        #return self.EV3Cache[0]
        if(self.sensornum == 1):
            return self.bank.readByte(PiStormsCom.PS_S1EV_Ready)
        if(self.sensornum == 2):
            return self.bank.readByte(PiStormsCom.PS_S2EV_Ready)
    def activateCustomSensorI2C(self):
        self.setType(self.PS_SENSOR_TYPE_CUSTOM)
        
    
    
class PSMotor():
    
    #bank = 0
    motornum = 0
    def __init__(self, bank, num):
        self.bank = bank
        self.motornum = num
    
    def pos(self):
        if(self.motornum == 1):
            return self.bank.readLongSigned(PiStormsCom.PS_Position_M1)
            
        elif(self.motornum == 2):
            return self.bank.readLongSigned(PiStormsCom.PS_Position_M2)
            
    def resetPos(self):
        if(self.motornum == 1):
            self.bank.writeByte(PiStormsCom.PS_Command, 114)
            
        elif(self.motornum == 2):
            self.bank.writeByte(PiStormsCom.PS_Command, 115)
         
    def setSpeedSync(self, speed):
        ctrl = 0
        ctrl |= PiStormsCom.PS_CONTROL_SPEED
        speed = int(speed)
        array = [speed, 0, 0, ctrl]
        self.bank.writeArray( PiStormsCom.PS_Speed_M1, array)
        self.bank.writeArray( PiStormsCom.PS_Speed_M2, array)
        # issue command 'S'
        self.bank.writeByte(PiStormsCom.PS_Command,PiStormsCom.S)

    def floatSync(self):
        self.bank.writeByte(PiStormsCom.PS_Command,PiStormsCom.c)

    def brakeSync(self):
        # Break while stopping; command C
        self.bank.writeByte(PiStormsCom.PS_Command,PiStormsCom.C)


    def setSpeed( self, speed):
        if(speed == 0):
            self.float()
            return
        
        ctrl = 0
        ctrl |= PiStormsCom.PS_CONTROL_SPEED
        
        #print speed
        speed = int(speed)
        
        
        ctrl |= PiStormsCom.PS_CONTROL_GO
        if (self.motornum == 1): 
            array = [speed, 0, 0, ctrl]
            self.bank.writeArray( PiStormsCom.PS_Speed_M1, array)
        if (self.motornum == 2):
            array = [speed, 0, 0, ctrl]
            self.bank.writeArray( PiStormsCom.PS_Speed_M2, array)
    def brake(self):
        if(self.motornum == 1):
            self.bank.writeByte(PiStormsCom.PS_Command, PiStormsCom.A)
        if(self.motornum == 2):
            self.bank.writeByte(PiStormsCom.PS_Command, PiStormsCom.B)
    def float(self):
        if(self.motornum == 1):
            self.bank.writeByte(PiStormsCom.PS_Command, PiStormsCom.a)
        if(self.motornum == 2):
            self.bank.writeByte(PiStormsCom.PS_Command, PiStormsCom.b)
    def hold(self):
        ctrl = 0
        ctrl |= PiStormsCom.PS_CONTROL_BRK
        ctrl |= PiStormsCom.PS_CONTROL_ON
        #ctrl |= PiStormsCom.PS_CONTROL_RELATIVE
        ctrl |= PiStormsCom.PS_CONTROL_TACHO
        ctrl |= PiStormsCom.PS_CONTROL_GO
        
        if(self.motornum == 1):
            self.bank.writeArray(PiStormsCom.PS_SetPoint_M1, [0,0,0,0])
            self.bank.writeByte(PiStormsCom.PS_CMDA_M1, ctrl)
        else:
            self.bank.writeArray(PiStormsCom.PS_SetPoint_M2, [0,0,0,0])
            self.bank.writeByte(PiStormsCom.PS_CMDA_M2, ctrl)

    def runSecs(self,secs,speed, brakeOnCompletion = False):
        ctrl = 0
        ctrl |= PiStormsCom.PS_CONTROL_SPEED
        ctrl |= PiStormsCom.PS_CONTROL_TIME
        if(brakeOnCompletion):
            ctrl |= PiStormsCom.PS_CONTROL_BRK
        ctrl |= PiStormsCom.PS_CONTROL_GO
        if(self.motornum == 1):
            array = [speed,secs,0,ctrl]
            self.bank.writeArray(PiStormsCom.PS_Speed_M1,array)
        if(self.motornum == 2):
            array = [speed,secs,0,ctrl]
            self.bank.writeArray(PiStormsCom.PS_Speed_M2,array)

    def status(self):
        if(self.motornum == 1):
            return self.bank.readByte(PiStormsCom.PS_Status_M1)
        if(self.motornum == 2):
            return self.bank.readByte(PiStormsCom.PS_Status_M2)
    def statusBit(self, bitno = 0):
        return (self.status() >> bitno) & 1
    def isBusy(self):
        return self.statusBit(0) == 1 or self.statusBit(1) == 1 or self.statusBit(3) == 1 or self.statusBit(6) == 1
    def waitUntilNotBusy(self, timeout=-1):
        while(self.isBusy()):
            time.sleep(.01)
            timeout -= 1
            if(timeout == 0):
                return 1
            if(timeout <-5):
                timeout = -1
            pass
        return 0
    def isStalled(self):
        return self.statusBit(7) == 1
    def isOverloaded(self):
        return self.statusBit(5) == 1
    def runDegs(self,degs,speed = 100,brakeOnCompletion = False, holdOnCompletion = False):
        # holdOnCompletion is not supported on LEGO motors.
        holdOnCompletion = False
        ctrl = 0
        ctrl |= PiStormsCom.PS_CONTROL_SPEED
        ctrl |= PiStormsCom.PS_CONTROL_TACHO
        ctrl |= PiStormsCom.PS_CONTROL_RELATIVE
        if(brakeOnCompletion):
            ctrl |= PiStormsCom.PS_CONTROL_BRK
        if(holdOnCompletion):
            ctrl |= PiStormsCom.PS_CONTROL_BRK
            ctrl |= PiStormsCom.PS_CONTROL_ON
        ctrl |= PiStormsCom.PS_CONTROL_GO
        
        b4 = (degs/0x1000000)
        b3 = ((degs%0x1000000)/0x10000)
        b2 = (((degs%0x1000000)%0x10000)/0x100)
        b1 = (((degs%0x1000000)%0x10000)%0x100)
        
        # b1 = degs & 0xFF
        # b2 = (degs >>8) & 0xFF
        # b3 = (degs >>16) & 0xFF
        # b4 = (degs >> 24) & 0xFF
        
        if(self.motornum == 1):
            array = [b1, b2, b3, b4, speed, 0, 0, ctrl]
            self.bank.writeArray(PiStormsCom.PS_SetPoint_M1, array) 
        if(self.motornum == 2):
            array = [b1, b2, b3, b4, speed, 0, 0, ctrl]
            self.bank.writeArray(PiStormsCom.PS_SetPoint_M2, array) 

    ## Reads the values of the PID control registers
    #  @param self The object pointer.
    def ReadPerformanceParameters(self):
        try:
            b0 = self.bank.readInteger(PiStormsCom.PS_P_Kp)
            b1 = self.bank.readInteger(PiStormsCom.PS_P_Ki)
            b2 = self.bank.readInteger(PiStormsCom.PS_P_Kd)
            b3 = self.bank.readInteger(PiStormsCom.PS_S_Kp)
            b4 = self.bank.readInteger(PiStormsCom.PS_S_Ki)
            b5 = self.bank.readInteger(PiStormsCom.PS_S_Kd)
            b6 = self.bank.readByte(PiStormsCom.PS_PassCount)
            b7 = self.bank.readByte(PiStormsCom.PS_PassTolerance)
            array = [b0, b1, b2, b3, b4, b5, b6, b7]
            return array
        except:
            print "Error: Could not read PID values"
            return []
            
    def SetPerformanceParameters(self, Kp_tacho, Ki_tacho, Kd_tacho, Kp_speed, Ki_speed, Kd_speed, passcount, tolerance):#untested
        Kp_t1 = Kp_tacho%0x100
        Kp_t2 = Kp_tacho/0x100    
        Ki_t1 = Ki_tacho%0x100
        Ki_t2 = Ki_tacho/0x100
        Kd_t1 = Kd_tacho%0x100
        Kd_t2 = Kd_tacho/0x100
        Kp_s1 = Kp_speed%0x100      
        Kp_s2 = Kp_speed/0x100
        Ki_s1 = Ki_speed%0x100 
        Ki_s2 = Ki_speed/0x100
        Kd_s1 = Kd_speed%0x100
        Kd_s2 = Kd_speed/0x100
        passcount = passcount
        tolerance = tolerance
        array = [Kp_t1 , Kp_t2 , Ki_t1, Ki_t2, Kd_t1, Kd_t2, Kp_s1, Kp_s2, Ki_s1, Ki_s2, Kd_s1, Kd_s2, passcount, tolerance]
        self.bank.writeArray(PiStormsCom.PS_P_Kp, array)       
    
## PiStormsCom: this class provides communication functions for PiStorms.
# do not use this class directly in user programs, instead use functions provided by LegoDevices or MsDevices class.
class PiStormsCom(object):

    PS_SENSOR_TYPE_NONE = 0
    PS_SENSOR_TYPE_SWITCH = 1
    PS_SENSOR_TYPE_ANALOG = 2
    PS_SENSOR_TYPE_LIGHT_REFLECTED = 3
    PS_SENSOR_TYPE_LIGHT_AMBIENT = 4
    PS_SENSOR_TYPE_SOUND_DB = 5
    PS_SENSOR_TYPE_SOUND_DBA = 6
    PS_SENSOR_TYPE_LOWSPEED_9V = 7
    PS_SENSOR_TYPE_LOWSPEED = 8
    PS_SENSOR_TYPE_CUSTOM = 9
    PS_SENSOR_TYPE_COLORFULL = 13
    PS_SENSOR_TYPE_COLORRED = 14
    PS_SENSOR_TYPE_COLORGREEN = 15
    PS_SENSOR_TYPE_COLORBLUE = 16
    PS_SENSOR_TYPE_COLORNONE = 17
    PS_SENSOR_TYPE_EV3_SWITCH = 18
    PS_SENSOR_TYPE_EV3 = 19

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

    PS_EV3CACHE_READY = 0
    PS_EV3CACHE_ID = 1
    PS_EV3CACHE_READY = 2
    PS_EV3CACHE_READY = 3
    PS_EV3CACHE_READY = 4

    PS_A_ADDRESS = 0x34
    PS_B_ADDRESS = 0x36
    
    # Registers
    PS_Command = 0x41
    
    PS_SetPoint_M1 =0x42
    PS_Speed_M1 = 0x46
    PS_Time_M1 = 0x47
    PS_CMDB_M1 = 0x48
    PS_CMDA_M1 = 0x49
    
    PS_SetPoint_M2 =0x4A
    PS_Speed_M2 = 0x4E
    PS_Time_M2 = 0x4F
    PS_CMDB_M2 = 0x50
    PS_CMDA_M2 = 0x51
    
    PS_Position_M1 = 0x52
    PS_Position_M2 = 0x56
    
    PS_Status_M1 = 0x5A
    PS_Status_M2 = 0x5B
    
    PS_Tasks_M1 = 0x5C
    PS_Tasks_M2 = 0x5D
    
    PS_P_Kp = 0x5E
    PS_P_Ki = 0x60
    PS_P_Kd = 0x62
    PS_S_Kp = 0x64
    PS_S_Ki = 0x66
    PS_S_Kd = 0x68
    PS_PassCount = 0x6A
    PS_PassTolerance = 0x6B
    PS_ChkSum = 0x6C
    PS_BattV = 0x6E
    # Sensor 1
    PS_S1_Mode = 0x6F
    # EV3
    PS_S1EV_Ready = 0x70
    PS_S1EV_SensorID = 0x71
    PS_S1EV_Mode = 0x81
    PS_S1EV_Length = 0x82
    PS_S1EV_Data = 0x83
    # LEGO Analog
    PS_S1AN_Read = 0x70
    # LEGO Color
    PS_S1C_Color = 0x70
    PS_S1C_R_cal = 0x71
    PS_S1C_G_cal = 0x72
    PS_S1C_B_cal = 0x73
    PS_S1C_N_cal = 0x74
    PS_S1C_R_raw = 0x75
    PS_S1C_G_raw = 0x76
    PS_S1C_B_raw = 0x77
    PS_S1C_N_raw = 0x78
    # Touchscreen Calibration
    PS_TS_CALIBRATION_DATA_READY = 0x70
    PS_TS_CALIBRATION_DATA = 0x71
    # Sensor 2
    PS_S2_Mode = 0xA3
    # EV3
    PS_S2EV_Ready = 0xA4
    PS_S2EV_SensorID = 0xA5
    PS_S2EV_Mode = 0xB5
    PS_S2EV_Length = 0xB6
    PS_S2EV_Data = 0xB7
    # LEGO Analog
    PS_S2AN_Read = 0xA4
    # LEGO Color
    PS_S2C_Color = 0xA4
    PS_S2C_R_cal = 0xA5
    PS_S2C_G_cal = 0xA6
    PS_S2C_B_cal = 0xA7
    PS_S2C_N_cal = 0xA8
    PS_S2C_R_raw = 0xA9
    PS_S2C_G_raw = 0xAA
    PS_S2C_B_raw = 0xAB
    PS_S2C_N_raw = 0xAC
    # LED 
    PS_R = 0xD7
    PS_G = 0xD8
    PS_B = 0xD9
    # Buttons
    PS_KeyPress = 0xDA
    PS_Key1Count = 0xDB
    PS_Key2Count = 0xDC
    
    PS_CONTROL_SPEED  = 0x01
    PS_CONTROL_RAMP   = 0x02
    PS_CONTROL_RELATIVE =  0x04
    PS_CONTROL_TACHO  = 0x08
    PS_CONTROL_BRK  =   0x10
    PS_CONTROL_ON    =  0x20
    PS_CONTROL_TIME  =   0x40
    PS_CONTROL_GO   =     0x80
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
    
    
    bankA = mindsensors_i2c(PS_A_ADDRESS >> 1)
    bankB = mindsensors_i2c(PS_B_ADDRESS >> 1)
    
    BAM1 = PSMotor(bankA,1)
    BAM2 = PSMotor(bankA,2)
    BBM1 = PSMotor(bankB,1)
    BBM2 = PSMotor(bankB,2)
    
    BAS1 = PSSensor(bankA,1)
    BAS2 = PSSensor(bankA,2)
    BBS1 = PSSensor(bankB,1)
    BBS2 = PSSensor(bankB,2)
    
    def __init__(self):
        try:
            self.bankA.readByte(self.PS_BattV)
        except:
            print "could not connect to pistorms"
        else:
            self.bankA.writeByte(self.PS_Command,self.R)
            self.bankB.writeByte(self.PS_Command,self.R)
        
        self.ts_cal = None # signified firmware version older than V2.10, use old touchscreen methods
        if self.GetFirmwareVersion() >= 'V2.10':
            # read touchscreen calibration values from cache file
            try:
                self.ts_cal = json.load(open('/tmp/ps_ts_cal', 'r'))
            except IOError:
                print 'Touchscreen Error: Failed to read touchscreen calibration values in PiStormsCom.py'
        
    def Shutdown(self):
        self.bankA.writeByte(self.PS_Command,self.H)
        
    def command(self, cmd, bank):
        if(bank == 1):
            self.bankA.writeByte(self.PS_Command,cmd)
        elif(bank == 2):
            self.bankB.writeByte(self.PS_Command,cmd)
            
    def battVoltage(self):
        try:
            return self.bankA.readByte(self.PS_BattV)*.040
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
                self.bankA.writeArray(self.PS_R, array)
            if(lednum == 2):
                array = [red, green, blue]
                self.bankB.writeArray(self.PS_R, array)
        except AttributeError:
            self.led(lednum,red,green,blue)
        time.sleep(.001)

    def isKeyPressed(self):
        x = 0
        try:
            x = self.bankA.readByte(self.PS_KeyPress)
            return int(0x01&x)
        except:
            return 0

    def getKeyPressValue(self):
        try:
            if self.ts_cal == None:
                return (self.bankA.readByte(self.PS_KeyPress))
            
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
            return(self.bankA.readByte(self.PS_Key1Count))
        except:
            return 0

    def resetKeyPressCount(self):
        try:
            self.bankA.writeByte(self.PS_Key1Count,0)
        except:
            pass

    def ping(self):
        self.bankA.readByte(0x00)

if __name__ == '__main__':
    psc = PiStormsCom()
    print "Version = "+ str(psc.GetFirmwareVersion())
    print "Vendor = "+ str(psc.GetVendorName())
    print "Device = "+ str(psc.GetDeviceId())
    try:
        while(True):
            print   psc.battVoltage()
            print psc.BAS1.SumoEyes(True)
            print psc.BAS2.colorSensorNXT()
            print psc.BBS1.lightSensorNXT(True)
            psc.BAM1.runSecs(1,100,True)
            psc.BBM1.runSecs(1,100,True)
            psc.BAM2.runSecs(1,100,True)
            psc.BBM2.runSecs(1,100,True)
            psc.BAM1.waitUntilNotBusy()
            
            psc.BAM1.runSecs(1,-100,True)
            psc.BBM1.runSecs(1,-100,True)
            psc.BAM2.runSecs(1,-100,True)
            psc.BBM2.runSecs(1,-100,True)
            psc.BAM1.waitUntilNotBusy()
            
            psc.BAM1.hold()
            psc.BAM2.hold()
            psc.BBM1.hold()
            psc.BBM2.hold()
            
            time.sleep(5)
            psc.BAM1.float()
            psc.BAM2.float()
            psc.BBM1.float()
            psc.BBM2.float()
            time.sleep(1)
            
    except KeyboardInterrupt:
        psc.BAM1.float()
        psc.BAM2.float()
        psc.BBM1.float()
        psc.BBM2.float()












