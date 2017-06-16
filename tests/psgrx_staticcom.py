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
    SERVO   = [0x42+i*0x02 for i in range(3)]
    ANALOG  = [0x48+i*0x16 for i in range(3)]
    DIGITAL = [0x8A+i*0x16 for i in range(2)]

    @classmethod
    def setType(self, i2c, address, newType, mode=0):
        i2c.writeByte(address, newType)
        i2c.writeByte(address+1, mode)
    
    @classmethod
    def digitalRead(self, i2c, address):
        offset = 4
        return i2c.readByte(address + offset)

class GroveSensorDigital():
    def __init__(self, port):
        bank = port[1]
        try:
            self.i2c = self.comm.I2C[bank]
        except KeyError:
            raise ValueError("Invalid bank (must be A or B).")
        
        if port[2]=="A":
            sensorType = self.ANALOG
        elif port[2]=="D":
            sensorType = self.DIGITAL
        else:
            raise ValueError("Invalid port type (must be A for analog or D for digital).")
        
        number = int(port[3]) - 1
        # not catching an IndexError here because -1 should not be valid
        if number not in range(len(sensorType)):
            raise TypeError("Invalid port number (must be 1, 2, or 3 for analog; or 1 or 2 for digital).")
        
        self.addr = sensorType[number]
        
        self.setType(GRXCom.TYPE.DIGITAL_INPUT)
    def setType(self, newType):
        # TODO: validate
        GRXCom.setType(self.i2c, self.address, newType)
    def getButtonState(self):
        return self.comm.digitalRead()

