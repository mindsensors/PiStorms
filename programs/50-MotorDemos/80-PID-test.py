#!/usr/bin/env python3
#
# Copyright (c) 2016 mindsensors.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code,
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# 04/15/16   Deepak     Initial development.
#

from PiStorms import PiStorms
import time
psm = PiStorms()

#m = ["Motor-Demo", "Connect motor to Bank A M1.",
# "Motor will turn 360 degrees, and stop",
# "with brake.",
#  "Click OK to continue"]
#psm.screen.askQuestion(m,["OK"])

# run motor for 360 degrees, and at the completion,
# brake while stopping
go_for = 360
encoder_pos = psm.BAM1.pos()
#default values: [7000, 0, 37500, 15000, 300, 7500, 5, 80]
aa = psm.BAM1.ReadPerformanceParameters()
print ("params: {0}".format(str(aa)))
aa[7] = 5
psm.BAM1.SetPerformanceParameters(aa[0], aa[1], aa[2], aa[3], aa[4], aa[5], aa[6], aa[7])
msg = "Motor encoder before:  " + str(encoder_pos)
psm.screen.drawAutoText(msg, 15, 150, fill=(255, 255, 255), size = 18)
psm.BAM1.runDegs(go_for, 75, True, False)
time.sleep(2.5)

encoder_pos = psm.BAM1.pos()
msg = "Motor encoder after:  " + str(encoder_pos)
psm.screen.drawAutoText(msg, 15, 175, fill=(255, 255, 255), size = 18)
msg = "difference: " + str(go_for - encoder_pos)
psm.screen.drawAutoText(msg, 15, 200, fill=(255, 255, 255), size = 18)

#m = ["Motor-Demo", "Motor should have turned 360 degrees",
#  "and stop with brake and hold.", "click EXIT to exit program"]
#psm.screen.askQuestion(m,["EXIT"])

doExit = False
while (doExit == False):
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        doExit = True
