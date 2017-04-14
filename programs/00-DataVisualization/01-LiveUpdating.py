import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('index')
plt.ylabel('random data')
plt.title('Live updating example')
plt.grid(True)
plt.ylim((0, 1)) # set y-axis range
y = np.zeros(10)
plt.plot(y)
line = plt.gca().lines[0] # gca means "get current axis"

psm = PiStorms()
image = tempfile.NamedTemporaryFile()
while not psm.isKeyPressed():
    y = np.roll(y, -1)
    y[-1] = np.random.random()
    line.set_ydata(y)
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
