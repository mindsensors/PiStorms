
#from PiStorms import PiStorms
#import PiStorms_GRX
from PiStorms_GRX import *
import time
import numpy
from GroveDevices import *

print "running program"
psm = PiStorms_GRX()
print "Device : "+ str(psm.GetDeviceId() )
print "Vendor : "+ str(psm.GetVendorName() )
print "Firmware : "+ str(psm.GetFirmwareVersion() )
print "Features : "+ str(psm.psc.GetDeviceFeatures())

_NONE = 0
_ANIN = 1
_DO  = 2
_DI  = 3
_I2C = 4
_TAC2X = 5
_SERIAL = 6



# test function to print battery voltage
def printBattVoltage():
    while (True):
        s = psm.battVoltage()
        print s
        time.sleep (1)


# test function to run servo motor
def runServo1(num):
    #servo1 = RCServo(psm.psc.bankB, num)
    servo1 = psm.BBM3
    x = 1500
    while (True):
        while x < 2500:
            print "running servo to>: ",str(x)," ",split_int(x)
            servo1.setPos(int(x))
            x += 50
            time.sleep (1)
        while x > 500:
            print "running servo to<: ",str(x)," ",split_int(x)
            servo1.setPos(int(x))
            time.sleep(1)
            x -= 50

# test function to blink leds
def blinkLED():
    while (True):
        print "blinking LEDs"
        psm.psc.led(1, 100,100,100)
        psm.psc.led(2, 0,0,0)
        time.sleep(1)
        psm.psc.led(2, 100,100,100)
        psm.psc.led(1, 0,0,0)
        time.sleep(1)


def split_int(a):
    b = [0,1]
    b[0] = int(numpy.ubyte(a))
    b[1] = int(numpy.ubyte(a>>8))
    return b

def testServoDirectControl():
    while (True):
        print "running servo (and blinking led)"
        colors = [100, 100, 40]
        psm.psc.bankA.writeArray(0xb6, colors)
        time.sleep(0.1)
        a = split_int(500)
        print a
        #a = [232,3]
        #psm.psc.bankA.writeArray(0x42, a)
        psm.psc.bankA.writeByte(0x44, a[0])
        psm.psc.bankA.writeByte(0x45, a[1])
        time.sleep(2)

        colors = [70, 10, 90]
        psm.psc.bankA.writeArray(0xb6, colors)
        time.sleep(0.1)

        a = split_int(2500)
        print a
        #a = [208,7]
        #psm.psc.bankA.writeArray(0x42, a)
        psm.psc.bankA.writeByte(0x44, a[0])
        psm.psc.bankA.writeByte(0x45, a[1])
        time.sleep(2)


def testGoButton():
    while (True):
        print "button: " , psm.isKeyPressed(), " press count: ", psm.getKeyPressCount()
        time.sleep(1)


def set_type():
        addr = 0x48
        psm.psc.bankA.writeByte(addr, _ANIN)
        psm.psc.bankA.writeByte(addr+1, 0)
    


x = 1500
old_x = x
servo1 = psm.BBM1
while (True):
    x = raw_input("enter ms value:")
    if ( x != old_x):
        print "value changed"
        old_x = x
        servo1.setPos(int(x))
