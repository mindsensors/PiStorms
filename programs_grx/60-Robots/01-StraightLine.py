import time
from PiStorms_GRX import PiStorms_GRX, RCServo, GrovePort
from PiStormsCom_GRX import GRXCom

psm = PiStorms_GRX()

leftServo = RCServo("BBS1", 1690)
rightServo = RCServo("BAS1", 1350)

leftEncoder = GrovePort("BBD1", type=GRXCom.TYPE.ENCODER) # no mode, not associated with any servo
rightEncoder = GrovePort("BAD2", type=GRXCom.TYPE.ENCODER)

GRXCom.I2C.A.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.RESET_ENCODERS)
GRXCom.I2C.B.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.RESET_ENCODERS)

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
    except TypeError: pass # I2C failure

leftServo.stop()
rightServo.stop()
