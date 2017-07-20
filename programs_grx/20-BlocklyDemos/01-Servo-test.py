#!/usr/bin/env python

# ATTENTION!
# Please do not manually edit the contents of this file
# Only use the web interface for editing
# Otherwise, the file may no longer be editable using the web interface, or you changes may be lost

# Copyright (c) 2017 mindsensors.com
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
#Learn more product option visit us @  http://www.mindsensors.com

"""
--BLOCKLY FILE--
--START BLOCKS--
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9InN5c3RlbV91bnRpbGtleXByZXNzIiBpZD0iRWVnVjovXVZmOVJvY2chOjg3Ky0iIHg9IjQzIiB5PSI0NCI+PHN0YXRlbWVudCBuYW1lPSJmdW5jIj48YmxvY2sgdHlwZT0ic2Vydm9fc2V0U3BlZWQiIGlkPSJ7XlpnYyhlKE5YL0kpdHpoc1I9dCI+PGZpZWxkIG5hbWU9InNwZWVkIj41MDwvZmllbGQ+PHZhbHVlIG5hbWU9InNlcnZvIj48YmxvY2sgdHlwZT0ic2Vydm9faW5pdCIgaWQ9ImA0OzZ9V3ZGYn02fWc5VXRFRm9RIj48ZmllbGQgbmFtZT0icG9ydCI+QkJTMTwvZmllbGQ+PC9ibG9jaz48L3ZhbHVlPjxuZXh0PjxibG9jayB0eXBlPSJzeXN0ZW1fc2xlZXAiIGlkPSJwQUw7dGUsfmVhaGgjMlY9cjJpUiI+PHZhbHVlIG5hbWU9IlRJTUUiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJaLFR4eCo0bylWKHhOMkB3U1t2ISI+PGZpZWxkIG5hbWU9Ik5VTSI+MTwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0ic2Vydm9fc3RvcCIgaWQ9Ii5+OE4xOEk7dXQlLFI2Z3NldllSIj48dmFsdWUgbmFtZT0ic2Vydm8iPjxibG9jayB0eXBlPSJzZXJ2b19pbml0IiBpZD0ibzNbYXlMPX1XLDJPdF0zY0llLUwiPjxmaWVsZCBuYW1lPSJwb3J0Ij5CQlMxPC9maWVsZD48L2Jsb2NrPjwvdmFsdWU+PG5leHQ+PGJsb2NrIHR5cGU9InN5c3RlbV9zbGVlcCIgaWQ9InBhUlhwa3FqZzJhTVQze3F9c2J0Ij48dmFsdWUgbmFtZT0iVElNRSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9ImFLYzJwUylnWkNoaDk4ZEVpYHsrIj48ZmllbGQgbmFtZT0iTlVNIj4xPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC9uZXh0PjwvYmxvY2s+PC9uZXh0PjwvYmxvY2s+PC9uZXh0PjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PC9ibG9jaz48L3htbD4=
c70aaded7b0b66cce0501c89245ba00e38e6f17d585cfc04570046128708434e
--END BLOCKS--
"""


from PiStorms_GRX import RCServo
import time
from PiStorms_GRX import PiStorms_GRX

servo_BBS1 = RCServo("BBS1")

grx = PiStorms_GRX()


def leCUI8hutHZI4480Dc():
  servo_BBS1.setSpeed(50)
  time.sleep(1)
  servo_BBS1.stop()
  time.sleep(1)
grx.untilKeyPress(leCUI8hutHZI4480Dc)
