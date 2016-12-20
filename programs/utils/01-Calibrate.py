from __future__ import division
import math

import os,sys,inspect,time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PiStorms import PiStorms
psm = PiStorms() # this may produce "Failed to read touchscreen calibration values" (mindsensorsUI.py)

s = psm.screen



##########################
# Get calibration values #
##########################

def getPoints():
    r = 200 # conf
    x = []
    y = []
    for i in range(r):
        x.append(s.RAW_X())
        y.append(s.RAW_Y())
    x = sum(x)/len(x)
    y = sum(y)/len(y)
    return (x, y)

# x and y coordinated for center of crosshair, length of lines, fill color
def drawCrosshair(x, y, l, f):
    s.fillRect(x-l, y, l*2, 0, fill=f, display=False)
    s.fillRect(x, y-l, 0, l*2, fill=f)
    
def getCalibrationValues(x, y):
    length = 10
    fill = (0,255,0)
    
    drawCrosshair(x, y, length, fill)
    while not psm.isKeyPressed(): pass
    rx, ry = getPoints()
    s.fillRect(0, 0, 320, 320, fill=s.PS_BLACK)
    return rx, ry

p = 0.25 # conf
rx4, ry4 = getCalibrationValues(320*(1-p), 240*p)     # top-right
rx1, ry1 = getCalibrationValues(320*p, 240*p)         # top-left
rx3, ry3 = getCalibrationValues(320*(1-p), 240*(1-p)) # bottom-right
rx2, ry2 = getCalibrationValues(320*p, 240*(1-p))     # bottom-left
rx5, ry5 = getCalibrationValues(320*0.5, 240*0.5)     # center

x1 = rx1-(rx5-rx1)*p*4
y1 = ry1-(ry5-ry1)*p*4
x2 = rx2-(rx5-rx2)*p*4
y2 = ry2+(ry2-ry5)*p*4
x3 = rx3+(rx3-rx5)*p*4
y3 = ry3+(ry3-ry5)*p*4
x4 = rx4+(rx4-rx5)*p*4
y4 = ry4-(ry5-ry4)*p*4

#print (int(rx1), int(ry1)), (int(rx2), int(ry2)), (int(rx3), int(ry3)), (int(rx4), int(ry4)), (int(rx5), int(ry5))
#print (int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3)), (int(x4), int(y4))



########################################
# Write calibration values to PiStorms #
########################################

for offset, value in enumerate([x1,y1,x2,y2,x3,y3,x4,y4]):
    psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x02*offset, value) # write to temporary memory
psm.psc.bankA.writeByte(psm.psc.PS_Command, psm.psc.E) # unlock permanent memory
psm.psc.bankA.writeByte(psm.psc.PS_Command, psm.psc.w) # copy from temporary memory to permanent memory
timeout = time.time() + 1 # wait for up to a second
while psm.psc.bankA.readByte(psm.psc.PS_TS_CALIBRATION_DATA_READY) != 1: # wait for ready byte
    time.sleep(0.01)
    if time.time() > timeout:
        break # no need to show an error message here, it will already show below

def calibrationEqual(offset, value):
    return psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x02*offset) == int(value)
if all([ calibrationEqual(offset, value) for offset, value in enumerate([x1,y1,x2,y2,x3,y3,x4,y4]) ]):
    print 'Successfully wrote calibration values to PiStorms'
    s.ts_cal = dict(zip(['x1','y1','x2','y2','x3','y3','x4','y4'],[x1,y1,x2,y2,x3,y3,x4,y4])) # manually update calibration values in mindsensorsUI. A new PiStorms object would be needed to have mindsensorsUI actually read the values, but MSBrowser would have to be launched first to write them to the cache file
    s.showMessage(['Success', 'Wrote calibration values', 'to PiStorms'])
else:
    print 'Error writing calibration values to PiStorms'
    s.showMessage(['Error', 'Failed to write calibration values', 'to PiStorms'])

#for i in range(8): print psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + i*2)
