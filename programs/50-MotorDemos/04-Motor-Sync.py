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
# 04/15/16   Deepak     Initial development.
#

from PiStorms import PiStorms
psm = PiStorms()

m = ["Motors-Synchronised", "Connect motors to Bank A M1 &M2.",
  "And click OK to continue"]
psm.screen.askQuestion(m,["OK"])

# Start the motor at speed 75 for unlimited duration.
psm.BAM1.setSpeedSync(45)

m = ["Motor-Demo", "Both Motors should be running now",
  "click STOP to stop"]
psm.screen.askQuestion(m,["STOP"])

# set the motor to float while stopping
psm.BAM1.floatSync()

m = ["Motor-Demo", "Motor should be stopped now",
  "click EXIT to exit program"]
psm.screen.askQuestion(m,["EXIT"])
