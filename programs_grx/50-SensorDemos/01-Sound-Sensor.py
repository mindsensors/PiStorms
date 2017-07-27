from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Sound_Sensor

psm = PiStorms_GRX()
soundSensor = Grove_Sound_Sensor("BAA1")

m = ["Grove Sound Sensor Demo",
     "Please connect a Grove sound sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    reading = soundSensor.soundIntensity()
    message = "Sound intensity: " + str(reading)
    psm.screen.termPrintAt(0, message)

psm.untilKeyPress(mainLoop)
