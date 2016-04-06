#!/usr/bin/env python
#
# Copyright (c) 2016 mindsensors.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# mindsensors.com invests time and resources providing this open source code,
# please support mindsensors.com  by purchasing products from mindsensors.com!
# Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date          Author          Comments
# March 2016    Roman Bohuk     Initial Authoring

import os,sys,inspect,time,thread
import socket,fcntl,struct
from PiStorms import PiStorms

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

class PiStormsInput:
    
    def __init__(self, screen, left_padding = True):
        self.psm = screen
        if left_padding:
            self.lm = 20
            self.w = 50
        else:
            self.lm = 1
            self.w = 53

    def update_textbox(self, txt, hide):
        # Replace with asterics if hide is set to true
        if hide:
            txt = "*" * len(txt)
        # Resize if text is too big
        sz = 22
        top = 82
        if len(txt) > 13:
            sz = 20
            top = 84
        if len(txt) > 19:
            sz = 18
            top = 86
        if len(txt) > 24:
            sz = 16
            top = 88
        # Draw on screen
        self.psm.screen.fillRect(self.lm+2, 77, 296, 45, fill = (220,220,220), display = False)
        if len(txt) > 0:
            self.psm.screen.drawAutoText(txt, self.lm+8, top, fill = (0,0,0), size = sz, display = False)
        self.psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
    
    # Draws the keyboard
    def redraw(self, layout, start):
        # Available symbols
        symbols = "., !?@#$%^&*()_-+=[]{}<>\\/|~`'\""
        numbers = "0123456789"
        letters = "abcdefghijklmnopqrstuvwxyz"
        # Setting the current layout
        used = ""
        if layout == "abc": used = letters
        elif layout == "ABC": used = letters.upper()
        elif layout == "?@!": used = symbols
        elif layout == "123": used = numbers
        
        # If the index is negative, circle around 
        if start < 0: start = len(used) + start
        
        # Draw buttons
        self.psm.screen.drawButton(self.lm + self.w, 195, width = self.w, height = 45, text=used[start%len(used)], display=False, align="center")
        self.psm.screen.drawButton(self.lm + self.w * 2, 195, width = self.w, height = 45, text=used[(start+1)%len(used)], display=False, align="center")
        self.psm.screen.drawButton(self.lm + self.w * 3, 195, width = self.w, height = 45, text=used[(start+2)%len(used)], display=False, align="center")
        self.psm.screen.drawButton(self.lm + self.w * 4, 195, width = self.w, height = 45, text=used[(start+3)%len(used)], display=False, align="center")
        self.psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
        # Return the list of current keys
        return [used[(start+i)%len(used)] for i in xrange(4)]
    
    def getInput(self, hide=False):
        self.psm.led(2,0,0,0)
        self.psm.screen.fillRect(self.lm, 0, 320, 240, fill = (0,0,0), display = False)
        #self.psm.screen.drawAutoText("Press 'GO' to submit.", 20, 47, fill = (0,255,0), size = 23, display = False)
        # Instructions
        self.psm.screen.drawButton(self.lm, 10, (320 - self.lm) / 2, 45, text="      Cancel", display=False, align="left")
        self.psm.screen.drawButton(self.lm + self.w * 3, 10, (320 - self.lm) / 2, 45, text="      Submit", display=False, align="left")
        
        # Prepare textbox
        self.psm.screen.fillRect(self.lm, 75, 320 - self.lm, 49, fill = (100,100,100), display = False)
        self.psm.screen.fillRect(self.lm + 2, 77, 320 - self.lm - 4, 45, fill = (220,220,220), display = False)
        
        #Draws the control buttons
        # Top Row
        self.psm.screen.drawButton(self.lm, 150, self.w, 45, text="Shft", display=False, align="left")
        self.psm.screen.drawButton(self.lm + self.w, 150, self.w, 45, text="Abc", display=False, align="left")
        self.psm.screen.drawButton(self.lm + self.w * 2, 150, self.w, 45, text="?-!", display=False, align="left")
        self.psm.screen.drawButton(self.lm + self.w * 3, 150, self.w, 45, text="123", display=False, align="left")
        self.psm.screen.drawButton(self.lm + self.w * 4, 150, self.w, 45, text="Clr", display=False, align="left")
        self.psm.screen.drawButton(self.lm + self.w * 5, 150, self.w, 45, text="Bsp", display=False, align="left")
        # Bottom Row
        self.psm.screen.drawButton(self.lm, 195, self.w, 45, text=" <", display=False, align="center")
        self.psm.screen.drawButton(self.lm + self.w * 5, 195, self.w, 45, text=" >", display=False, align="center")

        exit = False
        usr_input = ""
        layout = "abc"
        index = 0
        upper = False
        keys = self.redraw(layout,index)
        
        toSubmit = {}
        while(not exit):
            # Top row buttons
            shft = self.psm.screen.checkButton(self.lm, 150, self.w, 45)
            abc = self.psm.screen.checkButton(self.lm + self.w, 150, self.w, 45)
            sym = self.psm.screen.checkButton(self.lm + self.w * 2, 150, self.w, 45)
            num = self.psm.screen.checkButton(self.lm + self.w * 3, 150, self.w, 45)
            clr = self.psm.screen.checkButton(self.lm + self.w * 4, 150, self.w, 45)
            bsp = self.psm.screen.checkButton(self.lm + self.w * 5, 150, self.w, 45)
            
            cancel = self.psm.screen.checkButton(self.lm, 10, (320 - self.lm) / 2, 45)
            submit = self.psm.screen.checkButton(self.lm + self.w * 3, 10, (320 - self.lm) / 2, 45)
            
            # Bottom row buttons
            prev = self.psm.screen.checkButton(self.lm, 195, self.w, 45)
            next = self.psm.screen.checkButton(self.lm + self.w * 5, 195, self.w, 45)
            letter1 = self.psm.screen.checkButton(self.lm + self.w, 195, self.w, 45)
            letter2 = self.psm.screen.checkButton(self.lm + self.w * 2, 195, self.w, 45)
            letter3 = self.psm.screen.checkButton(self.lm + self.w * 3, 195, self.w, 45)
            letter4 = self.psm.screen.checkButton(self.lm + self.w * 4, 195, self.w, 45)
            
            # Keyboard display options
            if shft: upper = not upper
            elif abc:
                layout = "abc"
                index = 0
            elif sym:
                layout = "?@!"
                index = 0
            elif num:
                layout = "123"
                index = 0
            elif prev: index -= 4
            elif next: index += 4
            
            if upper: layout = layout.upper()
            else: layout = layout.lower()
            
            if shft or abc or sym or num or prev or next:
                keys = self.redraw(layout,index)
                continue
            
            # Input buttons
            if bsp:
                if len(usr_input) == 0:
                    for i in xrange(3):
                        self.psm.led(2,255,0,0) # flash LED 1 red
                        time.sleep(0.05)
                        self.psm.led(2,0,0,0)
                        time.sleep(0.02)
                else:
                    usr_input = usr_input[:len(usr_input)-1:]
            if clr: usr_input = ""
            elif letter1: usr_input += keys[0]
            elif letter2: usr_input += keys[1]
            elif letter3: usr_input += keys[2]
            elif letter4: usr_input += keys[3]
            
            if clr or bsp or letter1 or letter2 or letter3 or letter4:
                self.update_textbox(usr_input,hide)
                continue
            
            # Exit
            if submit: 
                exit = True
                toSubmit = {"submitted":True, "response":usr_input}
            elif self.psm.isKeyPressed() or cancel:
                exit = True
                toSubmit = {"submitted":False, "response":usr_input}
                
        
        return toSubmit
