#!/usr/bin/env python
#
# Copyright (c) 2014 OpenElectrons.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#

# History:
# Date       Author           Comments
# 07/26/14   Michael Giles   Initial authoring.
# 08/18/14   Michael Giles   Servo 
# 10/18/15   Nitin           PiStorm integration
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import PiStorms
import time,sys 

dict = {}
read_dict = {}
check_dict = {}   
                           
## rmap_PISTORMS: this class provides functions for PISTORMS integration with scratch
#  for read and write operations with scratch.
class rmap_PISTORMS(PiStorms.PiStorms):
    
    def __init__(self):
        PiStorms.PiStorms.__init__(self,"PiStorms") 
        self.screen.termPrintAt(0,"     Scratch Interface Program")        
       
    def process_read(self, cmd_string):
        if ( 'EV3LIGHT' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.reflectedLightSensorEV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.reflectedLightSensorEV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.reflectedLightSensorEV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.reflectedLightSensorEV3()
                #print cmd_string ,r
            #    check_dict[cmd_string] = r
                return r
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return "" 
        elif ( 'EV3AMBIENTLIGHT' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.ambientLightSensorEV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.ambientLightSensorEV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.ambientLightSensorEV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.ambientLightSensorEV3()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""    
        elif ( 'EV3COLOR' in cmd_string ):   
            #print cmd_string
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.colorSensorEV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.colorSensorEV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.colorSensorEV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.colorSensorEV3()
                #print cmd_string ,r
            #    check_dict[cmd_string] = r
                return r
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                 
        elif ( 'EV3TOUCHED' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.isTouchedEV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.isTouchedEV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.isTouchedEV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.isTouchedEV3()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                 
        elif ( 'EV3TOUCHES' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.numTouchesEV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.numTouchesEV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.numTouchesEV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.numTouchesEV3()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r  
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                 
        elif ( 'EV3IRDISTANCE' in cmd_string ):       
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.distanceIREV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.distanceIREV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.distanceIREV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.distanceIREV3()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r  
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                 
        elif ( 'EV3IRHEADING' in cmd_string ):     
            try:
                if ( 'BAS1' in cmd_string ):          
                    r = self.BAS1.headingIREV3(int(cmd_string[3]))
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.headingIREV3(int(cmd_string[3]))
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.headingIREV3(int(cmd_string[3]))
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.headingIREV3(int(cmd_string[3]))
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r 
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                 
        elif ( 'REMOTELEFT' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.remoteLeft(int(cmd_string[3]))
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.remoteLeft(int(cmd_string[3]))
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.remoteLeft(int(cmd_string[3]))
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.remoteLeft(int(cmd_string[3]))
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""     
        elif ( 'REMOTERIGHT' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.remoteRight(int(cmd_string[3]))
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.remoteRight(int(cmd_string[3]))
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.remoteRight(int(cmd_string[3]))
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.remoteRight(int(cmd_string[3]))
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""  
        elif ( 'EV3ULTRASONIC' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.distanceUSEV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.distanceUSEV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.distanceUSEV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.distanceUSEV3()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""    
        elif ( 'EV3GYROANGLE' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.gyroAngleEV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.gyroAngleEV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.gyroAngleEV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.gyroAngleEV3()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""    
        elif ( 'EV3GYRORATE' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.gyroRateEV3()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.gyroRateEV3()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.gyroRateEV3()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.gyroRateEV3()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""         
        elif ( 'NXTLIGHT' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.lightSensorNXT(True)
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.lightSensorNXT(True)
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.lightSensorNXT(True)
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.lightSensorNXT(True)
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return "" 
        elif ( 'NXTAMBIENTLIGHT' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.lightSensorNXT(False)
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.lightSensorNXT(False)
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.lightSensorNXT(False)
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.lightSensorNXT(False)
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                 
        elif ( 'NXTCOLOR' in cmd_string ):                
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.colorSensorNXT()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.colorSensorNXT()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.colorSensorNXT()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.colorSensorNXT()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""  
        elif ( 'NXTTOUCHED' in cmd_string ): 
            #print         cmd_string
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.isTouchedNXT()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.isTouchedNXT()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.isTouchedNXT()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.isTouchedNXT()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                 
        elif ( 'NXTTOUCHES' in cmd_string ):   
            #print         cmd_string
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.numTouchesNXT()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.numTouchesNXT()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.numTouchesNXT()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.numTouchesNXT()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r  
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""  

        elif ( 'SUMOEYES' in cmd_string ):                
            try:
                if ('SHORT' in cmd_string ):
                    range = False
                else:
                    range = True
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.SumoEyes(range)
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.SumoEyes(range)
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.SumoEyes(range)
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.SumoEyes(range)
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                    
        elif ( 'ANALOG' in cmd_string ):
            #print cmd_string     
            try:
                if ( 'BAS1' in cmd_string ): 
                    r = self.BAS1.analogSensor()
                elif ( 'BAS2' in cmd_string ): 
                    r = self.BAS2.analogSensor()
                elif ( 'BBS1' in cmd_string ): 
                    r = self.BBS1.analogSensor()
                elif ( 'BBS2' in cmd_string ): 
                    r = self.BBS2.analogSensor()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""       
        elif ( 'ENCODER' in cmd_string ):                
            #print cmd_string
            try:
                if ( 'BAM1' in cmd_string ): 
                    r = self.BAM1.pos()
                elif ( 'BAM2' in cmd_string ): 
                    r = self.BAM2.pos()
                elif ( 'BAM3' in cmd_string ): 
                    r = self.BBM2.pos()
                elif ( 'BAM4' in cmd_string ): 
                    r = self.BBM2.pos()
                #print cmd_string ,r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                  
        elif ( 'BATTVOLT' in cmd_string ):                
            try:
                r = self.battVoltage()
                #print r
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""   
        elif ( 'GOBUTTON' in cmd_string ):
            if 'COUNT' in cmd_string :
                try:
                    r = self.getKeyPressCount() 
                    check_dict[cmd_string] = r
                    return r   
                except:
                    rmap_print("Could not read PiStorms")
                    #rmap_print("Check I2C address and device connection to resolve issue")
                return ""
            else:    
                try:
                    r = self.isKeyPressed() 
                    check_dict[cmd_string] = r
                    return r   
                except:
                    rmap_print("Could not read PiStorms")
                    #rmap_print("Check I2C address and device connection to resolve issue")
                    return "" 
        elif ( 'TOUCHX' in cmd_string ):
            #print cmd_string        
            try:
                r = self.screen.TS_X() #isKeyPressed()
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""
        elif ( 'TOUCHY' in cmd_string ):
            #print cmd_string        
            try:
                r = self.screen.TS_Y() #isKeyPressed()
                check_dict[cmd_string] = r
                return r   
            except:
                rmap_print("Could not read PiStorms")
                #rmap_print("Check I2C address and device connection to resolve issue")
                return ""                 

    def run_command(self, cmd_string, message):
        #print cmd_string, message
        if ( 'ON' in cmd_string ): 
            if len(cmd_string) > 3:
                speed = int(cmd_string[3])
                if speed > 100:
                    speed = 100
                if speed < -100:
                    speed = -100   
            else:
                speed = 100        
            if ( 'BAM1' in cmd_string ): 
                #print "self.BAM1.setSpeed(speed)", speed
                self.BAM1.setSpeed(speed)
            if ( 'BAM2' in cmd_string ): 
                self.BAM2.setSpeed(speed)
            if ( 'BBM1' in cmd_string ): 
                self.BBM1.setSpeed(speed)
            if ( 'BBM4' in cmd_string ): 
                self.BBM2.setSpeed(speed)
                
        elif ( 'OFF' in cmd_string ): 
            speed = 0       
            if ( 'BAM1' in cmd_string ): 
                self.BAM1.setSpeed(speed)
            if ( 'BAM2' in cmd_string ): 
                self.BAM2.setSpeed(speed)
            if ( 'BBM1' in cmd_string ): 
                self.BBM1.setSpeed(speed)
            if ( 'BBM2' in cmd_string ): 
                self.BBM2.setSpeed(speed)  
                
        elif ( 'BRAKE' in cmd_string ): 
            if ( 'BAM1' in cmd_string ): 
                self.BAM1.brake()
            if ( 'BAM2' in cmd_string ): 
                self.BAM2.brake()
            if ( 'BBM1' in cmd_string ): 
                self.BBM1.brake()
            if ( 'BBM2' in cmd_string ): 
                self.BBM2.brake()  
                
        elif ( 'FLOAT' in cmd_string ): 
            if ( 'BAM1' in cmd_string ): 
                self.BAM1.float()
            if ( 'BAM2' in cmd_string ): 
                self.BAM2.float()
            if ( 'BBM1' in cmd_string ): 
                self.BBM1.float()
            if ( 'BBM2' in cmd_string ): 
                self.BBM2.float()                 
        elif ( 'RUNSEC' in cmd_string ): 
            if len(cmd_string) > 4:
                speed = int(cmd_string[4])
                if speed > 100:
                    speed = 100
                if speed < -100:
                    speed = -100
                runtime = int(cmd_string[3])
                if runtime > 100:
                    runtime = 100
            else:
                runtime = 1     
            if ( 'BAM1' in cmd_string ): 
                self.BAM1.runSecs(runtime,speed,True)
            if ( 'BAM2' in cmd_string ): 
                self.BAM2.runSecs(runtime,speed,True)
            if ( 'BBM1' in cmd_string ): 
                self.BBM1.runSecs(runtime,speed,True)
            if ( 'BBM2' in cmd_string ): 
                self.BBM2.runSecs(runtime,speed,True)
        elif ( 'RUNDEG' in cmd_string ): 
            #print cmd_string
            if len(cmd_string) > 4:
                speed = int(cmd_string[4])
                if speed > 100:
                    speed = 100
                if speed < -100:
                    speed = -100
                deg = int(cmd_string[3])
                if deg > 10000:
                    deg = 10000
                if deg < -10000:
                    deg = -10000     
               
            else:
                deg = 360
                speed = 100        
            #print  speed,deg       
            if ( 'BAM1' in cmd_string ): 
                self.BAM1.runDegs(deg,speed,True,False)
            if ( 'BAM2' in cmd_string ): 
                self.BAM2.runDegs(deg,speed,True,False)
            if ( 'BBM1' in cmd_string ): 
                self.BBM1.runDegs(deg,speed,True,False)
            if ( 'BBM2' in cmd_string ): 
                self.BBM2.runDegs(deg,speed,True,False)
        elif ( 'PRINT' in cmd_string ): 
            #print cmd_string
            if len(cmd_string) > 2:
                line = int(cmd_string[2])
                #print message[2:-2]
                self.screen.termPrintAt(line,message)
        elif ( 'EXIT' in cmd_string ): 
            #print cmd_string
            quit(0)   
        else :
            return False
        return True    
           
                 
def device_cr(class_name, variable_name, address = 0):
    if (class_name == "PILIGHT") :
        return rmap_PILIGHT(0x30) #int(address, base=16)
    if (class_name == "SERVO") :
        if (address == '0'):
            return rmap_SERVO()   
    if (class_name == "PISTORMS") :
        return rmap_PISTORMS() #int(address, base=16)
        
def save_read_data(command_string):
    x = 0
    max = len(command_string) + 1 
    read_dict[command_string[1]] = []
    for cmd in command_string:
        if x > 1:
            read_dict[command_string[1]].append(command_string[x])
        if x < max:
            x = x + 1
            
def rmap_print(message):
    print str(time.strftime("%d/%m/%Y-"))+str(time.strftime("%H:%M:%S"))+":"+message
    sys.stdout.flush()

def print_dict():
    print dict
    
