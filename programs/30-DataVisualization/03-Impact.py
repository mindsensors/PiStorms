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

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms
from mindsensors import ABSIMU
import threading, time

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('acceleration')
plt.title('AbsoluteIMU Car Impact')
plt.grid(True)

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()

datax = np.empty(0, dtype="int_")
datay = np.empty(0, dtype="int_")
dataz = np.empty(0, dtype="int_")

stop = False
def captureData():
    global datax, datay, dataz, stop
    while not psm.isKeyPressed():
        time.sleep(0.01) # take a short break to let the Pi do the other things it needs to
        accel = imu.get_accelall()[0]
        if accel == ('','',''): continue # try again if sensor is disconnected
        if accel[0] < 30000: datax = np.append(datax, accel[0])
        if accel[1] < 30000: datay = np.append(datay, accel[1])
        if accel[2] < 30000: dataz = np.append(dataz, accel[2])
    stop = True

threading.Thread(target=captureData).start() # create a new thread that will run this method and start it

image = tempfile.NamedTemporaryFile()
while not stop:
    plt.plot(datax, color="red")
    plt.plot(datay, color="green")
    plt.plot(dataz, color="blue")
    plt.tight_layout()
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)

plt.savefig("/home/pi/Documents/impact.png")
np.savetxt("/home/pi/Documents/impact.csv", np.column_stack([datax,datay,dataz]), delimiter=",", fmt="%i")

psm.resetKeyPressCount()
while psm.getKeyPressCount() < 1: time.sleep(0.1) # leave image on screen until you press GO
