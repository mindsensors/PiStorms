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

psm = PiStorms()
gyro = EV3GyroSensor("BAS1")
gyro.setMode(PS_SENSOR_MODE_EV3_GYRO_RATE)
psm.screen.drawAutoText("Recording data!",   45, 40,  size=32)
psm.screen.drawAutoText("Press GO to stop.", 65, 120, size=24)

data = np.empty(0)
while not psm.isKeyPressed():
    data = np.append(data, gyro.readValue())
plt.plot(data)

image = tempfile.NamedTemporaryFile()
plt.savefig(image.name, format="png")
psm.screen.fillBmp(0,0, 320,240, image.name)
