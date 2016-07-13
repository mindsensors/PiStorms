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
# September 20, 2015  Nitin Patil     Initial Authoring 

from PiStorms import PiStorms

#Demo Code for the PiStorms and Raspberry Pi


#initial setup code
import os,sys,inspect,time,thread, random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
#sys.path.insert(0,parentdir) 
from PiStorms  import PiStorms 

#starts an instance of PiStorms 
psm = PiStorms (rotation =1)

#exit variable will be used later to exit the program and return to PiStorms 
exit = False

#clears the screen of any unwanted text by displaying a white rectangle
psm.screen.fillRect(0, 0, 320, 240)

#displays PiDoG's greeting of "Hello, I PiDoG"
psm.screen.drawAutoText("Hello", 80, 30, fill=(255, 0, 0), size = 70)
psm.screen.drawAutoText("I am PyDog", 50, 140, fill=(255, 0, 0), size = 45)
count = 0


#main loop
while(not exit):
    
    if(psm.BBS2.distanceUSEV3() < 200): #if ultrasonic sensor reading is <200 (~6")
        
        #play Barking sound
        psm.screen.fillBmp(30, 0, 240, 240, path = currentdir+'/'+"dog.png")
        os.system('mpg123 -q  -f55000 /home/pi/PiStormsprograms/Puppy_Dog_Barking.mp3 &')
        mytime = int(round(time.time())) 
        
        while (int(round(time.time()))  - mytime ) < 10:
            #Quickly wag dog tail
            count = 0
            while count < 5:
                #psm.BAM2.setSpeed(-5);
                psm.BBM1.setSpeed(10);
                psm.BAM1.setSpeed(-10);
                time.sleep(0.05)
                #psm.BAM2.setSpeed(5);
                psm.BBM1.setSpeed(-10);
                psm.BAM1.setSpeed(10);
                time.sleep(0.05)
                count = count + 1
            psm.BAM2.setSpeed(0); 
            psm.BBM1.setSpeed(0); 
            psm.BAM1.setSpeed(0); 
            count = 0
            while count < 10:
                psm.BAM2.setSpeed(-5);
                #psm.BBM1.setSpeed(15);
                #psm.BAM1.setSpeed(-15);
                time.sleep(0.2)
                psm.BAM2.setSpeed(5);
                #psm.BBM1.setSpeed(-15);
                #psm.BAM1.setSpeed(15);
                time.sleep(0.2)
                count = count + 1
            psm.BAM2.setSpeed(0); 
            psm.BBM1.setSpeed(0); 
            psm.BAM1.setSpeed(0);         
            time.sleep(1)
 
        
        #clear screen of scared emoticon
        psm.screen.fillRect(0, 0, 320, 240)
        
              
        
        #redraw "Hello I am Sam"        
        psm.screen.drawAutoText("Hello", 80, 30, fill=(255, 0, 0), size = 70)
        psm.screen.drawAutoText("I am PyDog", 50, 140, fill=(255, 0, 0), size = 45)
        
        
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        exit = True 