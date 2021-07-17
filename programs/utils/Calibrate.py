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
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# 05/25/16   Deepak     Initial development.
#

import time, sys
from PiStorms import PiStorms

psm = PiStorms()

width=320
height=240

opt1 = ""

if ( len(sys.argv) > 1 ):
    opt1 = str(sys.argv[1])

psm.resetKeyPressCount()

if ( opt1 != "force" ):
    psm.screen.termPrintAt(1, "Touch Screen Calibration Program")
    psm.screen.termPrintAt(3, "You should only calibrate if you")
    psm.screen.termPrintAt(4, "upgraded PiStorms Firmware.")
    psm.screen.termPrintAt(6, "Do you still want to calibrate?")
    psm.screen.termPrintAt(7, "To Confirm 'Yes':")

    doCalibrate = False
    count = 11
    oldKeyPressCount = psm.getKeyPressCount()
    while ( count > 0 ):
        psm.screen.termPrintAt(8, "press GO button within " + str(count) +" seconds")
        count = count - 1
        newKeyPressCount = psm.getKeyPressCount()
        if ( newKeyPressCount > oldKeyPressCount ):
            count = 0
            doCalibrate = True
        time.sleep(1)

    if ( doCalibrate == False ):
        psm.screen.disp.clear()
        psm.screen.termPrintAt(8, "Not calibrating ...")
        quit()

psm.screen.disp.clear()
psm.screen.termPrintAt(1, "Touch Screen Calibration Program")
psm.screen.termPrintAt(3, "On next screen, touch and hold")
psm.screen.termPrintAt(4, "stylus PRECISELY on the")
psm.screen.termPrintAt(5, "Cross-Hair and Press GO button.")
psm.screen.termPrintAt(6, "Then follow on screen instructions.")
psm.screen.termPrintAt(8, "Press GO button to continue")
doExit = False
while (doExit == False):
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        doExit = True
time.sleep(2)

draw = psm.screen.disp.draw()
w = width/4
h = height/4

psm.screen.disp.clear()
draw.line((h-10, w, h+10, w), fill=(0,255,0))
draw.line((h, w-10, h, w+10), fill=(0,255,0))
psm.screen.disp.display()

psm.screen.termPrintAt(7, "Touch & Hold Stylus")
psm.screen.termPrintAt(8, "on the Cross-Hair")
psm.screen.termPrintAt(9, "And press the GO button")
doExit = False
while (doExit == False):
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        if (1 ):  # psm.screen.isTouched()
            time.sleep(1)
            psm.psc.bankA.writeByte(psm.psc.PS_Command, psm.psc.E)
            time.sleep(0.1)
            psm.psc.bankA.writeByte(psm.psc.PS_Command, psm.psc.t)
            time.sleep(0.1)
            doExit = True 
        else:
            psm.screen.termPrintAt(8, "Screen not touched!!")
            
psm.screen.disp.clear()
psm.screen.termPrintAt(8, "Do it again at new position")
w = (width/4)*3
h = (height/4)*3
draw.line((h-10, w, h+10, w), fill=(0,255,0))
draw.line((h, w-10, h, w+10), fill=(0,255,0))
psm.screen.disp.display()

doExit = False
while (doExit == False):
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        if ( 1 ):  #psm.screen.isTouched()
            time.sleep(1)
            psm.psc.bankA.writeByte(psm.psc.PS_Command, psm.psc.E)
            time.sleep(0.1)
            psm.psc.bankA.writeByte(psm.psc.PS_Command, psm.psc.T)
            time.sleep(0.1)
            doExit = True 
        else:
            psm.screen.termPrintAt(8, "Screen not touched!!")
            
psm.screen.disp.clear()
psm.screen.termPrintAt(8, "Calibration complete")
time.sleep(1)
quit()
