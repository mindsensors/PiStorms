import time

from PiStorms_GRX import PiStorms_GRX, RCServo, RCServoEncoder
psm = PiStorms_GRX()

# introduce program and intent
# give option to quit
bank = psm.screen.askQuestion(["Motor Bank", "Which bank is your servo connected to?"], ["<-- B", "A -->"], wrapText=True)
bank = ["B", "A"][bank]
port = psm.screen.askQuestion(["Motor Port", "Which port number is your servo connected to?"], [1, 2, 3], wrapText=True)
port = ["1", "2", "3"][port]
servo = "B{}M{}".format(bank, port)
print(servo)

if psm.screen.askYesOrNoQuestion(["Encoder", "Do you have an encoder attached to this servo?"], wrapText=True):
    port = psm.screen.askQuestion(["Encoder Port", "Which port is your encoder connected to?"],
            ["B1D{}".format(bank), "B{}D2".format(bank)], wrapText=True)
    port = ["1", "2"][port]
    encoder = "B{}D{}".format(bank, port)
    servo = RCServoEncoder(port=servo, encoder=encoder)
    # maybe add option to cancel here
    psm.screen.showMessage(["Ready to begin", "This program will now find the neutral point of this servo automatically."
                            " Please make sure the servo can spin freely before proceeding."], wrapText=True)
    servo.setPulse()
    servo.readEncoder()
else:
    servo = RCServo(servo)
    psm.screen.termPrintln("Please adjust this number")
    psm.screen.termPrintln("until the servo stops spinning.")
    psm.screen.termPrintln("(press GO to save and quit)")
    #            x  width val
    buttons = [[ 20, 55, -100],
               [100, 45, -10],
               [170, 47, +10],
               [240, 55, +100]]
    for b in buttons:
        psm.screen.drawButton(b[0], 140, b[1], 40, text=str(b[2]), display=False)
    pulse = 1500
    initialKeyPressCount = psm.getKeyPressCount()
    while psm.getKeyPressCount() == initialKeyPressCount:
        for b in buttons:
            if psm.screen.checkButton(b[0], 140, b[1], 40):
                pulse += b[2]
        psm.screen.fillRect(0, 5, 320, 32, fill=(0,0,0), display=False)
        psm.screen.drawDisplay(pulse)
        servo.setPulse(pulse)
        time.sleep(0.3)
    #TODO: save value

