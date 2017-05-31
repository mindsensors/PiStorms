SA1_base = 0x48
SD1_base = 0x8A
D1 = 3
_TAC2X = 5

from PiStorms_GRX import RCServo
s = RCServo("BAM1", 1400)
i2c = s.bankA
# Set_type
i2c.writeArray(SA1_base+D1*22, [_TAC2X, 1])
# set_Target
i2c.writeArray(SA1_base+8+D1*22, [180, 0, 0, 0])
# read_TACH1
i2c.readArray(SD1_base+4, 4)

import ctypes
ctypes.c_int(sum([b<<(n*8) for n,b in enumerate(i2c.readArray(SD1_base+4, 4))])).value

# or, across multiple lines
v = i2c.readArray(SD1_base+4, 4)
v = sum([b<<(n*8) for n,b in enumerate(v)])
v = ctypes.c_int(v).value

import struct
#int2arr = lambda n: [struct.unpack('B', struct.pack('l', n)[i])[0] for i in range(4)]
int2arr = lambda n: map(lambda b: struct.unpack('B', b)[0], struct.pack('l', n))
arr2int = lambda n: struct.unpack('l', ''.join(map(lambda b: struct.pack('B', b), n)))[0]

import time
while True: time.sleep(0.2); arr2int(i2c.readArray(SD1_base+4, 4))

# BAM1, BAD1
i2c.writeArray(SA1_base+D1*22, [_TAC2X, 1])
i2c.writeArray(SA1_base+8+D1*22, [180, 0, 0, 0])
i2c.readArray(SD1_base+4, 4)

# BAM1, BAD2
i2c.writeArray(SA2_base+D1*22, [_TAC2X, 1])
i2c.writeArray(SA2_base+8+D1*22, [180, 0, 0, 0])
i2c.readArray(SD2_base+4, 4)

# BAM2, BAD1
i2c.writeArray(SA1_base+D1*22, [_TAC2X, 2])
i2c.writeArray(SA1_base+8+D1*22, [180, 0, 0, 0])
i2c.readArray(SD1_base+4, 4)

# BAM2, BAD2
i2c.writeArray(SA2_base+D1*22, [_TAC2X, 2])
i2c.writeArray(SA2_base+8+D1*22, [180, 0, 0, 0])
i2c.readArray(SD2_base+4, 4)

