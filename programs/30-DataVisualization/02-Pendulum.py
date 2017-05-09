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
# 04/18/17  Seth Tenembaum  Initial development.
#

# This program demonstrates using a sensor, the AbsoluteIMU in this case.
# It also demonstrates how to capture data quickly on a separate thread,
# and update the graph on screen as the data comes in. Furthermore it will
# save the data to a file once the program stops.

from PiStorms import PiStorms
psm = PiStorms()
psm.screen.termPrintln("Please wait a moment")
psm.screen.termPrintln("as matplotlib loads...")

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from mindsensors import ABSIMU
import threading, time

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('acceleration')
plt.title('AbsoluteIMU Pendulum')
plt.grid(True)

imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C() # see example in 50-SensorDemos

data = np.empty(0, dtype="int_") # data starts completely empty (signed integer data type)

# We could take the same approach as the previous examples, but unfortunately
# the process of generating the graph image, saving it, and drawing it to the screen
# takes roughly 1 second (for 76,800 pixels in a roughly 15kb file). Taking
# readings this slowly would not be very useful, so instead we'll constantly read
# the sensor's value, and just update the graph as fast as we can.
# We use threads to accomplish this. The method below, captureData(), will be
# running on a separate thread. It will take a reading from the AbsoluteIMU about
# one hundred times per second, which should be plenty for this experiment.
# It stores these values in the data variable. Meanwile (further down) a loop
# will continue to re-plot the data as it is updated and show it on the screen.

stop = False
def captureData():
    global data, stop # share the data and stop variables from the global namespace
    while not psm.isKeyPressed():
        try:
            accel = imu.get_accely() + imu.get_accelx() # acceleration in the x+y direction
            if accel == '': raise TypeError("AbsoluteIMU not connected to BAS1")
            if accel > 3000: raise ValueError("AbsoluteIMU returned a crazy value")
            data = np.append(data, accel) # add the new (valid) data to the data array
        except TypeError:
            answer = psm.screen.askQuestion(["AbsoluteIMU not found!", "Please connect an AbsoluteIMU sensor", "to BAS1."], ["OK", "Cancel"], goBtn=True)
            if answer != 0: break
        except ValueError as e:
            print "Error: " + e.args[0]
        time.sleep(0.01) # take a short break to let the Pi do the other things it needs to (like draw the screen)
    stop = True

threading.Thread(target=captureData).start() # create a new thread that will run this method and start it

image = tempfile.NamedTemporaryFile()
while not stop:
    plt.plot(data, color="blue")
    plt.tight_layout()
    plt.savefig(image.name, format="png")
    if psm.screen.getMode() != psm.screen.PS_MODE_POPUP: # as long as there's not a popup about the sensor missing...
        psm.screen.fillBmp(0,0, 320,240, image.name) # draw the image

plt.savefig("/home/pi/Documents/pendulum.png")
np.savetxt("/home/pi/Documents/pendulum.csv", data, delimiter=",", fmt="%i")
