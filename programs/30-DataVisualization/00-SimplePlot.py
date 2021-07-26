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

# This program demonstrates how to create and display a basic, static graph
# on the PiStorms screen.
# It is heavily based on https://matplotlib.org/examples/pylab_examples/simple_plot.html

from PiStorms import PiStorms
psm = PiStorms()
psm.screen.termPrintln("Please wait a moment")
psm.screen.termPrintln("as matplotlib loads...")
psm.screen.termPrintAt(3, "Press GO to quit.")

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np

# setup figure
plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)

# generate and plot data
t = np.arange(0.0, 2.0, 0.01) # a range from 0.0 to 2.0 with 0.01 intervals: [0.0, 0.01, 0.02 ... 1.98, 1.99, 2.0]
s = 1 + np.sin(2*np.pi*t) # simple sine wave
plt.plot(t, s)
plt.tight_layout() # make sure the entire plot fits on screen

# save to temporary file
import tempfile
image = tempfile.NamedTemporaryFile()
plt.savefig(image.name, format="png")

# draw on screen
psm.screen.fillBmp(0,0, 320,240, image.name)

# wait until GO is pressed to exit
psm.waitForKeyPress()
