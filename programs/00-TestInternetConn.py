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

from PiStorms import PiStorms
import socket

# Globals
psm = PiStorms()

# Checks if internet is available
def available():
    try:
        socket.setdefaulttimeout(5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except Exception as e: pass
    return False

psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
psm.screen.drawAutoText("Testing internet connection", 20, 30, fill = (255,255,255), size = 23, display = False)
psm.screen.fillRect(20, 80, 320, 240, fill = (0,0,0), display = False)
psm.screen.fillBmp(110, 110, 100, 100, path = currentdir+'/'+'load.png', display = False)
psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)

    
test = available()
psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
if test:
    psm.screen.drawAutoText("You are connected", 35, 20, fill = (0,255,0), size = 25, display = False)
    psm.screen.drawAutoText("to the internet!", 35, 50, fill = (0,255,0), size = 25, display = False)
    psm.screen.fillBmp(120, 85, 80, 80, path = currentdir+'/'+'wifi_green.png', display = False)
else:
    psm.screen.drawAutoText("You are not connected", 35, 20, fill = (255,0,0), size = 25, display = False)
    psm.screen.drawAutoText("to the internet!", 35, 50, fill = (255,0,0), size = 25, display = False)
    psm.screen.fillBmp(130, 95, 60, 60, path = currentdir+'/'+'x_red.png', display = False)
    
psm.screen.drawButton(35, 170, width = 250, height = 40, text="Continue", display=False)
psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
exit = False
while not exit:
    cont = psm.screen.checkButton(35, 170, 250, 40)
    if cont or psm.isKeyPressed(): exit = True
