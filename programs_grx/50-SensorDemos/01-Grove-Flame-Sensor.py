from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Flame_Sensor

psm = PiStorms_GRX()
flameSensor = Grove_Flame_Sensor("BAA1")

m = ["Grove Flame Sensor Demo",
     "Please connect a Grove flame sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    if flameSensor.fireDetected():
        psm.screen.termPrintAt(0, "Fire detected")
    else:
        psm.screen.termPrintAt(0, "No fire detected")

psm.untilKeyPress(mainLoop)
