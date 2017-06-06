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
# 5/19/17    Seth       Rewrite

import sys, os, time, json, socket, signal, logging
from mindsensors_i2c import mindsensors_i2c
from mindsensorsUI import mindsensorsUI
from PiStormsCom import PiStormsCom
import Image, ImageDraw, ImageFont
from datetime import datetime
import ConfigParser

def getConfig():
    config = ConfigParser.RawConfigParser()
    config.read(configFile)
    return config
def getProgramDir():
    try:
        if (len(sys.argv) > 1):
            dir = str(sys.argv[1])
        else:
            home = config.get("msdev", "homefolder")
            dir = os.path.join(home, "programs")
    except:
        dir = "/home/pi/PiStorms/programs"
    # normalize the path that was provided to remove any trailing slash.
    return os.path.normpath(dir)
def getDeviceType():
    deviceID = config.get("msdev", "device") 
    if (deviceID == "PiStorms"):
        return 1
    elif (deviceID == "SensorShield"):
        return 2
    elif (deviceID == "SRVController"):
        return 3
    else:
        logging.error("Unknown device in configuration file, exiting...")
        sys.exit(1)
def getRotation():
    if (os.getenv("PSREVERSE", "0") == "1"):
        return 3
    else:
        return config.getint("msdev", "rotation") 
def initScreen():
    if (psc.GetFirmwareVersion() < "V3.00"):
        try:
            bootmode = mindsensors_i2c(0xEA>>1) 
            bootmode.readbyte()
            scrn = mindsensorsUI(deviceName, rotation, device=deviceType)
            scrn.termPrintAt(4, "PiStorms in fw upgrade mode")
            return scrn
        except:
            return mindsensorsUI(deviceName, rotation, device=deviceType)
    else:
        # load touchscreen calibration values from PiStorms and write to cache file
        ts_cal = None
        ts_cal_error = None
        ts_null = {u"x1": 0, u"y1": 0, u"x2": 0, u"x3": 0, u"y3": 0, u"y2": 0, u"y4": 0, u"x4": 0}
        try:
            oldBAS1type = psc.BAS1.getType()
            psc.BAS1.setType(psc.BAS1.PS_SENSOR_TYPE_NONE)
            psc.bankA.writeByte(psc.PS_Command, psc.l) # copy from permanent memory to temporary memory
            timeout = time.time() + 1 # wait for up to a second
            while (psc.bankA.readByte(psc.PS_TS_CALIBRATION_DATA_READY) != 1): # wait for ready byte
                time.sleep(0.01)
                if (time.time() > timeout):
                    raise TypeError() # same as failure from readInteger
            ts_cal = { "x1": psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x00),
                       "y1": psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x02),
                       "x2": psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x04),
                       "y2": psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x06),
                       "x3": psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x08),
                       "y3": psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x0A),
                       "x4": psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x0C),
                       "y4": psc.bankA.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x0E) }
            psc.BAS1.setType(oldBAS1type)
        except TypeError: # failed readInteger
            ts_cal_error = ["Touchscreen Error", "Failed to load", "touchscreen calibration values"]
        except IOError: # failed open in json.dump
            ts_cal_error = ["Touchscreen Error", "Failed to write", "touchscreen calibration values"]
        except:
            ts_cal_error = ["Touchscreen Error", "An unknown error occurred", "while attempting to load", "touchscreen calibration values"]
        json.dump(ts_cal or ts_null, open("/tmp/ps_ts_cal", "w"))

        scrn = mindsensorsUI(deviceName, rotation, device=deviceType)
        if ts_cal == ts_null:
            scrn.askQuestion(["Screen not calibrated.", "No touchscreen calibration values",
              "were found. Press GO to calibrate."], ["Press GO to continue..."], touch=False, goBtn=True)
            os.system("sudo python {}.py force".format(os.path.join(PROGRAM_DIRECTORY, "utils", "01-Calibrate")))
            return mindsensorsUI(deviceName, rotation, device=deviceType) # recreate with new calibration values
        if ts_cal_error is not None:
            logging.error('\n'.join(ts_cal_error))
            scrn.askQuestion(ts_cal_error, ["Press GO to continue..."], touch=False, goBtn=True)
            return scrn
def listPrograms(directory):
    return map(lambda i: i if not i.endswith(".py") else i[:-3], sorted(filter(lambda i: i[:2].isdigit(), os.listdir(directory))))

    # separate lines for readability:
    allFiles = os.listdir(directory)
    beginsWithNum = filter(lambda i: i[:2].isdigit(), allFiles)
    sortedFiles = sorted(beginsWithNum)
    withoutPy = map(lambda i: i if not i.endswith(".py") else i[:-3], sortedFiles)
    return withoutPy
def updateNeeded():
    try:
        with open(updateStatusFile, "r") as file:
            data = json.loads(file.read())
        return data["status"] == "New" and data["update"] != "none"
    except:
        return False
def newMessageExists():
    try:
        with open(messageFile, "r") as file:
            data = json.loads(file.read())
        return data["status"] == "New"
    except:
        return False
def runProgram(program):
    scrn.clearScreen()
    exitStatus = os.system("sudo python {}".format(program))
    # stop (float) motors, if they are still running after the program finishes
    psc.bankA.writeByte(PiStormsCom.PS_Command, PiStormsCom.c)
    psc.bankB.writeByte(PiStormsCom.PS_Command, PiStormsCom.c)
    return exitStatus
def promptUpdate():
    try:
        with open(messageFile, "r+") as file:
            data = json.loads(file.read())
            if data["status"] == "New":
                scrn.showMessage(data["message"].split("\n"))
                data["status"] = "Read"
                file.seek(0)
                json.dump(data, file)
                file.truncate()
                return
        with open(updateStatusFile, "r+") as file:
            data = json.loads(file.read())
            if data["status"] != "New" or data["update"] == "none":
                return
            message = {
                "update:none": "There are no updates available.",
                "update:hardware": "New PiStorms firmware is available.",
                "update:software": "New software, libraries, and samples are available.",
                "update:both": "New firmware, software, libraries, and samples are available."
            }
            response = scrn.askQuestion(
                    ["Software Update", message[data["update"]], "Install updates?"],
                    ["Yes", "Later", "Never"], wrapText=True)
            if response == 0:
                exitCode = os.system("sudo python {} {}"
                        .format(os.path.join(PROGRAM_DIRECTORY, "utils", "updater.py"), data["update"]))
                if exitCode == 0:
                    data["status"] = "Done"
            elif response == 1:
                data["status"] = "Later"
                data["date"] = datetime.now().strftime("%Y:%m:%d:%H:%M")
            elif response == 2:
                data["status"] = "Never"
            file.seek(0)
            json.dump(data, file)
            file.truncate()
    except:
        logging.warning("Could not prompt update.")

def drawHostnameTitle():
    size = 30
    maxWidth = 320-50-50-5-5 # screen width is 320, each arrow is 50px wide, 5px margin
    if newMessageExists() or updateNeeded():
        maxWidth -= 44
    getTextSize = ImageDraw.Draw(scrn.disp.buffer).textsize
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size)
    width, height = getTextSize(deviceName, font=font)
    while (width > maxWidth):
        size -= 1
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size)
        width, height = getTextSize(deviceName, font=font)
    scrn.fillRect(55, 0, maxWidth, 50, fill=(0,0,0), display=False)
    if (newMessageExists() or updateNeeded()) and width > 135:
        scrn.drawAutoText(deviceName, 60, (50-height)/2-5, fill=(0,255,255), size=size, display=False)
    else:
        scrn.drawAutoText(deviceName, 0, (50-height)/2-5, fill=(0,255,255), size=size, display=False, align="center")
def drawItemButton(folder, file, i):
    if os.path.isdir(os.path.join(folder, file)):
        icon = "folder.png"
    elif os.path.isfile(os.path.join(folder, file+".py")):
        icon = "python.png"
    else:
        icon = "missing.png"
    scrn.drawButton(50, 50+(i%FILES_PER_PAGE)*45, width=320-50*2, height=45, text=file, image=icon, display=False)
def drawRightArrow():
    scrn.drawButton(320-50, 0, 50, 50, image="rightarrow.png", text="", display=False, imageX=320-50+8)
def drawLeftArrow():
    scrn.drawButton(0, 0, 50, 50, image="leftarrow.png", text="", display=False, imageX=8)
def drawUpArrow():
    scrn.drawButton(0, 0, 50, 50, image="uparrow.png", text="", display=False, imageX=8)
def drawExclamation():
    scrn.fillBmp(230, 7, 34, 34, "Exclamation-mark-icon.png", display=False);
def drawBatteryIndicator(*ignored):
    if (scrn.currentMode == scrn.PS_MODE_POPUP):
        return
    battVoltage = psc.battVoltage()
    batteryFill = (255, 255, 255) # white: error, could not read
    if (battVoltage >= 7.7):
        batteryFill = (0, 166, 90) # green: voltage >= 7.7V
    elif (battVoltage >= 6.9):
        batteryFill = (243, 156,18) # yellow: 7.7V > voltage >= 6.9V
    else:
        batteryFill = (221, 75, 57) #red: 6.9V > voltage
    scrn.fillRect(281, 185, 39, 45, fill=(0, 0, 0), display=False)
    scrn.fillRect(291, 188, 13, 20, fill=batteryFill, display=False)
    scrn.fillRect(294, 185,  7,  3, fill=batteryFill, display=False)
    scrn.drawAutoText(("%1.1f V" if battVoltage < 10 else "%2.0f V") % battVoltage, 281, 213, size=16, display=True)
    signal.alarm(30) # redraw battery indicator in thirty seconds

def rightArrowPressed():
    return scrn.checkButton(320-50, 0, 50, 50)
def leftArrowPressed(index, filesPerPage):
    return (scrn.checkButton(0, 0, 50, 50) and index >= filesPerPage)
def upArrowPressed(stack):
    return (scrn.checkButton(0, 0, 50, 50) and len(stack) > 1)
def exclamationPressed():
    return scrn.checkButton(218, 5, 38, 38)
def itemButtonPressed(folder, files, index, filesPerPage):
    for i in getPageOfItems(files, index, filesPerPage):
        if scrn.checkButton(50, 50+(i%filesPerPage)*45, 320-50*2, 45):
            item = os.path.join(folder, files[i])
            isFolder = os.path.isdir(item)
            if not isFolder:
                return (item+".py", False)
            else:
                return (item, True)
    return (False, None)
def getPageOfItems(files, index, filePerPage):
    if (index+filePerPage-1 > len(files)-1):
        return range(INDEX, len(files))
    else:
        return range(INDEX, INDEX+FILES_PER_PAGE)

if __name__ == "__main__":
    try:
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        messageFile = "/var/tmp/ps_data.json"
        updateStatusFile = "/var/tmp/ps_versions.json"
        configFile = "/usr/local/mindsensors/conf/msdev.cfg"
        config = getConfig()
        PROGRAM_DIRECTORY = getProgramDir()
        deviceType = getDeviceType()
        deviceName = socket.gethostname()
        rotation = getRotation()
        psc = PiStormsCom()
        scrn = initScreen()
        # A stack of lists. One list is pushed each time a folder is opened,
        # and popped when going up a directory. The 0th element of the list is a string
        # for the folder, followed by a list of files in that folder, and finally
        # an integer for the index of which file will appear first in the list.
        # Note that stack[-1] is the "current" directory.
        stack = [[PROGRAM_DIRECTORY, listPrograms(PROGRAM_DIRECTORY), 0]]
        FILES_PER_PAGE = 4

        # Start the battery indicator routine update.
        signal.signal(signal.SIGALRM, drawBatteryIndicator)

        while True:
            logging.debug([(s[0],s[2]) for s in stack])

            FOLDER, FILES, INDEX = stack[-1]

            scrn.clearScreen(display=False)
            drawHostnameTitle()

            for i in getPageOfItems(FILES, INDEX, FILES_PER_PAGE):
                drawItemButton(FOLDER, FILES[i], i)

            drawRightArrow()
            if INDEX >= FILES_PER_PAGE:
                drawLeftArrow()
            elif len(stack) > 1:
                drawUpArrow()

            if newMessageExists() or updateNeeded():
                drawExclamation()

            drawBatteryIndicator()

            while True:
                if exclamationPressed():
                    promptUpdate()
                    break
                if rightArrowPressed():
                    newIndex = INDEX + FILES_PER_PAGE
                    if newIndex > len(FILES)-1:
                        newIndex = 0
                    stack[-1][2] = newIndex
                    break
                if leftArrowPressed(INDEX, FILES_PER_PAGE):
                    stack[-1][2] = INDEX-4 if INDEX >= 4 else 0
                    break
                if upArrowPressed(stack):
                    stack.pop()
                    break

                item, isFolder = itemButtonPressed(FOLDER, FILES, INDEX, FILES_PER_PAGE)
                if item and isFolder:
                    stack.append([item, listPrograms(item), 0])
                    break
                if item and not isFolder:
                    print("Running program " + item)
                    runProgram(item)
                    break
    except KeyboardInterrupt:
        logging.info("Quitting MSBrowser")
        scrn.refresh()
        scrn.termReplaceLastLine("PiStormsBrowser Exited")
