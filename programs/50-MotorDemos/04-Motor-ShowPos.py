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

import time
from PiStorms import PiStorms
psm = PiStorms()

m = ["Motor-Demo", "Connect NXT motor to Bank A M1.",
 "Turn the motor by hand and see ",
 "the encoder values on screen.",
 "Press Go to stop program",
  "Click OK to continue"]
psm.screen.askQuestion(m,["OK"])


doExit = False
old_pos = 0
encoder_pos = -1
counter = 0
while (doExit == False):
    counter = counter + 1
    old_pos = encoder_pos
    encoder_pos = psm.BAM1.pos()
    msg = "Motor encoder:  " + str(encoder_pos)

    # print value only if it was changed.
    if (old_pos != encoder_pos):
        psm.screen.clearScreen()
        psm.screen.drawAutoText(msg, 15, 200, fill=(255, 255, 255), size = 18)
        psm.screen.drawAutoText("Touch screen to reset counter", 15, 218, fill=(255, 255, 255), size = 18)

    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        doExit = True

    #
    # check if screen touched.
    #
    if(psm.screen.isTouched()):
        # if scren was touched,
        psm.BAM1.resetPos()
        time.sleep(.001)
