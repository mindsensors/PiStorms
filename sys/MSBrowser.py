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
from PiStormsCom_GRX import GRXCom
import Image, ImageDraw, ImageFont
from datetime import datetime
from fcntl import flock, LOCK_EX, LOCK_UN, LOCK_NB
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
    dir = os.path.normpath(dir)
    # possibly append "_grx" if a PiStorms GRX is connected, using the "programs_grx" folder
    if "GRX" in config.get('msdev', 'device'):
        dir += "_grx"
    return dir
def getRotation():
    if (os.getenv("PSREVERSE", "0") == "1"):
        return 3
    else:
        return config.getint("msdev", "rotation")
def initScreen():
    try:
        bootmode = mindsensors_i2c(0xEA>>1)
        bootmode.readbyte()
        scrn = mindsensorsUI(deviceName, rotation)
        scrn.termPrintAt(4, "PiStorms in fw upgrade mode")
        return scrn
    except:
        return mindsensorsUI(deviceName, rotation)
def listPrograms(directory):
    allFiles = os.listdir(directory)
    beginsWithNum = filter(lambda i: i[:2].isdigit(), allFiles)
    onlyPythonFiles = filter(lambda i: os.path.isdir(os.path.join(directory, i)) or i.endswith(".py"), beginsWithNum)
    sortedFiles = sorted(onlyPythonFiles)
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
    if psc == GRXCom:
        for s in GRXCom.SERVO:
            GRXCom.I2C.A.writeArray(s, [0,0])
            GRXCom.I2C.B.writeArray(s, [0,0])
    else:
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
                "none": "There are no updates available.",
                "hardware": "New PiStorms firmware is available.",
                "software": "New software, libraries, and samples are available.",
                "both": "New firmware, software, libraries, and samples are available."
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
def drawReturnArrow():
    scrn.drawButton(320-50, 0, 50, 50, image="returnarrow.png", text="", display=False, imageX=320-50+8)
def drawLeftArrow():
    scrn.drawButton(0, 0, 50, 50, image="leftarrow.png", text="", display=False, imageX=8)
def drawUpArrow():
    scrn.drawButton(0, 0, 50, 50, image="uparrow.png", text="", display=False, imageX=8)
def drawRefreshArrow():
    scrn.drawButton(0, 0, 50, 50, image="refresharrow.png", text="", display=False, imageX=8)
def drawExclamation():
    scrn.fillBmp(230, 7, 34, 34, "Exclamation-mark-icon.png", display=False)
def drawPageNumber(index, numberOfFiles, filesPerPage):
    scrn.drawAutoText("Page", 4, 195, size=16, display=False)
    string = "%d of %d" % (1+index/filesPerPage, 1+numberOfFiles/filesPerPage)
    scrn.drawAutoText(string, 4, 213, size=16, display=False)
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
def leftArrowPressed():
    return scrn.checkButton(0, 0, 50, 50)
def exclamationPressed():
    return scrn.checkButton(218, 5, 38, 38)
def itemButtonPressed(folder, files, index, filesPerPage):
    for i in getPageOfItems(files, index, filesPerPage):
        if scrn.checkButton(50, 50+(i%filesPerPage)*45, 320-50*2, 45):
            return os.path.join(folder, files[i])
    return False
def getPageOfItems(files, index, filesPerPage):
    if (index+filesPerPage-1 > len(files)-1):
        return range(index, len(files))
    else:
        return range(index, index+filesPerPage)

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    mutex = open("/var/lock/msbrowser", "w+")
    # allow lock to be modified without sudo permissions
    os.chown("/var/lock/msbrowser", 1000, 1000) # pi's UID, GID
    try:
        flock(mutex, LOCK_EX | LOCK_NB)
    except IOError:
        logging.error("MSBrowser is already running.")
        sys.exit(0)

    try:
        messageFile = "/var/tmp/ps_data.json"
        updateStatusFile = "/var/tmp/ps_versions.json"
        configFile = "/usr/local/mindsensors/conf/msdev.cfg"
        config = getConfig()
        PROGRAM_DIRECTORY = getProgramDir()
        deviceName = socket.gethostname()
        rotation = getRotation()
        scrn = initScreen()
        if "GRX" in config.get('msdev', 'device'):
            psc = GRXCom
        else:
            psc = PiStormsCom()
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

            if len(FILES) <= FILES_PER_PAGE:
                pass # don't draw a right arrow if there's only one page
            elif INDEX >= len(FILES) - FILES_PER_PAGE:
                drawReturnArrow()
            else:
                drawRightArrow()

            if INDEX >= FILES_PER_PAGE:
                drawLeftArrow()
            elif len(stack) > 1:
                drawUpArrow()
            else:
                drawRefreshArrow()

            exclamation = newMessageExists() or updateNeeded()
            if exclamation:
                drawExclamation()

            drawPageNumber(INDEX, len(FILES), FILES_PER_PAGE)

            drawBatteryIndicator()

            while True:
                if exclamation and exclamationPressed():
                    promptUpdate()
                    break
                if len(FILES) > FILES_PER_PAGE and rightArrowPressed():
                    newIndex = INDEX + FILES_PER_PAGE
                    if newIndex > len(FILES)-1:
                        newIndex = 0
                    stack[-1][2] = newIndex
                    break
                if leftArrowPressed():
                    if INDEX >= FILES_PER_PAGE: # left arrow
                        stack[-1][2] = INDEX-4 if INDEX >= 4 else 0
                    elif len(stack) > 1: # up arrow
                        stack.pop()
                    else: # refresh arrow
                        stack[-1][1] = listPrograms(PROGRAM_DIRECTORY)
                        scrn.clearScreen() # some visual feedback that the refresh happened
                    break
                item = itemButtonPressed(FOLDER, FILES, INDEX, FILES_PER_PAGE)
                if item:
                    if os.path.isdir(item): # folder
                        stack.append([item, listPrograms(item), 0])
                    else: # python program
                        print("Running program {}.py".format(item))
                        exitStatus = runProgram(item+".py")
                        if exitStatus != 0:
                            scrn.showMessage(["Error!", "The program stopped with exit status {}. " \
                                    "You might want to access the Logs tab in the PiStorms Web Interface " \
                                    "to check for a stacktrace.".format(exitStatus)], wrapText=True)
                    break
    except KeyboardInterrupt:
        logging.info("Quitting MSBrowser")
        scrn.refresh()
        scrn.termReplaceLastLine("PiStorms browser exited")
    finally:
        flock(mutex, LOCK_UN)
