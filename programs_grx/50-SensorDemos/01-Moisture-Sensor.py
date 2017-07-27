from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Moisture_Sensor

psm = PiStorms_GRX()
moistureSensor = Grove_Moisture_Sensor("BAA1")

m = ["Grove Moisture Sensor Demo",
     "Please connect a Grove moisture sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    reading = moistureSensor.lightLevel()
    message = "Detected moisture: " + str(reading)
    psm.screen.termPrintAt(0, message)

psm.untilKeyPress(mainLoop)
