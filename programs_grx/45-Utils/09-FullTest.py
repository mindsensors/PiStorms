import os, sys, time
import colorsys

import PiStorms_GRX
from PiStormsCom_GRX import GRXCom

DIGITAL = ["BBD1", "BBD2", "BAD2", "BAD1"]
ANALOG  = ["BBA1", "BBA2", "BBA3", "BAA3", "BAA2", "BAA1"]
ALL     = ["BBA1", "BBA2", "BBA3", "BBD1", "BBD2", "BAD2", "BAD1", "BAA3", "BAA2", "BAA1"]
SERVOS  = ["BBS1", "BBS2", "BBS3", "BAS3", "BAS2", "BAS1"]

psm = PiStorms_GRX.PiStorms_GRX()

def testGObutton():
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
    psm.screen.forceMessage(["Test resetKeyPressCount", "Press GO to verify the GO button", "count can be reset."])
    while psm.isKeyPressed(): time.sleep(0.01) # wait for release of previous GO button press
    psm.resetKeyPressCount()
    while psm.getKeyPressCount() == 0: time.sleep(0.01)

def testLEDs():
    psm.screen.forceMessage(["LED test",
                             "The LEDs should start cycling,",
                             "press GO to continue."])
    hueToRGB = lambda hue: [int(val*255) for val in colorsys.hsv_to_rgb(hue/360.0, 1, 1)]
    hue = 0
    while not psm.isKeyPressed():
        psm.led(1, *hueToRGB(hue))
        psm.led(2, *hueToRGB(hue+120))
        hue += 10
        time.sleep(0.05)
    psm.led(1, 0,0,0)
    psm.led(2, 0,0,0)
    while psm.isKeyPressed(): time.sleep(0.01) # wait for release

def testTouchscreen():
    psm.screen.showMessage(["Touchscreen Test", "Use the paint program to check for touchscreen accuracy in all 4 corners. Also check the software function keys. When you are done press GO to continue."], wrapText=True)
    os.system("sudo python /home/pi/PiStorms/programs_grx/60-Games/04-Paint.py")

def testServos():
    for port in SERVOS:
        servo = PiStorms_GRX.RCServo(port)
        time.sleep(0.03)
        servo.setSpeed(50)
        psm.screen.showMessage("Servo {} should be spinning.".format(port), goBtn=True)
        servo.stop()
        time.sleep(0.03)

def testDigitalInput():
    psm.screen.showMessage(["Digital Input", "Connect the Grove Button sensor to each port and verify its reading. Press GO to proceed."], wrapText=True, goBtn=True)
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.DIGITAL_INPUT) for port in ALL]
    while not psm.isKeyPressed():
        psm.screen.clearScreen(display=False)
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
    while psm.isKeyPressed(): time.sleep(0.01) # wait for release
    psm.screen.clearScreen(display=False)

def testAnalogInput():
    psm.screen.showMessage(["Analog Input", "Connect the Grove Light sensor to each port and verify its reading. Press GO to proceed."], wrapText=True, goBtn=True)
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.ANALOG_INPUT) for port in ANALOG]
    while not psm.isKeyPressed():
        psm.screen.clearScreen(display=False)
        psm.screen.drawAutoText(ports[0].readValue(), 20, 150, display=False)
        psm.screen.drawAutoText(ports[1].readValue(), 20, 120, display=False)
        psm.screen.drawAutoText(ports[2].readValue(), 20,  90, display=False)

        psm.screen.drawAutoText(ports[3].readValue(), 260,  90, display=False)
        psm.screen.drawAutoText(ports[4].readValue(), 260, 120, display=False)
        psm.screen.drawAutoText(ports[5].readValue(), 260, 150)
    while psm.isKeyPressed(): time.sleep(0.01) # wait for release
    psm.screen.clearScreen(display=False)

def testDigitalOutput():
    psm.screen.forceMessage(["Digital Output",
                             "Connect the Grove LED socket",
                             "to each port and verify it flashes.",
                             "Press GO to proceed."])
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.DIGITAL_OUTPUT) for port in ALL]
    initialKeyPressCount = psm.getKeyPressCount()
    while psm.getKeyPressCount() == initialKeyPressCount:
        for port in ports:
            port.writeValue(0)
            time.sleep(0.01)
        time.sleep(0.3)
        for port in ports:
            port.writeValue(1)
            time.sleep(0.01)
        time.sleep(0.3)

def testI2C():
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.I2C) for port in ALL]
    # read device name of AbsoluteIMU with Grove<->NXT cable

def testTachometer():
    psm.screen.showMessage(["Tachometer / Encoder", "Connect an encoder to each of the 4 digital ports along the top and verify its readings by manually rotate the wheel. Each rotation should measure 72 units. Press GO to proceed."], wrapText=True, goBtn=True)
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.ENCODER) for port in DIGITAL]
    while not psm.isKeyPressed():
        psm.screen.clearScreen(display=False)
        psm.screen.drawAutoText("BBD1: %s"%ports[0].readValue(),  20, 20, display=False)
        psm.screen.drawAutoText("BBD2: %s"%ports[1].readValue(),  20, 50, display=False)
        psm.screen.drawAutoText("BAD2: %s"%ports[2].readValue(), 210, 20, display=False)
        psm.screen.drawAutoText("BAD1: %s"%ports[3].readValue(), 210, 50)
    while psm.isKeyPressed(): time.sleep(0.01) # wait for release
    psm.screen.clearScreen(display=False)

testGObutton()
testLEDs()
testTouchscreen()
testServos()
testDigitalInput()
testDigitalOutput()
testAnalogInput()
testI2C()
testTachometer()

