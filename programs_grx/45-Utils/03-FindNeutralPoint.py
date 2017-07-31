#!/usr/bin/env python
#
# Copyright (c) 2017 mindsensors.com
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

import time, sys
import ConfigParser
from PiStormsCom_GRX import GRXCom
from PiStorms_GRX import PiStorms_GRX, RCServo, GrovePort

psm = PiStorms_GRX()
config = ConfigParser.RawConfigParser()
config.read("/usr/local/mindsensors/conf/msdev.cfg")

# introduce program and intent
m = ["Find Neutral Point - Introduction",
     'Every servo is slightly different due to the manufacturing process. This could make a continuous rotation servo "drift" when you set the speed to "0".']
psm.screen.showMessage(m, wrapText=True)
m[1] = "This program can help you find what value *actually* makes your servo stop. This will be saved to a configuration file so you don't have to worry about it again. Would you like to continue?"
if not psm.screen.askYesOrNoQuestion(m, wrapText=True, goBtn=True):
    sys.exit(0)

bank = psm.screen.askQuestion(["Motor Bank", "Which bank is your servo connected to?"], [" <-- B", " "*13+"A -->"], wrapText=True)
bank = ["B", "A"][bank]
port = psm.screen.askQuestion(["Motor Port", "Which port number is your servo connected to?"],
                              [1,2,3] if bank!="A" else [3,2,1], wrapText=True)
port = (["1","2","3"] if bank!="A" else ["3","2","1"])[port]
port = "B{}S{}".format(bank, port)
servo = RCServo(port)
servo.stop()

def exit():
    servo.stop()
    psm.screen.forceMessage(["Exiting...", "Calibration cancelled"])
    time.sleep(1)
    sys.exit(0)

if psm.screen.askYesOrNoQuestion(["Encoder", "Do you have an encoder attached to this servo?"], wrapText=True):
    # zero-indexed encoder port number
    encPortNum0 = psm.screen.askQuestion(["Encoder Port", "Which port is your encoder connected to?"],
                                         ["B{}D1".format(bank), "B{}D2".format(bank)], wrapText=True)
    encPortNum = ["1", "2"][encPortNum0]
    encPort = "B{}D{}".format(bank, encPortNum)
    encoder = GrovePort(encPort, type=GRXCom.TYPE.ENCODER, mode=int(encPortNum0))
    # no comma at the end of this line so the string merges with the following line (no backslash necessary)
    answer = psm.screen.askQuestion(["Ready to begin", "This program will now find the neutral point of this servo automatically."
                                     " Please make sure the servo can spin freely before proceeding."],
                                     ["OK", "Cancel"], goBtn=True, wrapText=True)
    if answer != 0: exit()

    def showStatus(n):
        psm.screen.forceMessage(["Please wait", "Finding neutral point...", "Trying to get this number to 0: {}".format(n), "", "(press GO to cancel)"])
    def find(direction):
        pulse = 1500
        initialKeyPressCount = psm.getKeyPressCount()
        while True:
            servo.setPulse(pulse)
            encoderStart = encoder.readValue()
            time.sleep(1)
            encoderEnd = encoder.readValue()
            encoderDifference = encoderEnd - encoderStart
            if abs(encoderDifference) < 2:
                return pulse
            else:
                pulse += direction*encoderDifference*2
            showStatus(encoderDifference)
            if psm.getKeyPressCount() != initialKeyPressCount:
                exit()
    psm.screen.forceMessage(["Please wait", "Finding neutral point...", "", "", "(press GO to cancel)"])
    try:
        pulse = find(+1)
    except ValueError:
        pulse = find(-1)
else:
    psm.screen.termPrintln("Please adjust this number")
    psm.screen.termPrintln("until the servo stops spinning.")
    psm.screen.termPrintln("(press GO to save and quit)")
    psm.screen.drawButton( 20, 140, 55, 40, text="-100", display=False)
    psm.screen.drawButton(100, 140, 45, 40, text="-10",  display=False)
    psm.screen.drawButton(170, 140, 47, 40, text="+10",  display=False)
    psm.screen.drawButton(240, 140, 55, 40, text="+100", display=False)
    pulse = 1500
    initialKeyPressCount = psm.getKeyPressCount()
    while psm.getKeyPressCount() == initialKeyPressCount:
        if psm.screen.checkButton( 20, 140, 55, 40):
            pulse -= 100
        if psm.screen.checkButton(100, 140, 45, 40):
            pulse -= 10
        if psm.screen.checkButton(170, 140, 47, 40):
            pulse += 10
        if psm.screen.checkButton(240, 140, 55, 40):
            pulse += 100
        psm.screen.fillRect(0, 5, 320, 32, fill=(0,0,0), display=False)
        psm.screen.drawDisplay(pulse)
        servo.setPulse(pulse)
        time.sleep(0.3)

answer = psm.screen.askQuestion(["Done!", "Found neutral point: {}".format(pulse),
                                 "Hit OK or GO to save"], ["OK", "Cancel"])
if answer == 1: exit()

if not config.has_section('neutralpoint'):
    config.add_section('neutralpoint')
config.set('neutralpoint', port, pulse)
with open("/usr/local/mindsensors/conf/msdev.cfg", 'wb') as configfile:
    config.write(configfile)

#TODO: account for possibility of a wider range of values which cause servo to still
