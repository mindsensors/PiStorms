from __future__ import division
import math
from time import sleep
import numpy

import os,sys,inspect,time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PiStorms import PiStorms
psm = PiStorms()

s = psm.screen

p = 0.25
size = 2
pause = 1

def getPoints():
    x = []
    y = []
    for i in range(200):
        x.append(s.RAW_X())
        y.append(s.RAW_Y())
    x = sum(x)/len(x)
    y = sum(y)/len(y)
    return (x, y)

# top-left
s.fillRect(320*p, 240*p, size, size)
sleep(pause)
while not psm.isKeyPressed(): pass
rx1, ry1 = getPoints()
s.fillRect(0, 0, 320, 320)
sleep(pause)
s.fillRect(0, 0, 320, 320, fill=s.PS_BLACK)

# bottom-left
s.fillRect(320*p, 240*(1-p), size, size)
sleep(pause)
while not psm.isKeyPressed(): pass
rx2, ry2 = getPoints()
s.fillRect(0, 0, 320, 320)
sleep(pause)
s.fillRect(0, 0, 320, 320, fill=s.PS_BLACK)

# bottom-right
s.fillRect(320*(1-p), 240*(1-p), size, size)
sleep(pause)
while not psm.isKeyPressed(): pass
rx3, ry3 = getPoints()
s.fillRect(0, 0, 320, 320)
sleep(pause)
s.fillRect(0, 0, 320, 320, fill=s.PS_BLACK)

#top-right
s.fillRect(320*(1-p), 240*p, size, size)
sleep(pause)
while not psm.isKeyPressed(): pass
rx4, ry4 = getPoints()
s.fillRect(0, 0, 320, 320)
sleep(pause)
s.fillRect(0, 0, 320, 320, fill=s.PS_BLACK)

#center
s.fillRect(320*0.5, 240*0.5, size, size)
sleep(pause)
while not psm.isKeyPressed(): pass
rx5, ry5 = getPoints()
s.fillRect(0, 0, 320, 320)
sleep(pause)
s.fillRect(0, 0, 320, 320, fill=s.PS_BLACK)

x1 = rx1-(rx5-rx1)*p*4
y1 = ry1-(ry5-ry1)*p*4
x2 = rx2-(rx5-rx2)*p*4
y2 = ry2+(ry2-ry5)*p*4
x3 = rx3+(rx3-rx5)*p*4
y3 = ry3+(ry3-ry5)*p*4
x4 = rx4+(rx4-rx5)*p*4
y4 = ry4-(ry5-ry4)*p*4

#print (int(rx1), int(ry1)), (int(rx2), int(ry2)), (int(rx3), int(ry3)), (int(rx4), int(ry4)), (int(rx5), int(ry5))
print (int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3)), (int(x4), int(y4))

psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x00, x1) # write to temporary memory
psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x02, y1) # write to temporary memory
psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x04, x2) # write to temporary memory
psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x06, y2) # write to temporary memory
psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x08, x3) # write to temporary memory
psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x0A, y3) # write to temporary memory
psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x0C, x4) # write to temporary memory
psm.psc.bankA.writeInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x0E, y4) # write to temporary memory
psm.psc.bankA.writeByte(psm.psc.PS_Command, psm.psc.E) # unlock permanent memory
psm.psc.bankA.writeByte(psm.psc.PS_Command, psm.psc.w) # copy from temporary memory to permanent memory
timeout = time.time() + 1 # wait for up to a second
while psm.psc.bankA.readByte(psm.psc.PS_TS_CALIBRATION_DATA_READY) != 1: # wait for ready byte
    time.sleep(0.01)
    if time.time() > timeout:
        break #s.showMessage(['Error', 'Failed to write configuration values.']) # no need to show message here, it will already show below
if not (psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x00) == int(x1)
    and psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x02) == int(y1)
    and psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x04) == int(x2)
    and psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x06) == int(y2)
    and psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x08) == int(x3)
    and psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x0A) == int(y3)
    and psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x0C) == int(x4)
    and psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + 0x0E) == int(y4)):
    print 'Error writing configuration values'
    s.showMessage(['Error', 'Failed to write configuration values.'])

for i in range(8):
    print psm.psc.bankA.readInteger(psm.psc.PS_TS_CALIBRATION_DATA + i*2)
