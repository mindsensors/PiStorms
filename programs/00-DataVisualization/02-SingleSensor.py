import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms
from LegoDevices import EV3InfraredSensor, PS_SENSOR_MODE_EV3_IR_PROXIMITY

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('proximity')
plt.title('Distance')
plt.grid(True)
plt.ylim((-5, 105))

data = np.zeros(10)
plt.plot(data)
line = plt.gca().lines[0] # gca means "get current axis"

psm = PiStorms()
ir = EV3InfraredSensor("BAS1")
ir.setMode(PS_SENSOR_MODE_EV3_IR_PROXIMITY) # see example in 50-SensorDemos
image = tempfile.NamedTemporaryFile()

while not psm.isKeyPressed():
    data = np.roll(data, -1)
    data[-1] = ir.readProximity()
    line.set_ydata(data)
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
