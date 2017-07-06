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

