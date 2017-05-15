# main.py -- put your code here!

import smbus
import time
import ctypes
import numpy
A1 = 0
A2 = 1
A3 = 2
D1 = 3
D2 = 4
NONE = 0
S1 = 1
S2 = 2
S3 = 3

_NONE = 0
_ANIN = 1
_DO = 2
_DI = 3
_I2C = 4
_TAC2X = 5
_SERIAL = 6

HIGH = 1
LOW = 0

Device_ADDRESS = (0x36 >> 1)

Device_WHO_AM_I = 0x10
Device_VERSION = 0x00
Device_VENDOR = 0x08
Device_FEATURES = 0x18
Servo_Base = 0x42
Led_Base = 0xB6
SA1_base = 0x48
SA2_base = 0x5E
SA3_base = 0x74
SD1_base = 0x8A
SD2_base = 0xA0
KEY1_count = 0xBA

Control_reg = 0x41

#I2C(1, I2C.MASTER, baudrate=30000).deinit()
#pyb.delay(200)
#i2c = I2C(1, I2C.MASTER, baudrate=30000)

# compatibility class
class I2C(object):
    def __init__(self):
        self.bus = smbus.SMBus(1)

    def mem_read(self, size, addr, reg, timeout=1000):
        #result = self.bus.read_byte_data(addr, reg)
        ss = ''
        for x in range(0, size):
            ss = ''.join([ss, chr(self.bus.read_byte_data(addr,reg+x))])
        return ss

    def mem_write(self, dataArray, addr, reg, timeout=1000):
        for i,x in enumerate(dataArray):
            self.bus.write_byte_data(addr, reg+i, x)

i2c = I2C()


def read_who_am_I():
    # read the Device WHO_AM_I
    list = i2c.mem_read(8, Device_ADDRESS, Device_WHO_AM_I, timeout=1000)
    print(list.decode("utf-8"))

def read_features():
    # read  the Device WHO_AM_I
    list = i2c.mem_read(8, Device_ADDRESS, Device_FEATURES, timeout=1000)
    print(list.decode("utf-8"))

def read_vendor():
    # read the Device vendor
    name = ""
    list = i2c.mem_read(8, Device_ADDRESS, Device_VENDOR, timeout=1000)
    print(list.decode("utf-8"))

def read_version():
    # read the Device version
    list = i2c.mem_read(5, Device_ADDRESS, Device_VERSION, timeout=1000)
    print(list.decode("utf-8"))

def read_info():
    # read the Device info
    list = i2c.mem_read(32, Device_ADDRESS, Device_VERSION, timeout=1000)
    print(list.decode("utf-8"))

def set_RGB(w, R,G,B):
    data = bytearray(3)
    data[0] = R
    data[1] = G
    data[2] = B
    #print(data)
    #i2c.mem_write(data, Device_ADDRESS, Led_Base, timeout=1000)
    if (w == 2):
        addr = Device_ADDRESS
    else:
        addr = (0x34>>1)
    i2c.mem_write(data, addr, Led_Base, timeout=1000)

def send_Command(cmd):
    data = bytearray(1)
    data[0] = cmd
    #print(data)
    i2c.mem_write(data, Device_ADDRESS, Control_reg, timeout=1000)

def set_Servo(device, value):
    if device==0: return
    device = device -1
    data = bytearray(2)
    data[1] = numpy.ubyte(value/256)
    data[0] = numpy.ubyte(value)
    i2c.mem_write(data, Device_ADDRESS, Servo_Base+2*int(device), timeout=1000)

def read_SD1():
    # read the SD1
    if int(i2c.mem_read(1, Device_ADDRESS, SD1_base+3)[0]) == 0:
        list = i2c.mem_read(14, Device_ADDRESS, SD1_base+4)
        return(list)

def read_TACH1():
    # read  the Tach1
    results = i2c.mem_read(4,Device_ADDRESS, SD1_base+4)
    val = results[0] + (results[1]<<8) + (results[2]<<16) + (results[3]<<24)
    if val > 2147483647: val -= 4294967296
    return val

def read_TACH2():
    # read the Tach2
    results = i2c.mem_read(4, Device_ADDRESS, SD2_base+4)
    val = results[0] + (results[1]<<8) + (results[2]<<16) + (results[3]<<24)
    if val > 2147483647: val -= 4294967296
    return val

def read_Key1Count():
    # read the Key1Count
    list = i2c.mem_read(1, Device_ADDRESS, KEY1_count)
    return(list[0])

def read_digital(port):
    # read the SA2_analog
    list = i2c.mem_read(5, Device_ADDRESS, SA1_base+port*22+4)
    return list[0]
    #if list[0] == 1 : return(list[4] + list[5]*256)
    #else: return 0

def Set_pin(port, mode):
    # read the SA2_mode
    data = bytearray(1)
    data[0] = int(mode)
    i2c.mem_write(data, Device_ADDRESS, SA1_base+4+port*22, timeout=1000)

def read_analog(port):
    # read the SA2_analog
    list = i2c.mem_read(6, Device_ADDRESS, SA1_base+port*22)
    print "Port:", port, "=", ":".join("{:02x}".format(ord(c)) for c in list)
    return int(numpy.ubyte(list[4]) + numpy.ubyte(list[5])*256)
    if (list[0] != 0x01):
        print "list0->1"
        return (list[4]) + (list[5])*256
    else:
        return 0
'''
def Set_type(port, type):
    # set port type
    data = bytearray(1)
    data[0] = int(type)
    i2c.mem_write(data, Device_ADDRESS, SA1_base+2+port*22, timeout=1000)
'''
def set_Target(port ,value):
    #if device==0: return
    #device -= 1
    data = bytearray(4)
    data[3] = int(value>>24)
    data[2] = int(value>>16)
    data[1] = int(value>>8)
    data[0] = int(value)
    i2c.mem_write(data, Device_ADDRESS, SA1_base+8+port*22, timeout=1000)

def Set_type(port, type, mode = 0):
    # set port_mode
    data = bytearray(2)
    data[0] = int(type)
    data[1] = int(mode)
    print(SA1_base+port*22)
    i2c.mem_write(data, Device_ADDRESS, SA1_base+port*22, timeout=1000)


if __name__ == "__main__":

    print(i2c.mem_read(8, Device_ADDRESS, Device_VENDOR))
    print(i2c.mem_read(8, Device_ADDRESS, Device_WHO_AM_I))
    print(i2c.mem_read(8, Device_ADDRESS, Device_VERSION))

    print ""

    #set_RGB(1, 75, 75, 75)
    #set_Servo(1 ,1000)

    #analog input testing
    #print("#analog input testing")
    Set_type(A2, _ANIN)
    Set_type(A3, _ANIN)
    Set_type(A1, _ANIN)

    while True:
        time.sleep(1)
        print("A1 = ", read_analog(A1), "A2 = ", read_analog(A2), "A3 = ",read_analog(A3))

    #Digital input testing
    #Set_type(A2, _ANIN)
    #Set_type(A3, _ANIN)
    #Set_type(A1, _ANIN)
    #Set_type(D2, _DI)
    #Set_type(D1, _DI)
    #
    #while True:
    #    time.sleep(1)
    #    print("A1 = ", read_digital(A1), "A2 = ", read_digital(A2), "A3 = ", read_digital(A3),
    #          "D1 = ", read_digital(D1), "D2 = ", read_digital(D2))
