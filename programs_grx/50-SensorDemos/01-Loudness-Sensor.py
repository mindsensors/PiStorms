from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Loudness_Sensor

psm = PiStorms_GRX()
loudnessSensor = Grove_Loudness_Sensor("BAA1")

m = ["Grove Loudness Sensor Demo",
     "Please connect a Grove loudness sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    reading = loudnessSensor.detectSound()
    message = "Loudness level: " + str(reading)
    psm.screen.termPrintAt(0, message)

psm.untilKeyPress(mainLoop)
