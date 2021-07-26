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
# 11/18/16  Deepak Patil  Initial authoring.
#
# EV3Lights Demo Program.


#initial setup code
import os,sys,inspect,time,threading, random
from mindsensors_i2c import mindsensors_i2c
from PiStorms import PiStorms
from mindsensors import EV3Lights

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

#starts an instance of PiStorms

ev3l = EV3Lights()
psm = PiStorms()
#exit variable will be used later to exit the program and return to PiStormsMaster
doExit = False

psm.screen.termPrintln("EV3Lights Demo")
psm.screen.termPrintln("connect mindsensors.com's ")
psm.screen.termPrintln("EV3Lights to BAS1 sensor Port")
psm.screen.termPrintln("")
psm.screen.termPrintln("")
psm.screen.termPrintln("")
psm.screen.termPrintln("")
psm.screen.termPrintln("Press GO button to exit")
psm.led(1, 0,0,0)
psm.led(2, 0,0,0)

psm.BAS1.activateCustomSensorI2C() #Connect the I2C sensor on the port BBS1
time.sleep(.1)
#main loop
# This test program will print IMU data on Terminal
# Compass heading is represented on Red LED on BANKB
# Program will exit when someone touch the screen or Go Button

time_gap = 0.5

while(not doExit):
    #
    try:
        psm.led(1, 100,0,0)
        ev3l.setColor(EV3Lights.RED, 100)
        time.sleep(time_gap)
        psm.led(1, 0,0,0)
        ev3l.setColor(EV3Lights.RED, 0)
        psm.led(1, 0,100,0)
        ev3l.setColor(EV3Lights.GREEN, 100)
        time.sleep(time_gap)
        psm.led(1, 0,0,0)
        ev3l.setColor(EV3Lights.GREEN, 0)
        psm.led(1, 0, 0, 100)
        ev3l.setColor(EV3Lights.BLUE, 100)
        time.sleep(time_gap)
        psm.led(1, 0,0,0)
        ev3l.setColor(EV3Lights.BLUE, 0)
        time.sleep(time_gap)
        for i in range(4):
            ev3l.setColor(EV3Lights.RED, 200)
            ev3l.setColor(EV3Lights.GREEN, 200)
            ev3l.setColor(EV3Lights.BLUE, 200)
            time.sleep(0.2)
            ev3l.setColor(EV3Lights.RED, 0)
            ev3l.setColor(EV3Lights.GREEN, 0)
            ev3l.setColor(EV3Lights.BLUE, 0)
            time.sleep(0.2)

    except:
        psm.led(1,0,0,0)
        psm.screen.termPrintAt(6,"connect EV3Lights on BAS1 ")

    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5)
        psm.led(1, 0,0,0)
        psm.led(2, 0,0,0)
        doExit = True
