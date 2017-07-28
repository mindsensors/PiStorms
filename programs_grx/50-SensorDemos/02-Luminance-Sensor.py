from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Luminance_Sensor

psm = PiStorms_GRX()
luminanceSensor = Grove_Luminance_Sensor("BAA1")

m = ["Grove Luminance Sensor Demo",
     "Please connect a Grove luminance sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    reading = luminanceSensor.luminance()
    message = "Luminance level: " + str(reading)
    psm.screen.termPrintAt(0, message)

psm.untilKeyPress(mainLoop)
