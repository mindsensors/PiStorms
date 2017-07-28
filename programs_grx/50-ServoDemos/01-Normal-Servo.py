from PiStorms_GRX import PiStorms_GRX
from PiStorms_GRX import RCServo

psm = PiStorms_GRX()
servo = RCServo("BAS1")

m = ["Grove Normal Servo Demo",
     "Please connect a normal RC servo to port BAS1 (Bank A, Servo 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

servo.setPos(0)
m[1] = "Position: 0"
psm.screen.showMessage(m, wrapText=True)

servo.setPos(180)
m[1] = "Position: 180"
psm.screen.showMessage(m, wrapText=True)

servo.setNeutral()
m[1] = "Neutral point"
psm.screen.showMessage(m, wrapText=True)
