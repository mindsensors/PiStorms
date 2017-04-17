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

# this time data will be a 3 by 10 array, storing the latest ten values for each axis
data = np.zeros([3,10])
plt.plot(data.T) # transpose
axis = plt.gca() # get current axis

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C()
image = tempfile.NamedTemporaryFile()

while not psm.isKeyPressed():
    data = np.roll(data, -1)
    tilt = imu.get_tiltall()[0] # read the x, y, and z tilt data
    for i in range(0,3): # update the data array and graph line for each axis
        data[i][-1] = tilt[i]
        axis.lines[i].set_ydata(data[i])
    axis.relim() # recompute axis limits/bounds
    axis.autoscale_view()
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
