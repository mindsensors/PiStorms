from PiStorms import PiStorms
psm = PiStorms()
import pygame
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
while not psm.isKeyPressed():
    pygame.event.pump()
    psm.BAM1.setSpeed(joystick.get_axis(1) * 100)
    psm.BAM2.setSpeed(joystick.get_axis(4) * 100)
