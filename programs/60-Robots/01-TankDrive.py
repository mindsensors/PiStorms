# SETUP PiStorms and joystick

from PiStorms import PiStorms
# initialize PiStorms object
psm = PiStorms()

m = ["Instructions",
     "Use the left and right joysticks",
     "to move the left and right motors.",
     "Press GO to Exit."]
psm.screen.showMessage(m)

import pygame
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

def mainLoop():
    # let Pygame update, check the joystick, etc.
    pygame.event.pump()
    # moves right motor foward and backwards with joystick value
    # the joystick returns -1 to 1, but the motor needs -100 to 100
    psm.BAM1.setSpeed(joystick.get_axis(1) * 100)
    # moves left motor foward and backwards with joystick value
    psm.BAM2.setSpeed(joystick.get_axis(4) * 100)

# keep checking the joysticks until you press GO
psm.untilKeyPress(mainLoop)
