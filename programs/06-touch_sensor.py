import os,sys,inspect,time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from PiStorms import PiStorms

psm = PiStorms()

psm.screen.termPrintln("EV3 touch sensor readout (BBS1):")
psm.screen.termPrintln(" ")

psm.BBS1.resetTouchesEV3()
exit = False

while(not exit):
    touch = psm.BBS1.isTouchedEV3()
    numTouch = psm.BBS1.numTouchesEV3()
	psm.screen.termReplaceLastLine(str(touch) + "  " + str(numTouch))
	if(psm.screen.checkButton(0,0,320,320)):
		psm.screen.termPrintln("")
		psm.screen.termPrintln("Exiting to menu")
		exit = True
