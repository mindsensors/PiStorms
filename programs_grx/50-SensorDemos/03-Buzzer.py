import time
from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Buzzer

psm = PiStorms_GRX()
buzzer = Grove_Buzzer("BAA1")

m = ["Grove Buzzer Demo",
     "Please connect a Grove buzzer to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    buzzer.on()
    psm.screen.termPrintAt(0, "Buzzer on")
    time.sleep(0.2)

    buzzer.off()
    psm.screen.termPrintAt(0, "Buzzer off")
    time.sleep(0.8)

psm.untilKeyPress(mainLoop)
