import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms
from mindsensors import ABSIMU

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('tilt')
plt.title('3-Axis AbsoluteIMU Tilt')
plt.grid(True)

data = np.zeros([3,10])
plt.plot(data.T) # transpose
axis = plt.gca() # get current axis

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()
image = tempfile.NamedTemporaryFile()

while not psm.isKeyPressed():
    data = np.roll(data, -1)
    tilt = imu.get_tiltall()[0]
    for i in range(0,3):
        data[i][-1] = tilt[i]
        axis.lines[i].set_ydata(data[i])
    axis.relim() # recompute axis limits
    axis.autoscale_view()
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
