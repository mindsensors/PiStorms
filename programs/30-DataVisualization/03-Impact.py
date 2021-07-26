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
import threading, time

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('acceleration')
plt.title('AbsoluteIMU Car Impact')
plt.grid(True)

imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()

datax = np.empty(0, dtype="int_")
datay = np.empty(0, dtype="int_")
dataz = np.empty(0, dtype="int_")

stop = False
def captureData():
    global datax, datay, dataz, stop
    while psm.getKeyPressCount() < 1:
        accel = imu.get_accelall()[0]
        if accel == ('','',''):
            answer = psm.screen.askQuestion(["AbsoluteIMU not found!", "Please connect an AbsoluteIMU sensor", "to BAS1."], ["OK", "Cancel"], goBtn=True)
            if answer != 0: break
        # append the data, but only if x, y, and z are all reasonable measurements (not something crazy like over 30,000)
        if all(accel[i] < 30000 for i in range(3)):
            datax = np.append(datax, accel[0])
            datay = np.append(datay, accel[1])
            dataz = np.append(dataz, accel[2])
        time.sleep(0.01) # take a short break to let the Pi do the other things it needs to (like draw the screen)
    stop = True

threading.Thread(target=captureData).start() # create a new thread that will run this method and start it

image = tempfile.NamedTemporaryFile()
while not stop:
    plt.plot(datax, color="red")
    plt.plot(datay, color="green")
    plt.plot(dataz, color="blue")
    plt.tight_layout()
    plt.savefig(image.name, format="png")
    if psm.screen.getMode() != psm.screen.PS_MODE_POPUP: # as long as there's not a popup about the sensor missing...
        psm.screen.fillBmp(0,0, 320,240, image.name) # draw the image

plt.savefig("/home/pi/Documents/impact.png")
np.savetxt("/home/pi/Documents/impact.csv", np.column_stack([datax,datay,dataz]), delimiter=",", fmt="%i")

psm.screen.drawAutoText("Press GO to exit.", 2, 219, psm.screen.PS_BLACK)
psm.waitForKeyPress()
