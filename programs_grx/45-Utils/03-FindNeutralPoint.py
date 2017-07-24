import time, sys
import ConfigParser
from PiStormsCom_GRX import GRXCom
from PiStorms_GRX import PiStorms_GRX, RCServo, GrovePort

psm = PiStorms_GRX()
config = ConfigParser.RawConfigParser()
config.read("/usr/local/mindsensors/conf/msdev.cfg")

# introduce program and intent
# give option to quit
bank = psm.screen.askQuestion(["Motor Bank", "Which bank is your servo connected to?"], [" <-- B", " "*13+"A -->"], wrapText=True)
bank = ["B", "A"][bank]
port = psm.screen.askQuestion(["Motor Port", "Which port number is your servo connected to?"],
                              [1,2,3] if bank!="A" else [3,2,1], wrapText=True)
port = (["1","2","3"] if bank!="A" else ["3","2","1"])[port]
port = "B{}M{}".format(bank, port)
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
