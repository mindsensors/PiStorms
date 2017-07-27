from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_PIR_Motion_Sensor

psm = PiStorms_GRX()
motionSensor = Grove_PIR_Motion_Sensor("BAA1")

m = ["Grove PIR Motion Sensor Demo",
     "Please connect a Grove PIR motion sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    if motionSensor.motionDetected():
        psm.screen.termPrintAt(0, "Motion detected")
    else:
        psm.screen.termPrintAt(0, "No motion detected")

psm.untilKeyPress(mainLoop)
