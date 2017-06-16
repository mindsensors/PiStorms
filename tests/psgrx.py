from mindsensors_i2c import mindsensors_i2c

class GRXCom():
    class I2C:
        A = mindsensors_i2c(0x34 >> 1)
        B = mindsensors_i2c(0x36 >> 1)
    class TYPE:
        NONE = 0
        ANALOG_INPUT = 1
        DIGITAL_OUTPUT = 2
        DIGITAL_INPUT = 3
        I2C = 4
        ENCODER = 5
        SERIAL = 6
#    class TYPE_SUPPORT:
#        ALL = [GRXCom.TYPE.NONE, GRXCom.TYPE.DIGITAL_OUTPUT, GRXCom.TYPE.DIGITAL_INPUT, GRXCom.TYPE.I2C]
#        ANALOG = ALL + [GRXCom.TYPE.ANALOG_INPUT]
#        DIGITAL = ALL + [GRXCom.TYPE.ENCODER]
#        # note: SERIAL is only supported on A1 and A2
    SERVO   = [0x42+i*0x02 for i in range(3)]
    ANALOG  = [0x48+i*0x16 for i in range(3)]
    DIGITAL = [0x8A+i*0x16 for i in range(2)]

    def __init__(self, i2c, address):
        self.i2c = i2c
        self.address = address

    def setType(self, newType, mode=0):
        self.i2c.writeByte(self.address, newType)
        self.i2c.writeByte(self.address+1, mode)

    def digitalRead(self):
        offset = 4
        return self.i2c.readByte(self.address + offset)

    def analogRead(self):
        offset = 4
        return self.i2c.readInteger(self.address + offset)
class TYPE_SUPPORT:
    ALL = [GRXCom.TYPE.NONE, GRXCom.TYPE.DIGITAL_OUTPUT, GRXCom.TYPE.DIGITAL_INPUT, GRXCom.TYPE.I2C]
    ANALOG = ALL + [GRXCom.TYPE.ANALOG_INPUT]
    DIGITAL = ALL + [GRXCom.TYPE.ENCODER]
    # note: SERIAL is only supported on A1 and A2
GRXCom.TYPE_SUPPORT = TYPE_SUPPORT
del TYPE_SUPPORT

class GroveDigitalPort():
    def __init__(self, port):
        bank = port[1]
        if bank == "A":
            i2c = GRXCom.I2C.A
        elif bank == "B":
            i2c = GRXCom.I2C.B
        else:
            raise ValueError("Invalid bank (must be A or B).")

        if port[2]=="A":
            addresses = GRXCom.ANALOG
        elif port[2]=="D":
            addresses = GRXCom.DIGITAL
        else:
            raise ValueError("Invalid port type (must be A for analog or D for digital).")

        number = int(port[3]) - 1
        # not catching an IndexError here because -1 should not be valid
        if number not in range(len(addresses)):
            raise ValueError("Invalid port number (must be 1, 2, or 3 for analog; or 1 or 2 for digital).")

        address = addresses[number]

        self.comm = GRXCom(i2c, address)

    def setType(self, newType, mode=0):
        if newType not in GRXCom.TYPE_SUPPORT.DIGITAL:
            raise TypeError("This port does not support that type.")
        self.comm.setType(newType, mode)

    def getButtonState(self):
        return self.comm.digitalRead()

class GroveAnalogPort(GroveDigitalPort):
    def __init__(self, port):
        super(GroveAnalogPort, self).__init__(port)

    def setType(self, newType, mode=0):
        if newType not in GRXCom.TYPE_SUPPORT.ANALOG:
            raise TypeError("This port does not support that type.")
        self.comm.setType(newType, mode)

    def getLightLevel(self):
        return self.comm.analogRead()
