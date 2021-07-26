#!/usr/bin/env python3
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
#mindsensors.com invests time and resources providing this open source code,
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# 05/25/16   Deepak     Initial development.
#

from PiStorms import PiStorms
import sys, subprocess, json, os
import socket
import ConfigParser

version_json_file = '/var/tmp/ps_versions.json'
cfg_file = '/usr/local/mindsensors/conf/msdev.cfg'

config = ConfigParser.RawConfigParser()
config.read(cfg_file)

download_url = config.get('servers', 'download_url')

psm = PiStorms()

def available():
    try:
        socket.setdefaulttimeout(5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except Exception as e: pass
    return False

def renameFolder(prefix, index):
    if (os.path.isdir(prefix+"."+str(index))):
        # folder exists
        # increment index and call the function again.
        index = index + 1
        return renameFolder(prefix, index)
    else:
        cmd = "sudo mv " + prefix +" " + prefix+"."+str(index)
        status = subprocess.call(cmd, shell=True)
        return (prefix+"."+str(index))

opt = str(sys.argv[1])

isConnected = available()
if (isConnected == False):
    m = ["Software Updater", "You are not connected to Internet.",
      "Internet connection required"]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)

print ("running software_update.py")

try:
    f = open(version_json_file, 'r')
    data = json.loads(f.read())
    sw_version = data['sw_ver']
    f.close()
except:
    # no local json
    # this can happen on old systems, so upgrade them to 4.000
    sw_version = "4.000"

#
# Download the update from mindsensors server.
#
psm.screen.termPrintAt(3, "Downloading the update")
psm.screen.termPrintAt(4, "Please wait...")

sw_file_name = "PiStorms." + sw_version + ".tar.gz"
cmd = "wget " + download_url + "/" + sw_file_name
status = subprocess.call(cmd, shell=True)

if ( status != 0 ):
    m = ["Software Updater", "Error while downloading update:",
      sw_file_name]
    psm.screen.askQuestion(m,["OK"])
    psm.screen.clearScreen()
    sys.exit(-1)
else:
    psm.screen.termPrintAt(3, "Download complete")
    psm.screen.termPrintAt(4, "              ")

#
# rename the prior folder with an indremental suffix
# Extract the new update in its place
#
newHtml = renameFolder("/var/www/html", 0)
if (os.path.isdir("/var/www/html")):
    # if the folder is still there, don't install
    m = ["Software Updater", "Error while renaming html folder" ]
    psm.screen.askQuestion(m,["OK"])
    psm.screen.clearScreen()
    sys.exit(-1)

newWebapi = renameFolder("/var/www/web_api", 0)
if (os.path.isdir("/var/www/web_api")):
    # if the folder is still there, don't install
    m = ["Software Updater", "Error while renaming web_api folder" ]
    psm.screen.askQuestion(m,["OK"])
    psm.screen.clearScreen()
    sys.exit(-1)

newName = renameFolder("/home/pi/PiStorms", 0)

if (os.path.isdir("/home/pi/PiStorms")):
    # if the folder is still there, don't install
    m = ["Software Updater", "Error while renaming PiStorms folder" ]
    psm.screen.askQuestion(m,["OK"])
    psm.screen.clearScreen()
    sys.exit(-1)
else:
    psm.screen.termPrintAt(3, "Unzipping ...")
    psm.screen.termPrintAt(4, "              ")


cmd = "cd /home/pi; tar -zxvf /var/tmp/upd/" + sw_file_name
status = subprocess.call(cmd, shell=True)
if ( status != 0 ):
    m = ["Software Updater", "Error while unzipping PiStorms folder" ]
    psm.screen.askQuestion(m,["OK"])
    psm.screen.clearScreen()
    sys.exit(-1)
else:
    psm.screen.termPrintAt(3, "Unzip complete.")
    psm.screen.termPrintAt(4, "Configuring...")

#
# run setup script.
#
cmd = "cd /home/pi/PiStorms/setup;chmod +x setup.sh"
status = subprocess.call(cmd, shell=True)

psm.screen.termPrintAt(3, "Configuration in process ...")
psm.screen.termPrintAt(5, "(this takes a while)")
psm.screen.termPrintAt(5, "Please wait ...")
cmd = "cd /home/pi/PiStorms/setup;./setup.sh"
status = subprocess.call(cmd, shell=True)

psm.screen.termPrintAt(3, "Update complete.")
psm.screen.termPrintAt(4, "Please restart your Pi.")

m = ["Software Update Complete.",
  "Prior installation saved in:",
  newName,
  newHtml,
  newWebapi,
  "Please restart your Pi"]
psm.screen.askQuestion(m,["OK"])

sys.exit(0)
