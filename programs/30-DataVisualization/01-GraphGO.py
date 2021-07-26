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

# This program demonstrates how to create a live-updating graph, but only displaying
# the latest n values on screen. It also explicitly sets the y-axis range.
# Don't hold the button too long, or you'll turn off the PiStorms!
# Tap the touchscreen to exit.

from PiStorms import PiStorms
psm = PiStorms()
psm.screen.termPrintln("Please wait a moment")
psm.screen.termPrintln("as matplotlib loads...")
psm.screen.termPrintAt(3, "Tap and hold the screen to quit.")

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('GO button state')
plt.title('GO Button')
plt.grid(True)
plt.ylim((-0.05, 1.05)) # set y-axis range, off by a bit so the line isn't right on the edge of the graph

axis = plt.gca() # get current axis
data = np.empty(0)
image = tempfile.NamedTemporaryFile() # we will be overwriting this same file

while not psm.screen.isTouched():
    data = np.append(data, psm.isKeyPressed()) # add a data point with the current GO button state
    if axis.lines: axis.lines.pop() # if there's already a line on the graph (old), remove it
    lines = plt.plot(data[-20:], color="blue") # plot the last 20 data points on the graph (new line)
    plt.tight_layout() # make sure the entire plot fits on screen
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
