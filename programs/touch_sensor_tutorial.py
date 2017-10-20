#
# This program is provided as reference for tutorial:
# http://www.mindsensors.com/blog/how-to/pistorms-python-programming-tutorial
#
# It is recommended that you write your own program based on tutorial.
#

# Imports (that would be used later)
import os,sys,inspect,time

#
# PiStorms library import.
#
from PiStorms import PiStorms

#
# Create a PiStorms variable
#
psm = PiStorms()

#
# Write on PiStorms screen
#
psm.screen.termPrintln("EV3 touch sensor readout (BBS1):")
psm.screen.termPrintln(" ")

#
# Touch counts are kept in memory (cumulative)
# You can also reseet them with following API.
#
psm.BBS1.resetTouchesEV3()

#
# variable to break out of loop and exit.
#
doExit = False

while(not doExit):
    touch = psm.BBS1.isTouchedEV3()
    numTouch = psm.BBS1.numTouchesEV3()
    psm.screen.termReplaceLastLine(str(touch) + "  " + str(numTouch))

    if(psm.screen.isTouched()):
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        doExit = True
