import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('Voltage (V)')
plt.title('Battery Voltage')
plt.grid(True)

data = np.empty(0) # start with a completely empty data array
psm = PiStorms()
image = tempfile.NamedTemporaryFile() # we will be overwriting this same file 

while not psm.isKeyPressed():
    data = np.append(data, psm.battVoltage()) # add a data point with the current battery voltage
    plt.plot(data, color="blue") # plot the data on the graph
    plt.savefig(image.name, format="png") # save it
    psm.screen.fillBmp(0,0, 320,240, image.name) # show it on screen
