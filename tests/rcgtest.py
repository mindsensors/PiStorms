
#from PiStorms import PiStorms
#import rcg
from rcg import *
import time
import numpy
from GroveDevices import *

print "running program"
psm = RCG()
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
    

def testDigitalButtonDirectControl():
    set_type()
    counter = 0
    while (True):
    #list = i2c.mem_read(6,Device_ADDRESS, SA1_base +port*22)
    #if list[0] == 1 : return(list[4] +list[5]*256) 
    #else: return 0
        counter = counter + 1
        print ""
        print counter, " button register: "
        addr = 0x42
        while (addr < 0x56):
            x = psm.psc.bankA.readByte(0x48)
            print "", x,
            addr = addr + 1
        time.sleep(1)

def button_test_dc():
    # set type
    port = 0
    addr = RCGCom.RCG_SA1_Base+(port*22)
    psm.psc.bankA.writeByte(addr, _DI)
    psm.psc.bankA.writeByte(addr+1, 0)
    
    while (True):
        x = psm.psc.bankA.readByte(addr+4)
        print "button_test_dc:", x
        time.sleep(1)



def button_test():
    btn = Grove_Button("BBD2")
    while (True):
        print "isPressed:", btn.isPressed()
        time.sleep(1)

def luminance_test():
    # FIXME: WARNING: when using analog sensor, there appears to
    # be noise on adjacent port if nothing is connected physically.
    sen = Grove_Luminance_Sensor("BBA1")
    while (True):
        print "luminance:", sen.readValue()
        time.sleep(1)

def dual_sensor_test():
    sen = Grove_Moisture_Sensor("BBA1")
    sen2 = Grove_Light_Sensor("BBA2")
    while (True):
        print "sen1:", sen.readValue(), "sen2:", sen2.readValue()
        time.sleep(1)

def test_sunlight_sensor_direct_read():
    sl = Grove_Sunlight_Sensor()
    while (True):
        print "visible:", \
        sl.readInteger(sl.SI114X_ALS_VIS_DATA0), \
        "IR:", \
        sl.readInteger(sl.SI114X_ALS_IR_DATA0), \
        "UV:", \
        sl.readInteger(sl.SI114X_AUX_DATA0_UVINDEX0)
        
        time.sleep(1)

def test_sunlight_sensor():
    sl = Grove_Sunlight_Sensor()
    while (True):
        print "visible:", sl.readVisible()
        print "IR:", sl.readIR()
        print "UV:", sl.readUV()
        time.sleep(1)

def PIR_test():
    pir = Grove_PIR_Sensor("BBD2")
    while (True):
        print "People present:", pir.peoplePresent()
        time.sleep(1)

PIR_test()
