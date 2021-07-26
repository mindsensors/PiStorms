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

m = ["Motor-Demo", "Connect motor to Bank A M1.",
 "Motor will run for 5 seconds, ",
 "and stop with float.",
  "Click OK to continue"]
psm.screen.askQuestion(m,["OK"])

# run motor for 5 seconds, and at the completion,
# brake while stopping and hold position while stopped
psm.BAM1.runSecs(5, 75, False)

m = ["Motor-Demo", "Motor is now turning for 5 seconds",
  "and will stop with float.", "Click EXIT to exit program"]
psm.screen.askQuestion(m,["EXIT"])
