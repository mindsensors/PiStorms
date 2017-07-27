from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Air_Quality_Sensor

psm = PiStorms_GRX()
airQualitySensor = Grove_Air_Quality_Sensor("BAA1")

m = ["Grove Air Quality Sensor Demo",
     "Please connect a Grove air quality sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    reading = airQualitySensor.airQuality()
    message = "Air quality: " + str(reading)
    psm.screen.termPrintAt(0, message)

    description = airQualitySensor.qualitativeMeasurement()
    message = "Description: " + description
    psm.screen.termPrintAt(1, message)

psm.untilKeyPress(mainLoop)
