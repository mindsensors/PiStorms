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
exit = False
while not exit:
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
        
    # Exit
    if(psm.isKeyPressed()): exit = True





"""

wifi = None
wlan_inteface = "wlan0"
psm = PiStorms()

# Check if a wifi adapter is available
try:
    wifi = Wireless()
    wlan_interface = wifi.interfaces()[0]
except Exception as e:
    psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
    psm.screen.drawAutoText("No Wi-Fi adapter", 35, 20, fill = (255,0,0), size = 25, display = False)
    psm.screen.drawAutoText("available!", 35, 50, fill = (255,0,0), size = 25, display = False)
    psm.screen.drawButton(35, 160, width = 250, height = 40, text="Continue", display=False)
    psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
    while True:
        cont = psm.screen.checkButton(35, 160, 250, 40)
        if cont: sys.exit(0)

current = wifi.current() # Currently connected network
available = Cell.all(wlan_interface) # Available networks
box = PiStormsInput(psm)

# Writes wifi configuration to wpa_supplicant.conf
def write_to_config(new):
    # Makes backup by appending to wpa_supplicant.conf~bk
    with open(config_file, "r") as f:
        bak = f.read()
    with open(config_file+"~bk", "a+") as f:
        f.write("\n\n---------------------------\n" + str(int(time.time())) + "\n\n" + new)
    # Writes new configuration
    with open(config_file, "w") as f:
        f.write(new)

# Deletes connection details for a network
def delete_interface(ssid):
    # Read configuration file
    with open(config_file, "r") as f:
        s = f.read()
    # Finds all networks and saves the rest as "extra"
    r = re.findall("network\s*=\s*{[^}]*}", s)
    for i in r: s = s.replace(i,"")
    extra = "\n".join([i for i in s.split("\n") if i != ""])

    # Goes through each setup and deletes the network if found
    for i in r:
        find = re.findall('(?<=\s)+ssid\s*=[\s]*"?[a-zA-Z0-9 ]*"', i)
        if len(find) != 1: extra += "\n\n" + i
        else:
            find = re.findall('=[\s]*"?[a-zA-Z0-9 ]*"', find[0])[0].strip().strip("=").strip().strip('"')
            # Appends to "extra" if not the needed network
            if ssid != find: extra += "\n\n" + i
    # Save the configuration data
    write_to_config(extra)

# Identifies whether or not the key is in ASCII or HEX and converts to HEX
def convert_wep(wep):
    if len(wep) == 5 or len(wep) == 13:
        return wep.encode("hex")
    else:
        npsk = ""
        for i in wep.upper():
            # If in HEX already, replace all non-HEX values
            if i in "0123456789ABCDEF": npsk += i
            else: npsk += "0"
        return npsk

# Adds a network configuration to wpa_supplicant.conf
def add_interface(ssid, key=False, pwd="", wep=False):
    # Deletes if already exists
    delete_interface(ssid)
    # Reads the config file
    with open(config_file, "r") as f:
        s = f.read()
    # If the connection is secured, include the key
    if key:
        # If the network uses WEP, use "nwep_key0" field for password & extra parameters
        if wep:
            pwd = convert_wep(pwd)
            s += '\n\nnetwork={\nssid="%s"\nscan_ssid=1\nkey_mgmt=NONE\nwep_tx_keyidx=0\nwep_key0=%s\n}' % (ssid.replace('"','\\"'), pwd.replace('"','\\"'))
        # Else, use "psk" field
        else: s += '\n\nnetwork={\nssid="%s"\npsk="%s"\n}' % (ssid.replace('"','\\"'), pwd.replace('"','\\"'))
    else:
        # If not secured, just create a network without the password
        s += '\n\nnetwork={\nssid="%s"\nproto=RSN\nkey_mgmt=NONE\n}' % (ssid.replace('"','\\"'))
    # Save the configuration data
    write_to_config(s)

def update_current_connection():
    global wifi, current
    wifi = Wireless()
    current = wifi.current()

# Reload adapter to apply config changes
def reload_adapter():
    # Clear the screen and show the loading image
    show_loading(up=True)
    # Turn off and back on the wlan interface
    subprocess.call(["sudo","ifdown",wlan_interface])
    subprocess.call(["sudo","ifup",wlan_interface])
    # Refresh the currently connected network
    update_current_connection()

# Display the current network and UI options
def draw_options():
    # Refresh the currently connected network
    update_current_connection()
    # Clear the screen
    psm.screen.fillRect(0, 0, 320, 240, (0,0,0))
    # Display current network
    if current != None:
        psm.screen.drawAutoText("Connected to:", 20, 3, fill = (0,255,0), size = 20, display = False)
        psm.screen.drawAutoText("Hidden Network" if current.split("  ")[0] == "" else current.split("  ")[0], 20, 23, fill = (255,255,255), size = 16, display = False)
        psm.screen.drawButton(240, 5, width = 80, height = 40, text="Leave", display=False)
    # Say that not connected to a network
    else: psm.screen.drawAutoText("Not Connected", 20, 8, fill = (255,0,0), size = 27, display = False)
    # Display navigation buttons and an option to refresh
    psm.screen.drawButton(20, 45, width = 100, height = 35, text="        <", display=False)
    psm.screen.drawButton(120, 45, width = 100, height = 35, text="Refresh", display=False)
    psm.screen.drawButton(220, 45, width = 100, height = 35, text="        >", display=False)

# Displays a max of 4 available networks
def draw_connections(ssid_lst, page):
    # Clear the available ones
    psm.screen.fillRect(20, 80, 320, 240, fill = (0,0,0), display = False)
    # Show "No networks available" if applicable
    if len(ssid_lst) <= 0:
        psm.screen.drawAutoText("No networks available", 20, 90, fill = (255,0,0), size = 20, display = False)
        psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
        return []
    # Sort networks by name
    ssid_lst.sort(key=lambda x: x[0].lower())
    # Get the current page number to fit within index
    page = page % ((len(ssid_lst)-1) / 4 + 1)
    # Get the 4 networks to display
    toBeShown = ssid_lst[page*4::]
    if len(toBeShown) > 4: toBeShown = toBeShown[:4:]
    # Display on the screen each option
    ystart = 80
    ind = 0
    for i in toBeShown:
        # Identify whether the network is secured or not with a lock
        img = "ulock.png"
        if i[1]: img = "lock.png"
        psm.screen.fillBmp(25, ystart + ind * 40 + 5, 30, 30, path = currentdir+'/'+img, display = False)
        psm.screen.drawButton(60, ystart + ind * 40, width = 260, height = 40, text="Hidden Network" if i[0] == "" else i[0], display=False)
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

# Connect to a network
def connect(ssid, secure, encType):
    # Clear the screen
    psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
    # If network is secured
    if secure:
        # If WPA / WPA2 or not WEP
        if not "wep" in encType.lower():
            # Message about the pre-shared key & option to cancel
            psm.screen.drawAutoText("The network is secured.", 35, 20, fill = (255,0,0), size = 25, display = False)
            psm.screen.drawAutoText("Please enter the", 35, 50, fill = (255,0,0), size = 25, display = False)
            psm.screen.drawAutoText("pre-shared key for", 35, 80, fill = (255,0,0), size = 25, display = False)
            psm.screen.drawAutoText("Hidden Network" if ssid == "" else ssid, 35, 120, fill = (0,0,255), size = 25, display = False)
            psm.screen.drawButton(35, 160, width = 125, height = 40, text="Continue", display=False)
            psm.screen.drawButton(160, 160, width = 125, height = 40, text="Cancel", display=False)
            psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
            answered = False
            while not answered:
                yes = psm.screen.checkButton(35, 160, 125, 40)
                no = psm.screen.checkButton(160, 160, 125, 40)
                if no: return # cancel
                elif yes:
                    pwdIn = box.getInput()
                    if pwdIn["submitted"]:
                        if len(pwdIn["response"]) < 8:
                            # Notify about a key if it is too short
                            psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
                            psm.screen.drawAutoText("The entered key", 35, 20, fill = (255,0,0), size = 25, display = False)
                            psm.screen.drawAutoText("is too short!", 35, 50, fill = (255,0,0), size = 25, display = False)
                            psm.screen.drawButton(35, 160, width = 250, height = 40, text="Continue", display=False)
                            psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
                            while True:
                                cont = psm.screen.checkButton(35, 160, 250, 40)
                                if cont: return
                        answered = True
                        if current != None: delete_interface(current.split("  ")[0])
                        add_interface(ssid,key=True,pwd=pwdIn["response"])
                    else: return # cancel
        else:
            # Message about WEP key
            psm.screen.drawAutoText("The network is secured.", 35, 20, fill = (255,0,0), size = 25, display = False)
            psm.screen.drawAutoText("Please enter the WEP", 35, 50, fill = (255,0,0), size = 25, display = False)
            psm.screen.drawAutoText("key in ASCII or HEX for", 35, 80, fill = (255,0,0), size = 25, display = False)
            psm.screen.drawAutoText("Hidden Network" if ssid == "" else ssid, 35, 120, fill = (0,0,255), size = 25, display = False)
            psm.screen.drawButton(35, 160, width = 125, height = 40, text="Continue", display=False)
            psm.screen.drawButton(160, 160, width = 125, height = 40, text="Cancel", display=False)
            psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
            answered = False
            while not answered:
                yes = psm.screen.checkButton(35, 160, 125, 40)
                no = psm.screen.checkButton(160, 160, 125, 40)
                if no: return
                elif yes:
                    pwdIn = box.getInput()
                    if pwdIn["submitted"]:
                        if not len(pwdIn["response"]) in [5,10,13,26]:
                            # Notify about an incorrect WEP key
                            psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
                            psm.screen.drawAutoText("The entered WEP key", 35, 20, fill = (255,0,0), size = 25, display = False)
                            psm.screen.drawAutoText("has invalid length!", 35, 50, fill = (255,0,0), size = 25, display = False)
                            psm.screen.drawButton(35, 160, width = 250, height = 40, text="Continue", display=False)
                            psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
                            while True:
                                cont = psm.screen.checkButton(35, 160, 250, 40)
                                if cont: return
                        else:
                            if current != None:
                                delete_interface(current.split("  ")[0])
                            add_interface(ssid,key=True,pwd=pwdIn["response"],wep=True)
                        answered = True
                    else: return

    else:
        # Confirmation to connect if the network is insecure
        psm.screen.drawAutoText("Are you sure you want to", 35, 20, fill = (255,0,0), size = 20, display = False)
        psm.screen.drawAutoText("connect to this network?", 35, 50, fill = (255,0,0), size = 20, display = False)
        psm.screen.drawAutoText("All current connections", 35, 80, fill = (255,0,0), size = 20, display = False)
        psm.screen.drawAutoText("will be reset.", 35, 110, fill = (255,0,0), size = 20, display = False)
        psm.screen.drawButton(35, 160, width = 125, height = 40, text="Continue", display=False)
        psm.screen.drawButton(160, 160, width = 125, height = 40, text="Cancel", display=False)
        psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
        answered = False
        while not answered:
            yes = psm.screen.checkButton(35, 160, 125, 40)
            no = psm.screen.checkButton(160, 160, 125, 40)
            if no: return
            elif yes:
                answered = True
                add_interface(ssid)
    # Reload adapter to apply settings
    reload_adapter()
    time.sleep(2)

# Disconnect from the current network
def disconnect():
    # Show loading image
    show_loading(up=True)
    # Delete the network
    if current != None: delete_interface(current.split("  ")[0])
    # Reload adapter to apply settings
    reload_adapter()

# Ask if the user really wants to dissconnect
def disconnect_question():
    # Clear the screen and display the information
    psm.screen.fillRect(0, 0, 320, 240, fill = (0,0,0), display = False)
    psm.screen.drawAutoText("Do you really want", 35, 20, fill = (255,0,0), size = 25, display = False)
    psm.screen.drawAutoText("to disconnect from", 35, 50, fill = (255,0,0), size = 25, display = False)
    psm.screen.drawAutoText("Hidden Network" if current.split("  ")[0] == "" else current.split("  ")[0], 35, 90, fill = (0,0,255), size = 25, display = False)
    psm.screen.drawButton(35, 160, width = 125, height = 40, text="Yes", display=False)
    psm.screen.drawButton(160, 160, width = 125, height = 40, text="No", display=False)
    psm.screen.fillRect(0, 0, 1, 1, fill = (0,0,0), display = True)
    # Wait until the user says Yes or No
    while True:
        yes = psm.screen.checkButton(35, 160, 125, 40)
        no = psm.screen.checkButton(160, 160, 125, 40)
        if no: return False
        elif yes: return True

# Gets available networks [ssid, is_encrypted, encryption_type]
def get_available():
    names = []
    for cell in available:
        nlst = [cell.ssid,cell.encrypted]
        if cell.encrypted: nlst.append(cell.encryption_type)
        else: nlst.append(None)
        names.append(nlst)
    return names

# Variables for the main loop
page = 0 # Current page
ssids = get_available() # Available ssid's
draw_options() # Displays UI options
shown = draw_connections(ssids, page) # Displays a page of available networks
exit = False

# Main loop
while not exit:
    # Navigation buttons
    next = psm.screen.checkButton(220, 45, 100, 35)
    prev = psm.screen.checkButton(20, 45, 100, 35)
    refresh = psm.screen.checkButton(120, 45, 100, 35)
    # Button to leave the network
    leave = psm.screen.checkButton(240, 5, 80, 40)
    # Available networks
    label1 = psm.screen.checkButton(20, 80, 300, 40)
    label2 = psm.screen.checkButton(20, 120, 300, 40)
    label3 = psm.screen.checkButton(20, 160, 300, 40)
    label4 = psm.screen.checkButton(20, 200, 300, 40)
    
    # If connected and the leave button is pressed, disconnect
    if leave and current != None:
        # Ask for confirmation
        answer = disconnect_question()
        if answer: disconnect()
        # Redraw
        draw_options()
        draw_connections(ssids, page)

    # Change the page
    if next: page += 1
    elif prev:
        page -= 1
        if page < 0: page = (len(ssids)-1) / 4
    elif refresh:
        show_loading()
        available = Cell.all(wlan_interface)
        ssids = get_available()
    # Redraw connections if changed
    if next or prev or refresh: shown = draw_connections(ssids, page)
    
    # Connect to a chosen network
    if label1 and len(shown) > 0: connect(shown[0][0],shown[0][1],shown[0][2])
    if label2 and len(shown) > 1: connect(shown[1][0],shown[1][1],shown[1][2])
    if label3 and len(shown) > 2: connect(shown[2][0],shown[2][1],shown[2][2])
    if label4 and len(shown) > 3: connect(shown[3][0],shown[3][1],shown[3][2])
    # Redraws options and available connections
    if (label1 and len(shown) > 0) or (label2 and len(shown) > 1) or (label3 and len(shown) > 2) or (label4 and len(shown) > 3):
        draw_options()
        shown = draw_connections(ssids, page)
    
    # Exit
    if(psm.isKeyPressed()): exit = True
"""