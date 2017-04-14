import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms

plt.figure(figsize=(4,3), dpi=80)
x,y = [],[]
psm = PiStorms()
image = tempfile.NamedTemporaryFile()
while True:
    x.append(np.random.random())
    y.append(np.random.random())
    plt.cla() # clear axis
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.plot(x, y)
    plt.savefig(image.name+".png")
    psm.screen.fillBmp(0,0, 320,240, image.name+".png")
