from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Temperature_Sensor

psm = PiStorms_GRX()
temperatureSensor = Grove_Temperature_Sensor("BAA1")

m = ["Grove Temperature Sensor Demo",
     "Please connect a Grove temperature sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    reading = temperatureSensor.temperature()
    message = "Temperature (Celsius): " + str(reading)
    psm.screen.termPrintAt(0, message)

    convertedReading = Grove_Temperature_Sensor.CtoF(reading)
    message = "Temperature (Fahrenheit): " + str(convertedReading)
    psm.screen.termPrintAt(1, message)

psm.untilKeyPress(mainLoop)
