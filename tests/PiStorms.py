# PiStorms module

''' example usage

import PiStorms
PiStorms.draw.line(0, 0, 20, 20)
PiStorms.sensors[0].setType(PiStorms.Sensor.TYPE.touch)


'''

from mindsensors_i2c import mindsensors_i2c
import Adafruit_ILI9341 as TFT
import Adafruit_GPIO.SPI as SPI


BANK_A_I2C_ADDRESS = 0x34 >> 1
BANK_B_I2C_ADDRESS = 0x36 >> 1

# module-shared
#i2c = mindsensors_i2c(BANK_A)
bankA = mindsensors_i2c(BANK_A_I2C_ADDRESS)
bankB = mindsensors_i2c(BANK_B_I2C_ADDRESS)


#class 



class Screen():
    def __init__(self):
        #raise RuntimeError("You may not instantiate this class.")
        raise TypeError("PiStorms.Screen' class is not instantiatable")

    s = TFT.ILI9341(24, rst=25, spi=SPI.SpiDev(0,0,max_speed_hz=64000000))
    s.begin()

    d = s.draw()

    @staticmethod
    def rectangle(x1, y1, x2, y2):
        Screen.d.rectangle((x1, y1, x2, y2), fill=(255, 255, 255), outline=(0, 0, 0))
        Screen.s.display()

screen = Screen

