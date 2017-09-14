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

import os, socket
import ConfigParser
from PiStorms import PiStorms
psm = PiStorms()

config = ConfigParser.RawConfigParser()
config.read("/usr/local/mindsensors/conf/msdev.cfg")
homefolder = config.get("msdev", "homefolder")
try:
    with open(os.path.join(homefolder, ".version"), "r") as f:
        version_no = f.readline().strip()
except IOError:
    version_no = "unknown"

psm.screen.drawDisplay("About Me")
psm.screen.termPrintln("Device: {}".format(psm.GetDeviceId().rstrip("\0")))
psm.screen.termPrintln("Feature: {}".format(psm.psc.GetDeviceFeatures().rstrip("\0")))
psm.screen.termPrintln("f/w version: {}".format(psm.GetFirmwareVersion().rstrip("\0")))
psm.screen.termPrintln("s/w version: {}".format(version_no))
psm.screen.termPrintln("Hostname: {}".format(socket.gethostname()))
psm.screen.termPrintln("Battery: {}V".format(psm.battVoltage()))

def getIP(iface):
    ip = os.popen("ifconfig {} | tail +2 | awk '/inet / {{print $2}}'".format(iface)).read()
    return ip if ip != '' else "not present"
def updateNetworkInfo():
    psm.screen.termPrintAt(6, "eth0: {}".format(getIP("eth0")))
    psm.screen.termPrintAt(7, "wlan0: {}".format(getIP("wlan0")))
psm.untilKeyPressOrTouch(updateNetworkInfo)

psm.screen.termPrintAt(8, "Exiting to menu")
