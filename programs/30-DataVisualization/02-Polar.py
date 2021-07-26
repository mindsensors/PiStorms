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
# 06/15/17  Seth Tenembaum  Initial development
#

# This program demonstrates using a polar graph
# to show the AbsoluteIMU's compass heading.

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

plt.figure(figsize=(4,3), dpi=80)
plt.title('AbsoluteIMU Compass Heading')

data = np.empty(0)
sub = plt.subplot(projection='polar')
sub.set_theta_direction(-1)
sub.set_rticks([]) # hide ticks
tau = 2*np.pi

imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()
image = tempfile.NamedTemporaryFile()

while psm.getKeyPressCount() < 1:
    h = imu.get_heading()
    data = np.append(data, \
            np.interp(h, [0,360], [0,tau]))
    r = np.arange(len(data))
    plt.plot(data, r, color="blue")
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
