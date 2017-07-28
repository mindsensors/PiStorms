from PiStorms_GRX import PiStorms_GRX
from PiStorms_GRX import RCServo

psm = PiStorms_GRX()
servo = RCServo("BAS1")

m = ["Grove Continous Rotation Servo Demo",
     "Please connect a continuous rotation RC servo to port BAS1 (Bank A, Servo 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

m[1] = "If your servo is spinning right now, please run 45-Utils/03-FindNeutralPoint."
psm.screen.showMessage(m, wrapText=True)

servo.setSpeed(100)
m[1] = "Speed: 100"
psm.screen.showMessage(m, wrapText=True)

servo.setSpeed(-100)
m[1] = "Speed: -100"
psm.screen.showMessage(m, wrapText=True)

servo.stop()
m[1] = "Stopped"
psm.screen.showMessage(m, wrapText=True)
