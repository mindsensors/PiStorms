import os,sys,inspect,time,thread,random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

from PiStorms import PiStorms
psm = PiStorms()

color = (255, 255, 255)

while True:
    if psm.isKeyPressed():
        break;

    if psm.isF1Pressed():
        color = (255, 0, 0)
    if psm.isF2Pressed():
        color = (255, 255, 0)
    if psm.isF3Pressed():
        color = (0, 255, 0)
    if psm.isF4Pressed():
        color = (0, 0, 255)

    if psm.screen.isTouched():
        x = psm.screen.TS_To_ImageCoords_X(psm.screen.x, psm.screen.y)
        y = psm.screen.TS_To_ImageCoords_Y(psm.screen.x, psm.screen.y)
        psm.screen.fillRect(x-1, y-1, 2, 2, fill=color)
