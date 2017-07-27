from PiStorms_GRX import PiStorms_GRX
psm = PiStorms_GRX()

from PiStorms_GRX import RCServo
l = RCServo("BAS1", 1300)
r = RCServo("BAS2", 1690)

import pygame, sys
try:
    pygame.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except:
    psm.screen.showMessage("Please connect a joystick and try again.")
    sys.exit(0)

import time
while not psm.isKeyPressed() and not joystick.get_button(16):
    pygame.event.pump()
    l.setSpeed(joystick.get_axis(1)*-40)
    r.setSpeed(joystick.get_axis(3)*-100)
    time.sleep(0.05)

l.stop()
r.stop()
