#!/usr/bin/env python
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
# 04/18/16   Deepak     Initial development.
#

from PiStorms import PiStorms
psm = PiStorms()

m = ["EV3Gyro-Rate-Demo", "Connect EV3 Gyro to BAS1",
 "and Press OK to continue.",
 "Then move sensor to see readings.",
 "",
 "Press Go to stop program."]
psm.screen.showMessage(m)

old_rateValue = -10
rateValue = 0

def mainLoop():
    #save the previous value
    old_rateValue = rateValue
    #
    # read from EV3 Gyro
    #
    rateValue = psm.BAS1.gyroRateEV3()
    msg = "Rate of Change: " + str(rateValue)

    # print value only if it was changed.
    if (old_rateValue != rateValue):
        psm.screen.clearScreen()
        psm.screen.drawAutoText(msg, 15, 164, fill=(255, 255, 255), size = 18)

psm.untilKeyPress(mainLoop)

psm.screen.clearScreen()
psm.screen.termPrintln("")
psm.screen.termPrintln("Exiting to menu")
