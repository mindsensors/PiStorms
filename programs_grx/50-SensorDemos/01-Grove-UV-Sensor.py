from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_UV_Sensor

psm = PiStorms_GRX()
uvSensor = Grove_UV_Sensor("BAA1")

m = ["Grove UV Sensor Demo",
     "Please connect a Grove UV sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    # note this takes an average of 1024 readings, it takes a moment
    reading = uvSensor.intensity()
    message = "UV intensity: " + str(reading)
    psm.screen.termPrintAt(0, message)

    # note this is an approximation
    index = uvSensor.UVindex()
    message = "UV index: " + str(index)
    psm.screen.termPrintAt(1, message)

psm.untilKeyPress(mainLoop)
