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
import sys,rmap,threading,time,math,socket,scratch,subprocess,datetime
import rmapcfg
from PiStorms import PiStorms

debug = False
device_dict = rmap.dict
read_dict = rmap.read_dict
command_array = []
command_array1 = []
string_message = ""
psm = PiStorms()
lasttime = int(round(time.time() * 1000))
# Connect to Scratch
try:
    s = scratch.Scratch(host=rmapcfg.host, port=rmapcfg.port)
    if s.connected:
        rmap.rmap_print("Connected")
except scratch.ScratchError:
    rmap.rmap_print("Scratch is either not opened or remote sensor connections aren't enabled")

# Broadcast 'READY' to Scratch
try:
    s.broadcast('READY')
    time.sleep(.5)
except NameError:
    #pass
    print "Did not send Ready"

doExit = False
# Handles messages received from Scratch
while doExit == False:
    try:
        # Receives message from Scratch
        msg = s.receive()
        
        
        # Checks for python format documentation
        if msg[0] == 'broadcast':
            command_array1 = []
            string_message = ""
            if ('@' in msg[1] )and ('#' in msg[1]):
                pos = msg[1].find('#')
                pos1 = msg[1].find('@')
                if pos > pos1 :
                    command_array1.append(msg[1][0:pos1])
                    string_message = string_message+(msg[1][pos1+1:pos])
                else :
                    command_array1.append(msg[1][0:pos])
                    string_message = string_message+(msg[1][pos1+1:])                    
                    
                
            elif '#' in msg[1]: 
                pos = msg[1].find('#')
                command_array1.append(msg[1][0:pos])
            elif '@' in msg[1]: 
                pos = msg[1].find('@')
                command_array1.append(msg[1][0:pos])
                string_message = string_message+(msg[1][pos+1:])
            else:    
                command_array1.append(msg[1])
            
        command_array = []        
        for cmd in command_array1:
            command_array.append(cmd.upper())
        if(debug) :
            print  command_array ,string_message,"DT = ",int(round(time.time() * 1000)) -lasttime 
            lasttime = int(round(time.time() * 1000))
        # Split message into words
        for cmd in command_array:  
            split_cmd = cmd.split()
            # Creates and assigns object to a variable and store in device_dict
            #print device_dict
            if (split_cmd[0] == 'CR'):
                if len(split_cmd) > 2:
                    s.sensorupdate({"RMAP Status" : 1})  
                    if (split_cmd[2] in device_dict):
                        pass
                    else:
                        device_dict[split_cmd[2]] = rmap.device_cr(split_cmd[1], split_cmd[2])#, split_cmd[3])
                else:
                    s.sensorupdate({"RMAP Status" : 2})
                    rmap.rmap_print("Error:Command too short, expects 3 received "+str(len(cmd))+":"+cmd)                    
            # Creates variable lists in read_dict
            elif (split_cmd[0] == 'RD'):
                if len(split_cmd) > 2:
                    x = 0
                    max = len(cmd) + 1 
                    if (split_cmd[1] in device_dict):
                        s.sensorupdate({"RMAP Status" : 1})  
                        if (split_cmd[1] in read_dict):
                            pass
                        else:
                            read_dict[split_cmd[1]] = []
                        # Creates variables in variable lists in read_dict
                        ''' for word in split_cmd:
                                if x > 1:
                                    if (str(split_cmd[1])+'_'+str(split_cmd[x]) in read_dict[split_cmd[1]]): 
                                        pass
                                    else:
                                        read_dict[split_cmd[1]].append(str(split_cmd[1])+'_'+str(split_cmd[x]))
                                if x < max:
                                 x = x + 1
                        '''
                        newvar = str(split_cmd[2])
                        for word in split_cmd:
                            if x > 2:
                                newvar =  newvar+': '+str(split_cmd[x])
                            if x < max:
                                x = x + 1 
                        if newvar not in read_dict[split_cmd[1]]: 
                            read_dict[split_cmd[1]].append(newvar)        
                        if(debug) :
                            print read_dict[split_cmd[1]]
                        # Reads data and updates to Scratch
                        '''    if split_cmd[1] in read_dict:
                            if (str(split_cmd[1])+'_'+str(split_cmd[2]) in read_dict[split_cmd[1]]): 
                                listpos = read_dict[split_cmd[1]].index(str(split_cmd[1])+'_'+str(split_cmd[2]))
                                s.sensorupdate({str(read_dict[split_cmd[1]][listpos]) : device_dict[split_cmd[1]].process_read(read_dict[split_cmd[1]][listpos])})                      
                        '''            #time.sleep(.15) 
                        if split_cmd[1] in read_dict:
                            if newvar in read_dict[split_cmd[1]]: 
                                listpos = read_dict[split_cmd[1]].index(newvar)
                                s.sensorupdate({str(read_dict[split_cmd[1]][listpos]) : device_dict[split_cmd[1]].process_read(read_dict[split_cmd[1]][listpos])})                      
                                
                    else:
                        s.sensorupdate({"RMAP Status" : 2}) 
                        rmap.rmap_print("Error:Sensor variable not recognized:"+split_cmd[1])                          
                else:
                    rmap.rmap_print("Error:Command too short, expects 3 received "+str(len(cmd))+":"+cmd)         
                    s.sensorupdate({"RMAP Status" : 2})                      
            # Writes data to sensor
            elif (split_cmd[0] in device_dict): 
                if(debug) :
                    print split_cmd
                if device_dict[split_cmd[0]].run_command(split_cmd, string_message) == True:
                    s.sensorupdate({"RMAP Status" : 1})
                else:
                    s.sensorupdate({"RMAP Status" : 2}) 
                    #rmap.rmap_print("Error:Command too short:"+cmd)                                                  
            # Handles shell commands
            elif (split_cmd[0] == 'SHELL'):
                if len(split_cmd) > 1:
                    s.sensorupdate({"RMAP Status" : 3})  
                    command = cmd[6:]
                    subprocess.call(command, shell=True) 
                else: 
                    s.sensorupdate({"RMAP Status" : 2})  
                    rmap.rmap_print("Error:Command too short, expected more than 1 received "+str(len(cmd)) +":"+cmd)  
            # Handles unrecognized commands
            else:
                rmap.rmap_print("Error:Command not recognized:"+split_cmd[0]) 
                s.sensorupdate({"RMAP Status" : 2})                
        command_array = []         
        #time.sleep(.15)
        if(psm.isKeyPressed() == True): # if the GO button is pressed
            psm.screen.clearScreen()
            psm.screen.termPrintln("")
            psm.screen.termPrintln("Exiting to menu")
            #time.sleep(0.2) 
            doExit = True 

    # Keyboard interrupt exception
    except KeyboardInterrupt:
        running= False
        rmap.rmap_print("Disconnected")
        break
    # Connection disruption exception
    except (scratch.ScratchError,NameError) as e:
        errorCounter = 0
        error = 1
        while (error == 1) and (doExit == False) :
            rmap.rmap_print("Disconnected")
            time.sleep(5)
            # Reconnects to Scratch 
            try:
                s = scratch.Scratch(host=rmapcfg.host, port=rmapcfg.port)
                s.broadcast('READY')
                rmap.rmap_print("Connected")
                error = 0
            except scratch.ScratchError:
                errorCounter += 1
                rmap.rmap_print("Scratch is either not opened or remote sensor connections aren't enabled")
                if ( errorCounter > 10 ):
                    psm.screen.clearScreen()
                    psm.screen.termPrintln("Scrach connection failed")
                    time.sleep(10)
                    sys.exit(0)
