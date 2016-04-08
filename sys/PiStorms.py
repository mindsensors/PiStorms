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
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# July 2015  Henry     Initial Authoring 
# Oct. 2015  Nitin     Editing and improved functionality
# Oct. 2015  Michael   Comments and documentation

## @file PiStorms.py
#  PiStorms.py defines the main interfaces used in the PiStorms library.
#  @mainpage PiStorms Library Reference
#  @section intro_sec  Introduction
#  PiStorms library provides interfaces to use PiStorms by mindsensors.com on Raspberry Pi.
#
#  At the time of this writing, PiStorms and this library can be used with the following boards:
#
#    <b>Raspberry Pi boards:</b>\n
#    model A+\n
#    model B+\n
#    2 model B
#
#  @section more_info  More Information
#  More information about PiStorms is available at: http://www.mindsensors.com/stem-education/13-pistorms-base-kit
#
#  Online documentation of this Library Reference is available at:
#  http://www.mindsensors.com/reference/PiStorms/html/
#  (Note however, the online version may not match exactly with the library files you have installed on your computer).
#
#  @section install_sec Installation Instructions
#  To download PiStorms libary and features to your Raspberry Pi:\n
#  navigate to /home/pi\n 
#  sudo wget http://www.mindsensors.com/largefiles/PiStorms.tar.gz
#
#  Untar the file using command:\n
#  cd /home/pi\n 
#  tar -zxvf PiStorms.tar.gz
#
#  Install using following commands:\n
#  cd PiStorms\n
#  ./setup.sh
#  
#  It will take a few minutes to install the software.

from PiStormsCom import PiStormsCom
from mindsensorsUI import mindsensorsUI
import time,sys,os,ctypes,math,random

## @package PiStorms
#  This module contains classes and functions necessary for the use of PiStorms from mindsensors.com

Dev_PiStorms = 1

## PiStormsSensor: This class provides functions for configuration, reading, and writing of sensors for use with PiStorms.
#  @remark
#  There is no need to initialize this class directly. This is done automatically during the PiStorms init.
class PiStormsSensor:
    
    ## Constant to specify no color
    PS_SENSOR_COLOR_NONE = 0
    ## Constant to specify black color
    PS_SENSOR_COLOR_BLACK = 1
    ## Constant to specify blue color
    PS_SENSOR_COLOR_BLUE = 2
    ## Constant to specify green color
    PS_SENSOR_COLOR_GREEN = 3
    ## Constant to specify yellow color
    PS_SENSOR_COLOR_YELLOW = 4
    ## Constant to specify red color
    PS_SENSOR_COLOR_RED = 5
    ## Constant to specify white color
    PS_SENSOR_COLOR_WHITE = 6
    ## Constant to specify brown color
    PS_SENSOR_COLOR_BROWN = 7
    
    ### @cond 
    ## Initialize the PiStorms sensor port
    #  @param self The object pointer.
    #  @param sensor The sensor port to use.
    def __init__(self,sensor):
        self.pssensor = sensor
    ### @endcond
    
    ## Returns the EV3 Touch Sensor touch value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  touch = psm.BAS1.isTouchedEV3()
    #  if(touch == True ):
    #      # do some task
    #  @endcode      
    def isTouchedEV3(self):
        return self.pssensor.isTouchedEV3()
        
    ## Returns the EV3 Touch Sensor touch count
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  touchCount = psm.BAS1.numTouchesEV3()
    #  if(touchCount == 5):
    #      #do some task
    #  @endcode 
    def numTouchesEV3(self):
        return self.pssensor.numTouchesEV3()
    
    ## Resets the EV3 Touch Sensor touch count to zero
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAS1.resetTouchesEV3()
    #  @endcode 
    def resetTouchesEV3(self):
        self.pssensor.resetTouchesEV3()
    
    ## Returns the EV3 Infrared Sensor distance value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  dist = psm.BAS1.distanceIREV3()
    #  if(dist < 30 ):
    #      # do some task
    #  @endcode 
    def distanceIREV3(self):
        return self.pssensor.distanceIREV3()
    
    ## Returns the EV3 Infrared Sensor heading value
    #  @param self The object pointer.
    #  @param channel The channel of your remote control or other IR device.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  heading = psm.BAS1.headingIREV3(1)
    #  if(heading > 10 ):
    #      # do some task
    #  @endcode 
    def headingIREV3(self,channel):
        return self.pssensor.headingIREV3(channel)
    
    ## Returns the LEGO IR remote distance value
    #  @param self The object pointer.
    #  @param channel The channel of your remote control or other IR device.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  remDist = psm.BAS1.distanceRemoteIREV3(1)
    #  if(remDist < 50 ):
    #      # do some task
    #  @endcode 
    def distanceRemoteIREV3(self,channel):
        return self.pssensor.distanceRemoteIREV3(channel)
    
    ## Returns the left button status of the LEGO IR remote (1 = Forward, 0 = Not pressed, -1 = Backwards)
    #  @param self The object pointer.
    #  @param channel The channel of your remote control or other IR device. 
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  remLeftButton = psm.BAS1.remoteLeft(1)
    #  if(remLeftButton == 1 ):
    #      # do some task
    #  @endcode 
    def remoteLeft(self,channel):
        return self.pssensor.remoteLeft(channel)
    
    ## Returns the right button status of the LEGO IR remote (1 = Forward, 0 = Not pressed, -1 = Backwards)
    #  @param self The object pointer.
    #  @param channel The channel of your remote control or other IR device.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  remRightButton = psm.BAS1.remoteRight(1)
    #  if(remRightButton == 1 ):
    #      # do some task
    #  @endcode 
    def remoteRight(self,channel):
        return self.pssensor.remoteRight(channel)
    
    ## Returns the EV3 Ultrasonic Sensor distance value in centimeters
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  dist = psm.BAS1.distanceUSEV3()
    #  if(dist < 60 ):
    #      # do some task
    #  @endcode 
    def distanceUSEV3(self):
        return self.pssensor.distanceUSEV3cm()
    
    ## Returns the EV3 Ultrasonic Sensor distance value in inches
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  dist = psm.BAS1.distanceUSEV3in()
    #  if(dist < 100 ):
    #      # do some task
    #  @endcode 
    def distanceUSEV3in(self):
        return self.pssensor.distanceUSEV3in()
        
    ## Returns the EV3 Ultrasonic Sensor presence boolean value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  here = psm.BAS1.presenceUSEV3()
    #  if(here == True ):
    #      # do some task
    #  @endcode 
    def presenceUSEV3(self):
        return self.pssensor.presenceUSEV3()
    
    ## Returns the EV3 Gyro Sensor angle value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  angle = psm.BAS1.gyroAngleEV3()
    #  if(angle > 90 ):
    #      # do some task
    #  @endcode 
    def gyroAngleEV3(self):
        return self.pssensor.gyroAngleEV3()
    
    ## Returns the EV3 Gyro Sensor rate value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  rate = psm.BAS1.gyroRateEV3()
    #  if(rate > 20 ):
    #      # do some task
    #  @endcode 
    def gyroRateEV3(self):
        return self.pssensor.gyroRateEV3()
    
    ## Returns the EV3 Color Sensor reflected light value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  refLight = psm.BAS1.reflectedLightSensorEV3()
    #  if(refLight > 20 ):
    #      # do some task
    #  @endcode 
    def reflectedLightSensorEV3(self):
        return self.pssensor.reflectedLightSensorEV3()
    
    ## Returns the EV3 Color Sensor ambient light value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  ambLight = psm.BAS1.ambientLightSensorEV3()
    #  if(ambLight > 20 ):
    #      # do some task
    #  @endcode 
    def ambientLightSensorEV3(self):
        return self.pssensor.ambientLightSensorEV3()
    
    ## Returns the EV3 Color Sensor color value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  color = psm.BAS1.colorSensorEV3()
    #  if(color == 5 ):
    #      # do some task
    #  @endcode 
    def colorSensorEV3(self):
        return self.pssensor.colorSensorEV3()
    
    ## Returns the NXT Touch Sensor touch value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  touch = psm.BAS1.isTouchedNXT()
    #  if(touch == True):
    #      # do some task
    #  @endcode 
    def isTouchedNXT(self):
        return self.pssensor.isTouchedNXT()
    
    ## Returns the NXT Touch Sensor touch count
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  touchCount = psm.BAS1.numTouchesNXT()
    #  if(touchCount == 5 ):
    #      # do some task
    #  @endcode 
    def numTouchesNXT(self):
        return self.pssensor.numTouchesNXT()
    
    ## Resets the NXT Touch Sensor touch count to zero
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAS1.resetTouchesNXT()
    #  @endcode 
    def resetTouchesNXT(self):
        self.pssensor.resetTouchesNXT()
    
    ## Returns the mindsensors.com's SumoEyes value (0 = None, 1 = Front, 2 = Left, 3 = Right)
    #  @param self The object pointer.
    #  @param long The mode of the SumoEyes sensor. (True = long range | False = short range)
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  sumo = psm.BAS1.SumoEyes(True)
    #  if(sumo == 2 ):
    #      # do some task
    #  @endcode 
    def SumoEyes(self, long=True):
        return self.pssensor.SumoEyes(long)
    
    ## Returns the NXT light sensor value
    #  @param self The object pointer.
    #  @param active The mode of the nxt light sensor. (True = active/reflected | False = nonactive/ambient)
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  light = psm.BAS1.lightSensorNXT(True)
    #  if(light < 450 ):
    #      # do some task
    #  @endcode 
    def lightSensorNXT(self, active=True):
        return self.pssensor.lightSensorNXT(active)
    
    ## Returns the NXT color sensor color value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  color = psm.BAS1.colorSensorNXT()
    #  if(color == 5):
    #      # do some task
    #  @endcode 
    def colorSensorNXT(self):
        return self.pssensor.colorSensorNXT()
    
    ## Returns the NXT color sensor ambient light value
    #  @param self The object pointer. 
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  ambLight = psm.BAS1.colorSensorNoneNXT()
    #  if(ambLight > 20 ):
    #      # do some task
    #  @endcode 
    def colorSensorNoneNXT(self):
        return self.pssensor.colorSensorNoneNXT()
    
    ## Returns the NXT color sensor reflected red light value
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  redRefLight = psm.BAS1.colorSensorRedNXT()
    #  if(redRefLight > 20 ):
    #      # do some task
    #  @endcode 
    def colorSensorRedNXT(self):
        return self.pssensor.colorSensorRedNXT()
    
    ## Returns the NXT color sensor reflected green light value
    #  @param self The object pointer. 
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  greenRefLight = psm.BAS1.colorSensorGreenNXT()
    #  if(greenRefLight > 20 ):
    #      # do some task
    #  @endcode     
    def colorSensorGreenNXT(self):
        return self.pssensor.colorSensorGreenNXT()
    
    ## Returns the NXT color sensor reflected blue light value
    #  @param self The object pointer. 
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  blueRefLight = psm.BAS1.colorSensorBlueNXT()
    #  if(blueRefLight > 20 ):
    #      # do some task
    #  @endcode     
    def colorSensorBlueNXT(self):
        return self.pssensor.colorSensorBlueNXT()
    
    ## Returns an analog sensor value 0-1024
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  analog = psm.BAS1.analogSensor()
    #  if(analog < 600):
    #      # do some task
    #  @endcode 
    def analogSensor(self):
        return self.pssensor.analogSensor()
    
    ## Configures the sensor port for a custom I2C sensor
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAS1.activateCustomSensorI2C()
    #  @endcode 
    def activateCustomSensorI2C(self):
        self.pssensor.activateCustomSensorI2C()

## PiStormsMotor: This class provides functions for motor control.
#  @remark
#  There is no need to initialize this class directly. This is done automatically during the PiStorms init.
class PiStormsMotor():
    
    ### @cond
    # Initialize the PiStorms motor port
    #  @param self The object pointer.
    #  @param motor The motor port to use.
    def __init__(self, motor):
        self.psmotor = motor
    ### @endcond
    
    ## Returns the current encoder position of the motor
    #  @param self The object pointer.  
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  position = psm.BAM1.pos()
    #  if(position > 720):
    #      # do some task
    #  @endcode
    def pos(self):
        return self.psmotor.pos()
        
    #def resPos(self, bnk):
    #    return self.psmotor.resPos(bnk)
    
    ## Run the motor at a set speed for an unlimited duration
    #  @param self The object pointer.
    #  @param speed The speed at which to turn the motor.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAM1.setSpeed(100)
    #  @endcode   
    def setSpeed(self,speed):
        self.psmotor.setSpeed(speed)
    
    ## Stop the motor abruptly with brake
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAM1.brake()
    #  @endcode   
    def brake(self):
        self.psmotor.brake()
    
    ## Stop the motor smoothly with float
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAM1.float()
    #  @endcode   
    def float(self):
        self.psmotor.float()
    
    ## Stop the motor abruptly and hold the current position
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAM1.hold()
    #  @endcode   
    def hold(self):
        self.psmotor.hold()
    
    ## Run the motor for a specific time in seconds
    #  @param self The object pointer.
    #  @param secs The number of seconds to run the motor.
    #  @param speed The speed at which to turn the motor.
    #  @param brakeOnCompletion Choose to brake or float the motor upon completion with True (brake) or False (float).
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAM1.runSecs(5,100,True)
    #  @endcode   
    def runSecs(self,secs,speed,brakeOnCompletion = False):
        self.psmotor.runSecs(secs,speed,brakeOnCompletion)
    
    ## Check if the motor is running
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  motorState = psm.BAM1.isBusy()
    #  if(motorState == False):
    #      # do some task
    #  @endcode   
    def isBusy(self):
        return self.psmotor.isBusy()
    
    ## Wait until the motor is no longer running
    #  @param self The object pointer.
    #  @param timeout The timeout value as a factor of 10ms.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  boolMotorState = psm.BAM1.waitUntilNotBusy()
    #  if(overloadState == True):
    #      # do some task
    #  @endcode   
    def waitUntilNotBusy(self,timeout=-1):
        return self.psmotor.waitUntilNotBusy(timeout)
    
    ## Check if the motor is stalled
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  stallState = psm.BAM1.isStalled()
    #  if(stallState == True):
    #      # do some task
    #  @endcode   
    def isStalled(self):
        return self.psmotor.isStalled()
    
    ## Check if the motor is overloaded
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  overloadState = psm.BAM1.isOverloaded()
    #  if(overloadState == True):
    #      # do some task
    #  @endcode   
    def isOverloaded(self):
        return self.psmotor.isOverloaded()
    
    ## Run the motor for a specific amount of degrees
    #  @param self The object pointer.
    #  @param degs The number of degrees to run the motor.
    #  @param speed The speed at which to turn the motor.
    #  @param brakeOnCompletion Choose to brake or float the motor upon completion with True (brake) or False (float).
    #  @param holdOnCompletion Choose to hold the motor position upon completion with True (hold) or False (release).
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAM1.runDegs(720,100,True,False)
    #  @endcode   
    def runDegs(self,degs,speed = 100,brakeOnCompletion = False, holdOnCompletion = False):
        self.psmotor.runDegs(degs,speed,brakeOnCompletion,holdOnCompletion)
    
    ## Set the motor PID parameters (PiStorms PID parameters are default for NXT/EV3 motors). Only one set of PID parameters can be set per bank and will reset to default upon new power cycle
    #  @param self The object pointer.
    #  @param Kp_tacho Proportional-gain of the encoder position of the motor.
    #  @param Ki_tacho Integral-gain of the encoder position of the motor.
    #  @param Kd_tacho Derivative-gain of the encoder position of the motor.
    #  @param Kp_speed Proportional-gain of the speed of the motor.
    #  @param Ki_speed Integral-gain of the speed of the motor.
    #  @param Kd_speed Derivative-gain of the speed of the motor.
    #  @param passcount The number of times the encoder reading should be within tolerance.
    #  @param tolerance The tolerance (in ticks) for encoder positioning .
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.BAM1.SetPerformanceParameters(6,0,0,1,0,0,10,5)
    #  @endcode   
    def SetPerformanceParameters(self, Kp_tacho, Ki_tacho, Kd_tacho, Kp_speed, Ki_speed, Kd_speed, passcount, tolerance):
        self.psmotor.SetPerformanceParameters(Kp_tacho, Ki_tacho, Kd_tacho, Kp_speed, Ki_speed, Kd_speed, passcount, tolerance)
    

## PiStorms: This class provides functions for PiStorms.
#  PiStormsSensor, PiStormsMotor, and mindsensorsUI are subclasses of PiStorms and are automatically initialized with initialization of PiStorms class.
class PiStorms:
    
    ## Initialize the PiStorms motor and sensor ports
    #  @param self The object pointer.
    #  @param name The display title that will appear at the top of the LCD touchscreen.
    #  @param rotation The rotation of the LCD touchscreen.
    #  @remark
    #  There is no need to use this function directly. To initialize the PiStorms class in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  @endcode    
    def __init__(self, name = "PiStorms", rotation = 3 ):
        
        self.screen = mindsensorsUI(name ,rotation)
        self.psc = PiStormsCom()
        self.BAS1 = PiStormsSensor(self.psc.BAS1)
        self.BAS2 = PiStormsSensor(self.psc.BAS2)
        self.BBS1 = PiStormsSensor(self.psc.BBS1)
        self.BBS2 = PiStormsSensor(self.psc.BBS2)
            
        self.BAM1 = PiStormsMotor(self.psc.BAM1)
        self.BAM2 = PiStormsMotor(self.psc.BAM2)
        self.BBM1 = PiStormsMotor(self.psc.BBM1)
        self.BBM2 = PiStormsMotor(self.psc.BBM2)
        
    def command (self, cmd, bank):
        self.psc.command(cmd, bank)
        
    #Shutdown command not yet implemented 
    # def Shutdown(self):
        # self.psc.Shutdown()
        
    ## Resets encoders for motors on BankA
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.resPosA()
    #  @endcode        
    def resPosA(self):
        self.psc.resPosA() 
        
    ## Resets encoders for motors on BankB
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.resPosA()
    #  @endcode        
    def resPosB(self):
        self.psc.resPosB()
        
    ## Returns the input battery voltage
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  volts = psm.battVoltage()
    #  if(volts > 6):
    #      # do some task
    #  @endcode    
    def battVoltage(self):
        return self.psc.battVoltage()
    
    ## Returns the PiStorms firmware version
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  fwVersion = psm.GetFirmwareVersion()
    #  print str(devID)
    #  @endcode    
    def GetFirmwareVersion(self):
        return self.psc.GetFirmwareVersion()
    
    ## Returns the PiStorms vendor name
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  venName = psm.GetVendorName()
    #  print str(devID)
    #  @endcode    
    def GetVendorName(self):
        return self.psc.GetVendorName()
    
    ## Returns the PiStorms device ID
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  devID = psm.GetDeviceId()
    #  print str(devID)
    #  @endcode    
    def GetDeviceId(self):
        return self.psc.GetDeviceId()
    
    ## Writes to the specified RGB LED
    #  @param self The object pointer.
    #  @param lednum The number to specify the LED (1 for BankA, 2 for BankB).
    #  @param red The red value to write to the specified LED (0-255).
    #  @param green The green value to write to the specified LED (0-255).
    #  @param blue The blue value to write to the specified LED (0-255).
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  psm.led(1,255,0,0)
    #  @endcode    
    def led(self,lednum,red,green,blue):
        return self.psc.led(lednum,red,green,blue)
    
    ## Check if the GO button is pressed
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  key = psm.isKeyPressed()
    #  if(key == True):
    #      # do some task
    #  @endcode    
    def isKeyPressed(self):
        return self.psc.isKeyPressed()

    ## Check if any Function button is pressed
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  key = psm.getKeyValue()
    #  if(key == 40):
    #      # (40 is F4), do some task
    #  @endcode    
    def getKeyPressValue(self):
        return self.psc.getKeyPressValue()

    ## Check if F1 Function button is pressed
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  key = psm.isF1Pressed()
    #  if(key == True):
    #      # F1 is pressed, do some task
    #  @endcode    
    def isF1Pressed(self):
        return (self.psc.getKeyPressValue() == 8)

    ## Check if F2 Function button is pressed
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  key = psm.isF2Pressed()
    #  if(key == True):
    #      # F2 is pressed, do some task
    #  @endcode    
    def isF2Pressed(self):
        return (self.psc.getKeyPressValue() == 16)

    ## Check if F3 Function button is pressed
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  key = psm.isF3Pressed()
    #  if(key == True):
    #      # F3 is pressed, do some task
    #  @endcode    
    def isF3Pressed(self):
        return (self.psc.getKeyPressValue() == 24)

    ## Check if F4 Function button is pressed
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  key = psm.isF4Pressed()
    #  if(key == True):
    #      # F4 is pressed, do some task
    #  @endcode    
    def isF4Pressed(self):
        return (self.psc.getKeyPressValue() == 40)
    
    ## Returns the GO button press count
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  keyCount = psm.getKeyPressCount()
    #  if(keyCount == 5):
    #      # do some task
    #  @endcode   
    def getKeyPressCount(self):
        return self.psc.getKeyPressCount()
    
    ## Resets the GO button press count
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from PiStorms import PiStorms 
    #  ...
    #  psm = PiStorms()
    #  resetKeyPressCount()
    #  @endcode   
    def resetKeyPressCount(self):
        self.psc.resetKeyPressCount()
    
    ### @cond
    ## Pings the PiStorms for reliable I2C communication
    #  @param self The object pointer.
    def ping(self):
        self.psc.ping()
    ### @endcond
    

if __name__ == '__main__':
    psm = PiStorms("PiStorms",rotation =3)
    buttonCount = 0
    psm.BBS1.resetTouchesEV3()
    print "Version = "+ str(psm.GetFirmwareVersion())
    print "Vendor = "+ str(psm.GetVendorName())
    print "Device = "+ str(psm.GetDeviceId())
    psm.screen.termPrintAt(3," Version is  "+ str(psm.GetFirmwareVersion() )[:5])
    psm.screen.termPrintAt(4," Version is  "+ str(psm.GetVendorName() ))
    psm.screen.termPrintAt(5," Version is  "+ str(psm.GetDeviceId() ))
   
    while(True):
        time.sleep(.300)
        print ' Touched at ( '+str(psm.screen.TS_X())+' , '+str(psm.screen.TS_Y())+')'
        psm.screen.termPrintAt(6,' Touched at  ('+str(psm.screen.TS_X())+' , '+str(psm.screen.TS_Y())+')')
        print " Voltage = "+str( psm.battVoltage())
        psm.screen.termPrintAt(7," Voltage = "+str( psm.battVoltage()))
        
        

