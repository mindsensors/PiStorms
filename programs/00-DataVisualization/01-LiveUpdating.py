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
plt.ylim((0,1))
y = np.zeros(10)
plt.plot(range(0,len(y)), y)
line = plt.gca().lines[0] # gca means "get current axis"

psm = PiStorms()
image = tempfile.NamedTemporaryFile()
while True:
    y = np.roll(y, -1)
    y[y.size-1] = np.random.random()
    line.set_ydata(y)
    plt.savefig(image.name+".png")
    psm.screen.fillBmp(0,0, 320,240, image.name+".png")
