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
plt.savefig("test.png", dpi=40)
#plt.show()

from PIL import Image
img = Image.open("test.png")
img.save("test.bmp")
from PiStorms import PiStorms
psm = PiStorms()
import os
psm.screen.fillBmp( 0,0, 320,240, os.path.join(os.getcwd(),"test.bmp") )
