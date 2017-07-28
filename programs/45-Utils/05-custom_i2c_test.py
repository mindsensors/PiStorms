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
# 09/11/15  Nitin Patil     Initial Authoring
#
#Demo Code for the PiStorms and Raspberry Pi


#initial setup code
import os,sys,inspect,time,thread, random
from mindsensors_i2c import mindsensors_i2c
from PiStorms import PiStorms
from mindsensors import ABSIMU

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

#starts an instance of PiStorms

imu=ABSIMU()
psm = PiStorms()
#exit variable will be used later to exit the program and return to PiStormsMaster
exit = False

#clears the screen of any unwanted text by displaying a white rectangle
#psm.screen.fillRect(0, 0, 320, 240)
psm.screen.termPrintln("Custom I2C test program")
psm.screen.termPrintln("connect mindsensors.com's ")
psm.screen.termPrintln("AbsImu on port BBS1 ")
psm.led(1, 0,0,0)
psm.led(2, 0,0,0)

psm.BBS1.activateCustomSensorI2C() #Connect the I2C sensor on the port BBS1
#main loop
# This test program will print IMU data on Terminal 
# Compass heading is represented on Red LED on BANKB 
# Program will exit when someone touch the screen or Go Button

while(not exit):
    #
    try:
        heading = imu.get_heading()
        accl = imu.get_accelall()
        mag = imu.get_magall()
        gyro = imu.get_gyroall()
        psm.led(2,heading/3, 0,0)
        psm.screen.termPrintAt(6," Heading to "+ str(heading) +" degree")
    except:
        psm.led(2,0, 0,0)
        psm.screen.termPrintAt(6,"connect AbsImu on port BBS1 ")
     
    print " Accelerometer: " + str(accl)
    print " Magnetometer" + str(mag)
    print " Gyroscope: " + str(gyro)
    print " Compass: " + str(heading)
    
    time.sleep(.1)    
       
        
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        psm.led(1, 0,0,0)
        psm.led(2, 0,0,0)
        exit = True 