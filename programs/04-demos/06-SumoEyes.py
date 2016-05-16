import os,sys,inspect,time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms

psm = PiStorms()

psm.screen.termPrintln("EV3 SumoEyes readout (BAS1):")
psm.screen.termPrintln(" ")
#print psm.BAS1.SE_None
exit = False
while(not exit):
    psm.screen.termPrintAt(4," SumoEyes " +str(psm.BAS1.SumoEyes(True)))
    '''
    if psm.BAS1.SumoEyes(True) == psm.BAS1.SumoEyes.SE_None :
        psm.screen.termPrintAt(4," SumoEyes None infront")
    if psm.BAS1.SumoEyes(True) == psm.BAS1.SE_Front :
        psm.screen.termPrintAt(4," SumoEyes something infront")
    if psm.BAS1.SumoEyes(True) == psm.BAS1.SE_Left :
        psm.screen.termPrintAt(4," SumoEyes something on Left")
    if psm.BAS1.SumoEyes(True) == psm.BAS1.SE_Right :
        psm.screen.termPrintAt(4," SumoEyes something on Right")
    '''
    if(psm.screen.checkButton(0,0,320,320)):
		psm.screen.termPrintln("")
		psm.screen.termPrintln("Exiting to menu")
		exit = True
        
