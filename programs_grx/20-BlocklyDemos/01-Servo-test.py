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
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9ImNvbnRyb2xzX3doaWxlVW50aWwiIGlkPSJwWSVdWHlSbkNYallYKVpnTURxJSIgeD0iNDkiIHk9IjQ3Ij48ZmllbGQgbmFtZT0iTU9ERSI+VU5USUw8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJCT09MIj48YmxvY2sgdHlwZT0ic3lzdGVtX2tleXByZXNzZWQiIGlkPSJzZTJJSyk1ck9gfCt5Wy1NdVdXZiI+PC9ibG9jaz48L3ZhbHVlPjxzdGF0ZW1lbnQgbmFtZT0iRE8iPjxibG9jayB0eXBlPSJzZXJ2b19zZXRTcGVlZCIgaWQ9InteWmdjKGUoTlgvSSl0emhzUj10Ij48ZmllbGQgbmFtZT0ic3BlZWQiPjUwPC9maWVsZD48dmFsdWUgbmFtZT0ic2Vydm8iPjxibG9jayB0eXBlPSJzZXJ2b19pbml0IiBpZD0iYDQ7Nn1XdkZifTZ9ZzlVdEVGb1EiPjxmaWVsZCBuYW1lPSJwb3J0Ij5CQlMxPC9maWVsZD48L2Jsb2NrPjwvdmFsdWU+PG5leHQ+PGJsb2NrIHR5cGU9InN5c3RlbV9zbGVlcCIgaWQ9InBBTDt0ZSx+ZWFoaCMyVj1yMmlSIj48dmFsdWUgbmFtZT0iVElNRSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlosVHh4KjRvKVYoeE4yQHdTW3YhIj48ZmllbGQgbmFtZT0iTlVNIj4xPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjxuZXh0PjxibG9jayB0eXBlPSJzZXJ2b19zdG9wIiBpZD0iLn44TjE4STt1dCUsUjZnc2V2WVIiPjx2YWx1ZSBuYW1lPSJzZXJ2byI+PGJsb2NrIHR5cGU9InNlcnZvX2luaXQiIGlkPSJvM1theUw9fVcsMk90XTNjSWUtTCI+PGZpZWxkIG5hbWU9InBvcnQiPkJCUzE8L2ZpZWxkPjwvYmxvY2s+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0ic3lzdGVtX3NsZWVwIiBpZD0icGFSWHBrcWpnMmFNVDN7cX1zYnQiPjx2YWx1ZSBuYW1lPSJUSU1FIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iYUtjMnBTKWdaQ2hoOThkRWlgeysiPjxmaWVsZCBuYW1lPSJOVU0iPjE8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L3N0YXRlbWVudD48L2Jsb2NrPjwveG1sPg==
28cd1eb4167fe114e80579ba1f83a8cc8a84cc4db539e2289261b45303015824
--END BLOCKS--
"""


from PiStorms_GRX import PiStorms_GRX
from PiStorms_GRX import RCServo
import time

grx = PiStorms_GRX()

servo_BBS1 = RCServo("BBS1")


while not (grx.isKeyPressed()):
  servo_BBS1.setSpeed(50)
  time.sleep(1)
  servo_BBS1.stop()
  time.sleep(1)
