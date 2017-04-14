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
x = np.zeros(10)
y = np.zeros(10)
z = np.zeros(10)
plt.plot(range(0,len(x)), x)
plt.plot(range(0,len(y)), y)
plt.plot(range(0,len(z)), z)
ax = plt.gca() # get current axis

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()
image = tempfile.NamedTemporaryFile()
while True:
    x = np.roll(x, -1)
    y = np.roll(y, -1)
    z = np.roll(z, -1)
    x[x.size-1] = imu.get_tiltx()
    y[y.size-1] = imu.get_tilty()
    z[z.size-1] = imu.get_tiltz()
    ax.lines[0].set_ydata(x)
    ax.lines[1].set_ydata(y)
    ax.lines[2].set_ydata(z)
    ax.relim() # recompute axis limits
    ax.autoscale_view()
    plt.savefig(image.name+".png")
    psm.screen.fillBmp(0,0, 320,240, image.name+".png")
