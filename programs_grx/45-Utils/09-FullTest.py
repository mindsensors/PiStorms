import os, sys, time

import PiStorms_GRX
from PiStormsCom_GRX import GRXCom

DIGITAL = ["BBD1", "BBD2", "BAD1", "BAD2"]
ANALOG  = ["BBA1", "BBA2", "BBA3", "BAA3", "BAA2", "BAA1"]
ALL     = ["BBA1", "BBA2", "BBA3", "BBD1", "BBD2", "BAD1", "BAD2", "BAA3", "BAA2", "BAA1"]
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

def testLEDs():
    psm.screen.forceMessage(["LED test",
                             "The LEDs should start cycling,",
                             "press GO to continue.",
                             "",
                             "(this also tests resetKeyPressCount)"])
    stage = 0
    timeout = time.time()
    psm.resetKeyPressCount()
    while psm.getKeyPressCount() == 0:
        if time.time() > timeout:
            stage = stage+1 if stage<=7 else 0
            if stage==0:
                psm.led(1,   0,   0,   0)
                psm.led(2,   0,   0,   0)
            elif stage==1:
                psm.led(1, 255,   0,   0)
                psm.led(2, 255,   0,   0)
            elif stage==2:
                psm.led(1,   0, 255,   0)
                psm.led(2,   0, 255,   0)
            elif stage==3:
                psm.led(1,   0,   0, 225)
                psm.led(2,   0,   0, 225)
            elif stage==4:
                psm.led(1, 255, 255,   0)
                psm.led(2, 255, 255,   0)
            elif stage==5:
                psm.led(1,   0, 255, 255)
                psm.led(2,   0, 255, 255)
            elif stage==6:
                psm.led(1, 255,   0, 255)
                psm.led(2, 255,   0, 255)
            elif stage==7:
                psm.led(1, 255, 255, 255)
                psm.led(2, 255, 255, 255)
        time.sleep(0.05)

def testTouchscreen():
    psm.screen.showMessage(["Touchscreen Test", "Use the paint program to check for touchscreen accuracy in all 4 corners. Also check the software function keys. When you are done press GO to continue."], wrapText=True)
    os.system("sudo python /home/pi/PiStorms/programs_grx/60-Games/04-Paint.py")

def testServos():
    for port in SERVOS:
        servo = PiStorms_GRX.RCServo(port)
        servo.setSpeed(50)
        psm.screen.showMessage("Servo {} should be spinning.".format(port), goBtn=True)
        servo.stop()

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

        psm.screen.drawAutoText(ports[7].readValue(), 290, 150, display=False)
        psm.screen.drawAutoText(ports[8].readValue(), 290, 120, display=False)
        psm.screen.drawAutoText(ports[9].readValue(), 290,  90)

def testAnalogInput():
    psm.screen.showMessage(["Analog Input", "Connect the Grove Light sensor to each port and verify its reading. Press GO to proceed."], wrapText=True, goBtn=True)
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.ANALOG_INPUT) for port in ANALOG]
    while not psm.isKeyPressed():
        psm.screen.clearScreen(display=False)
        psm.screen.drawAutoText(ports[0].readValue(), 20, 150, display=False)
        psm.screen.drawAutoText(ports[1].readValue(), 20, 120, display=False)
        psm.screen.drawAutoText(ports[2].readValue(), 20,  90, display=False)

        psm.screen.drawAutoText(ports[3].readValue(), 260, 150, display=False)
        psm.screen.drawAutoText(ports[4].readValue(), 260, 120, display=False)
        psm.screen.drawAutoText(ports[5].readValue(), 260,  90)

def testDigitalOutput():
    psm.screen.forceMessage(["Digital Output",
                             "Connect the Grove LED socket",
                             "to each port and verify it flashes.",
                             "Hold GO to proceed."])
    ports = [PiStorms_GRX.GrovePort(port, GRXCom.TYPE.DIGITAL_OUTPUT) for port in ALL]
    while not psm.isKeyPressed():
        for port in ports: port.writeValue(0)
        time.sleep(0.5)
        for port in ports: port.writeValue(1)
        time.sleep(0.5)

def testI2C():
    pass # read device name of AbsoluteIMU with Grove<->NXT cable, check ALL ports

def testTachometer():
    pass # manually rotate wheel, check DIGITAL ports

testGObutton()
testLEDs()
testTouchscreen()
testServos()
testDigitalInput()
testDigitalOutput()
testAnalogInput()
testI2C()
testTachometer()

