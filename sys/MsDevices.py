
from mindsensors_i2c import mindsensors_i2c

## AbsoluteIMU: this class provides PiStorms specific interface for all 
# models of the AbsoluteIMU from mindsensors.com
#  for detailed member functions for this class, please refer to mindsensors.ABSIMU
class AbsoluteIMU(mindsensors_i2c):

    ## Default ABSIMU I2C Address 
    ABSIMU_ADDRESS = (0x22)
    ## Command Register 
    COMMAND = 0x41
    ## X-Axis Tilt Register. Will return a signed integer reading
    TILT_X = 0x42
    ## Y-Axis Tilt Register. Will return a signed integer reading
    TILT_Y = 0x43
    ## Z-Axis Tilt Register. Will return a signed integer reading
    TILT_Z = 0x44
    ## X-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050) 
    ACCEL_X = 0x45
    ## Y-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050)
    ACCEL_Y = 0x47
    ## Z-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050)
    ACCEL_Z = 0x49
    ## Compass Heading Register. Will return an unsigned integer reading (0 - 360)
    CMPS = 0x4B
    ## X-Axis Magnetometer Register. Will return a signed integer reading 
    MAG_X = 0x4D
    ## Y-Axis Magnetometer Register. Will return a signed integer reading 
    MAG_Y = 0x4F
    ## Z-Axis Magnetometer Register. Will return a signed integer reading 
    MAG_Z = 0x51
    ## X-Axis Gyroscope Register. Will return a signed integer reading 
    GYRO_X = 0x53
    ## Y-Axis Gyroscope Register. Will return a signed integer reading 
    GYRO_Y = 0x55
    ## Z-Axis Gyroscope Register. Will return a signed integer reading 
    GYRO_Z = 0x57
    
    ## Initialize the class with the i2c address of your AbsoluteIMU
    #  @param self The object pointer.
    #  @param i2c_address Address of your AbsoluteIMU.
    #  @remark
    def __init__(self, port, address=ABSIMU_ADDRESS):
        port.activateCustomSensorI2C()
        mindsensors_i2c.__init__(self, address >> 1)        

    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, command):
        self.writeByte(COMMAND, int(command)) 
    
    ## Reads the tilt value along the x-axis
    #  @param self The object pointer.
    def get_tiltx(self):
        try:
            return self.readByteSigned(self.TILT_X)
        except:
            print "Error: Could not read tilt along x-axis"
            return ""
      
    ## Reads the tilt value along the y-axis
    #  @param self The object pointer.
    def get_tilty(self):
        try:
            return self.readByteSigned(self.TILT_Y)
        except:
            print "Error: Could not read tilt along y-axis"
            return ""
            
    ## Reads the tilt value along the z-axis
    #  @param self The object pointer.
    def get_tiltz(self):
        try:
            return self.readByteSigned(self.TILT_Z)
        except:
            print "Error: Could not read tilt along z-axis"
            return ""
            
    ## Reads the tilt values 
    #  @param self The object pointer.
    def get_tiltall(self):
        try:
            res = [(self.get_tiltx(),
                    self.get_tilty(),
                    self.get_tiltz())]
            return res
        except:
            print "Error: Could not read tilt values"
            return ""
            
    ## Reads acceleromter value along the x-axis
    #  @param self The object pointer.
    def get_accelx(self):
        try:
            return self.readIntegerSigned(self.ACCEL_X)
        except:
            print "Error: Could not read accelerometer value along x-axis"
            return ""
            
    ## Reads acceleromter value along the y-axis
    #  @param self The object pointer.
    def get_accely(self):
        try:
            return self.readIntegerSigned(self.ACCEL_Y)
        except:
            print "Error: Could not read accelerometer value along y-axis"
            return ""
            
    ## Reads acceleromter value along the z-axis
    #  @param self The object pointer.
    def get_accelz(self):
        try:
            return self.readIntegerSigned(self.ACCEL_Z)
        except:
            print "Error: Could not read accelerometer value along z-axis"
            return ""
            
    ## Reads the accelerometer values 
    #  @param self The object pointer.
    def get_accelall(self):
        try:
            res = [(self.get_accelx(),
                    self.get_accely(),
                    self.get_accelz())]
            return res
        except:
            print "Error: Could not read accelerometer values"
            return ""
            
    ## Reads compass heading
    #  @param self The object pointer.
    def get_heading(self):
        try:
            head = self.readInteger(self.CMPS)
            while(head > 360 or head < 0):
                head = self.readInteger(self.CMPS)
            return head
        except:
            print "Error: Could not read compass heading"
            return ""
    
    ## Reads magnetometer value along the x-axis
    #  @param self The object pointer.
    def get_magx(self):
        try:
            return self.readIntegerSigned(self.MAG_X)
        except:
            print "Error: Could not read magnetometer value along x-axis"
            return ""
            
    ## Reads magnetometer value along the y-axis
    #  @param self The object pointer.
    def get_magy(self):
        try:
            return self.readIntegerSigned(self.MAG_Y)
        except:
            print "Error: Could not read magnetometer value along y-axis"
            return ""
            
    ## Reads magnetometer value along the z-axis
    #  @param self The object pointer.
    def get_magz(self):
        try:
            return self.readIntegerSigned(self.MAG_Z)
        except:
            print "Error: Could not read magnetometer value along z-axis"
            return ""
            
    ## Reads the magnetometer values 
    #  @param self The object pointer.
    def get_magall(self):
        try:
            res = [(self.get_magx(),
                    self.get_magy(),
                    self.get_magz())]
            return res
        except:
            print "Error: Could not read magnetometer values"
            return ""
            
    ## Reads gyroscope value along the x-axis
    #  @param self The object pointer.
    def get_gyrox(self):
        try:
            return self.readIntegerSigned(self.GYRO_X)
        except:
            print "Error: Could not read gyroscope value along x-axis"
            return ""
            
    ## Reads gyroscope value along the y-axis
    #  @param self The object pointer.
    def get_gyroy(self):
        try:
            return self.readIntegerSigned(self.GYRO_Y)
        except:
            print "Error: Could not read gyroscope value along y-axis"
            return ""
            
    ## Reads gyroscope value along the z-axis
    #  @param self The object pointer.
    def get_gyroz(self):
        try:
            return self.readIntegerSigned(self.GYRO_Z)
        except:
            print "Error: Could not read gyroscope value along z-axis"
            return ""
            
    ## Reads the tilt values 
    #  @param self The object pointer.
    def get_gyroall(self):
        try:
            res = [(self.get_gyrox(),
                    self.get_gyroy(),
                    self.get_gyroz())]
            return res
        except:
            print "Error: Could not read gyroscope values"
            return ""
            
    ## Starts the compass calibration process
    #  @param self The object pointer.
    def start_cmpscal(self):
        try:
            self.command(67)
        except:
            print "Error: Could not start compass calibration process"
            return ""    

    ## Stops the compass calibration process
    #  @param self The object pointer.
    def stop_cmpscal(self):
        try:
            self.command(99)
        except:
            print "Error: Could not stop compass calibration process"
            return ""   
    
    ## Sets accelerometer sensitivity to 2G
    #  @param self The object pointer.
    def accel_2G(self):
        try:
            self.command(49)
        except:
            print "Error: Could not change accelerometer sensitivity"
            return ""   

    ## Sets accelerometer sensitivity to 4G
    #  @param self The object pointer.
    def accel_4G(self):
        try:
            self.command(50)
        except:
            print "Error: Could not change accelerometer sensitivity"
            return ""   

    ## Sets accelerometer sensitivity to 8G
    #  @param self The object pointer.
    def accel_8G(self):
        try:
            self.command(51)
        except:
            print "Error: Could not change accelerometer sensitivity"
            return "" 

    ## Sets accelerometer sensitivity to 16G
    #  @param self The object pointer.
    def accel_16G(self):
        try:
            self.command(52)
        except:
            print "Error: Could not change accelerometer sensitivity"
            return ""  



"""
AbsoluteIMU -> ABSIMU
AngleSensor  -> ANGLE
DISTNx -> DIST
LightSensorArray  -> LSA
LineLeader -> LINELEADER
NXTMMX -> MMX
NXTServo -> NXTSERVO
PFMate -> PFMATE
CurrentMeter  -> CURRENT
VoltMeter -> VOLT
PressureSensor -> PPS58
NXTCam -> NXTCAM
PSPNx -> needs implementation
EV3SensorMux -> EV3SensAdapt (3 channels -> change i2c address based on channel).
IRThermometer -> needs implementation in mindsensors.py
EV3SensorAdapter -> EV3SensAdapt 
SumoEyes (is an analog device - needs different implementation).

"""
