#!/usr/bin/env python
#
# Copyright (c) 2015 mindsensors.com
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
#
# History:
# Date      Author      Comments
# Oct 2015  Michael     Initial Authoring

import os,sys,inspect,time,thread
import socket,fcntl,struct    

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms

print "running program"
psm = PiStorms()
psm.screen.drawButton(75, 70, width = 75, height = 40, text="Greet", display=False)
psm.screen.drawButton(75, 115, width = 75, height = 40, text="Exit", display=True)

exit = False
lastled = 0

while(not exit):
    greet = psm.screen.checkButton(75, 70,width=75,height=40)
    bye = psm.screen.checkButton(75, 115,width=75,height=40)
    if(greet == True):
        psm.screen.drawAutoText("Hello World!", 50, 175,fill = (255,255,255), size = 25, display = True, align = "center")
    if(bye == True):
        psm.screen.termPrintln("")
        psm.screen.drawAutoText("Exiting to menu", 50, 210,fill = (255,255,255), size = 20, display = True, align = "left")
        exit = True