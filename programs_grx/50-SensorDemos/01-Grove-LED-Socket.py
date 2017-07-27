from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_LED_Socket

psm = PiStorms_GRX()
led = Grove_LED_Socket("BAA1")

m = ["Grove LED Socket Demo",
     "Please connect a Grove LED socket to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    led.on()
    psm.screen.termPrintAt(0, "LED on")
    time.sleep(1)

    led.off()
    psm.screen.termPrintAt(0, "LED off")
    time.sleep(1)

psm.untilKeyPress(mainLoop)
