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
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9ImNvbnRyb2xzX3doaWxlVW50aWwiIGlkPSJaUXgoXnBbWkBiWWUlS1RbK2hlNCIgeD0iMjYiIHk9IjM2Ij48ZmllbGQgbmFtZT0iTU9ERSI+VU5USUw8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJCT09MIj48YmxvY2sgdHlwZT0ic3lzdGVtX2tleXByZXNzZWQiIGlkPSJyVUEhMGxFYmYsOyltWzFJfksyZiI+PC9ibG9jaz48L3ZhbHVlPjxzdGF0ZW1lbnQgbmFtZT0iRE8iPjxibG9jayB0eXBlPSJjb250cm9sc19pZiIgaWQ9ImktRi0pbW5JcV1fMTFtdzFSLXQ7Ij48bXV0YXRpb24gZWxzZT0iMSI+PC9tdXRhdGlvbj48Y29tbWVudCBwaW5uZWQ9InRydWUiIGg9IjY1IiB3PSIyNTQiPklmIHNlbnNvciBpcyBwcmVzc2VkLCBkcmF3IGEgcmVkIGNpcmNsZS4KT3RoZXJ3aXNlIGRyYXcgYSB5ZWxsb3cgY2lyY2xlLjwvY29tbWVudD48dmFsdWUgbmFtZT0iSUYwIj48YmxvY2sgdHlwZT0iR3JvdmVfQnV0dG9uX19pc1ByZXNzZWQiIGlkPSIrMXx2ay1yVl1nNE1VTVY0UDMxWCI+PHZhbHVlIG5hbWU9InNlbnNvciI+PGJsb2NrIHR5cGU9Ikdyb3ZlX0J1dHRvbiIgaWQ9IihTeExDcWcxMWkwfWlkcnd8PTcyIj48ZmllbGQgbmFtZT0icG9ydCI+QkJEMTwvZmllbGQ+PGNvbW1lbnQgcGlubmVkPSJ0cnVlIiBoPSI5MSIgdz0iMzMwIj5UaGlzIGRlbW8gcmVxdWlyZXMgYSBHcm92ZSB0b3VjaCBzZW5zb3IuCkNvbm5lY3QgeW91ciBHcm92ZSB0b3VjaCBzZW5zb3IgdG8gQkJEMSBwb3J0LCBvciBzZWxlY3QgYSBkaWZmZXJlbnQgcG9ydCBmcm9tIHRoZSBkcm9wLWRvd24gbGlzdDwvY29tbWVudD48L2Jsb2NrPjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjxzdGF0ZW1lbnQgbmFtZT0iRE8wIj48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSJZOyE2bktJMGBbQVhjdFJ0X3tTRSI+PGZpZWxkIG5hbWU9IkNPTE9SIj4jZmYwMDAwPC9maWVsZD48ZmllbGQgbmFtZT0iRElTUExBWSI+VFJVRTwvZmllbGQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIuW01dYChsaGtuQSNnRFV0alg5RyI+PGZpZWxkIG5hbWU9Ik5VTSI+MTAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iOTAucGJpeC8ram1yVng0d2dXdVsiPjxmaWVsZCBuYW1lPSJOVU0iPjEwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iOkxGZi4jREkwQV4wenUxdy1ocngiPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PHN0YXRlbWVudCBuYW1lPSJFTFNFIj48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSIoWUpVaTZKUFt3UUV6KVVXXSx1KCI+PGZpZWxkIG5hbWU9IkNPTE9SIj4jZmZmZjAwPC9maWVsZD48ZmllbGQgbmFtZT0iRElTUExBWSI+VFJVRTwvZmllbGQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJmXjdzTVMzRXNXaXlAUXAtMXIpaCI+PGZpZWxkIG5hbWU9Ik5VTSI+MTAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iK19bO0lYdGxweS85ST9gc1RGV10iPjxmaWVsZCBuYW1lPSJOVU0iPjEwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0id0BleHd4Yi1saSNoU18oOF1ZO0siPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PC9ibG9jaz48L3N0YXRlbWVudD48L2Jsb2NrPjwveG1sPg==
7c7ca2fd876e1d18344ac8b521712cf530bbdf2cd291997fee73488ee0394f02
--END BLOCKS--
"""


from PiStorms_GRX import PiStorms_GRX
import GroveDevices
from PiStorms import PiStorms

grx = PiStorms_GRX()

groveButton_BBD1 = GroveDevices.Grove_Button("BBD1")

psm = PiStorms()


while not (grx.isKeyPressed()):
  # If sensor is pressed, draw a red circle.
  # Otherwise draw a yellow circle.
  # This demo requires a Grove touch sensor.
  # Connect your Grove touch sensor to BBD1 port, or select a different port from the drop-down list
  if groveButton_BBD1.isPressed():
    psm.screen.fillCircle(100, 100, 30, (255, 0, 0), display = True)
  else:
    psm.screen.fillCircle(100, 100, 30, (255, 255, 0), display = True)
