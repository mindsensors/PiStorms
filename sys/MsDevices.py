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
# Date          Author     Comments
# January 2017  Deepak     Support for LineLeader and LightSensorArray
# January 2017  Roman      Support for SumoEyes

from mindsensors_i2c import mindsensors_i2c

## AbsoluteIMU: this class provides PiStorms specific interface for all
# models of the AbsoluteIMU from mindsensors.com
#  for detailed member functions for this class, please refer to mindsensors.ABSIMU
class AbsoluteIMU(mindsensors_i2c):

    ## Default ABSIMU I2C Address
    ABSIMU_ADDRESS = (0x22)
    ## Command Register
    COMMAND = 0x41
    ## X-Axis Tilt Register. Will return a signed integer reading
    TILT_X = 0x42
    ## Y-Axis Tilt Register. Will return a signed integer reading
    TILT_Y = 0x43
    ## Z-Axis Tilt Register. Will return a signed integer reading
    TILT_Z = 0x44
    ## X-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050)
    ACCEL_X = 0x45
    ## Y-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050)
    ACCEL_Y = 0x47
    ## Z-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050)
    ACCEL_Z = 0x49
    ## Compass Heading Register. Will return an unsigned integer reading (0 - 360)
    CMPS = 0x4B
    ## X-Axis Magnetometer Register. Will return a signed integer reading
    MAG_X = 0x4D
    ## Y-Axis Magnetometer Register. Will return a signed integer reading
    MAG_Y = 0x4F
    ## Z-Axis Magnetometer Register. Will return a signed integer reading
    MAG_Z = 0x51
    ## X-Axis Gyroscope Register. Will return a signed integer reading
    GYRO_X = 0x53
    ## Y-Axis Gyroscope Register. Will return a signed integer reading
    GYRO_Y = 0x55
    ## Z-Axis Gyroscope Register. Will return a signed integer reading
    GYRO_Z = 0x57

    ## Initialize the class with the i2c address of your AbsoluteIMU
    #  @param self The object pointer.
    #  @param port The PiStorms bank.
    #  @param address Address of your AbsoluteIMU.
    #  @remark
    def __init__(self, port, address=ABSIMU_ADDRESS):
        port.activateCustomSensorI2C()
        mindsensors_i2c.__init__(self, address >> 1)

    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param command Value to write to the command register.
    def command(self, command):
        self.writeByte(self.COMMAND, int(command))

    ## Reads the tilt value along the x-axis
    #  @param self The object pointer.
    def get_tiltx(self):
        try:
            return self.readByteSigned(self.TILT_X)
        except:
            print ("Error: Could not read tilt along x-axis")
            return ""

    ## Reads the tilt value along the y-axis
    #  @param self The object pointer.
    def get_tilty(self):
        try:
            return self.readByteSigned(self.TILT_Y)
        except:
            print ("Error: Could not read tilt along y-axis")
            return ""

    ## Reads the tilt value along the z-axis
    #  @param self The object pointer.
    def get_tiltz(self):
        try:
            return self.readByteSigned(self.TILT_Z)
        except:
            print ("Error: Could not read tilt along z-axis")
            return ""

    ## Reads the tilt values
    #  @param self The object pointer.
    def get_tiltall(self):
        try:
            res = [(self.get_tiltx(),
                    self.get_tilty(),
                    self.get_tiltz())]
            return res
        except:
            print ("Error: Could not read tilt values")
            return ""

    ## Reads acceleromter value along the x-axis
    #  @param self The object pointer.
    def get_accelx(self):
        try:
            return self.readIntegerSigned(self.ACCEL_X)
        except:
            print ("Error: Could not read accelerometer value along x-axis")
            return ""

    ## Reads acceleromter value along the y-axis
    #  @param self The object pointer.
    def get_accely(self):
        try:
            return self.readIntegerSigned(self.ACCEL_Y)
        except:
            print ("Error: Could not read accelerometer value along y-axis")
            return ""

    ## Reads acceleromter value along the z-axis
    #  @param self The object pointer.
    def get_accelz(self):
        try:
            return self.readIntegerSigned(self.ACCEL_Z)
        except:
            print ("Error: Could not read accelerometer value along z-axis")
            return ""

    ## Reads the accelerometer values
    #  @param self The object pointer.
    def get_accelall(self):
        try:
            res = [(self.get_accelx(),
                    self.get_accely(),
                    self.get_accelz())]
            return res
        except:
            print ("Error: Could not read accelerometer values")
            return ""

    ## Reads compass heading
    #  @param self The object pointer.
    def get_heading(self):
        try:
            head = self.readInteger(self.CMPS)
            while(head > 360 or head < 0):
                head = self.readInteger(self.CMPS)
            return head
        except:
            print ("Error: Could not read compass heading")
            return ""

    ## Reads magnetometer value along the x-axis
    #  @param self The object pointer.
    def get_magx(self):
        try:
            return self.readIntegerSigned(self.MAG_X)
        except:
            print ("Error: Could not read magnetometer value along x-axis")
            return ""

    ## Reads magnetometer value along the y-axis
    #  @param self The object pointer.
    def get_magy(self):
        try:
            return self.readIntegerSigned(self.MAG_Y)
        except:
            print ("Error: Could not read magnetometer value along y-axis")
            return ""

    ## Reads magnetometer value along the z-axis
    #  @param self The object pointer.
    def get_magz(self):
        try:
            return self.readIntegerSigned(self.MAG_Z)
        except:
            print ("Error: Could not read magnetometer value along z-axis")
            return ""

    ## Reads the magnetometer values
    #  @param self The object pointer.
    def get_magall(self):
        try:
            res = [(self.get_magx(),
                    self.get_magy(),
                    self.get_magz())]
            return res
        except:
            print ("Error: Could not read magnetometer values")
            return ""

    ## Reads gyroscope value along the x-axis
    #  @param self The object pointer.
    def get_gyrox(self):
        try:
            return self.readIntegerSigned(self.GYRO_X)
        except:
            print ("Error: Could not read gyroscope value along x-axis")
            return ""

    ## Reads gyroscope value along the y-axis
    #  @param self The object pointer.
    def get_gyroy(self):
        try:
            return self.readIntegerSigned(self.GYRO_Y)
        except:
            print ("Error: Could not read gyroscope value along y-axis")
            return ""

    ## Reads gyroscope value along the z-axis
    #  @param self The object pointer.
    def get_gyroz(self):
        try:
            return self.readIntegerSigned(self.GYRO_Z)
        except:
            print ("Error: Could not read gyroscope value along z-axis")
            return ""

    ## Reads the tilt values
    #  @param self The object pointer.
    def get_gyroall(self):
        try:
            res = [(self.get_gyrox(),
                    self.get_gyroy(),
                    self.get_gyroz())]
            return res
        except:
            print ("Error: Could not read gyroscope values")
            return ""

    ## Starts the compass calibration process
    #  @param self The object pointer.
    def start_cmpscal(self):
        try:
            self.command(67)
        except:
            print ("Error: Could not start compass calibration process")
            return ""

    ## Stops the compass calibration process
    #  @param self The object pointer.
    def stop_cmpscal(self):
        try:
            self.command(99)
        except:
            print ("Error: Could not stop compass calibration process")
            return ""

    ## Sets accelerometer sensitivity to 2G
    #  @param self The object pointer.
    def accel_2G(self):
        try:
            self.command(49)
        except:
            print ("Error: Could not change accelerometer sensitivity")
            return ""

    ## Sets accelerometer sensitivity to 4G
    #  @param self The object pointer.
    def accel_4G(self):
        try:
            self.command(50)
        except:
            print ("Error: Could not change accelerometer sensitivity")
            return ""

    ## Sets accelerometer sensitivity to 8G
    #  @param self The object pointer.
    def accel_8G(self):
        try:
            self.command(51)
        except:
            print ("Error: Could not change accelerometer sensitivity")
            return ""

    ## Sets accelerometer sensitivity to 16G
    #  @param self The object pointer.
    def accel_16G(self):
        try:
            self.command(52)
        except:
            print ("Error: Could not change accelerometer sensitivity")
            return ""


## LineLeader: this class provides PiStorms specific interface for LineLeader-v2
# and NXTLineLeader
class LineLeader(mindsensors_i2c):

    ## Default Lineleader I2C Address
    LL_ADDRESS = 0x02
    ## Command Register
    LL_COMMAND = 0x41
    ## Steering Register. Will return a signed byte value
    LL_STEERING = 0x42
    ## Average Register. Will return a byte value
    LL_AVERAGE = 0x43
    ## Steering Register. Will return a byte value
    LL_RESULT = 0x44
    ## Setpoint Register
    LL_SETPOINT = 0x45
    ## KP Register
    LL_Kp = 0x46
    ## Ki Register
    LL_KI = 0x47
    ## Kd Register
    LL_KD = 0x48
    ## Kp factor Register
    LL_KPfactor = 0x61
    ## Ki factor Register
    LL_KIfactor = 0x62
    ## Kd factor Register
    LL_KDfactor = 0x63

    LL_CALIBRATED = 0x49
    LL_UNCALIBRATED = 0x74

    ## Initialize the class with the i2c address of your LineLeader
    #  @param self The object pointer.
    #  @param port The PiStorms bank.
    #  @param address Address of your LineLeader
    #  @remark
    def __init__(self, port, address=LL_ADDRESS):
        port.activateCustomSensorI2C()
        mindsensors_i2c.__init__(self, address >> 1)

    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param command Value to write to the command register.
    def command(self, command):
        self.writeByte(self.LL_COMMAND, int(command))

    ## Calibrates the white value for the LineLeader
    #  @param self The object pointer.
    def White_Cal(self):
        self.command(87)


    ## Calibrates the black value for the LineLeader
    #  @param self The object pointer.
    def Black_Cal(self):
        self.command(66)

    ## Wakes up or turns on the LEDs of the LineLeader
    #  @param self The object pointer.
    def Wakeup(self):
        self.command(80)

    ## Puts to sleep, or turns off the LEDs of the LineLeader
    #  @param self The object pointer.
    def Sleep(self):
        self.command(68)

    ## Reads the eight(8) calibrated light sensor values of the LineLeader
    #  @param self The object pointer.
    def ReadRaw_Calibrated(self):
        try:
            return self.readArray(self.LL_CALIBRATED, 8)
        except:
            print ("Error: Could not read Lineleader")
            return ""

    ## Reads the eight(8) uncalibrated light sensor values of the LineLeader
    #  @param self The object pointer.
    def ReadRaw_Uncalibrated(self):
        try:
            s1 = self.readInteger(self.LL_UNCALIBRATED)
            s2 = self.readInteger(self.LL_UNCALIBRATED + 2)
            s3 = self.readInteger(self.LL_UNCALIBRATED + 4)
            s4 = self.readInteger(self.LL_UNCALIBRATED + 6)
            s5 = self.readInteger(self.LL_UNCALIBRATED + 8)
            s6 = self.readInteger(self.LL_UNCALIBRATED + 10)
            s7 = self.readInteger(self.LL_UNCALIBRATED + 12)
            s8 = self.readInteger(self.LL_UNCALIBRATED + 14)
            array = [s1, s2, s3, s4, s5, s6, s7, s8]
            return array
        except:
            print ("Error: Could not read Lineleader")
            return ""

    ## Read the steering value from the Lineleader (add or subtract this value to the motor speed)
    #  @param self The object pointer.
    def steering(self):
        try:
            return self.readByteSigned(self.LL_STEERING)
        except:
            print ("Error: Could not read Lineleader")
            return ""

    ## Read the average weighted value of the current line from position from the Lineleader
    #  @param self The object pointer.
    def average(self):
        try:
            return self.readByte(self.LL_AVERAGE)
        except:
            print ("Error: Could not read Lineleader")
            return ""

    ## Reads the result of all 8 light sensors form the LineLeader as 1 byte (1 bit for each sensor)
    #  @param self The object pointer.
    def result(self):
        try:
            return self.readByte(self.LL_RESULT)
        except:
            print ("Error: Could not read Lineleader")
            return ""

    ## Reads the setpoint register.
    #  @param self The object pointer.
    def getSetPoint(self):
        try:
            return self.readByte(self.LL_SETPOINT)
        except:
            print ("Error: Could not read Lineleader")
            return ""

    ## Writes the Setpoint register.
    #  @param self The object pointer.
    def setSetPoint(self):
        try:
            return self.writeByte(self.LL_SETPOINT)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Write the Kp value to the Lineleader
    #  @param self The object pointer.
    def setKP(self):
        try:
            return self.writeByte(self.LL_KP)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Write the Ki value to the Lineleader
    #  @param self The object pointer.
    def setKI(self):
        try:
            return self.writeByte(self.LL_KI)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Write the Kd value to the Lineleader
    #  @param self The object pointer.
    def setKD(self):
        try:
            return self.writeByte(self.LL_KD)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Write the Kp factor value to the Lineleader
    #  @param self The object pointer.
    def setKPfactor(self):
        try:
            return self.writeByte(self.LL_KPfactor)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Write the Ki factor value to the Lineleader
    #  @param self The object pointer.
    def setKIfactor(self):
        try:
            return self.writeByte(self.LL_KIfactor)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Write the Kd factor value to the Lineleader
    #  @param self The object pointer.
    def setKDfactor(self):
        try:
            return self.writeByte(self.LL_KDfactor)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Read the Kp value from the Lineleader
    #  @param self The object pointer.
    def getKP(self):
        try:
            return self.readByte(self.LL_KP)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Read the Ki value from the Lineleader
    #  @param self The object pointer.
    def getKI(self):
        try:
            return self.readByte(self.LL_KI)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Read the Kd value from the Lineleader
    #  @param self The object pointer.
    def getKD(self):
        try:
            return self.readByte(self.LL_KD)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Read the Kp factor value to the Lineleader
    #  @param self The object pointer.
    def getKPfactor(self):
        try:
            return self.readByte(self.LL_KPfactor)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Read the Ki factor value to the Lineleader
    #  @param self The object pointer.
    def getKIfactor(self):
        try:
            return self.readByte(self.LL_KIfactor)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

    ## Read the Kd factor value to the Lineleader
    #  @param self The object pointer.
    def getKDfactor(self):
        try:
            return self.readByte(self.LL_KDfactor)
        except:
            print ("Error: Could not write to Lineleader")
            return ""

## LightSensorArray: this class provides PiStorms specific interface for LightSensorArray
#
class LightSensorArray(mindsensors_i2c):
    ## Default LightSensorArray I2C Address
    LSA_ADDRESS = 0x14
    ## Command Register
    LSA_COMMAND = 0x41
    ## Calibrated Register. Will return an 8 byte array
    LSA_CALIBRATED = 0x42
    ## Uncalibrated Register. Will return an 8 byte array
    LSA_UNCALIBRATED = 0x6A

    ## Initialize the class with the i2c address of your device
    #  @param self The object pointer.
    #  @param port The PiStorms bank.
    #  @param address Address of your device
    #  @remark
    def __init__(self, port, address=LSA_ADDRESS):
        port.activateCustomSensorI2C()
        mindsensors_i2c.__init__(self, address >> 1)

    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param cmd Value to write to the command register.
    def command(self, cmd):
        self.writeByte(self.LSA_COMMAND, int(cmd))

    ## Calibrates the white value for the LightSensorArray
    #  @param self The object pointer.
    def White_Cal(self):
        self.command(87)

    ## Calibrates the black value for the LightSensorArray
    #  @param self The object pointer.
    def Black_Cal(self):
        self.command(66)

    ## Wakes up or turns on the LEDs of the LightSensorArray
    #  @param self The object pointer.
    def Wakeup(self):
        self.command(80)

    ## Puts to sleep, or turns off the LEDs of the LightSensorArray
    #  @param self The object pointer.
    def Sleep(self):
        self.command(68)

    ## Reads the eight(8) calibrated light sensor values of the LightSensorArray
    #  @param self The object pointer.
    def ReadRaw_Calibrated(self):
        try:
            return self.readArray(self.LSA_CALIBRATED, 8)
        except:
            print ("Error: Could not read LSArray")
            return ""

    ## Reads the eight(8) uncalibrated light sensor values of the LightSensorArray
    #  @param self The object pointer.
    def ReadRaw_Uncalibrated(self):
        try:
            s1 = self.readInteger(self.LSA_UNCALIBRATED)
            s2 = self.readInteger(self.LSA_UNCALIBRATED + 2)
            s3 = self.readInteger(self.LSA_UNCALIBRATED + 4)
            s4 = self.readInteger(self.LSA_UNCALIBRATED + 6)
            s5 = self.readInteger(self.LSA_UNCALIBRATED + 8)
            s6 = self.readInteger(self.LSA_UNCALIBRATED + 10)
            s7 = self.readInteger(self.LSA_UNCALIBRATED + 12)
            s8 = self.readInteger(self.LSA_UNCALIBRATED + 14)
            array = [s1, s2, s3, s4, s5, s6, s7, s8]
            return array
        except:
            print ("Error: Could not read LSArray")
            return ""


## SumoEyes: this class provides PiStorms specific interface for the
#  SumoEyes obstacle detection sensor from mindsensors.com
class SumoEyes(mindsensors_i2c):
    # Responses for SumoEyes
    SE_None = [0, "None"]
    SE_Values = {
        465: [1, "Front"],
        555: [3, "Right"],
        800: [2, "Left"]
    }

    # Sensor
    PS_S1EV_Ready = 0x70
    PS_S2EV_Ready = 0xA4

    # Settings for the setRange method
    LONG_RANGE = True
    SHORT_RANGE = False

    ## Initialize the class with the PiStorms bank
    #  @param self The object pointer.
    #  @param port The PiStorms bank.
    #  @remark
    #  Example implementation in your program:
    #  @code
    #  ...
    #  psm = PiStorms()
    #  se_sensor = MsDevices.SumoEyes(psm.BAS1)
    #  ...
    #  @endcode
    def __init__(self, port):
        # Get the instance of the PSSensor class
        self.sensor = port.pssensor
        # Initialize the class with the i2c address of the bank
        mindsensors_i2c.__init__(self, self.sensor.bank.address)
        # Set range to long range by default
        self.setRange()
        # Method used in the original implementation
        self.sensor.setModeEV3(0)

    ## Check the zones for an obstacle
    #  @param self The object pointer.
    #  @param verbose Outputs the string value of the direction if set to True
    #  @remark
    #  Example implementation in your program:
    #  @code
    #  ...
    #  psm = PiStorms()
    #  se_sensor = MsDevices.SumoEyes(psm.BAS1)
    #  print se_sensor.detectObstactleZone()
    #  ...
    #  @endcode
    def detectObstactleZone(self, verbose = False):
        reading = self.readSensorValue()
        for reference in self.SE_Values.keys():
            if self.isNear(reference, reading):
                output = self.SE_Values[reference]
                return output[1] if verbose else ouput[0]
        return self.SE_None[1] if verbose else self.SE_None[0]

    ## Reads the value from the SumoEyes sensor
    #  @param self The object pointer.
    #  @remark
    #  Should not be used in other programs
    def readSensorValue(self):
        return self.readInteger(self.PS_S1EV_Ready if self.sensor.sensornum == 1 else self.PS_S2EV_Ready)

    ## Sets the sensor range to LONG_RANGE or SHORT_RANGE setting
    #  @param self The object LONG_RANGE.
    #  @param range The range (long is default)
    #  @remark
    #  Example implementation in your program:
    #  @code
    #  ...
    #  psm = PiStorms()
    #  se_sensor = MsDevices.SumoEyes(psm.BAS1)
    #  se_sensor.setRange(se_sensor.SHORT_RANGE)
    #  ...
    #  @endcode
    def setRange(self, range = LONG_RANGE):
        if range == self.LONG_RANGE:
            self.sensor.setType(self.sensor.PS_SENSOR_TYPE_LIGHT_INACTIVE)
        elif range == self.SHORT_RANGE:
            self.sensor.setType(self.sensor.PS_SENSOR_TYPE_LIGHT_ACTIVE)

    ## Checks if the sensor reading is within a tolerance to find the zone
    #  @param self The object pointer.
    #  @param reference The reference value.
    #  @param value The sensor measurement.
    #  @param tolerance The tolerance.
    #  @remark
    #  Should not be used in other programs
    def isNear(self, reference, value, tolerance = 40):
        return (value > (reference - tolerance)) and (value < (reference + tolerance))

## IRThermometer : this class provides PiStorms specific interface for the
#  IR Thermometer sensor:
#  http://www.mindsensors.com/products/170-ir-temperature-sensor-for-ev3-or-nxt
#
class IRThermometer(mindsensors_i2c):
    ## Default I2C Address
    IRT_ADDRESS = 0x2A
    ## Command Register
    IRT_COMMAND = 0x41
    # temperature registers
    IRT_AMBIENT_CELSIUS = 0x42
    IRT_TARGET_CELSIUS = 0x44
    IRT_AMBIENT_FAHR = 0x46
    IRT_TARGET_FAHR = 0x48

    ## Initialize the class with the i2c address of your device
    #  @param self The object pointer.
    #  @param port The PiStorms bank.
    #  @param address Address of your device
    #  @remark
    def __init__(self, port, address=IRT_ADDRESS):
        port.activateCustomSensorI2C()
        mindsensors_i2c.__init__(self, address >> 1)

    def readAmbientCelsius(self):
        return (float(self.readInteger(self.IRT_AMBIENT_CELSIUS))/100)

    def readTargetCelsius(self):
        return (float(self.readInteger(self.IRT_TARGET_CELSIUS))/100)

    def readAmbientFahr(self):
        return (float(self.readInteger(self.IRT_AMBIENT_FAHR))/100)

    def readTargetFahr(self):
        return (float(self.readInteger(self.IRT_TARGET_FAHR))/100)


## BLOB: this class is a subclass of NXTCAM. There is no need to call this class directly.
class BLOB():

    ## Initialize the class with the parameters passed from getBlobs() in the NXTCAM() class
    #  @param self The object pointer.
    #  @param color The color of the specified tracked object.
    #  @param left The left coordinate of the specified tracked object.
    #  @param top The top coordinate of the specified tracked object.
    #  @param right The right coordinate of the specified tracked object.
    #  @param bottom The bottom coordinate of the specified tracked object.
    #  @remark
    def __init__(self, color, left, top, right, bottom):
        self.color = color
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

## NXTCam5 : this class provides PiStorms specific interface for NXTCam5
#  http://www.mindsensors.com/pages/317
#
class NXTCam5(mindsensors_i2c):
    ## Default I2C Address
    CAM_ADDRESS = 0x02
    ## Command Register
    CAM_COMMAND = 0x41

    NumberObjects = 0x42
    ## First Register Containing Tracked Object Data. This is to be read in an array
    Color = 0x43
    ## X-axis Top Register
    X_Top = 0x44
    ## Y-axis Top Register
    Y_Top = 0x45
    ## X-axis Bottom Register
    X_Bottom = 0x46
    ## Y-axis Bottom Register
    Y_Bottom = 0x47


    ## Initialize the class with the i2c address of your device
    #  @param self The object pointer.
    #  @param port The PiStorms bank.
    #  @param address Address of your device
    #  @remark
    def __init__(self, port, address=CAM_ADDRESS):
        port.activateCustomSensorI2C()
        mindsensors_i2c.__init__(self, address >> 1)

    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param command Value to write to the command register.
    def command(self, command):
        self.writeByte(self.CAM_COMMAND, int(command))

    ## Track a line
    #  @param self The object pointer.
    def trackLine(self):
        try:
            self.command(76)
        except:
            print ("Error: couldn't write command to Cam.")
            return ""

    ## Track Object (this is default mode of NXTCam5)
    #  @param self The object pointer.
    def trackObject(self):
        try:
            self.command(79)
        except:
            print ("Error: couldn't write command to Cam.")
            return ""

    ## Track Face
    #  @param self The object pointer.
    def trackFace(self):
        try:
            self.command(70)
        except:
            print ("Error: couldn't write command to Cam.")
            return ""

    ## Track Eye
    #  @param self The object pointer.
    def trackEye(self):
        try:
            self.command(101)
        except:
            print ("Error: couldn't write command to Cam.")
            return ""

    ## Capture Image
    #  @param self The object pointer.
    #  the resultimg image is stored on the SD card attached to NXTCam5.
    #  the file forma is JPEG
    def captureImage(self):
        try:
            self.command(80)
        except:
            print ("Error: couldn't write command to Cam.")
            return ""

    ## Capture Short Video
    #  @param self The object pointer.
    #  Capture a short Video (about 10 seconds)
    #  the resultimg video file is stored on the SD card attached to NXTCam5.
    #  the file forma is MJPEG
    #  you can use VLC player by www.videolan.org to view these files
    def captureShortVideo(self):
        try:
            self.command(77)
        except:
            print ("Error: couldn't write command to Cam.")
            return ""

    ## Capture Continuous Video
    #  @param self The object pointer.
    #  Capture a continuous Video,
    #  the recording is stopped when different command is received.
    #  the resultimg video file is stored on the SD card attached to NXTCam5.
    #  the file forma is MJPEG
    #  you can use VLC player by www.videolan.org to view these files
    def captureContinuousVideo(self):
        try:
            self.command(82)
        except:
            print ("Error: couldn't write command to Cam.")
            return ""

    ## Read the number of objects detected (0-8)
    #  @param self The object pointer.
    def getNumberObjects(self):
        try:
            return self.readByte(self.NumberObjects)
        except:
            print ("Error: Could not read from Cam.")
            return ""

    ## Reads data of the tracked object(s)
    #  @param self The object pointer.
    #  @param blobNum The number of the tracked object.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from mindsensors  import NXTCAM
    #  ...
    #  cam = NXTCAM()
    #  cam.startTracking()
    #  cam.trackObject()
    #  b = cam.getBlobs(1)
    #  print "Color: " + str(b.color)
    #  print "Left: " + str(b.left)
    #  print "Top: " + str(b.top)
    #  print "Right: " + str(b.right)
    #  print "Bottom: " + str(b.bottom)
    #  @endcode
    def getBlobs(self, blobNum = 1):
        try:

            data= [0,0,0,0,0]
            blobs = self.getNumberObjects()
            i = blobNum - 1
            if (blobNum > blobs):
                print ("blobNum is greater than amount of blobs tracked.")
                return 0
            else:
                #while(i < blobs):
                data[0] = color = self.readByte(self.Color + (i*5))
                data[1] = left = self.readByte(self.X_Top + (i*5))
                data[2] = top = self.readByte(self.Y_Top + (i*5))
                data[3] = right = self.readByte(self.X_Bottom + (i*5))
                data[4] = bottom = self.readByte(self.Y_Bottom + (i*5))
                return BLOB(color,left,top,right,bottom)
        except:
            print ("Error: Could not read from Cam.")
            return ""


"""
new class name -> old class name (if there is one)
AbsoluteIMU -> ABSIMU **
LineLeader -> LINELEADER **
LightSensorArray  -> LSA **
IRThermometer -> (done - IRThermometer)
AngleSensor  -> ANGLE
DISTNx -> DIST
NXTMMX -> MMX
NXTServo -> NXTSERVO
PFMate -> PFMATE
CurrentMeter  -> CURRENT
VoltMeter -> VOLT
PressureSensor -> PPS58
NXTCam5 -> new NXTCam5 **
PSPNx -> needs implementation
EV3SensorMux -> EV3SensAdapt (3 channels -> change i2c address based on channel).
EV3SensorAdapter -> EV3SensAdapt
SumoEyes (is an analog device - needs different implementation).
"""
