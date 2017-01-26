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
# Date       Author      Comments
# 07/15      Henry      Initial Authoring from PiStorms import PiStorms
# 10/18/15   Deepak     UI improvements and messenger integration
# 12/27/16   Roman      Fix to allow to run programs with a space
# 1/25/17    Seth       Reorder touschreen calibration value loading

from mindsensorsUI import mindsensorsUI
from mindsensors_i2c import mindsensors_i2c
from PiStormsCom import PiStormsCom
import sys, os, time, json, socket, signal
from datetime import datetime
import ConfigParser

if (len(sys.argv) > 1):
    # normalize the path that was provided
    # to remove extra slash if there is.
    PROGRAM_DIRECTORY = os.path.normpath(str(sys.argv[1]))
else:
    print "  ERROR: not enough arguments supplied"
    print "  Usage: "
    print "  python MSBrowser.py <programs_folder>"
    sys.exit(1)

json_file = '/var/tmp/ps_data.json'
version_json_file = '/var/tmp/ps_versions.json'
cfg_file = '/usr/local/mindsensors/conf/msdev.cfg'

config = ConfigParser.RawConfigParser()
config.read(cfg_file)

device_name = config.get('msdev', 'device') 
host_name = socket.gethostname()

#rotation = 3 
rotation = config.getint('msdev', 'rotation') 

if(os.getenv("PSREVERSE","0")=="1"):
    rotation = 3
#print os.getcwd()

device_number = 1
if ( device_name == "PiStorms"):
    device_number = 1
elif ( device_name == "SensorShield"):
    device_number = 2
elif ( device_name == "SRVController"):
    device_number = 3
else:
    print "Unknown device in configuration file, exiting..."
    sys.exit(1)

if PiStormsCom().GetFirmwareVersion() < 'V2.10':
    try:
        bootmode = mindsensors_i2c(0xEA>>1) 
        bootmode.readbyte()
        #psm = PiStorms("PiStorms",rotation)
        scrn = mindsensorsUI(host_name, rotation, device=device_number)
        scrn.termPrintAt(4,"PiStorms in fw upgrade mode")
    except:
        scrn = mindsensorsUI(host_name, rotation, device=device_number)
else:
    # load touchscreen calibration values from PiStorms and write to cache file
    ts_cal = None
    ts_cal_error = None
    try:
        psc = PiStormsCom()
        oldBAS1type = psc.BAS1.getType()
        psc.BAS1.setType(psc.BAS1.PS_SENSOR_TYPE_NONE)
        psc.bankA.writeByte(psc.PS_Command, psc.l) # copy from permanent memory to temporary memory
        timeout = time.time() + 1 # wait for up to a second
        while psc.bankA.readByte(psc.PS_TS_CALIBRATION_DATA_READY) != 1: # wait for ready byte
            time.sleep(0.01)
            if time.time() > timeout:
                raise TypeError() # same as failure from readInteger
        ts_cal = { 'x1': psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x00),
                   'y1': psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x02),
                   'x2': psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x04),
                   'y2': psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x06),
                   'x3': psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x08),
                   'y3': psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x0A),
                   'x4': psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x0C),
                   'y4': psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x0E) }
        psc.BAS1.setType(oldBAS1type)
    except TypeError: # failed readInteger
        ts_cal_error = ['Touchscreen Error', 'Failed to load', 'touchscreen calibration values']
    except IOError: # failed open in json.dump
        ts_cal_error = ['Touchscreen Error', 'Failed to write', 'touchscreen calibration values']
    except:
        ts_cal_error = ['Touchscreen Error', 'An unknown error occurred', 'while attempting to load', 'touchscreen calibration values']
    json.dump(ts_cal or {u'x1': 0, u'y1': 0, u'x2': 0, u'x3': 0, u'y3': 0, u'y2': 0, u'y4': 0, u'x4': 0}, open('/tmp/ps_ts_cal', 'w'))

    scrn = mindsensorsUI(host_name, rotation, device=device_number)

    if ts_cal == {u'x1': 0, u'y1': 0, u'x2': 0, u'x3': 0, u'y3': 0, u'y2': 0, u'y4': 0, u'x4': 0}:
        scrn.askQuestion(["Screen not calibrated.", "No touchscreen calibration values",
          "were found. Press GO to calibrate."], ["Press GO to continue..."], touch = False, goBtn = True)
        os.system("sudo python " + os.path.join(PROGRAM_DIRECTORY, "utils", "01-Calibrate") + ".py force")
        scrn = mindsensorsUI(host_name, rotation, device=device_number) # recreate with new calibration values

    if ts_cal_error is not None:
        scrn.askQuestion(ts_cal_error, ["Press GO to continue..."], touch = False, goBtn = True)

def listPrograms(directory):
    files =  os.listdir(directory)
    x = 0
    returnFiles = list()

    while(x<len(files)):
        if (os.path.isfile(directory+"/"+files[x])):
            # if it's a file, strip the extension to display.
            if(files[x].endswith(".py")) and (files[x][0:2].isdigit()):
                f = files[x][0:len(files[x])-3]
                returnFiles.append(f)
        elif (os.path.isdir(directory+"/"+files[x]) and files[x][0:2].isdigit()):
        # if it is a folder, display it
            returnFiles.append(files[x])

        x += 1
            
    #print "returnFiles: " + str(returnFiles)

    return sorted(returnFiles)

def checkIfUpdateNeeded():
    try:
        f = open(version_json_file, 'r')
        try:
            data = json.loads(f.read())
            s = data['status']
            u = data['update']
            f.close()
        except:
            # no json in the file (or file missing)
            s = ""
            u = ""
    except:
            # no json in the file (or file missing)
            s = ""        
            u = ""
    if ( s == 'New' and u != 'none' ):
        return u
    else:
        return 'none'
    
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

def version_json_update_field(field, new_value):
    f = open(version_json_file, 'r')
    json_data = json.loads(f.read())
    f.close()
    f = open(version_json_file, 'w')
    json_data[field] = new_value
    json.dump(json_data, f)
    f.close()

def message_update_status( json_data, new_status ):
    f = open(json_file, 'w')
    json_data['status'] = new_status
    json.dump(json_data, f)
    f.close()

def runProgram(progName,progDir):
    scrn.clearScreen()
    return os.system("sudo python '" +   progDir + "/" + progName + ".py'")
    
def drawBatteryIndicator(signum=None, stack=None, delay=300):
    battVoltage = PiStormsCom().battVoltage()
    batteryFill = (255,255,255) # white: error, could not read
    if ( battVoltage >= 7.7 ):
        batteryFill = (0,  166,90) # green: voltage >= 7.7V
    elif (battVoltage >= 6.9 ):
        batteryFill = (243,156,18) # yellow: 7.7V > voltage >= 6.9V
    else:
        batteryFill = (221,75, 57) #red: 6.9V > voltage
    scrn.fillRect(281, 185, 39, 45, fill=(0,0,0), display=False)
    scrn.fillRect(291, 188, 13, 20, fill=batteryFill, display=False)
    scrn.fillRect(294, 185,  7,  3, fill=batteryFill, display=False)
    scrn.drawAutoText(("%1.1f V" if battVoltage < 10 else "%2.0f V") % battVoltage, 281, 213, size=16, display=False)

    signal.alarm(delay)
    
def displaySmallFileList(folder, fileList, displayLeft = 1):
    initialYpos = 50
    xpos = 50
    height = 45
    width = 225
    
    scrn.clearScreen(display=False)
    scrn.drawDisplay(host_name, display=False)
    counter = 0

    while(counter<4 and counter<len(fileList)):
        if (os.path.isdir(folder+"/"+fileList[counter])):
            img="folder.png"
        elif (os.path.isfile(folder+"/"+fileList[counter]+".py")):
            img="python.png"
        scrn.drawButton(xpos,initialYpos + (height*counter),width=width,height=height,text=fileList[counter], image=img, display=False)
        counter += 1

    pageXPos = 0
    pageYPos = 0
    pageWidth = 50
    pageHeight = 50

    if(displayLeft == 1):
        scrn.drawButton(pageXPos, pageYPos, width=pageWidth, height=pageHeight, image="leftarrow.png", text="", display=False, imageX=8)
    elif(displayLeft == 2):
        scrn.drawButton(pageXPos, pageYPos, width=pageWidth, height=pageHeight, image="uparrow.png", text="", display=False, imageX=8)

    scrn.drawButton((320-pageXPos)-pageWidth, pageYPos, pageWidth, pageHeight, image="rightarrow.png", text="", display=False, imageX=(320-pageXPos)-pageWidth+8)

    updateReqd = checkIfUpdateNeeded()
    if ( updateReqd != 'none' ):
        scrn.fillBmp(220,7,34,34, "Exclamation-mark-icon.png", False);
    
    newMessage = newMessageExists()
    if ( newMessage == True ):
        scrn.fillBmp(220,7,34,34, "Exclamation-mark-icon.png", False);
    
    drawBatteryIndicator(delay=5*60) # redraw battery indicator every 5 minutes

    # display the buffered data on screen.
    scrn.disp.display()

    while(True):
        
        if ( newMessage ):
            # handle the exclamation button
            if ( scrn.checkButton(218,5,38,38)):
                # exclamation button was clicked
                return "message"
        elif ( updateReqd ):
            # handle the exclamation button
            #if ( scrn.checkButton(278,53,38,38)):
            if ( scrn.checkButton(218,5,38,38)):
                # exclamation button was clicked
                return "update:"+updateReqd


        if(displayLeft != 0 and scrn.checkButton(pageXPos,pageYPos,pageWidth,pageHeight)):
            return 4
        if(scrn.checkButton((320-pageXPos)-pageWidth,pageYPos,pageWidth,pageHeight)):
            return 5
        counter = 0
        while(counter<4 and counter<len(fileList)):
            if(scrn.checkButton(xpos,initialYpos + (height*counter),width=width,height=height)):
                return counter
            counter += 1
            
def displayFullFileList(folder, fileList, index, isSubFolder):

    newPath = folder
    if(index*4>len(fileList)):
        return displayFullFileList(folder, fileList, 0, isSubFolder)
    if(index <0):
        return displayFullFileList(folder, fileList, 0, isSubFolder)
    
    result = 0
    #displayLeft = index != 0
    if (index != 0):
        displayLeft = 1
    else:
        displayLeft = 0

    if (isSubFolder == True):
        if (index != 0):
            displayLeft = 1
        else:
            displayLeft = 2

    if(index*4+4<len(fileList)):
        result = displaySmallFileList(folder, fileList[index*4:index*4+4], displayLeft)
    else:
        result = displaySmallFileList(folder, fileList[index*4:len(fileList)], displayLeft)

    if(result == 4):
        # User clicked left arrow
        if ( isSubFolder == True):
            if (index == 0):
                # if the index is zero, then go back to parent folder.
                if ( not os.path.samefile(folder, PROGRAM_DIRECTORY) ):
                    # go back oly if we are already not at the home folder
                    newPath = os.path.dirname(folder)
                    f2 = listPrograms(newPath)
                    # On home directory, don't show left icon
                    if ( os.path.samefile(newPath, PROGRAM_DIRECTORY) ):
                        showLeftIcon = False
                    else:
                        showLeftIcon = True
                    return displayFullFileList(newPath, f2, 0, showLeftIcon)
                else:
                    return displayFullFileList(newPath, fileList, 0, False)
            else:
                # if index is not zero, just go to previous page.
                return displayFullFileList(folder, fileList,index - 1, isSubFolder)
        else:
            return displayFullFileList(folder, fileList,index - 1, isSubFolder)

    if(result == 5):
        # User clicked right arrow
        return displayFullFileList(folder, fileList,index + 1, isSubFolder)
    
    try:
        newResult = result + (index*4)
        ff = folder+"/"+fileList[newResult]
        if (os.path.isdir(ff)):
            newPath = ff
            f2 = listPrograms(newPath)
            return displayFullFileList(newPath, f2, 0, True)
        else:
            newFile = fileList[newResult]
    except TypeError:
        newResult = result
        newFile = ""
        
    return [newResult, newPath, newFile]

#
# main program loop
#
try:
    folder = PROGRAM_DIRECTORY

    signal.signal(signal.SIGALRM, drawBatteryIndicator)

    while(True):
        result = 0
        #if(psm.battVoltage()<=6.5):
        #    scrn.askQuestion(["LOW BATTERY","Your battery is low","Change or charge your batteries"],["Ignore"])
        #if(psm.isKeyPressed()):
        #     scrn.refresh()
        #files = listPrograms(PROGRAM_DIRECTORY)
        files = listPrograms(folder)
        if ( os.path.samefile(folder, PROGRAM_DIRECTORY) ):
            showLeftIcon = False
        else:
            showLeftIcon = True
        x = displayFullFileList(folder, files, 0, showLeftIcon)
        file_id = x[0]
        folder = x[1]
        fileName = x[2]
        if ( isinstance( file_id, int ) ):
            # if the value returned was integer
            #result = runProgram(files[file_id], folder)
            result = runProgram(fileName, folder)

        elif ( "update:" in file_id  and file_id != "update:none"):
            #
            # check what kind of update is available
            # and prompt message in dialog box
            #
            msg = ""
            msg2 = ""
            if ( file_id == "update:hardware" ):
                msg = "New Firmware for PiStorms is available"
                msg2 = ""
            if ( file_id == "update:software" ):
                msg = "New Software, libraries and samples"
                msg2 = "for PiStorms are available"
            if ( file_id == "update:both" ):
                msg = "New Firmware, Software, libraries and"
                msg2 = "samples for PiStorms are available"
            msg3 = "Install Updates?"
            answer = scrn.askQuestion(["Software Update", msg, msg2, "", msg3],["Yes", "Later", "Never"])

            if ( answer == 0 ):
                #print "User clicked OK"
                # perform the update
                result = os.system("sudo python " +   PROGRAM_DIRECTORY +
                          "/" + "utils/updater.py " + file_id)
                if (result == 0):
                    version_json_update_field('status', 'Done')

            if ( answer == 1 ):
                #print "User clicked Later"
                # User clicked Later, 
                # write the current time & status in the json file,
                # json updates will be deferred for some time
                # length of that time is defined in cron script
                version_json_update_field('status', 'Later')
                now = datetime.now()
                dd = now.strftime("%Y:%m:%d:%H:%M")
                version_json_update_field('date', dd)
            if ( answer == 2 ):
                #print "User clicked Never"
                # cron script will never update the json
                version_json_update_field('status', 'Never')

            # All errors must be gracefully handled by our updater script.
            # Force the result to be zero, so that even if there was error
            # browser does not show error dialog
            result = 0

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
            scrn.askQuestion(m,["OK"])
            result = 0 

        # FIXME: find a method (without psm) to float the motors.
        # possibly with direct i2c access.
        #psm.BAM1.float()
        #psm.BAM2.float()
        #psm.BBM1.float()
        #psm.BBM2.float()
        if(result != 0):
            scrn.refresh()
            scrn.askQuestion(["ERROR","Program exited with error.","(Error Code " + str(result) + ")"],["OK"])
            
except KeyboardInterrupt:
    print "Quitting..."
    scrn.refresh()
    scrn.termPrintln("PiStormsBrowser Exited")
