
from mindsensorsUI import mindsensorsUI
import sys

X =  int(sys.argv[1])
Y =  int(sys.argv[2])
W =  int(sys.argv[3])
H =  int(sys.argv[4])
IMAGE   =   str(sys.argv[5])


screen = mindsensorsUI("PiStorms",3)
screen.fillBmp(X, Y, W, H, path = IMAGE)
