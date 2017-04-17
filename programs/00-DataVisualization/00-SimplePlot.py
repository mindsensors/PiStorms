# heavily based on https://matplotlib.org/examples/pylab_examples/simple_plot.html

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np

# setup figure
plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)

# generate and plot data
t = np.arange(0.0, 2.0, 0.01) # a range from 0.0 to 2.0 with 0.01 intervals: [0.0, 0.01, 0.02 ... 1.98, 1.99, 2.0]
s = 1 + np.sin(2*np.pi*t) # simple sine wave
plt.plot(t, s)

# save to temporary file
import tempfile
image = tempfile.NamedTemporaryFile()
plt.savefig(image.name, format="png")

# draw on screen
from PiStorms import PiStorms
psm = PiStorms()
psm.screen.fillBmp(0,0, 320,240, image.name)
