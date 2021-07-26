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
# 06/22/16   Deepak     Initial development.
#

from PiStorms import PiStorms
import sys, subprocess

psm = PiStorms()
m = ["PiStorms",
 "Are you sure you want to shutdown?" ]
res = psm.screen.askQuestion(m,["OK", "Cancel"])

if (res == 0):
    cmd = "sudo psm_shutdown -h now"
    status = subprocess.call(cmd, shell=True)
