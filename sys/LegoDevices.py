#!/usr/bin/env python
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

from mindsensors_i2c import mindsensors_i2c
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
        self.bank.writeArray(self.PS_P_Kp, array)       
    
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
    
    
    bankA = mindsensors_i2c(PS_A_ADDRESS >> 1)
    bankB = mindsensors_i2c(PS_B_ADDRESS >> 1)
    
    # BAM1 = PSMotor(bankA,1)
    # BAM2 = PSMotor(bankA,2)
    # BBM1 = PSMotor(bankB,1)
    # BBM2 = PSMotor(bankB,2)
    
    # BAS1 = PSSensor(bankA,1)
    # BAS2 = PSSensor(bankA,2)
    # BBS1 = PSSensor(bankB,1)
    # BBS2 = PSSensor(bankB,2)
    
    def __init__(self):
        try:
            self.bankA.readByte(self.PS_BattV)
        except:
            print "could not connect to pistorms"
        else:
            self.bankA.writeByte(self.PS_Command,self.R)
            self.bankB.writeByte(self.PS_Command,self.R)
        
    def Shutdown(self):
        self.bankA.writeByte(self.PS_Command,self.H)
        
    def command(self, cmd, bank):
        if(bank == 1):
            self.bankA.writeByte(self.PS_Command,cmd)
        elif(bank == 2):
            self.bankB.writeByte(self.PS_Command,cmd)
            
    def battVoltage(self):
        return self.bankA.readByte(self.PS_BattV)*.040
    ##  Read the firmware version of the i2c device
    
    def GetFirmwareVersion(self):
        ver = self.bankA.readString(0x00, 8)
        return ver

    ##  Read the vendor name of the i2c device
    def GetVendorName(self):
        vendor = self.bankA.readString(0x08, 8)
        return vendor

    ##  Read the i2c device id
    def GetDeviceId(self):
        device = self.bankA.readString(0x10, 8)
        return device    
        
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
        return int(0x01&self.bankA.readByte(self.PS_KeyPress))
    def getKeyPressValue(self):
        return self.bankA.readByte(self.PS_KeyPress)
    def getKeyPressCountx(self):
        return self.bankA.readByte(self.PS_Key1Count)
    def resetKeyPressCount(self):
        self.bankA.writeByte(self.PS_Key1Count,0)
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
            print "no such port???"
        self.type = self.PS_SENSOR_TYPE_NONE
        self.EV3Cache = [0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0,0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

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
    def __init__(self, port, mode = PS_SENSOR_MODE_EV3_COLOR_REFLECTED): #mode can be PS_SENSOR_MODE_NXT_COLOR_COLOR
        super(self.__class__,self).__init__(port)
        self.setType(13)
        self.mode = mode
        self.setMode(mode)
    ## read raw value from the sensor
    def rawValue(self):
        self.retrieveUARTData()
        return self.EV3Cache[0:1] + self.EV3Cache[1]
    ## read color value from the sensor
    def getColor(self): #test
        self.retrieveUARTData()
        raw = self.EV3Cache[0:1] + self.EV3Cache[1]
        return raw[0]
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
            

#class SumoEyes

# class analogSensor(self): #untested
    # def __init__(self, port, mode=0):
        # super(self.__class__,self).__init__(port)
        # self.setType(self.PS_SENSOR_TYPE_ANALOG)
        # self.setMode(mode)
    # def getValue(self):
        # if(self.sensornum == 1):
            # return self.bank.readByte(PiStormsCom.PS_S1EV_Ready)
        # if(self.sensornum == 2):
            # return self.bank.readByte(PiStormsCom.PS_S2EV_Ready)

# class I2CSensor(self): 
    # def __init__(self):
        # self.setType(self.PS_SENSOR_TYPE_CUSTOM)



"""

TODO: also implement motor class & its functions here.

"""
