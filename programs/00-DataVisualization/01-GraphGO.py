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
plt.ylabel('GO button')
plt.title('GO Button')
plt.grid(True)
plt.ylim((-0.05, 1.05)) # set y-axis range, off by a bit so the line isn't right on the edge of the graph

# make a data array of 50 values, they are all 0 at the beginning
# in this example we are only displaying the latest 50 readings
data = np.zeros(50)
plt.plot(data)
line = plt.gca().lines[0] # gca means "get current axis"

psm = PiStorms()
image = tempfile.NamedTemporaryFile() # we will be overwriting this same file 
while not psm.screen.isTouched():
    data = np.roll(data, -1) # shift the data left one
    data[-1] = psm.isKeyPressed() # change the last value to 0 or 1 depending on the GO button
    line.set_ydata(data) # overwrite the data for the line so it updates
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
