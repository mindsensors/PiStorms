#!/usr/bin/env python3
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
from PiStormsCom_GRX import GRXCom
from PiStorms_GRX import GrovePort
import math, time

## This class supports the Grove Button v1.1
#
#  The Grove Button is a momentary push button. The button will release when you let go.
#
#  Documentation: http://wiki.seeed.cc/Grove-Button/
#
#  @code
#  import GroveDevices
#  # initialize a button connected to Bank A digital 1
#  button = GroveDevices.Grove_Button("BAD1")
#  if (button.isPressed()):
#    print("Pointless button pressed (warning: pointless).")
#  @endcode
class Grove_Button(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.DIGITAL_INPUT)
    ## @ return True if the button is pressed, False if the button is released
    def isPressed(self):
        return self.readValue() == 1

## This class supports the Grove PIR Motion Sensor v1.2
#
#  The Grove PIR Motion Sensor allows you to sense motion withing its range.
#  You can change whether or not it is retriggerable with an on-board jumper.
#
#  Documentation: http://wiki.seeed.cc/Grove-PIR_Motion_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a PIR motion sensor connected to Bank A digital 1
#  button = GroveDevices.Grove_PIR_Motion_Sensor("BAD1")
#  if (button.motionDetected()):
#    print("I see you, hi there!")
#  @endcode
class Grove_PIR_Motion_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.DIGITAL_INPUT)
    ## @ return True if motion is detected, False otherwise
    def motionDetected(self):
        return self.readValue() == 1

## This class supports the Grove Flame Sensor v1.1
#
#  This sensor can detect fire in front of it and is essential in a fire-fighting robot game.
#  It can also detect "other light sources of the wavelength in the range of 760nm - 1100 nm."
#
#  Documentation: http://wiki.seeed.cc/Grove-Flame_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a flame sensor connected to Bank A digital 1
#  f = GroveDevices.Grove_Flame_Sensor("BAD1")
#  if (f.fireDetected()):
#    print("Fire! Fire!!")
#  @endcode
class Grove_Flame_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.DIGITAL_INPUT)
    ## @ return True if infrared light is found in a line straight in front of
    #           the sensor (looks like a black LED), False otherwise
    def fireDetected(self):
        return self.readValue() == 1

## This class supports the Grove LED Socket Kit v1.4
#
#  This simple Grove module lets you connect and LED and turn it on or off.
#  You can use it for a power light, a simple status indicator,
#  or anything else you might use and LED for.
#
#  Documentation: http://wiki.seeed.cc/Grove-LED_Socket_Kit/
#
#  @code
#  import time
#  import GroveDevices
#  # initialize a Grove LED connected to Bank A digital 1
#  led = GroveDevices.Grove_LED_Socket("BAD1")
#  led.setLED(True)
#  time.sleep(1)
#  led.setLED(False)
#  @endcode
class Grove_LED_Socket(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.DIGITAL_OUTPUT)
    def setLED(self, state):
        self.writeValue(1 if state else 0)
    def on(self):
        self.writeValue(1)
    def off(self):
        self.writeValue(0)

## This class supports the Grove Buzzer v1.2
#
#  The Grove Buzzer uses a piezoelectric buzzer to produce an audible tone.
#
#  Documentation: http://wiki.seeed.cc/Grove-Buzzer/
#
#  @code
#  import time
#  import GroveDevices
#  # initialize a Grove Buzzer connected to Bank A digital 1
#  buzzer = GroveDevices.Grove_Buzzer("BAD1")
#  buzzer.on()
#  time.sleep(1)
#  buzzer.off()
#  @endcode
class Grove_Buzzer(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.DIGITAL_OUTPUT)
    def setBuzz(self, state):
        self.writeValue(1 if state else 0)
    def on(self):
        self.writeValue(1)
    def off(self):
        self.writeValue(0)

## This class supports the Grove Luminance Sensor v1.0
#
#  The Grove Luminance Sensor detects the ambient light level.
#
#  Documentation: http://wiki.seeed.cc/Grove-Luminance_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a luminance sensor connected to Bank A analog 1
#  lum = GroveDevices.Grove_Luminance_Sensor("BAA1")
#  if (lum.luminance() < 20.0):
#    print("Someone turn on the lights, I can't see anything!")
#  @endcode
class Grove_Luminance_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.ANALOG_INPUT)

    ## @return A decimal for the detected light intensity in lux
    def luminance(self):
        val = self.readValue() * (3.0 / 4096.0)

        vout = [ 0.0011498,  0.0033908,  0.011498,  0.041803,  0.15199,  0.53367,  1.3689,  1.9068,  2.3  ]
        lux  = [ 1.0108,     3.1201,     9.8051,    27.43,     69.545,   232.67,   645.11,  73.52,   1000 ]

        # take care the value is within range
        if (val <= vout[0]):  return lux[0]
        if (val >= vout[-1]): return lux[-1]

        # search right interval
        pos = 1 # _in[0] allready tested
        while (val > vout[pos]): pos += 1

        # this will handle all exact "points" in the _in array
        if (val == vout[pos]): return lux[pos]

        # interpolate in the right segment for the rest
        return (val - vout[pos-1]) * (lux[pos] - lux[pos-1]) / (vout[pos] - vout[pos-1]) + lux[pos-1]

## This class supports the Grove Light Sensor v1.1
#
#  This is a simple sensor that uses a photoresistor to detect light.
#
#  Documentation: http://wiki.seeed.cc/Grove-Light_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a light sensor connected to Bank A analog 1
#  light = GroveDevices.Grove_Light_Sensor("BAA1")
#  if (light.lightLevel() < 1000):
#    print("It's pretty dark in here.")
#  @endcode
class Grove_Light_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.ANALOG_INPUT)
    ## @return A number corresponding with the current detected light level.
    #          Average indoor lighting might be in the 2000's.
    def lightLevel(self):
        return self.readValue()

## This class supports the Grove Temperature Sensor v1.2
#
#  This sensor uses a thermistor (portmanteau of "thermal" and "resistor") to detect temperature.
#  Note that, in the case of a sudden temperature change (such as putting it in the freezer),
#  the sensor will take a minute for its reading to stabalize at the new temperature.
#
#  Documentation: http://wiki.seeed.cc/Grove-Temperature_Sensor_V1.2/
#
#  @code
#  import GroveDevices
#  # initialize a temperature sensor connected to Bank A analog 1
#  temp = GroveDevices.Grove_Temperature_Sensor("BAA1")
#  if (temp.temperature() > 22.0):
#    print("You might want a fan, it's getting a bit hot.")
#  @endcode
class Grove_Temperature_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.ANALOG_INPUT)

    ## @return A decimal corresponding to the detected temperature in Celsius
    def temperature(self):
        B = 4275 # B value of the thermistor
        a = self.readValue()
        R = (4096.0 / a) - 1.0 # or 4095.0?
        temperature = 1.0 / (math.log(R)/B + 1/298.15) - 273.15 # convert to temperature via datasheet
        return temperature

    ## A convenience function to convert Celsius to Fahrenheit
    @classmethod
    def CtoF(self, degreesCelsius):
        return degreesCelsius * 1.8 + 32

## This class supports the Grove UV Sensor v1.1
#
#  The Grove UV Sensor measures ultraviolet light intensity.
#
#  Documentation: http://wiki.seeed.cc/Grove-UV_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a UV sensor connected to Bank A analog 1
#  uv = GroveDevices.Grove_UV_Sensor("BAA1")
#  if (uv.UVindex() > 3.0):
#    print("It might be a good idea to put on some sunscreen!")
#  @endcode
class Grove_UV_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.ANALOG_INPUT)

    ## @return Measured illumination intensity in mW/m^2
    def intensity(self):
        val = 0
        for i in range(1024): # take many readings
            val = val + self.readValue()
        val = val / 1024.0 # mean value
        Vsig = val/4096.0 * 5
        return 307 * Vsig

    ## @note This is an approximation!
    #  @return The estimated measured EPA standard UV index
    def UVindex(self):
        return int(self.intensity()/200.0)

## This class supports the Grove Moisture Sensor v1.4
#
#  This sensor can detect moisture in soil. Simply insert the leads in the soil.
#
#  Documentation: http://wiki.seeed.cc/Grove-Moisture_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a moisture sensor connected to Bank A analog 1
#  m = GroveDevices.Grove_Moisture_Sensor("BAA1")
#  if (m.moistureLevel() < 450):
#    print("Your plant needs water!")
#  @endcode
class Grove_Moisture_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.ANALOG_INPUT)
    ## @return A number corresponding to the detected moisture level
    def moistureLevel(self):
        return self.readValue()

## This class supports the Grove Sound Sensor v1.6
#
#  This sensor uses a basic microphone to detect sound intensity.
#
#  Documentation: http://wiki.seeed.cc/Grove-Sound_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a sound sensor connected to Bank A analog 1
#  s = GroveDevices.Grove_Sound_Sensor("BAA1")
#  if (s.soundIntensity() < 3200):
#    print("I heard a clap!")
#  @endcode
class Grove_Sound_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.ANALOG_INPUT)
    ## @return A number corresponding with the current detected sound intensity.
    def soundIntensity(self):
        return self.readValue()

## This class supports the Grove Loudness Sensor v0.9b
#
#  This sensor detects the sound of its environment. It has a potentiometer to
#  adjust its output. It filters the sound signal to increased accuracy.
#
#  Documentation: http://wiki.seeed.cc/Grove-Sound_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a loudness sensor connected to Bank A analog 1
#  s = GroveDevices.Grove_Loudness_Sensor("BAA1")
#  if (s.detectSound() < 500):
#    print("Hey, stop blowing on the mic!")
#  @endcode
class Grove_Loudness_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.ANALOG_INPUT)
    ## @return A number corresponding with the sound of the environment.
    def detectSound(self):
        return self.readValue()

## This class supports the Grove Air Quality Sensor v1.3
#
#  This sensor detects harmful gases like "carbon monoxide, alcohol, acetone, thinner, formaldehyde."
#  It is best to leave the sensor on for a bit and let the value stabalize for an accurate reading.
#
#  Documentation: http://wiki.seeed.cc/Grove-Air_Quality_Sensor_v1.3/
#
#  @code
#  import GroveDevices
#  # initialize an air quality sensor connected to Bank A analog 1
#  air = GroveDevices.Grove_Air_Quality_Sensor("BAA1")
#  if (air.qualitativeMeasurement() != "Fresh air"):
#    print("There are harmful gases nearby, you might want to open a window.")
#  @endcode
class Grove_Air_Quality_Sensor(GrovePort):
    def __init__(self, port):
        GrovePort.__init__(self, port, type=GRXCom.TYPE.ANALOG_INPUT)

    ## @return A number corresponding with the air quality. Higher numbers mean more pollutants are present.
    def airQuality(self):
        return self.readValue()

    def qualitativeMeasurement(self):
        sensor_value = self.airQuality()
        if sensor_value > 700:
            return "High pollution"
        elif sensor_value > 300:
            return "Low pollution"
        else:
            return "Fresh air"

## This class supports the Grove Sunlight Sensor v1.4
#
#  This versatile sensor can read IR, visible, and UV light, all in one convenient package!
#
#  Documentation: http://wiki.seeed.cc/Grove-Sunlight_Sensor/
#
#  @code
#  import GroveDevices
#  # initialize a sunlight sensor (make sure it is plugged in to the I2C port first)
#  sun = GroveDevices.Grove_Sunlight_Sensor()
#  print("I see this {} IR light, {} visible light, and {} UV light.".format(sun.readIR(), sun.readVisible(), sun.readUV()))
#  @endcode
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


    ## Initialize the class with the i2c address of your sunlight sensor
    #  @param address Address of your sunlight sensor
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
