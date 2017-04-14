import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms

plt.figure(figsize=(4,3), dpi=80)
y = []
psm = PiStorms()
image = tempfile.NamedTemporaryFile()
while True:
    y.append(np.random.random())
    y = y[-10:]
    plt.cla() # clear axis
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.ylim((0,1))
    plt.plot(range(0,len(y)), y)
    plt.savefig(image.name+".png")
    psm.screen.fillBmp(0,0, 320,240, image.name+".png")
