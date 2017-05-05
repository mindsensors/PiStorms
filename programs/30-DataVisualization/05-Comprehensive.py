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

DATA_SIZE = 80 # only the latest n data points will be shown on screen (this is not a cap on how much data will be recorded in total)

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('tilt')
plt.title('3-Axis AbsoluteIMU Tilt')
plt.grid(True)

data = np.zeros([3,DATA_SIZE], dtype="int_")
plt.plot(data.T) # transpose
axis = plt.gca() # get current axis
axis.set_xticklabels([]) # hide x-axis tick labels
axis.set_color_cycle(['red', 'green', 'blue'])
smooth_x = np.linspace(0, DATA_SIZE-1, 247) # the x-axis for the smoothed lines    

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C() # attach AbsoluteIMU to BAS1, or change this line

canvas = plt.get_current_fig_manager().canvas # used to quickly redraw the screen
disp = psm.screen.disp # just shorthand

stop = False
def captureData():
    global data, stop
    while not psm.isKeyPressed():
        tilt = imu.get_tiltall()[0] # read the x, y, and z tilt data
        if tilt == ('','',''):
            psm.screen.showMessage(["AbsoluteIMU not found!", "Please connect an AbsoluteIMU sensor", "to BAS1."])
        else:
            data = np.column_stack([data, tilt]) # add the new numbers at the end of the array
        time.sleep(0.01) # let the screen update
    stop = True
threading.Thread(target=captureData).start()

while not stop:
    plt.cla() # clear axis, get rid of old lines
    slicedata = data[:,-1*DATA_SIZE:] # use only the last n data points, where n is DATA_SIZE
    try:
        for i in range(3): # plot a spline (smooth line) for each axis
            plt.plot(smooth_x, spline(np.arange(len(slicedata[i])), slicedata[i], smooth_x))
    except: continue # if there's an error, just try again (don't crash)
    canvas.draw()
    if psm.screen.getMode() != psm.screen.PS_MODE_POPUP: # as long as there's not a popup about the sensor missing...
        # directly write the matplotlib canvas to the PiStorms screen (faster than using an intermediary)
        disp.buffer = Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb()).rotate(-90*psm.screen.currentRotation)
        disp.display() # update the screen

# save the final picture and data to files in ~/Documents
plt.savefig("/home/pi/Documents/smoothfastfast.png")
np.savetxt("/home/pi/Documents/smoothfastfast.csv", data.T[DATA_SIZE:], delimiter=",", fmt="%i")
