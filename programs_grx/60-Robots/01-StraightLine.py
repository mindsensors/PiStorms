import time
from PiStorms_GRX import PiStorms_GRX, RCServo, GroveDigitalPort
from PiStormsCom_GRX import GRXCom

psm = PiStorms_GRX()

leftServo = RCServo("BAM1", 1690)
rightServo = RCServo("BBM1", 1300)

leftEncoder = GroveDigitalPort("BBD2", GRXCom.TYPE.ENCODER) # no mode, not associated with any servo
rightEncoder = GroveDigitalPort("BAD1", GRXCom.TYPE.ENCODER)

for bank in [GRXCom.I2C.A, GRXCom.I2C.B]: bank.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.RESET_ENCODERS)

for i in range(200):
    try:
        leftEncoderValue = -1*leftEncoder.comm.readEncoderValue()
        rightEncoderValue = rightEncoder.comm.readEncoderValue()

        print "{:6d} {:6d}".format(leftEncoderValue, rightEncoderValue)
        if leftEncoderValue < rightEncoderValue:
            leftServo.setSpeed(30)
            rightServo.setSpeed(50)
        else:
            leftServo.setSpeed(50)
            rightServo.setSpeed(30)
    except TypeError: pass # I2C fail

leftServo.stop()
rightServo.stop()

