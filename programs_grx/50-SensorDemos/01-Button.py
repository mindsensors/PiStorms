from PiStorms_GRX import PiStorms_GRX
from GroveDevices import Grove_Button

psm = PiStorms_GRX()
button = Grove_Button("BAA1")

m = ["Grove Button Demo",
     "Please connect a Grove button to port BAA1 (Bank A, Analog 1) and press OK (or GO) to continue."]
psm.screen.showMessage(m, wrapText=True)

def mainLoop():
    if button.isPressed():
        psm.screen.termPrintAt(0, "The button is pressed.")
    else:
        psm.screen.termPrintAt(0, "The button is not pressed.")

psm.untilKeyPress(mainLoop)
