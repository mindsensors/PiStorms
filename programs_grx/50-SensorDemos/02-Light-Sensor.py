from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Light_Sensor

psm = PiStorms_GRX()
lightSensor = Grove_Light_Sensor("BAA1")

m = ["Grove Light Sensor Demo",
     "Please connect a Grove light sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    reading = lightSensor.lightLevel()
    message = "Light level: " + str(reading)
    psm.screen.termPrintAt(0, message)

psm.untilKeyPress(mainLoop)
