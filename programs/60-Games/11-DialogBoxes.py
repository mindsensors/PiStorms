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
#mindsensors.com invests time and resources providing this open source code,
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/

# This is an example of using the dialog box methods from mindsensorsUI

from PiStorms import PiStorms
psm = PiStorms()

# The question is a list of strings. Each string is one line.
# So the first string is the title, then the first line,
# then the second line, etc.
question = ["Lights, Camera, Action!",
            "What color do you want the LED",
            "to show?"]
choices = ["Red", "Green", "Blue"]
response = psm.screen.askQuestion(question, choices)
if (response == 0): # red
    psm.led(2, 255, 0, 0)
elif (response == 1): # green
    psm.led(2, 0, 255, 0)
elif (response == 2): # blue
    psm.led(2, 0, 0, 255)

# For convenience, you can use askYesOrNoQuestion
# to ask a simple question.
question = ["Lights out?",
            "Do you want the other LED on?"]
response = psm.screen.askYesOrNoQuestion(question)
if (response): # no need for `== True`, it's implied
    psm.led(1, 255, 255, 255)
else:
    psm.led(1, 0, 0, 0)

# Use showMessage to show a message with the only option "OK".
# You can set wrapText to True to, you guessed it, wrap text
# at the end of the line so everything is on screen. You can
# also use this with askQuestion, etc. If the text is too long
# to fit in the box it will end with an ellipsis...
# You can also set goBtn to True to be able to close the popup
# with the GO button.
message = ["A Long Message!",
           "mindsensors.com provides high quality parts for Raspberry Pi, LEGO Mindstorms NXT & EV3 Robotic systems. Our objective is to make technology products readily accessible; so your child can achieve highest level of learning."]
psm.screen.showMessage(message, wrapText = True, goBtn = True)

# forceMessage puts a pop-up on screen without any options.
# You must change it yourself later in your program.
message = ["Loading... (not really)",
           "Please wait 5 seconds..."]
psm.screen.forceMessage(message)
import time
time.sleep(5)
psm.screen.setMode(psm.screen.PS_MODE_TERMINAL)
psm.screen.termPrintln("Thank you for waiting!")
psm.screen.termPrintAt(8, "Press GO to exit")
psm.waitForKeyPress()
