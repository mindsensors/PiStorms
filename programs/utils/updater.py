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
# 05/02/16  Deepak      Initial development

from PiStorms import PiStorms
import sys
import socket
import subprocess
import ConfigParser

cfg_file = '/usr/local/mindsensors/conf/msdev.cfg'

print "updater program"
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

opt = str(sys.argv[1])

#m = ["Software Updater", "Not yet implemented.",
#  "option: " + opt]
#psm.screen.askQuestion(m,["OK"])

isConnected = available()
if (isConnected == False):
    m = ["Software Updater", "You are not connected to Internet.",
      "Internet connection required."]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)

if ( opt == "update:hardware" ):
    script = "hardware_update.py"

if ( opt == "update:software" ):
    script = "software_update.py"

if ( opt == "update:both" ):
    script = "software_update.py"

cmd = "sudo rm -rf /var/tmp/upd"
subprocess.call(cmd, shell=True)

cmd = "mkdir -p /var/tmp/upd"
subprocess.call(cmd, shell=True)

cmd = "sudo chmod a+rwx /var/tmp/upd"
subprocess.call(cmd, shell=True)

cmd = "cd /var/tmp/upd; wget " + download_url +"/" + script
subprocess.call(cmd, shell=True)

cmd = "cd /var/tmp/upd;chmod +x " + script
subprocess.call(cmd, shell=True)

cmd = "cd /var/tmp/upd; python " + script + " " + opt
subprocess.call(cmd, shell=True)

exit(-1)
