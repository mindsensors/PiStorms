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
# Date      Author          Comments
# Mar 2017  Deepak          Initial Authoring
# Apr 2017  Seth Tenembaum  Implement additional Grove sensors

from mindsensors_i2c import mindsensors_i2c
from PiStorms_GRX import *
import math, time

class GroveSensor(GRXCom):

    GRX_SENSOR_TYPE_NONE = 0
    GRX_SENSOR_TYPE_ANALOG = 1
    GRX_SENSOR_TYPE_DIGITAL = 2
    GRX_SENSOR_TYPE_I2C = 3

    def __init__(self, port=None):
        if port == None:
            raise TypeError('You must specify a port as an argument')

        self.port = port
        if ( port == "BAA1" ):
            self.bank = self.bankA
            self.sensornum = 0
        elif ( port == "BAA2" ):
            self.bank = self.bankA
            self.sensornum = 1
        elif ( port == "BAA3" ):
            self.bank = self.bankA
            self.sensornum = 2

        elif ( port == "BBA1" ):
            self.bank = self.bankB
            self.sensornum = 0
        elif ( port == "BBA2" ):
            self.bank = self.bankB
            self.sensornum = 1
        elif ( port == "BBA3" ):
            self.bank = self.bankB
            self.sensornum = 2

        elif ( port == "BAD1" ):
            self.bank = self.bankA
            self.sensornum = 3
        elif ( port == "BAD2" ):
            self.bank = self.bankA
            self.sensornum = 4

        elif ( port == "BBD1" ):
            self.bank = self.bankB
            self.sensornum = 3
        elif ( port == "BBD2" ):
            self.bank = self.bankB
            self.sensornum = 4

        else:
            self.bank = None
            self.sensornum = 0
            self.type = self.GRX_SENSOR_TYPE_NONE
            raise ValueError ('No such port: %s' %(port))

    def verifyPort(self):
        #
        # ports A1,A2,A3:
        # allows analog as well as digital sensors, does not allow tachometers.
        #
        # port D1,D2:
        # allows digital sensors or tachometer inputs
        # does not allow analog sensors
        #
        if ( self.type == self.GRX_SENSOR_TYPE_ANALOG ):
            if ( self.port == "BAD1" or self.port == "BAD2" or
                 self.port == "BBD1" or self.port == "BBD2" ):
                    raise ValueError ('Analog sensor not supported on: %s' %(self.port ))

    def setType(self, type, mode=0):
        addr = self.GRX_SA1_Base +(self.sensornum*22)
        self.type = type
        if ( type == self.GRX_SENSOR_TYPE_DIGITAL):
            _type = self._DI
        elif ( type == self.GRX_SENSOR_TYPE_ANALOG):
            _type = self._ANIN

        self.bank.writeByte(addr, _type)
        self.bank.writeByte(addr+1, mode)
        
    def digitalInput(self):
        reg = self.GRX_SA1_Base +(self.sensornum*22)+4
        return (self.bank.readByte(reg))

    def analogInput(self):
        reg = self.GRX_SA1_Base +(self.sensornum*22)
        x = self.bank.readByte(reg)
        if (x == 1):
            y = self.bank.readByte(reg+4)
            z = self.bank.readByte(reg+5)
            return (y + (z*256))
        else:
            return 0

class Grove_Digital_Sensor(GroveSensor):
    def __init__(self, port=None):
        super(Grove_Digital_Sensor,self).__init__(port)
        self.setType(self.GRX_SENSOR_TYPE_DIGITAL)
        self.verifyPort()

    def readValue(self):
        return self.digitalInput()

class Grove_Analog_Sensor(GroveSensor):
    def __init__(self, port=None):
        super(Grove_Analog_Sensor,self).__init__(port)
        self.setType(self.GRX_SENSOR_TYPE_ANALOG)
        self.verifyPort()

    def readValue(self):
        return self.analogInput()

## Grove_Button: This class supports Grove Button v1.1
#  Documentation: http://wiki.seeed.cc/Grove-Button/
class Grove_Button(Grove_Digital_Sensor):
    def isPressed(self):
        return self.readValue()

## Grove_PIR_Motion_Sensor: This class supports Grove PIR Motion Sensor v1.2
#  Documentation: http://wiki.seeed.cc/Grove-PIR_Motion_Sensor/
class Grove_PIR_Motion_Sensor(Grove_Digital_Sensor):
    def motionDetected(self):
        return self.readValue()

## Grove_Luminance_Sensor: This class supports Grove Luminance Sensor v1.0
#  Documentation: http://wiki.seeed.cc/Grove-Luminance_Sensor/
class Grove_Luminance_Sensor(Grove_Analog_Sensor):
    # TODO: untested
    def luminance(self):
        val = self.readValue() * (3.0 / 4096.0)

        vout = [ 0.0011498,  0.0033908,  0.011498,  0.041803,  0.15199,  0.53367,  1.3689,  1.9068,  2.3  ]
        lux  = [ 1.0108,     3.1201,     9.8051,    27.43,     69.545,   232.67,   645.11,  73.52,   1000 ]

        # take care the value is within range
        if (val <= vout[0]):  return lux[0]
        if (val >= vout[-1]): return lux[-1]

        # search right interval
        pos = 1 # _in[0] allready tested
        while (val > vout[pos]): pos = pos + 1

        # this will handle all exact "points" in the _in array
        if (val == vout[pos]): return lux[pos]

        # interpolate in the right segment for the rest
        return (val - vout[pos-1]) * (lux[pos] - lux[pos-1]) / (vout[pos] - vout[pos-1]) + lux[pos-1]

## Grove_Light_Sensor: This class supports Grove Light Sensor v1.1
#  Documentation: http://wiki.seeed.cc/Grove-Light_Sensor/
class Grove_Light_Sensor(Grove_Analog_Sensor):
    def lightLevel(self):
        return self.readValue()

## Grove_Temperature_Sensor: This class supports Grove Temperature Sensor v1.2
#  Documentation: http://wiki.seeed.cc/Grove-Temperature_Sensor_V1.2/
class Grove_Temperature_Sensor(Grove_Analog_Sensor):
    # LM358 8AK YTM1430
    # TODO: readings do not seem to be correct
    def temperature(self):
        B = 4275 # B value of the thermistor
        a = self.readValue()
        R = (4096.0 / a) - 1.0 # or 4095.0?
        temperature = 1.0 / (math.log(R)/B + 1/298.15) - 273.15 # convert to temperature via datasheet
        return temperature

## Grove_UV_Sensor: This class supports Grove UV Sensor v1.1
#  Documentation: http://wiki.seeed.cc/Grove-UV_Sensor/
class Grove_UV_Sensor(Grove_Analog_Sensor):
    # TODO: untested
    def getUVindex(self):
        val = 0
        for i in range(32): # take many readings
            val = val + self.readValue()
            time.sleep(0.02)
        val = val / 32 # mean value

        return (val*1000/4.3 - 83) / 21

## Grove_Moisture_Sensor: This class supports Grove Moisture Sensor v1.4
#  Documentation: http://wiki.seeed.cc/Grove-Moisture_Sensor/
class Grove_Moisture_Sensor(Grove_Analog_Sensor):
    def moistureLevel(self):
        return self.readValue()

## Grove_Sound_Sensor: This class supports Grove Sound Sensor v1.6
#  Documentation: http://wiki.seeed.cc/Grove-Sound_Sensor/
class Grove_Sound_Sensor(Grove_Analog_Sensor):
    def soundIntensity(self):
        return self.readValue()

## Grove_Sunlight_Sensor: This class supports Grove Sunlight Sensor v1.4
#  Documentation: http://wiki.seeed.cc/Grove-Sunlight_Sensor/
class Grove_Sunlight_Sensor(mindsensors_i2c):
    # Commands
    SI114X_SET = 0xA0
    SI114X_RESET = 0x01
    SI114X_PSALS_AUTO = 0x0F

    # I2C Registers
    SI114X_INT_CFG    = 0x03
    SI114X_IRQ_ENABLE = 0x04
    SI114X_IRQ_MODE1  = 0x05
    SI114X_IRQ_MODE2  = 0x06
    SI114X_HW_KEY     = 0x07
    SI114X_MEAS_RATE0 = 0x08
    SI114X_MEAS_RATE1 = 0x09
    SI114X_PS_LED21   = 0x0F
    SI114X_UCOEFF0    = 0x13
    SI114X_UCOEFF1    = 0x14
    SI114X_UCOEFF2    = 0x15
    SI114X_UCOEFF3    = 0x16
    SI114X_WR         = 0x17
    SI114X_COMMAND    = 0x18
    SI114X_IRQ_STATUS         = 0x21
    SI114X_ALS_VIS_DATA0      = 0x22
    SI114X_ALS_IR_DATA0       = 0x24
    SI114X_AUX_DATA0_UVINDEX0 = 0x2C
    SI114X_RD                 = 0x2E

    # Parameters
    SI114X_CHLIST          = 0x01
    SI114X_CHLIST_ENUV     = 0x80
    SI114X_CHLIST_ENALSIR  = 0x20
    SI114X_CHLIST_ENALSVIS = 0x10
    SI114X_CHLIST_ENPS1    = 0x01
    SI114X_PSLED12_SELECT  = 0x02
    SI114X_PSLED3_SELECT   = 0x03
    SI114X_PS1_ADCMUX      = 0x07
    SI114X_PS_ADC_COUNTER  = 0x0A
    SI114X_PS_ADC_GAIN     = 0x0B
    SI114X_PS_ADC_MISC     = 0x0C
    SI114X_ALS_VIS_ADC_COUNTER = 0x10
    SI114X_ALS_VIS_ADC_GAIN    = 0x11
    SI114X_ALS_VIS_ADC_MISC    = 0x12
    SI114X_ALS_IR_ADC_COUNTER  = 0x1D
    SI114X_ALS_IR_ADC_GAIN     = 0x1E
    SI114X_ALS_IR_ADC_MISC     = 0x1F

    # User settings
    SI114X_ADCMUX_LARGE_IR  = 0x03
    SI114X_PSLED12_SELECT_PS1_LED1 = 0x01
    SI114X_ADC_GAIN_DIV1 = 0x00
    SI114X_LED_CURRENT_22MA = 0x03
    SI114X_ADC_COUNTER_511ADCCLK = 0x07 # recovery period the ADC takes before making a PS measurement
    SI114X_ADC_MISC_HIGHRANGE = 0x20
    SI114X_ADC_MISC_ADC_RAWADC = 0x04
    SI114X_INT_CFG_INTOE = 0x01
    SI114X_IRQEN_ALS = 0x01


    ## Initialize the class with the i2c address of your LineLeader
    #  @param i2c_address Address of your LineLeader TODO:(?)
    #  @remark
    def __init__(self, address=0x60):
        mindsensors_i2c.__init__(self, address)        
        self.reset()
        self.deInit()

    def deInit(self):
        # initialize the device with Grove sensor-specifications.
        self.writeByte(self.SI114X_UCOEFF0, 0x29)
        self.writeByte(self.SI114X_UCOEFF1, 0x89)
        self.writeByte(self.SI114X_UCOEFF2, 0x02)
        self.writeByte(self.SI114X_UCOEFF3, 0x00)
        self.writeParamData(self.SI114X_CHLIST, self.SI114X_CHLIST_ENUV | self.SI114X_CHLIST_ENALSIR | self.SI114X_CHLIST_ENALSVIS | self.SI114X_CHLIST_ENPS1)

        # set LED1 current (22.4mA) (it is a normal value for many LED)
        self.writeParamData(self.SI114X_PS1_ADCMUX, self.SI114X_ADCMUX_LARGE_IR)
        self.writeByte(self.SI114X_PS_LED21, self.SI114X_LED_CURRENT_22MA)
        self.writeParamData(self.SI114X_PSLED12_SELECT, self.SI114X_PSLED12_SELECT_PS1_LED1)

        # PS ADC setting
        self.writeParamData(self.SI114X_PS_ADC_GAIN,    self.SI114X_ADC_GAIN_DIV1)
        self.writeParamData(self.SI114X_PS_ADC_COUNTER, self.SI114X_ADC_COUNTER_511ADCCLK)
        self.writeParamData(self.SI114X_PS_ADC_MISC,    self.SI114X_ADC_MISC_HIGHRANGE | self.SI114X_ADC_MISC_ADC_RAWADC)

        # VIS ADC setting
        self.writeParamData(self.SI114X_ALS_VIS_ADC_GAIN,    self.SI114X_ADC_GAIN_DIV1)
        self.writeParamData(self.SI114X_ALS_VIS_ADC_COUNTER, self.SI114X_ADC_COUNTER_511ADCCLK)
        self.writeParamData(self.SI114X_ALS_VIS_ADC_MISC,    self.SI114X_ADC_MISC_HIGHRANGE)

        # IR ADC setting
        self.writeParamData(self.SI114X_ALS_IR_ADC_GAIN,    self.SI114X_ADC_GAIN_DIV1)
        self.writeParamData(self.SI114X_ALS_IR_ADC_COUNTER, self.SI114X_ADC_COUNTER_511ADCCLK)
        self.writeParamData(self.SI114X_ALS_IR_ADC_MISC,    self.SI114X_ADC_MISC_HIGHRANGE)

        # interrupt enable
        self.writeByte(self.SI114X_INT_CFG,    self.SI114X_INT_CFG_INTOE)
        self.writeByte(self.SI114X_IRQ_ENABLE, self.SI114X_IRQEN_ALS)

        # auto run
        self.writeByte(self.SI114X_MEAS_RATE0, 0xFF)
        self.writeByte(self.SI114X_COMMAND, self.SI114X_PSALS_AUTO)

    def reset(self):
        self.writeByte(self.SI114X_MEAS_RATE0, 0)
        self.writeByte(self.SI114X_MEAS_RATE1, 0)
        self.writeByte(self.SI114X_IRQ_ENABLE, 0)
        self.writeByte(self.SI114X_IRQ_MODE1,  0)
        self.writeByte(self.SI114X_IRQ_MODE2,  0)
        self.writeByte(self.SI114X_INT_CFG,    0)
        self.writeByte(self.SI114X_IRQ_STATUS, 0xFF)

        self.writeByte(self.SI114X_COMMAND, self.SI114X_RESET)
        time.sleep(0.01)
        self.writeByte(self.SI114X_HW_KEY, 0x17)
        time.sleep(0.01)

    def writeParamData(self, reg, value):
        self.writeByte(self.SI114X_WR, value)
        self.writeByte(self.SI114X_COMMAND, reg | self.SI114X_SET)
        return self.readByte(self.SI114X_RD)

    def readIR(self):
        return self.readInteger(self.SI114X_ALS_IR_DATA0)

    def readVisible(self):
        return self.readInteger(self.SI114X_ALS_VIS_DATA0)

    def readUV(self):
        return self.readInteger(self.SI114X_AUX_DATA0_UVINDEX0)
