import time
from PiStormsCom_GRX import GRXCom
from PiStorms_GRX import PiStorms_GRX, RCServo, GrovePort
psm = PiStorms_GRX()

# introduce program and intent
# give option to quit
bank = psm.screen.askQuestion(["Motor Bank", "Which bank is your servo connected to?"], [" <-- B", " "*13+"A -->"], wrapText=True)
bank = ["B", "A"][bank]
port = psm.screen.askQuestion(["Motor Port", "Which port number is your servo connected to?"], [1, 2, 3], wrapText=True)
port = ["1", "2", "3"][port]
servo = "B{}M{}".format(bank, port)
#print(servo)
servo = RCServo(servo)
#time.sleep(0.5)
#servo.stop()

if psm.screen.askYesOrNoQuestion(["Encoder", "Do you have an encoder attached to this servo?"], wrapText=True):
    port = psm.screen.askQuestion(["Encoder Port", "Which port is your encoder connected to?"],
            ["B{}D1".format(bank), "B{}D2".format(bank)], wrapText=True)
    port = ["1", "2"][port]
    encoder = "B{}D{}".format(bank, port)
    encoder = GrovePort(encoder, type=GRXCom.TYPE.ENCODER, mode=int(port))
    # maybe add option to cancel here
    # no comma at the end of this line so the string merges with the following line (no backslash necessary)
    psm.screen.showMessage(["Ready to begin", "This program will now find the neutral point of this servo automatically."
                            " Please make sure the servo can spin freely before proceeding."], wrapText=True)
    pulse = 1500
    initialKeyPressCount = psm.getKeyPressCount()
    while psm.getKeyPressCount() == initialKeyPressCount:
        servo.setPulse(pulse)
        encoderStart = encoder.readValue()
        time.sleep(1)
        encoderEnd = encoder.readValue()
        encoderDifference = encoderEnd - encoderStart
        psm.screen.termReplaceLastLine(encoderDifference)
        if abs(encoderDifference) < 2:
            break
        else:
            pulse += encoderDifference*2
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
    #TODO: account for possibility of a wider range of values which cause servo to still
    #TODO: save value

servo.stop()
