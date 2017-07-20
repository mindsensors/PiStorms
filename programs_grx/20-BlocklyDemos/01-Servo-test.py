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
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9ImNvbnRyb2xzX3doaWxlVW50aWwiIGlkPSJwWSVdWHlSbkNYallYKVpnTURxJSIgeD0iNDkiIHk9IjQ3Ij48ZmllbGQgbmFtZT0iTU9ERSI+VU5USUw8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJCT09MIj48YmxvY2sgdHlwZT0ic2NyZWVuX2lzdG91Y2hlZCIgaWQ9IlhsS05YPStgMDFANCk6LUh8VTZkIj48L2Jsb2NrPjwvdmFsdWU+PHN0YXRlbWVudCBuYW1lPSJETyI+PGJsb2NrIHR5cGU9InNlcnZvX3NldFNwZWVkIiBpZD0ie15aZ2MoZShOWC9JKXR6aHNSPXQiPjxmaWVsZCBuYW1lPSJzcGVlZCI+NTA8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJzZXJ2byI+PGJsb2NrIHR5cGU9InNlcnZvX2luaXQiIGlkPSJgNDs2fVd2RmJ9Nn1nOVV0RUZvUSI+PGZpZWxkIG5hbWU9InBvcnQiPkJCUzE8L2ZpZWxkPjwvYmxvY2s+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0ic3lzdGVtX3NsZWVwIiBpZD0icEFMO3RlLH5lYWhoIzJWPXIyaVIiPjx2YWx1ZSBuYW1lPSJUSU1FIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iWixUeHgqNG8pVih4TjJAd1NbdiEiPjxmaWVsZCBuYW1lPSJOVU0iPjE8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PG5leHQ+PGJsb2NrIHR5cGU9InNlcnZvX3N0b3AiIGlkPSIufjhOMThJO3V0JSxSNmdzZXZZUiI+PHZhbHVlIG5hbWU9InNlcnZvIj48YmxvY2sgdHlwZT0ic2Vydm9faW5pdCIgaWQ9Im8zW2F5TD19VywyT3RdM2NJZS1MIj48ZmllbGQgbmFtZT0icG9ydCI+QkJTMTwvZmllbGQ+PC9ibG9jaz48L3ZhbHVlPjxuZXh0PjxibG9jayB0eXBlPSJzeXN0ZW1fc2xlZXAiIGlkPSJwYVJYcGtxamcyYU1UM3txfXNidCI+PHZhbHVlIG5hbWU9IlRJTUUiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJhS2MycFMpZ1pDaGg5OGRFaWB7KyI+PGZpZWxkIG5hbWU9Ik5VTSI+MTwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvbmV4dD48L2Jsb2NrPjwvbmV4dD48L2Jsb2NrPjwvbmV4dD48L2Jsb2NrPjwvc3RhdGVtZW50PjwvYmxvY2s+PGJsb2NrIHR5cGU9InN5c3RlbV9rZXlwcmVzc2VkIiBpZD0ic2UySUspNXJPYHwreVstTXVXV2YiIHg9IjE5MyIgeT0iNjciPjwvYmxvY2s+PC94bWw+
28942bc0e658b02dd3571b5e230b7eef00f8a78962dc91f2e210dec6733ea248
--END BLOCKS--
"""


from PiStorms import PiStorms
from PiStorms_GRX import RCServo
import time

psm = PiStorms()

servo_BBS1 = RCServo("BBS1")


while not (psm.screen.isTouched()):
  servo_BBS1.setSpeed(50)
  time.sleep(1)
  servo_BBS1.stop()
  time.sleep(1)

bool(psm.isKeyPressed())
