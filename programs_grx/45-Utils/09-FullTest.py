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

import os, sys, time

import PiStorms_GRX
from PiStormsCom_GRX import GRXCom

DIGITAL = ["BBD1", "BBD2", "BAD2", "BAD1"]
ANALOG  = ["BBA1", "BBA2", "BBA3", "BAA3", "BAA2", "BAA1"]
ALL     = ["BBA1", "BBA2", "BBA3", "BBD1", "BBD2", "BAD2", "BAD1", "BAA3", "BAA2", "BAA1"]
SERVOS  = ["BBS1", "BBS2", "BBS3", "BAS3", "BAS2", "BAS1"]

psm = PiStorms_GRX.PiStorms_GRX()

def testGObutton(helpText):
    if psm.isKeyPressed():
        psm.screen.forceMessage(["Quitting Test",
                                 "GO button was detected to be pressed",
                                 "when starting the test.",
                                 "Please do not press the GO button",
                                 "when starting the test."])
        time.sleep(5)
        sys.exit(0)
    psm.screen.forceMessage(["Test GO Button", "Verify the GO button is working", "by pressing it continue."])
    while not psm.isKeyPressed(): time.sleep(0.01)
    while psm.isKeyPressed(): time.sleep(0.01) # wait for release
    psm.screen.forceMessage(["Test resetKeyPressCount", "Press GO to verify the GO button", "count can be reset."])
    psm.resetKeyPressCount()
    while psm.getKeyPressCount() == 0: time.sleep(0.01)

def testLEDs(helpText):
    psm.screen.forceMessage(["LED test",
                             "The LEDs should start cycling,",
                             "press GO to continue."])
    def run():
        for color in [(255,0,0), (0,255,0), (0,0,255)]:
            psm.led(1, *color)
            time.sleep(0.5)
            psm.led(2, *color)
            time.sleep(0.5)
    psm.untilKeyPress(run)
    psm.led(1, 0,0,0)
    time.sleep(0.01)
    psm.led(2, 0,0,0)

def testTouchscreen(helpText):
    if helpText: psm.screen.showMessage(["Touchscreen Test", "Use the paint program to check for touchscreen accuracy in all 4 corners. Also check the software function keys. When you are done press GO to continue."], wrapText=True)
    psm.screen.forceMessage(["Loading...",
                             "Starting the 04-Paint.py"])
    os.system("sudo python /home/pi/PiStorms/programs_grx/60-Games/04-Paint.py")

def testServos(helpText):
    psm.screen.dumpTerminal()
    psm.screen.termPrintln("Setting servos in sequence")
    psm.screen.setMode(psm.screen.PS_MODE_TERMINAL)
    servos = [PiStorms_GRX.RCServo(port) for port in SERVOS]
    def run():
        for servo in servos:
            servo.setPos(0)
            time.sleep(0.5)
        for servo in servos:
            servo.setPos(180)
            time.sleep(0.5)
    psm.untilKeyPress(run)

def testDigitalInput(helpText):
    if helpText: psm.screen.showMessage(["Digital Input", "Connect the Grove Button sensor to each port and verify its reading. Press GO to proceed."], wrapText=True, goBtn=True)
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.DIGITAL_INPUT) for port in ALL]
    def run():
        psm.screen.clearScreen(display=False)
        psm.screen.drawAutoText("Digital input", x=999, y=50, align="center", display=False)

        psm.screen.drawAutoText(ports[0].readValue(), 20, 150, display=False)
        psm.screen.drawAutoText(ports[1].readValue(), 20, 120, display=False)
        psm.screen.drawAutoText(ports[2].readValue(), 20,  90, display=False)

        psm.screen.drawAutoText(ports[3].readValue(), 20, 20, display=False)
        psm.screen.drawAutoText(ports[4].readValue(), 50, 20, display=False)

        psm.screen.drawAutoText(ports[5].readValue(), 270, 20, display=False)
        psm.screen.drawAutoText(ports[6].readValue(), 300, 20, display=False)

        psm.screen.drawAutoText(ports[7].readValue(), 290,  90, display=False)
        psm.screen.drawAutoText(ports[8].readValue(), 290, 120, display=False)
        psm.screen.drawAutoText(ports[9].readValue(), 290, 150)
    psm.untilKeyPress(run)
    psm.screen.clearScreen(display=False)

def testAnalogInput(helpText):
    if helpText: psm.screen.showMessage(["Analog Input", "Connect the Grove Light sensor to each port and verify its reading. Press GO to proceed."], wrapText=True, goBtn=True)
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.ANALOG_INPUT) for port in ANALOG]
    def run():
        psm.screen.clearScreen(display=False)
        psm.screen.drawAutoText("Analog input", x=999, y=50, align="center", display=False)

        psm.screen.drawAutoText(ports[0].readValue(), 20, 150, display=False)
        psm.screen.drawAutoText(ports[1].readValue(), 20, 120, display=False)
        psm.screen.drawAutoText(ports[2].readValue(), 20,  90, display=False)

        psm.screen.drawAutoText(ports[3].readValue(), 260,  90, display=False)
        psm.screen.drawAutoText(ports[4].readValue(), 260, 120, display=False)
        psm.screen.drawAutoText(ports[5].readValue(), 260, 150)
    psm.untilKeyPress(run)
    psm.screen.clearScreen(display=False)

def testDigitalOutput(helpText):
    psm.screen.forceMessage(["Digital Output",
                             "Connect the Grove LED socket",
                             "to each port and verify it flashes.",
                             "Press GO to proceed."])
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.DIGITAL_OUTPUT) for port in ALL]
    def run():
        for port in ports:
            port.writeValue(0)
            time.sleep(0.01)
        time.sleep(0.2)
        for port in ports:
            port.writeValue(1)
            time.sleep(0.01)
        time.sleep(0.2)
    psm.untilKeyPress(run)

def testTachometer(helpText):
    if helpText: psm.screen.showMessage(["Tachometer / Encoder", "Connect an encoder to each of the 4 digital ports along the top and verify its readings by manually rotate the wheel. Each rotation should measure 72 units. Press GO to proceed."], wrapText=True, goBtn=True)
    GRXCom.I2C.A.writeByte(GRXCom.DIGITAL[0] + GRXCom.OFFSET.TYPE, 0)
    GRXCom.I2C.A.writeByte(GRXCom.DIGITAL[1] + GRXCom.OFFSET.TYPE, 0)
    GRXCom.I2C.B.writeByte(GRXCom.DIGITAL[0] + GRXCom.OFFSET.TYPE, 0)
    #GRXCom.I2C.B.writeByte(GRXCom.DIGITAL[1] + GRXCom.OFFSET.TYPE, 0)
    time.sleep(0.1)
    GRXCom.I2C.A.writeByte(GRXCom.DIGITAL[0] + GRXCom.OFFSET.TYPE, GRXCom.TYPE.ENCODER)
    GRXCom.I2C.A.writeByte(GRXCom.DIGITAL[1] + GRXCom.OFFSET.TYPE, GRXCom.TYPE.ENCODER)
    GRXCom.I2C.B.writeByte(GRXCom.DIGITAL[0] + GRXCom.OFFSET.TYPE, GRXCom.TYPE.ENCODER)
    #GRXCom.I2C.B.writeByte(GRXCom.DIGITAL[1] + GRXCom.OFFSET.TYPE, GRXCom.TYPE.ENCODER)
    def run():
        BAD1 = GRXCom.I2C.A.readLongSigned(GRXCom.DIGITAL[0] + GRXCom.OFFSET.ENCODER_VALUE)
        BAD2 = GRXCom.I2C.A.readLongSigned(GRXCom.DIGITAL[1] + GRXCom.OFFSET.ENCODER_VALUE)
        #BBD2 = GRXCom.I2C.B.readLongSigned(GRXCom.DIGITAL[1] + GRXCom.OFFSET.ENCODER_VALUE)
        BBD1 = GRXCom.I2C.B.readLongSigned(GRXCom.DIGITAL[0] + GRXCom.OFFSET.ENCODER_VALUE)
        psm.screen.clearScreen(display=False)
        psm.screen.drawAutoText("Tachometer test", x=999, y=100, align="center", display=False)
        psm.screen.drawAutoText("BBD1: %s"%BBD1,  20, 20, display=False)
        #psm.screen.drawAutoText("BBD2: %s"%BBD2,  20, 50, display=False)
        psm.screen.drawAutoText("BBD2: Disabled", 20, 50, display=False)
        psm.screen.drawAutoText("BAD2: %s"%BAD2, 210, 20, display=False)
        psm.screen.drawAutoText("BAD1: %s"%BAD1, 210, 50)
    psm.untilKeyPress(run)
    time.sleep(0.1)
    GRXCom.I2C.A.writeByte(GRXCom.DIGITAL[0] + GRXCom.OFFSET.TYPE, 0)
    GRXCom.I2C.A.writeByte(GRXCom.DIGITAL[1] + GRXCom.OFFSET.TYPE, 0)
    GRXCom.I2C.B.writeByte(GRXCom.DIGITAL[0] + GRXCom.OFFSET.TYPE, 0)
    #GRXCom.I2C.B.writeByte(GRXCom.DIGITAL[1] + GRXCom.OFFSET.TYPE, 0)
    psm.screen.clearScreen(display=False)

if __name__ == "__main__":
    psm.screen.setMode(psm.screen.PS_MODE_DEAD)
    def drawOption(text):
        psm.screen.termPrint(" "*5)
        psm.screen.termPrintln(text)
    for option in ["GO button", "LEDs", "Touchscreen", "Servos", "Digital input", "Digital output", "Analog input", "Tachometer"]:
        drawOption(option)
    psm.screen.setMode(psm.screen.PS_MODE_TERMINAL)
    psm.screen.drawDisplay("Tests")
    for y in range(42, 202, 20):
        psm.screen.drawButton(0, y, 30, 20, text="O", display=False)
    psm.screen.drawButton(0, 205, 320, 35, text="Run", align="center", display=False)
    psm.screen.drawAutoText("Help: No", 200, 42, display=False)
    psm.screen.drawButton(200, 68, 83, 30, text="Toggle", display=False)
    psm.screen.drawButton(200, 120, 100, 30, text="Deselect all", display=False)
    psm.screen.disp.display()
    # state variables
    subtests = [True]*8
    selectText = True # True for "Deselect", False for "Select"
    helpText = False
    # poll buttons
    while not psm.screen.checkButton(0, 205, 320, 35):
        for i in range(len(subtests)):
            y = 42+20*i
            if psm.screen.checkButton(0, y, 30, 20):
                subtests[i] = not subtests[i]
                if subtests[i]:
                    psm.screen.drawButton(0, y, 30, 20, text="O")
                else:
                    psm.screen.drawButton(0, y, 30, 20, text=" ")
        if psm.screen.checkButton(200, 120, 100, 30):
            for i in range(len(subtests)):
                if subtests[i] == selectText:
                    subtests[i] = not selectText
                    psm.screen.drawButton(0, 42+20*i, 30, 20, text=" " if selectText else "O", display=False)
            selectText = not selectText
            psm.screen.drawButton(200, 120, 100, 30, text="Deselect all" if selectText else "Select all", display=False)
            psm.screen.disp.display()
        if psm.screen.checkButton(200, 68, 83, 30):
            psm.screen.fillRect(200, 42, 83, 21, fill=(0,0,0), display=False)
            psm.screen.drawAutoText("Help: No" if helpText else "Help: Yes", 200, 42)
            helpText = not helpText
    psm.screen.clearScreen()
    for i, test in enumerate([testGObutton, testLEDs, testTouchscreen, testServos, testDigitalInput, testDigitalOutput, testAnalogInput, testTachometer]):
        if subtests[i]: test(helpText)
