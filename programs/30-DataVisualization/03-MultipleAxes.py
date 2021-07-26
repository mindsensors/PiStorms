#!/usr/bin/env python3
#
# Copyright (c) 2017 mindsensors.com
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
# Date      Author          Comments
# 04/18/17  Seth Tenembaum  Initial development.
#

# This program demonstrates using a sensor and displaying multiple lines
# (overlapping data series). Here we plot the three axes of tilt from the
# AbsoluteIMU sensor.

from PiStorms import PiStorms
psm = PiStorms()
psm.screen.termPrintln("Please wait a moment")
psm.screen.termPrintln("as matplotlib loads...")
psm.screen.termPrintAt(3, "Press GO to quit.")

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from mindsensors import ABSIMU
import time

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('tilt')
plt.title('3-Axis AbsoluteIMU Tilt')
plt.grid(True)
plt.ylim((-130, 130))

# this time data will be a 3 by 10 array, storing the latest ten values for each axis
data = np.zeros([3,10])
plt.plot(data.T) # transpose
axis = plt.gca() # get current axis
axis.set_xticklabels([]) # hide x-axis tick labels

imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()
image = tempfile.NamedTemporaryFile()

while psm.getKeyPressCount() < 1:
    tilt = imu.get_tiltall()[0] # read the x, y, and z tilt data
    if tilt == ('','',''):
        answer = psm.screen.askQuestion(["AbsoluteIMU not found!", "Please connect an AbsoluteIMU sensor", "to BAS1."], ["OK", "Cancel"], goBtn=True)
        if answer != 0: break
        continue # try again after you tap "OK" or press GO
    data = np.roll(data, -1)
    for i in range(3): # update the data array and graph line for each axis
        data[i][-1] = tilt[i]
        axis.lines[i].set_ydata(data[i])
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
