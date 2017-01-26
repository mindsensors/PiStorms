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
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author           Comments
# 01/20/17  Seth Tenembaum   Run on startup to upgrade any firmware below V2.10 for new touchscreen calibration strategy
#

import os

from mindsensorsUI import mindsensorsUI
from PiStormsCom import PiStormsCom
ui = mindsensorsUI()
comm = PiStormsCom()

fwver = comm.GetFirmwareVersion()
if fwver != 'ReadErr' and fwver < 'V2.10':
    ui.askQuestion(["Firmware Updater", "The hardware potion of this update", "will now run. Please remove", "all sensors and motors."], ["Press GO to continue..."], touch = False, goBtn = True)
    ui.forceMessage(["Upgrade in process...", "This will take a minute.", "Please wait..."])
    os.system('cd /usr/local/bin/fwupgrader;./fwupgrader PiStorms B_PiStormsV2.10.hex -a')
    ui.askQuestion(["Update complete.", "The hardware update was successful.", "To complete it, press GO to shutdown.", "Then disconnect and reconnect power", "and press GO to power on.", "You will then calibrate the screen."], ["Press GO to continue..."], touch = False, goBtn = True)
    os.system("sleep 1; sudo psm_shutdown -h now")
