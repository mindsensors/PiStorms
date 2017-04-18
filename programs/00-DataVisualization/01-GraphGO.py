# This program demonstrates how to create a live-updating graph, but only displaying
# the latest n values on screen. It also explicitly sets the y-axis range.
# Don't hold the button too long, or you'll turn off the PiStorms!
# Tap the touchscreen to exit.

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('GO button state')
plt.title('GO Button')
plt.grid(True)
plt.ylim((-0.05, 1.05)) # set y-axis range, off by a bit so the line isn't right on the edge of the graph

axis = plt.gca() # get current axis
data = np.empty(0)
psm = PiStorms()
image = tempfile.NamedTemporaryFile() # we will be overwriting this same file 

while not psm.screen.isTouched():
    data = np.append(data, psm.isKeyPressed()) # add a data point with the current GO button state
    if axis.lines: axis.lines.pop() # if there's already a line on the graph (old), remove it
    lines = plt.plot(data[-20:], color="blue") # plot the last 20 data points on the graph (new line)
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
