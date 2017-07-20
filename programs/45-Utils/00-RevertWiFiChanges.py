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
import datetime, subprocess

# Globals
config_file = "/etc/wpa_supplicant/wpa_supplicant.conf~bk"
config_file_actual = "/etc/wpa_supplicant/wpa_supplicant.conf" # Config file for Wi-Fi
opt = []
entries = []
error = False
psm = PiStorms()

try:
    with open(config_file, "r") as f:
        dat = f.read()
    entries = dat.split("\n\n---------------------------\n")[1::]
    lt = ""
    for i in entries:
        tim = datetime.datetime.fromtimestamp(int(i.split("\n")[0])).strftime('%Y-%m-%d %H:%M:%S')
        if lt != tim:
            opt.append([tim,i.split("\n",1)[1],int(i.split("\n")[0])])
            lt = tim
    opt = opt[::-1]
except Exception as e:
    error = True
    with open(config_file, "w+") as f:
        f.write("")
        
if error or len(opt) == 0:
    psm.screen.drawAutoText("You have no Wi-Fi", 35, 20, fill = (255,0,0), size = 22, display = False)
    psm.screen.drawAutoText("configurations backups", 35, 50, fill = (255,0,0), size = 22, display = False)    
    psm.screen.drawButton(35, 170, width = 250, height = 40, text="Continue", display=False)
    psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
    while True:
        cont = psm.screen.checkButton(35, 170, 250, 40)
        if cont or psm.isKeyPressed(): sys.exit(0)

# Reload adapter to apply config changes
def reload_adapter():
    # Clear the screen and show the loading image
    show_loading(up=True)
    # Turn off and back on the wlan interface
    subprocess.call(["sudo","ifdown","wlan0"])
    subprocess.call(["sudo","ifup","wlan0"])

def draw_options():
    # Clear the screen
    psm.screen.fillRect(0, 0, 320, 240, (0,0,0))
    psm.screen.drawAutoText("Revert WiFi configuration", 20, 10, fill = (255,0,0), size = 24, display = False)
    psm.screen.drawButton(20, 45, width = 150, height = 35, text="        <", display=False)
    psm.screen.drawButton(170, 45, width = 150, height = 35, text="        >", display=False)

# Displays a max of 4 available networks
def draw_connections(lst, page):
    psm.screen.fillRect(20, 80, 320, 240, fill = (0,0,0), display = False)
    page = page % ((len(lst)-1) / 4 + 1)
    toBeShown = lst[page*4::]
    if len(toBeShown) > 4: toBeShown = toBeShown[:4:]
    # Display on the screen each option
    ystart = 80
    ind = 0
    for i in toBeShown:
        psm.screen.drawButton(20, ystart + ind * 40, width = 300, height = 40, text=i[0], display=False)
        ind += 1
    # Finally display all options
    psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
    # Return the list of available networks
    return toBeShown

# Display a loading image
def show_loading(up=False):
    # If fullscreen
    if up:
        psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
        psm.screen.fillBmp(110, 70, 100, 100, path = currentdir+'/'+'load.png', display = False)
    else:
        psm.screen.fillRect(20, 80, 320, 240, fill = (0,0,0), display = False)
        psm.screen.fillBmp(110, 110, 100, 100, path = currentdir+'/'+'load.png', display = False)
    # Finally display
    psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)

def revert(tmsmp,dat,timint):
    psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
    psm.screen.drawAutoText("Are you sure you want to", 35, 20, fill = (255,0,0), size = 21, display = False)
    psm.screen.drawAutoText("revert changes to", 35, 50, fill = (255,0,0), size = 21, display = False)
    psm.screen.drawAutoText(tmsmp, 35, 90, fill = (0,0,255), size = 23, display = False)
    psm.screen.drawButton(35, 160, width = 125, height = 40, text="Continue", display=False)
    psm.screen.drawButton(160, 160, width = 125, height = 40, text="Cancel", display=False)
    psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
    answered = False
    while not answered:
        yes = psm.screen.checkButton(35, 160, 125, 40)
        no = psm.screen.checkButton(160, 160, 125, 40)
        if no: return
        elif yes:
            with open(config_file_actual,"w+") as f:
                f.write(dat)
            reload_adapter()
            psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
            psm.screen.drawAutoText("Configuration has been", 35, 20, fill = (0,255,0), size = 22, display = False)
            psm.screen.drawAutoText("successfully reverted!", 35, 50, fill = (0,255,0), size = 22, display = False)    
            psm.screen.drawButton(35, 170, width = 250, height = 40, text="Continue", display=False)
            psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
            while True:
                cont = psm.screen.checkButton(35, 170, 250, 40)
                if cont or psm.isKeyPressed(): sys.exit(0)

page = 0
draw_options()
shown = draw_connections(opt,page)
def mainLoop():
    # Navigation buttons
    next = psm.screen.checkButton(170, 45, 150, 35)
    prev = psm.screen.checkButton(20, 45, 150, 35)
    label1 = psm.screen.checkButton(20, 80, 300, 40)
    label2 = psm.screen.checkButton(20, 120, 300, 40)
    label3 = psm.screen.checkButton(20, 160, 300, 40)
    label4 = psm.screen.checkButton(20, 200, 300, 40)

    if next: page += 1
    elif prev:
        page -= 1
        if page < 0: page = (len(opt)-1) / 4
    if next or prev: shown = draw_connections(opt,page)
    
    # Connect to a chosen network
    if label1 and len(shown) > 0: revert(shown[0][0],shown[0][1],shown[0][2])
    if label2 and len(shown) > 1: revert(shown[1][0],shown[1][1],shown[1][2])
    if label3 and len(shown) > 2: revert(shown[2][0],shown[2][1],shown[2][2])
    if label4 and len(shown) > 3: revert(shown[3][0],shown[3][1],shown[3][2])
    
    if (label1 and len(shown) > 0) or (label2 and len(shown) > 1) or (label3 and len(shown) > 2) or (label4 and len(shown) > 3):
        psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
        draw_options()
        shown = draw_connections(opt, page)

psm.untilKeyPress(mainLoop)
