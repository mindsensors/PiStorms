import matplotlib
matplotlib.use("GTK")
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)

import tempfile
image = tempfile.NamedTemporaryFile()
plt.savefig(image.name+".png", dpi=40)

from PIL import Image
Image.open(image.name+".png").save(image.name+".bmp")
from PiStorms import PiStorms
psm = PiStorms()
psm.screen.fillBmp(0,0, 320,240, image.name+".bmp")
