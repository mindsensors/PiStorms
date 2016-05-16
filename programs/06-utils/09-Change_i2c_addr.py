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
# Oct 2015  Michael     Initial Authoring

import os,sys,inspect,time,thread
import socket,fcntl,struct,ms_explorerlib,subprocess    

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms

print "running program"
psm = PiStorms()
psm.screen.termPrintln("Connect your I2C device to BAS1")
psm.screen.termPrintln("and click Explore")
psm.screen.drawButton(75, 95, width = 85, height = 40, text="Explore", display=False)
psm.screen.drawButton(175, 95, width = 60, height = 40, text="Exit", display=True)

exit = False
lastled = 0

def explore():
    psm.screen.termPrintAt(5, "Searching for i2c device...")        
    psm.BAS1.activateCustomSensorI2C()
    time.sleep(3)
    addr = 0x00     # DO NOT change this address!!!
    i2c = ms_explorerlib.Explorer(addr)
    found = i2c.ping(0x00)  
    # Checks for connection on all I2C addresses until connection is found
    count = 0 
    while found == -1:     
        if (addr < 0xef):
            addr = addr + 1
            count = count + 1
            if (addr != 0x34 and addr != 0x35 and addr != 0x36 and addr != 0x37):
                i2c = ms_explorerlib.Explorer(addr)
                found = i2c.ping(0x00)
            if (count > 2000):
                found = 5
        else:
            addr = 0x00         
    if (found == 5):
        psm.screen.termPrintAt(5, "No Device found!")
        psm.screen.termPrintAt(6, "Click Exit to return to main menu")
        time.sleep(2)
        global exit
        exit = True
    else:
        global currAddr
        currAddr = addr
        #psm.screen.termPrintAt(5, "8 bit address: " + str(hex(addr)))      
        
def selectAddress():
    psm.screen.clearScreen()
    psm.screen.drawDisplay("PiStorms")
    psm.screen.drawArrows()
    psm.screen.termPrintAt(0, "Use arrows to choose i2c address")
    psm.screen.termPrintAt(1, "and click Change")
    psm.screen.drawButton(75, 95, width = 85, height = 40, text="Change", display=False)
    psm.screen.drawButton(175, 95, width = 60, height = 40, text="Exit", display=True)
    psm.screen.termPrintAt(5, "Address: " + str(hex(currAddr)))
    global nextAddr
    nextAddr = currAddr + 2
    psm.screen.termPrintAt(6, "New Address: ")
    psm.screen.termPrintAt(7, "       " + str(hex(nextAddr)))
    check = psm.screen.checkButton(75, 95,width=85,height=40)
    while(check == False): 
        check = psm.screen.checkButton(75, 95,width=85,height=40)
        bye = psm.screen.checkButton(175, 95,width=60,height=40)         
        if(psm.screen.checkArrows() == (False, True)):
            nextAddr = nextAddr + 2
        if(psm.screen.checkArrows() == (True, False)):
            nextAddr = nextAddr - 2        
        if(bye == True):
            psm.screen.termPrintAt(9, "Exiting to menu")
            global exit
            exit = True   
            check = True            
        psm.screen.termPrintAt(7, "       " + str(hex(nextAddr)))        
        #time.sleep(.25)
    
def changeAddress():
    psm.screen.termPrintAt(8, "Changing Address...")
    command = "/home/pi/PiStormsprograms/addresschange " + str(hex(currAddr)) + " " + str(hex(nextAddr))
    psm.screen.termPrintAt(9, command)
    #os.system
    subprocess.call(command, shell=True)  
    time.sleep(2)
    global exit
    exit = True
    
while(not exit):
    action = psm.screen.checkButton(75, 95,width=85,height=40)
    bye = psm.screen.checkButton(175, 95,width=60,height=40)
    #currAddr = 356
    #nextAddr = 36
    #command = './addresschange ' + str(hex(currAddr)) + " " + str(hex(nextAddr))
    #subprocess.call(command, shell=True) 
    if(action == True): 
        explore()
        if(exit == False):
            selectAddress()
            time.sleep(.25)
            if(exit == False):
                changeAddress()            
    if(bye == True):
        psm.screen.termPrintAt(9, "Exiting to menu")
        exit = True
    time.sleep(.1)