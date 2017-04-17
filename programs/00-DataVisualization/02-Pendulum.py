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
plt.title('AbsoluteIMU Pendulum')
plt.grid(True)

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()

data = np.empty(0)

def captureData():
    global data
    while not psm.isKeyPressed():
        accel = imu.get_accely()
        if not accel > 30000:
            data = np.append(data, accel)
        time.sleep(0.01)
threading.Thread(target=captureData).start()

while not psm.isKeyPressed():
    plt.plot(data, color="blue")
    image = tempfile.NamedTemporaryFile()
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
