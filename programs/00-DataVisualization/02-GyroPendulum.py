import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms
from mindsensors import ABSIMU

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('acceleration')
plt.title('AbsoluteIMU Pendulum')
plt.grid(True)

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()
psm.screen.drawAutoText("Recording data!",   45, 40,  size=32)
psm.screen.drawAutoText("Press GO to stop.", 65, 120, size=24)

data = np.empty(0)
while not psm.isKeyPressed():
    accel = imu.get_accely()
    if not accel > 30000:
        data = np.append(data, accel)
plt.plot(data)

image = tempfile.NamedTemporaryFile()
plt.savefig(image.name, format="png")
psm.screen.fillBmp(0,0, 320,240, image.name)
