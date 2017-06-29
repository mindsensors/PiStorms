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
# 01/04/17   Deepak     Initial development.
# 06/29/17   Seth       Simplify using `enumerate`
#

from PiStorms import PiStorms
import MsDevices
import time
psm = PiStorms()

m = ["LineLeader-Demo",
     "Connect LineLeader-v2 sensor",
     "to BAS1, and Press OK to continue"]
psm.screen.showMessage(m)

# we are attaching a LineLeader to Port BAS1,
# initialize the variable for the sensor
sensor = MsDevices.LineLeader(psm.BAS1)

doExit = False
readings = []

psm.screen.termPrintAt(7, "LineLeader readings")
psm.screen.termPrintAt(8, "Press GO to stop program")

# main loop
while(not doExit):
    # wipe the old graph
    for i, reading in enumerate(readings):
        psm.screen.fillRect(10+(i*35), 10, 30, reading, fill = (0,0,0), display = False)

    # read from the sensor
    readings = sensor.ReadRaw_Calibrated()
    readings = [reading for reading in readings if reading is not None]

    # draw new graph
    for i, reading in enumerate(readings):
        print reading
        psm.screen.fillRect(10+(i*35), 10, 30, reading, fill = (200,200,0), display = False)

    time.sleep(0.4)
    psm.screen.fillRect(5, 0, 300, 4, fill = (200,0,0), display = True)

    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintAt(8, "Exiting to menu")
        doExit = True
