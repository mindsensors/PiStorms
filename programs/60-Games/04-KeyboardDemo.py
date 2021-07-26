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
# May 2016    Deepak            Initial authoring

# Setup (to be present in all programs)
import os,sys,inspect,time,threading
import socket,fcntl,struct
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# PiStorms and Input classes
from PiStorms import PiStorms
from TouchScreenInput import TouchScreenInput

# Create an instance of PiStorms class
psm = PiStorms()

# Create an instance of the TouchScreenInput class
textbox = TouchScreenInput(psm.screen)

doExit = False
while (doExit != True):
    # Take user input
    userInput = textbox.getInput()

    # Take user input while hiding the characters (replaces with *)
    #userInput = textbox.getInput(hide = True)

    if userInput["submitted"]:
        m2 = "User Submitted"
    else:
        m2 = "User Cancelled"

    m = ["User Input", m2, "Entry: " + userInput["response"]]
    choice = psm.screen.askQuestion(m,["OK", "Exit"])
    if ( choice == 1):
        doExit = True
