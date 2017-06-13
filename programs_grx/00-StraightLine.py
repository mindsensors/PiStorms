import time
from PiStorms_GRX import PiStorms_GRX, RCServo, GroveDigitalPort
from PiStormsCom_GRX import GRXCom

psm = PiStorms_GRX()

leftServo = RCServo("BAM1", 1690)
rightServo = RCServo("BBM1", 1300)

leftEncoder = GroveDigitalPort("BBD2", GRXCom.TYPE.ENCODER) # no mode, not associated with any servo
rightEncoder = GroveDigitalPort("BAD1", GRXCom.TYPE.ENCODER)

GRXCom.I2C.A.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.RESET_ENCODERS)
GRXCom.I2C.B.writeByte(GRXCom.REGISTER.COMMAND, GRXCom.COMMAND.RESET_ENCODERS)
time.sleep(0.1)

def lEnc(): return -1*leftEncoder.comm.readEncoderValue()
def rEnc(): return rightEncoder.comm.readEncoderValue()

for i in range(20):
    try:
        print "{:6d} {:6d}".format(lEnc(), rEnc())
        if lEnc() < rEnc():
            leftServo.setSpeed(30)
            rightServo.setSpeed(50)
        else:
            leftServo.setSpeed(50)
            rightServo.setSpeed(30)
        time.sleep(0.1)
    except: pass

leftServo.stop()
rightServo.stop()

