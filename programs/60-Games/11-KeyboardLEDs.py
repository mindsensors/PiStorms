#!/usr/bin/env python
#
# Copyright (c) 2017 mindsensors.com
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
# May 2017    Seth Tenembaum    Initial authoring

# This program demonstrates some more advanced on-screen keyboard usage

# Standard setup for every PiStorms program
import os,sys,inspect,time,thread
import socket,fcntl,struct
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# Import the PiStorms class and the class for the on-screen keyboard
from PiStorms import PiStorms
from TouchScreenInput import TouchScreenInput

# We will use this for the LEDs in a bit
from functools import partial

# Create an instance of PiStorms class
psm = PiStorms()

# Create an instance of the TouchScreenInput class
textbox = TouchScreenInput(psm.screen)

# If you wanted to set the bank A LED to red, you might use the following code:
#         psm.led(1, 255, 0, 0)
# The first argument is which LED (bank A or bank B) and the rest of the arguments are
# how much red, green, and blue to light up. These numbers can be from 0 up to 255.
# Here we are calling the led method, so the LED will turn red. We don't quite want that for the keyboard.
# The TouchScreenInput class's methods include bind_led_on_func and bind_led_off_func.
# These let you call a function when you hit backspace when there aren't any more letters to delete.
# We want to make it flash red. So bind_led_on_func will have to set the LED to red,
# and bind_led_off_function should set it to black (off, no color).
# In our code example the LED would turn red right away. We want to pass the bind method
# a function that will make it red. You could do something like this:
#         def red():
#             psm.led(1, 255, 0, 0)
#         textbox.bind_led_on_func(red)
# Here we define a method called red. This method makes the LED red.
# This is perfectly fine, but I'd like to teach you a bit about functional programming.
# So why don't get just tell it to call psm.led?
#         textbox.bind_led_on_func(psm.led)
# Well, we have to tell the led function which LED to light up and what colors to use.
#         textbox.bind_led_on_func(psm.led(1, 255, 0, 0))
# This won't work either. The led function will run and will evaluate to None.
# bind_led_on_func will try to call None as a method, and of course this won't work.
# We need to somehow give the led functions its arguments, but not invoke it.
# bind_led_on_func will call the function its given with no parameters, so we need something else.
# We use the partial function from the functools module. We can partially apply the led function.
# The first argument partial takes is the function it will call. Then we pass in the arguments.
# Parial returns the method with those arguments already applied, so in this case we get a function
# That takes no parameters and will make the LED red! We do the same for the off function.
red = partial(psm.led, 1, 255, 0, 0)
off = partial(psm.led, 1,   0, 0, 0)
textbox.bind_led_on_func(red)
textbox.bind_led_off_func(off)

# Show the keyboard to ask for text input, showing only asterisks like a password
result = textbox.getInput(hide=True)

psm.screen.showMessage(["Result is...", result])

