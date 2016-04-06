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
#  July 2015  Henry     Initial Authoring from PiStorms import PiStorms
# 10/18/15   Deepak     UI improvements and messenger integration

from PiStorms import PiStorms
from mindsensors_i2c import mindsensors_i2c
import sys, os, time, json

print str(sys.argv[1])
PROGRAM_DIRECTORY = str(sys.argv[1])
json_file = '/var/tmp/ps_data.json'
rotation = 3 
if(os.getenv("PSREVERSE","0")=="1"):
    rotation = 3
#print os.getcwd()

try:
    bootmode = mindsensors_i2c(0xEA>>1) 
    bootmode.readbyte()
    psm = PiStorms("PiStorms",rotation)
    psm.screen.termPrintAt(4,"PiStorms in fw upgrade mode")
    
except:
    psm = PiStorms("PiStorms",rotation) 

#sudo 
def listPrograms(directory):
    files =  os.listdir( directory)
    x = 0
    while(x<len(files)):
        if(not files[x].endswith(".py")) or (not files[x][0:2].isdigit()):
            del files[x]
           
        else:
            #if not(files[x][0:2].isdigit()):
            #    files[x] =  '0' + files[x][0:]
            files[x] = files[x][0:len(files[x])-3]
            x += 1

    return sorted(files)

def newMessageExists():
    try:
        f = open(json_file, 'r')
        try:
            data = json.loads(f.read())
            s = data['status']
            f.close()
        except:
            # no json in the file (or file missing)
            s = ""
    except:
            # no json in the file (or file missing)
            s = ""        
    if ( s == 'New' ):
        return True
    else:
        return False

def message_update_status( json_data, new_status ):
    f = open(json_file, 'w')
    json_data['status'] = new_status
    json.dump(json_data, f)
    f.close()

def runProgram(progName,progDir):
    psm.screen.clearScreen()
    return os.system("sudo python " +   progDir + "/" + progName + ".py")
    
    
def displaySmallFileList(fileList, displayLeft = True):
    initialYpos = 50
    xpos = 50
    height = 45
    width = 225
    
    psm.screen.clearScreen(display=False)
    psm.screen.drawDisplay("PiStorms",display=False)
    counter = 0
    while(counter<4 and counter<len(fileList)):
        psm.screen.drawButton(xpos,initialYpos + (height*counter),width=width,height=height,text=fileList[counter], display=False)
        counter += 1
    pageXPos = 0
    pageYPos = 0
    pageWidth = 50
    pageHeight = 50
    if(displayLeft):
        psm.screen.drawButton(pageXPos, pageYPos, width=pageWidth, height=pageHeight, text="<", display=False)

    psm.screen.drawButton((320-pageXPos)-pageWidth, pageYPos, pageWidth, pageHeight, text=">", display=False)

    newMessage = newMessageExists()
    if ( newMessage == True ):
        psm.screen.fillBmp(220,7,34,34, "Exclamation-mark-icon.png", False);
    
    # display the buffered data on screen.
    psm.screen.disp.display()

    while(True):
        
        if ( newMessage ):
            # handle the exclamation button
            if ( psm.screen.checkButton(218,5,38,38)):
                # exclamation button was clicked
                return "message"

        if(displayLeft and psm.screen.checkButton(pageXPos,pageYPos,pageWidth,pageHeight)):
            return 4
        if(psm.screen.checkButton((320-pageXPos)-pageWidth,pageYPos,pageWidth,pageHeight)):
            return 5
        counter = 0
        while(counter<4 and counter<len(fileList)):
            if(psm.screen.checkButton(xpos,initialYpos + (height*counter),width=width,height=height)):
                return counter
            counter += 1
            
def displayFullFileList(fileList,index = 0):
    if(index*4>len(fileList)):
        return displayFullFileList(fileList,0)
    if(index <0):
        return displayFullFileList(fileList,0)
    
    result = 0
    displayLeft = index != 0
    if(index*4+4<len(fileList)):
        result = displaySmallFileList(fileList[index*4:index*4+4],displayLeft)
    else:
        result = displaySmallFileList(fileList[index*4:len(fileList)],displayLeft)
    if(result == 4):
        return displayFullFileList(fileList,index - 1)
    if(result == 5):
        return displayFullFileList(fileList,index + 1)
    
    try:
        newResult = result + (index*4)
    except TypeError:
        newResult = result

    return newResult

#
# main program loop
#
try:
    while(True):
        result = 0
        #if(psm.battVoltage()<=6.5):
        #    psm.screen.askQuestion(["LOW BATTERY","Your battery is low","Change or charge your batteries"],["Ignore"])
        #if(psm.isKeyPressed()):
        #     psm.screen.refresh()
        files = listPrograms(PROGRAM_DIRECTORY)
        file_id = displayFullFileList(files)
        if ( isinstance( file_id, int ) ):
            result = runProgram(files[file_id],PROGRAM_DIRECTORY)
        elif ( file_id == "message"):
            f = open(json_file, 'r')
            try:
                data = json.loads(f.read())
                m = data['message'].split("\n")
                s = data['status']
                f.close()
            except:
                pass
            message_update_status( data, "Read" )
            psm.screen.askQuestion(m,["OK"])
            result = 0 

        psm.BAM1.float()
        psm.BAM2.float()
        psm.BBM1.float()
        psm.BBM2.float()
        if(result != 0):
            psm.screen.refresh()
            psm.screen.askQuestion(["ERROR","Program exited with error.","(Error Code " + str(result) + ")"],["OK"])
            
except KeyboardInterrupt:
    print "Quitting..."
    psm.screen.refresh()
    psm.screen.termPrintln("PiStormsBrowser Exited")
