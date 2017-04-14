import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile, random
from PiStorms import PiStorms

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)

t = np.arange(0.0, 2.0, 0.01)
psm = PiStorms()
image = tempfile.NamedTemporaryFile()
while True:
    s = map(lambda n: random.randint(1,100), t)
    plt.cla() # clear axis
    plt.plot(t, s)
    plt.savefig(image.name+".png")
    psm.screen.fillBmp(0,0, 320,240, image.name+".png")
