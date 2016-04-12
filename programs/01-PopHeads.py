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
# Jan 2016   Nitin     Initial Authoring 

from picamera.array import PiRGBArray
from picamera import PiCamera
import os,sys,inspect,time#thread
import cv2
import imutils
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms
psm = PiStorms()


print "running program"
psm.screen.termPrintln(" ")

# Get user supplied values
#cascPath = sys.argv[1]

# Create the haar cascade
#faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier("/home/pi/PiStorms/programs/haarcascade_frontalface_default.xml")

# initialize the camera and grab a reference to the raw camera capture
#down size the image resolution for imporving speed. 
try:
    camera = PiCamera()
except:
    m = ["PopHeads", "Camera not enabled.", "Run raspi-config and enable camera"]
    psm.screen.askQuestion(m,["OK"])
    exit()
    
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

# allow the camera to warmup
time.sleep(0.1)

#create milisecond time variable for benchmarking
lastTime = time.time()*1000.0

# capture frames from the camera
lastfaces = {}
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array
    (imh, imw) = image.shape[:2]
    
    #convert the image from color to Grayscale space
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    
    #print benchmarking information on Console
    print time.time()*1000.0-lastTime," Found {0} faces!".format(len(faces))
    lastTime = time.time()*1000.0
    
    # Draw a rectangle around the faces
    
    for (x, y, w, h) in lastfaces:
        psm.screen.fillCircle(imw-(x+w), y+h, int((w+h)/3), fill = (0,0,0),display = True)
    
    for (x, y, w, h) in faces:
        # for displaying on exported display
        cv2.circle(image, (x+w/2, y+h/2), int((w+h)/3), (255, 255, 255), 1)
        
        # for showing on PiStorms screen
        psm.screen.fillCircle(imw-(x+w), y+h, int((w+h)/3), fill = (255,255,255),display = False)
        psm.screen.fillCircle(imw-(x+w), y+h, int(-2+(w+h)/3), fill = (0,0,0),display = False)
        psm.screen.fillCircle(imw-(x+w)+w/4, y+h-h/4, 4, fill = (255,255,255),display = False)
        psm.screen.fillCircle(imw-(x+w)-w/4, y+h-h/4, 4, fill = (255,255,255),display = True)
        
        
    # show the frame use this if you are setup for Display export on your pc or VNC
    #you may use Xming server for this
    
    #cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    lastfaces = faces
 
	# clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
	# if the `q` key was pressed, break from the loop
    if(psm.isKeyPressed() == True):
        break
    #if key == ord("q"):
    #    break
        
  
        

