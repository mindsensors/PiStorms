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
tilt = np.zeros([3,10])
plt.plot(tilt.T)
ax = plt.gca() # get current axis

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()
image = tempfile.NamedTemporaryFile()
while True:
    tilt = np.roll(tilt, -1)
    tiltnow = imu.get_tiltall()[0]
    for i in range(0,3):
        tilt[i][tilt[i].size-1] = tiltnow[i]
        ax.lines[i].set_ydata(tilt[i])
    ax.relim() # recompute axis limits
    ax.autoscale_view()
    plt.savefig(image.name+".png")
    psm.screen.fillBmp(0,0, 320,240, image.name+".png")
