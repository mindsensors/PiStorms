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
import os,sys,inspect,time#thread
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
     m = ["PopHeads", "Camera not enabled.", "Run raspi-config and enable camera"]
     psm.screen.askQuestion(m,["OK"])
     exit()
exitNow = 0
time.sleep(.2)
# Create the haar cascade
haar_path=currentdir+"/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(haar_path)
#psm.screen.fillRect(95, 145, 110, 160)
#psm.screen.fillRect(100, 150, 100, 150, fill=(0,0,0))
while not exitNow:
	psm.screen.termPrintAt(9, "Click Go to take a picture")
	if(psm.isKeyPressed()):
		# call("raspistill -o /tmp/cam.jpg", shell=True)
		# time.sleep(2)
		# psm.screen.fillBmp(0,0,100,100,path = "/tmp/cam.jpg")
		# time.sleep(2)
		picam.capture('/tmp/pic.jpg')
		psm.screen.fillBmp(0,0,320,240,path = "/tmp/pic.jpg")
		psm.screen.termPrintAt(8, "Captured!")
		time.sleep(1)
		psm.screen.termPrintAt(8, "Detecting faces...")
		img = cv2.imread('/tmp/pic.jpg')
		(imh, imw) = img.shape[:2]
		grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(grayimg, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
		print( imw, imh, faces)
		for (x,y,w,h) in faces:
			psm.screen.fillCircle(x-(w/4), y, int((w+h)/6), fill = (255,255,255),display = False)
			psm.screen.fillCircle(x-(w/4), y, int(-2+(w+h)/6), fill = (0,0,0),display = False)
			psm.screen.fillCircle(x-(w/4)+w/6, y-h/6, 4, fill = (255,255,255),display = False)
			psm.screen.fillCircle(x-(w/4)-w/6, y-h/6, 4, fill = (255,255,255),display = True)
			#psm.screen.fillRect(x-(w/2), x-(w/2), w/2, h/2, fill = (0,0,0))
		if ((len(faces)) > 1) or ((len(faces)) == 0):
			psm.screen.termPrintAt(8, " Found {0} faces!".format(len(faces)))
		elif (len(faces)) == 1:
			psm.screen.termPrintAt(8, " Found {0} face!".format(len(faces)))

	if (psm.screen.isTouched()):
			psm.screen.clearScreen()
			psm.screen.termPrintAt(9,"Exiting to menu")
			time.sleep(0.5)
			exitNow = True
