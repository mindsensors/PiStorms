#!/usr/bin/env python
#
# Copyright (c) 2015 mindsensors.com
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
# Date            Author            Comments
# 01/30/14    Deepak            Initial authoring.
# 02/03/14    Michael           Error message, signed byte, and integer fix
# 03/09/14    Nitin             Changed the 16 and 32 bit read

## @package mindsensors_i2c
# This is the i2c module for mindsensors i2c devices.

import smbus
import ctypes

## mindsensors_i2c: this class provides i2c functions
#  for read and write operations.
class mindsensors_i2c(object):

    @staticmethod
    def pi_rev():
        try:
            with open('/proc/cpuinfo','r') as cpuinfo:
                for line in cpuinfo: 
                    if line.startswith('Hardware'):
                        #print " rstrip output  " +str(line.rstrip()[-4:])
                        cpu = 10 if line.rstrip()[-4:] in ['2709'] else 0
                       
                    if line.startswith('Revision'):
                        # case '3' is for some rare pi board - Deepak
                        #print " rstrip output  " +str(line.rstrip()[-4:])
                        rev =  0 if line.rstrip()[-4:] in [ '0001', '0002','0003'] else 1
                                        
                         
                #print "rev is ",rev        
                return rev        
                     
        except:
            return 0

    @staticmethod
    def which_bus():
        return 1 if mindsensors_i2c.pi_rev() >= 1 else 0

    ## Initialize the class with the i2c address of your device
    #  @param self The object pointer.
    #  @param i2c_address Address of your device.
    def __init__(self, i2c_address):
        self.address = i2c_address
        b = mindsensors_i2c.which_bus()
        self.bus = smbus.SMBus(b)
        
    ## Prints an error message if a read error is detected
    #  @param self The object pointer.
    def errMsg(self):
        print ("Error accessing 0x%02X: Check your I2C address" % self.address)
        return -1

    ## Write a byte to your i2c device at a given location
    #  @param self The object pointer.
    #  @param reg The register to write value at.
    #  @param value Value to write.
    def writeByte(self, reg, value):
        try:
            self.bus.write_byte_data(self.address, reg, value)
        except:
            pass
            
    ## Read an unsigned byte from your i2c device at a given location
    #  @param self The object pointer.
    #  @param reg The register to read from.
    def readByte(self, reg):
        try:
            result = self.bus.read_byte_data(self.address, reg)
            return (result)
        except:
            pass
            
    ## Read a signed byte from your i2c device at a given location
    #  @param self The object pointer.
    #  @param reg The register to read from.
    def readByteSigned(self, reg):
        a = self.readByte(reg)
        signed_a = ctypes.c_byte(a).value
        return signed_a
     
    # for read_i2c_block_data and write_i2c_block_data to work correctly,
    # ensure that i2c speed is set correctly on your pi:
    # ensure following file with contents as follows:
    #    /etc/modprobe.d/i2c.conf
    # options i2c_bcm2708 baudrate=50000
    # (without the first # and space on line above)
    #
    
    ## Read a byte array from your i2c device starting at a given location
    #  @param self The object pointer.
    #  @param reg The first register in the array to read from.
    #  @param length The length of the array.
    def readArray(self, reg, length):
        result = []
        try:
            while length > 0:
                result.append(self.readByte(reg))
                reg = reg+1
                length = length -1
            #results = self.bus.read_i2c_block_data(self.address, reg, length)
            return result
        except:
            pass

    ## Write a byte array from your i2c device starting at a given location
    #  @param self The object pointer.
    #  @param reg The first register in the array to write to.
    #  @param arr The array to write.
    def writeArray(self, reg, arr):
        try:
            self.bus.write_i2c_block_data(self.address, reg, arr)
        except:
            pass

    ## Read a string from your i2c device starting at a given location
    #  @param self The object pointer.
    #  @param reg The first register of the string to read from.
    #  @param length The length of the string.
    def readString(self, reg, length):
        ss = ''
        for x in range(0, length):
            ss = ''.join([ss, chr(self.readByte(reg+x))])
        return ss

    ## Read an unsigned 16 bit integer from your i2c device from a given location.  Big-endian read integers .
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to read.
    def readIntegerBE(self, reg):        
        results = self.readArray( reg, 2)
        return results[1] + (results[0]<<8)
        
    ## Read an unsigned 16 bit integer from your i2c device from a given location. little endian read integers.
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to read.
    def readInteger(self, reg):        
        results = self.readArray(reg, 2)
        return results[0] + (results[1]<<8)        

    ## Write an unsigned 16 bit integer from your i2c device from a given location. little endian write integers.
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to write.
    #  @param int The integer to write.
    def writeInteger(self, reg, i):        
        i = int(i)
        results = self.writeArray(reg, [i%256, (i>>8)%256])

    ## Read a signed 16 bit integer from your i2c device from a given location. Big endian read integers .
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to read.
    def readIntegerSignedBE(self, reg):
        a = self.readIntegerBE(reg)
        signed_a = ctypes.c_short(a).value
        return signed_a        
    
    ## Read a signed 16 bit integer from your i2c device from a given location. little endian read integers .
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to read.
    def readIntegerSigned(self, reg):
        a = self.readInteger(reg)
        signed_a = ctypes.c_short(a).value
        return signed_a

    ## Read an unsigned 32bit integer from your i2c device from a given location. Big endian read integers.
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to read.
    def readLongBE(self, reg):
        
        results = self.readArray(reg,4)
        return results[3] + (results[2]<<8)+(results[1]<<16)+(results[0]<<24)           
        
    ## Read an unsigned 32bit integer from your i2c device from a given location. little endian read integers.
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to read.
    def readLong(self, reg):
        results = self.readArray(reg,4)
        return results[0] + (results[1]<<8)+(results[2]<<16)+(results[3]<<24)       

    ## Read a signed 32bit integer from your i2c device from a given location. Big endian read integers .
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to read.
    def readLongSignedBE(self, reg):
        a = self.readLongBE(reg)
        signed_a = ctypes.c_long(a).value
        return signed_a      
          
    ## Read a signed 32bit integer from your i2c device from a given location. little endian read integers .
    #  @param self The object pointer.
    #  @param reg The first register of the first byte of the integer to read.
    def readLongSigned(self, reg):
        a = self.readLong(reg)
        signed_a = ctypes.c_long(a).value
        return signed_a

    ##  Read the firmware version of the i2c device
    #  @param self The object pointer.
    def GetFirmwareVersion(self):
        try:
            ver = self.readString(0x00, 8)
            return ver
        except:
            print ("Error: Could not retrieve Firmware Version" )
            print ("Check I2C address and device connection to resolve issue")
            return ""

    ##  Read the vendor name of the i2c device
    #  @param self The object pointer.
    def GetVendorName(self):
        try:
            vendor = self.readString(0x08, 8)
            return vendor
        except:
            print("Error: Could not retrieve Vendor Name")
            print ("Check I2C address and device connection to resolve issue")
            return ""
            
    ##  Read the i2c device id
    #  @param self The object pointer.
    def GetDeviceId(self):
        try:    
            device = self.readString(0x10, 8)
            return device
        except:
            print ("Error: Could not retrieve Device ID")
            print ("Check I2C address and device connection to resolve issue")
            return ""




