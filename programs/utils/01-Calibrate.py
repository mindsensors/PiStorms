#!/usr/bin/env python
#
# Copyright (c) 2016 mindsensors.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code,
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# 05/25/16   Deepak     Initial development.
# 12/21/16   Seth       Rewrite for new touchscreen calibration strategy
#

from __future__ import division # for decimal division
import os # to check if cache file exists, possibly launch a painting program, and restart the browser
import ConfigParser # to get PiStorms home folder if launching paint
import time # to periodically decrement calibration confirmation countdown
import sys # to exit if GO button is not pressed to confirm beginning calibration
import json # to write calibration values to cache file
from mindsensorsUI import mindsensorsUI
from PiStormsCom import PiStormsCom

if PiStormsCom().GetFirmwareVersion() < 'V3.00':
    os.system("sudo python " + os.path.join(os.path.dirname(os.path.realpath(__file__)), "01-Calibrate_old.py"))
    sys.exit(0)

#########
# Setup #
#########

# the browser needs to be stopped and restarted to read the new touchscreen values when calibration finishes
os.system("/etc/init.d/MSBrowser.sh stop")

# avoid 'Failed to read touchscreen calibration values' popup from mindsensorsUI if the touchscreen calibration values cache file doesn't exist
if not os.path.isfile('/tmp/ps_ts_cal'):
    open('/tmp/ps_ts_cal', 'w').write('{}')

# modeled after PiStorms class
s = mindsensorsUI("PiStorms", 3) # screen
psc = PiStormsCom() # commmunications
comm = psc.bankA # short hand

# how many samples to take and average when capturing touchscreen values
# 200 takes about a second
CALIBRATION_POINTS_COUNT = 200

# what percent to push the crosshairs from the edges of the screen
# 0 is the exact corner, 0.5 is the center
INSET_PERCENT = 0.25



#############################
# Introduce program to user #
#############################
if not (len(sys.argv) > 1 and str(sys.argv[1]) == "force"):
    s.termGotoLine(0)
    s.termPrintln("Touch Screen Calibration Program")
    s.termPrintln("")
    s.termPrintln("You should only calibrate if you")
    s.termPrintln("notice your touchscreen being")
    s.termPrintln("inaccurate.")
    s.termPrintln("")
    s.termPrintln("If you still want to calibrate,")
    s.termPrintln("press the GO button")

    countdown = 10
    startKeyPressCount = psc.getKeyPressCount()
    while countdown > 0 and psc.getKeyPressCount() == startKeyPressCount:
        s.termReplaceLastLine("within %d second%s" % (countdown, 's' if countdown > 1 else ''))
        time.sleep(1)
        countdown = countdown - 1

    if psc.getKeyPressCount() == startKeyPressCount:
        sys.exit(0) # note: MSBrowser will automatically restart

s.clearScreen()
s.dumpTerminal()
s.termGotoLine(0)
s.termPrintln("Touch and hold the stylus")
s.termPrintln("PRECISELY on each crosshair.")
s.termPrintln("")
s.termPrintln("Don't move the stylus until")
s.termPrintln("the crosshair moves to the")
s.termPrintln("next point.")
s.termPrintln("")
s.termPrintln("Press the GO button to continue.")
startKeyPressCount = psc.getKeyPressCount()
while psc.getKeyPressCount() == startKeyPressCount: time.sleep(0.1)



##########################
# Get calibration values #
##########################

def getPoints():
    x = []
    y = []
    for i in range(CALIBRATION_POINTS_COUNT):
        x.append(s.RAW_X())
        y.append(s.RAW_Y())
    x = sum(x)/len(x)
    y = sum(y)/len(y)
    return (x, y)

# x and y coordinates for center of crosshair, l is the length of lines, f is the fill color
def drawCrosshair(x, y, l, f):
    s.fillRect(x-l, y, l*2, 0, fill=f, display=False)
    s.fillRect(x, y-l, 0, l*2, fill=f)

def getCalibrationValues(x, y):
    LENGTH = 10
    FILL = (0,255,0)

    s.clearScreen()
    drawCrosshair(x, y, LENGTH, FILL)
    startKeyPressCount = psc.getKeyPressCount()
    while psc.getKeyPressCount() == startKeyPressCount: time.sleep(0.1)
    return getPoints()

p = INSET_PERCENT
rx4, ry4 = getCalibrationValues(320*(1-p), 240*p)     # top-right
rx1, ry1 = getCalibrationValues(320*p, 240*p)         # top-left
rx3, ry3 = getCalibrationValues(320*(1-p), 240*(1-p)) # bottom-right
rx2, ry2 = getCalibrationValues(320*p, 240*(1-p))     # bottom-left
rx5, ry5 = getCalibrationValues(320*0.5, 240*0.5)     # center
s.clearScreen()

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

oldBAS1type = psc.BAS1.getType()
psc.BAS1.setType(psc.BAS1.PS_SENSOR_TYPE_NONE)

# write to temporary memory
for offset, value in enumerate([x1,y1,x2,y2,x3,y3,x4,y4]):
    comm.writeInteger(psc.PS_TS_CALIBRATION_DATA + 0x02*offset, value)

comm.writeByte(psc.PS_Command, psc.E) # unlock permanent memory
comm.writeByte(psc.PS_Command, psc.w) # copy from temporary memory to permanent memory

timeout = time.time() + 1 # wait for up to a second
while comm.readByte(psc.PS_TS_CALIBRATION_DATA_READY) != 1 and time.time() < timeout: time.sleep(0.01) # wait for ready byte
# if it failed there is no need to show an error message here, it will already show below

# check if write succeeded
def calibrationEqual(offset, value):
    return comm.readInteger(psc.PS_TS_CALIBRATION_DATA + 0x02*offset) == int(value)

psc.BAS1.setType(oldBAS1type)

#for i in range(8): print comm.readInteger(psc.PS_TS_CALIBRATION_DATA + i*2)

if all([ calibrationEqual(offset, value) for offset, value in enumerate([x1,y1,x2,y2,x3,y3,x4,y4]) ]):
    print 'Successfully wrote calibration values to PiStorms'
    # write the calibration values to the cache file and recreate the mindsensorsUI object to load them
    json.dump(dict( (v,eval(v)) for v in ['x1','y1','x2','y2','x3','y3','x4','y4'] ), open('/tmp/ps_ts_cal', 'w'))
    s = mindsensorsUI("PiStorms", 3)
    res = s.askQuestion(['Success', 'Wrote calibration values', 'to PiStorms'], ['Paint', 'Exit'])
    if res == 0:
        config = ConfigParser.RawConfigParser() # modeled after parts of MSBrowser
        config.read('/usr/local/mindsensors/conf/msdev.cfg')
        os.system("sudo python " + os.path.join(config.get('msdev', 'homefolder'),"programs","60-Games","04-Paint.py"))
else:
    print 'Error writing calibration values to PiStorms'
    s.showMessage(['Error', 'Failed to write calibration values', 'to PiStorms'])

# note: MSBrowser will automatically restart
