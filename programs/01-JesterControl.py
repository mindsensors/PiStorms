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
#  Aug 2015  Andrew     Initial Authoring from SensorShield import SensorShield


import os,sys,inspect,time,thread,random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms

# starts an instance of PiStorms
psm = PiStorms()

### setup variables ###
# exit is used to eventually exit the main running loop
exit = False

# sets screen to a white background
psm.screen.fillRect(0, 0, 320, 240)

# initial loading screen
psm.screen.fillBmp(50, 20, 100, 100, path = currentdir+'/'+"faceClown.png")
psm.screen.drawAutoText("Hi There!", 15, 140, fill=(0, 0, 0), size = 30)
psm.screen.drawAutoText("poke my eyes or tap my nose", 15, 170, fill=(0, 0, 0), size = 20)
time.sleep(.5)
psm.screen.drawAutoText("3", 50,200,fill=(0,0,0),size=25)
time.sleep(.5)
psm.screen.fillRect(50,200,25,25)
psm.screen.drawAutoText("2", 50,200,fill=(0,0,0),size=25)
time.sleep(.5)
psm.screen.fillRect(50,200,25,25)
psm.screen.drawAutoText("1", 50,200,fill=(0,0,0),size=25)
time.sleep(.5)
psm.screen.fillRect(50,200,25,25)
psm.screen.drawAutoText("GO", 50,200,fill=(0,0,0),size=25)
time.sleep(.5)

currFace = -1

# sets screen to a white background
psm.screen.fillRect(0, 0, 320, 240)

while(not exit):
    #plain face
    if(currFace != 0):
        psm.screen.fillBmp(40, 0, 240, 240, path = currentdir+'/'+"faceClown.png")
        currFace = 0
        
    #right eye
    if(psm.screen.checkButton(106, 68, 44, 53)):
        psm.screen.fillBmp(40,0,240,240, path = currentdir+'/'+"faceClown_eyeRight.png")
        currFace = 1
        
    #left eye
    if(psm.screen.checkButton(175, 68, 44, 53)):
        psm.screen.fillBmp(40,0,240,240, path = currentdir+'/'+"faceClown_eyeLeft.png")
        currFace = 1
    
    #nose
    if(psm.screen.checkButton(130, 122, 70, 60)):
        psm.screen.fillBmp(40,0,240,240, path = currentdir+'/'+"faceClown_nose.png")
        currFace = 1
    
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        exit = True 