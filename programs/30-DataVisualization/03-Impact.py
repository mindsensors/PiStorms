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
        accel = imu.get_accelall()[0]
        if accel[0] < 30000: datax = np.append(datax, accel[0])
        if accel[1] < 30000: datay = np.append(datay, accel[1])
        if accel[2] < 30000: dataz = np.append(dataz, accel[2])
        time.sleep(0.01) # take a short break to let the Pi do the other things it needs to
    stop = True

threading.Thread(target=captureData).start() # create a new thread that will run this method and start it

image = tempfile.NamedTemporaryFile()
while not stop:
    plt.plot(datax, color="red")
    plt.plot(datay, color="green")
    plt.plot(dataz, color="blue")
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)

plt.savefig("/home/pi/Documents/impact.png")
np.savetxt("/home/pi/Documents/impact.csv", [datax,datay,dataz], delimiter=",", fmt="%i")

while psm.isKeyPressed(): time.sleep(0.01) # leave image on screen until you release...
while not psm.isKeyPressed(): time.sleep(0.01) # ...and press the button again
