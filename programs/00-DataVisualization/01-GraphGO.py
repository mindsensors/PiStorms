import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('GO button')
plt.title('GO Button')
plt.grid(True)
plt.ylim((-0.05, 1.05))

data = np.zeros(50)
plt.plot(data)
line = plt.gca().lines[0] # gca means "get current axis"

psm = PiStorms()
image = tempfile.NamedTemporaryFile()
while not psm.screen.isTouched():
    data = np.roll(data, -1)
    data[-1] = psm.isKeyPressed()
    line.set_ydata(data)
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
