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
#
#mindsensors.com invests time and resources providing this open source code,
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date            Author      Comments
# July 7, 2016    Yug Rao     Initial Authoring


from picamera.array import PiRGBArray
from picamera import PiCamera
import os,sys,inspect,time
from subprocess import call
import cv2
import imutils
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PiStorms import PiStorms
psm = PiStorms()

try:
    picam = PiCamera()
except:
     m = ["Take Selfie", "Camera not enabled.", "Run raspi-config and enable camera"]
     psm.screen.askQuestion(m,["OK"])
     exit()
exitNow = 0
time.sleep(.2)
while not exitNow:
	psm.screen.termPrintAt(8, "Click Go to take a picture")
	if(psm.isKeyPressed()):
		picam.capture('/tmp/pic.jpg')
		psm.screen.fillBmp(0,0,320,240,path = "/tmp/pic.jpg")
		psm.screen.termPrintAt(8, "Captured!")
		time.sleep(1)
		psm.screen.termPrintAt(9, "Touch the screen to exit")

	if (psm.screen.isTouched()):
			psm.screen.clearScreen()
			psm.screen.termPrintAt(9,"Exiting to menu")
			time.sleep(0.5)
			exitNow = True
