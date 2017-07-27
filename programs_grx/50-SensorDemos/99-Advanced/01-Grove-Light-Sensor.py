from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Light_Sensor

psm = PiStorms_GRX()
lightSensor = Grove_Light_Sensor("BAA1")

m = ["Grove Light Sensor Demo",
     "Please connect a Grove light sensor to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

# title
psm.screen.drawDisplay("Grove Light Sensor Demo")

def mainLoop():
    reading = lightSensor.lightLevel()
    message = "Light level: {}".format(reading)
    # not familiar with "".format()? See https://pyformat.info/
    psm.screen.termPrintAt(0, message)
    
    margin = 20
    barWidth = psm.screen.screenWidth() - 2*margin
    psm.screen.fillRect(x=margin, y=72, width=barWidth, height=20, fill=(0,0,0), outline=(255,255,255), display=False)
    # shrink reading from the range 0-4096 to 0-280
    barLength = reading * barWidth / 2**12
    psm.screen.fillRect(x=margin, y=72, width=barLength, height=20, fill=(255,255,255))

    intensity = int(reading / 4096.0 * 255)
    grey = (intensity, intensity, intensity)
    psm.screen.fillRect(x=margin, y=120, width=barWidth, height=100, fill=grey)

psm.untilKeyPress(mainLoop)
