import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms
from LegoDevices import EV3GyroSensor, PS_SENSOR_MODE_EV3_GYRO_RATE, PS_SENSOR_MODE_EV3_GYRO_ANGLE

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('angle')
plt.title('Gyro Pendulum')
plt.grid(True)
plt.ylim((-500, 500))

data = np.zeros(10)
plt.plot(data)
line = plt.gca().lines[0] # gca means "get current axis"

psm = PiStorms()
gyro = EV3GyroSensor("BAS1")
gyro.setMode(PS_SENSOR_MODE_EV3_GYRO_RATE)
image = tempfile.NamedTemporaryFile()

while not psm.isKeyPressed():
    data = np.roll(data, -1)
    data[-1] = gyro.readValue()
    line.set_ydata(data)
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
