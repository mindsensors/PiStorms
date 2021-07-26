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
hw_version_file = '/var/tmp/.hw_version'

cfg_file = '/usr/local/mindsensors/conf/msdev.cfg'

config = ConfigParser.RawConfigParser()
config.read(cfg_file)

download_url = config.get('servers', 'download_url')
homefolder = config.get('msdev', 'homefolder')

psm = PiStorms()

def version_json_update_field(field, new_value):
    f = open(version_json_file, 'r')
    json_data = json.loads(f.read())
    f.close()
    f = open(version_json_file, 'w')
    json_data[field] = new_value
    json.dump(json_data, f)
    f.close()

def available():
    try:
        socket.setdefaulttimeout(5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except Exception as e: pass
    return False

isConnected = available()
if (isConnected == False):
    m = ["Hardware Updater", "You are not connected to Internet.",
      "Internet connection required"]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)

print ("running hardware_update.py")

# find hw version on this pi.
try:
    f = open(hw_version_file, 'r')
    hw_version = f.read()
    hw_version = hw_version.strip()
    hw_version = hw_version.replace('V','')
    f.close()
except:
    hw_version = "0.000"

print ("hw_version from file: " + str(hw_version))

if ( hw_version < "1.7"):
    print ("Firmware unknown or too old for auto update")
    m = ["Firmware Updater", "Current Firmware unkown or too old.",
      "Can not auto update."]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)

try:
    f = open(version_json_file, 'r')
    data = json.loads(f.read())
    new_firmware = data['hw_ver']
    new_firmware = new_firmware.replace('V','')
    f.close()
except:
    # no local json
    # this can happen on old systems, so upgrade them to 2.00
    new_firmware = "2.00"

m = ["Firmware Updater", "Remove all sensors and motors.",
  "Then press OK to continue."]
psm.screen.askQuestion(m,["OK"])
#
# Download the update from mindsensors server.
#
psm.screen.termPrintAt(3, "Downloading the update")
psm.screen.termPrintAt(4, "Please wait...")

#B_PiStormsV160.hex
upgrader = "fwupgrader.tar.gz"
cmd = "sudo rm -f /var/tmp/upd/"+upgrader
status = subprocess.call(cmd, shell=True)

cmd = "cd /var/tmp/upd/; wget " + download_url + "/" + upgrader
status = subprocess.call(cmd, shell=True)
if ( status != 0 ):
    m = ["Firmware Updater", "Error while downloading upgrader.",
      upgrader]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)

cmd = "cd /var/tmp/upd/; tar -zxvf /var/tmp/upd/" + upgrader
status = subprocess.call(cmd, shell=True)

fw_file_name = "B_PiStormsV" + new_firmware + ".hex"
cmd = "cd /var/tmp/upd/; wget " + download_url + "/" + fw_file_name
status = subprocess.call(cmd, shell=True)

if ( status != 0 ):
    m = ["Firmware Updater", "Error while downloading update:",
      fw_file_name]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)
else:
    psm.screen.termPrintAt(3, "Download complete")
    psm.screen.termPrintAt(4, "              ")

#
# perform the update
#
psm.screen.termPrintAt(3, "Upgrade in process...")
psm.screen.termPrintAt(4, "(this takes a while)")
psm.screen.termPrintAt(5, "Please wait...")
cmd = "cd /var/tmp/upd/;./fwupgrader PiStorms "+ fw_file_name + " -a"
print "cmd: " + str(cmd)
status = subprocess.call(cmd, shell=True)
if ( status != 0 ):
    m = ["Firmware Updater", "Error while performing update.",
      "status: " + str(status)]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)
else:
    version_json_update_field('status', 'Done')
    psm.screen.termPrintAt(3, "Update complete.")
    psm.screen.termPrintAt(4, "new Firmware is: ")
    psm.screen.termPrintAt(5, fw_file_name)
    psm.screen.termPrintAt(7, "Now Calibrate screen ...")
    psm.screen.termPrintAt(8, "Press GO button to continue")
    doExit = False
    while (doExit == False):
        if(psm.isKeyPressed() == True): # if the GO button is pressed
            doExit = True

    # screen calibration required after firmware change
    # force calibrations
    os.system("sudo python3 " +  homefolder + "/programs/utils/01-Calibrate.py force")
    sys.exit(0)
