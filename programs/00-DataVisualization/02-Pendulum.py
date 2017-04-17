import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PiStorms import PiStorms
from mindsensors import ABSIMU
import threading, time

plt.figure(figsize=(4,3), dpi=80)
plt.xlabel('time')
plt.ylabel('acceleration')
plt.title('AbsoluteIMU Pendulum')
plt.grid(True)

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C() # see example in 50-SensorDemos

data = np.empty(0) # data starts completely empty

# We could take the same approach as the previous examples, but unfortunately
# the process of generating the graph image, saving it, and drawing it to the screen
# takes roughly 2.5 seconds (for 76,800 pixels in a roughly 15kb file). Taking
# readings this slowly would not be very useful, so instead we'll constantly read
# the sensor's value, and just update the graph as fast as we can.
# We use threads to accomplish this. The method below, captureData(), will be
# running on a separate thread. It will take a reading from the AbsoluteIMU about
# one hundred times per second, which should be plenty for this experiment.
# It stores these values in the data variable. Meanwile (further down) a loop
# will continue to re-plot the data as it is updated and show it on the screen.

def captureData():
    global data # share the data variable from the global namespace
    while not psm.isKeyPressed():
        accel = imu.get_accely() # acceleration in the y direction
        if not accel > 30000: # as long as it's not a crazy value...
            data = np.append(data, accel) # add it to the data array
        time.sleep(0.01) # take a short break to let the Pi do the other things it needs to
threading.Thread(target=captureData).start() # create a new thread that will run this method and start it

while not psm.isKeyPressed():
    plt.plot(data, color="blue")
    image = tempfile.NamedTemporaryFile()
    plt.savefig(image.name, format="png")
    psm.screen.fillBmp(0,0, 320,240, image.name)
