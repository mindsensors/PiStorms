#!/usr/bin/env python
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
# 05/03/17  Seth Tenembaum  Initial development.
#

# Smooth lines
# Fast data collection
# Fast drawing
# Save final graph and data
# Multiple simultaneous axes

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
import threading, time
from PIL import Image
from PiStorms import PiStorms
from mindsensors import ABSIMU

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('tilt')
plt.title('3-Axis AbsoluteIMU Tilt')
plt.grid(True)

data = np.zeros([3,0], dtype="int_")
plt.plot(data.T) # transpose
axis = plt.gca() # get current axis
axis.set_xticklabels([]) # hide x-axis tick labels

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()

canvas = plt.get_current_fig_manager().canvas
disp = psm.screen.disp

stop = False
def captureData():
    global data, stop, axis
    while len(axis.lines) < 3: time.sleep(0.1) # wait for the three lines to exist
    while not psm.isKeyPressed():
        tilt = imu.get_tiltall()[0] # read the x, y, and z tilt data
        for i in range(3): # update the data array and graph line for each axis
            data[i] = np.append(data[i], tilt[i])
            axis.lines[i].set_ydata(data[i])
        time.sleep(0.01)
    stop = True
threading.Thread(target=captureData).start()

while len(data[0]) < 1: time.sleep(0.1) # wait for the first data points before plotting
while not stop:
    if axis.lines:
        for i in range(3): axis.lines.pop()
    smooth_x = np.linspace(0, len(data[0])-1, 320)
    for i in range(3): plt.plot(smooth_x, spline(np.arange(len(data[i])), data[i], smooth_x))
    axis.relim() # recompute axis limits/bounds
    axis.autoscale_view()
    canvas.draw()
    disp.buffer = Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb()).rotate(-90*psm.screen.currentRotation)
    disp.display()

plt.savefig("/home/pi/Documents/smoothfastfast.png")
np.savetxt("/home/pi/Documents/smoothfastfast.csv", data, delimiter=",", fmt="%i")
