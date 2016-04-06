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

# Setup (to be present in all programs)
import os,sys,inspect,time,thread
import socket,fcntl,struct
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# PiStorms and Input classes
from PiStorms import PiStorms
from PiStormsInput import PiStormsInput

# Create an instance of PiStorms class
psm = PiStorms()

# Create an instance of the PiStormsInput class
textbox = PiStormsInput(psm)

# Take user input
userInput = textbox.getInput()

# Take user input while hiding the characters (replaces with *)
userInput = textbox.getInput(hide = True)

if userInput["submitted"]:
    print "User entered: " + userInput["response"]
else:
    print "User cancelled the operation, but he entered: " + userInput["response"]

# By default, the widget has a 20px margin on the left
# Set left_padding to False so that the widget takes up the whole screen
textbox2 = PiStormsInput(psm, left_padding = False)

userInput = textbox2.getInput()

userInput = textbox2.getInput(hide = True)


