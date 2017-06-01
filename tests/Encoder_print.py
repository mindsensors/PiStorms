from __future__ import print_function
from PiStorms_GRX import PiStorms_GRX, RCServo
import struct

SD1_base = 0x8A
_TAC2X = 5

s = RCServo("BAM1", 1400)
i2c = s.bankA
i2c.writeArray(SD1_base, [_TAC2X, 1])

arr2int = lambda n: struct.unpack('l', ''.join(map(lambda b: struct.pack('B', b), n)))[0]

getenc = lambda: arr2int(i2c.readArray(SD1_base+4, 4))

def p(n):
    v = int(str(abs(n))[:2]) # most-significant two digits
    c = (31 if n<1 else 32) + (abs(n)>100)*60 # ANSI color code
    print(u"\r{num:5d}: \033[{color}m{bar}{blank}\033[0m".format(num=n, bar=unichr(0x2588)*v, blank=" "*(100-v), color=c), end="")

psm = PiStorms_GRX()
while not psm.isKeyPressed(): p(getenc())


