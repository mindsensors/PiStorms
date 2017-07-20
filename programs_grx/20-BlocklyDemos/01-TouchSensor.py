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
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9InN5c3RlbV9rZXlwcmVzc2VkIiBpZD0iclVBITBsRWJmLDspbVsxSX5LMmYiIHg9IjE3NSIgeT0iMTciPjwvYmxvY2s+PGJsb2NrIHR5cGU9ImNvbnRyb2xzX3doaWxlVW50aWwiIGlkPSJaUXgoXnBbWkBiWWUlS1RbK2hlNCIgeD0iMjYiIHk9IjM2Ij48ZmllbGQgbmFtZT0iTU9ERSI+VU5USUw8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJCT09MIj48YmxvY2sgdHlwZT0ic2NyZWVuX2lzdG91Y2hlZCIgaWQ9IlEyQE5aTHd1S2Alakh1YWdxUH5ZIj48L2Jsb2NrPjwvdmFsdWU+PHN0YXRlbWVudCBuYW1lPSJETyI+PGJsb2NrIHR5cGU9ImNvbnRyb2xzX2lmIiBpZD0iaS1GLSltbklxXV8xMW13MVItdDsiPjxtdXRhdGlvbiBlbHNlPSIxIj48L211dGF0aW9uPjxjb21tZW50IHBpbm5lZD0idHJ1ZSIgaD0iNjUiIHc9IjI1NCI+SWYgc2Vuc29yIGlzIHByZXNzZWQsIGRyYXcgYSByZWQgY2lyY2xlLgpPdGhlcndpc2UgZHJhdyBhIHllbGxvdyBjaXJjbGUuPC9jb21tZW50Pjx2YWx1ZSBuYW1lPSJJRjAiPjxibG9jayB0eXBlPSJHcm92ZV9CdXR0b25fX2lzUHJlc3NlZCIgaWQ9IisxfHZrLXJWXWc0TVVNVjRQMzFYIj48dmFsdWUgbmFtZT0ic2Vuc29yIj48YmxvY2sgdHlwZT0iR3JvdmVfQnV0dG9uIiBpZD0iKFN4TENxZzExaTB9aWRyd3w9NzIiPjxmaWVsZCBuYW1lPSJwb3J0Ij5CQkQxPC9maWVsZD48Y29tbWVudCBwaW5uZWQ9InRydWUiIGg9IjkxIiB3PSIzMzAiPlRoaXMgZGVtbyByZXF1aXJlcyBhIEdyb3ZlIHRvdWNoIHNlbnNvci4KQ29ubmVjdCB5b3VyIEdyb3ZlIHRvdWNoIHNlbnNvciB0byBCQkQxIHBvcnQsIG9yIHNlbGVjdCBhIGRpZmZlcmVudCBwb3J0IGZyb20gdGhlIGRyb3AtZG93biBsaXN0LjwvY29tbWVudD48L2Jsb2NrPjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjxzdGF0ZW1lbnQgbmFtZT0iRE8wIj48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSJZOyE2bktJMGBbQVhjdFJ0X3tTRSI+PGZpZWxkIG5hbWU9IkNPTE9SIj4jZmYwMDAwPC9maWVsZD48ZmllbGQgbmFtZT0iRElTUExBWSI+VFJVRTwvZmllbGQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIuW01dYChsaGtuQSNnRFV0alg5RyI+PGZpZWxkIG5hbWU9Ik5VTSI+MTAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iOTAucGJpeC8ram1yVng0d2dXdVsiPjxmaWVsZCBuYW1lPSJOVU0iPjEwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iOkxGZi4jREkwQV4wenUxdy1ocngiPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PHN0YXRlbWVudCBuYW1lPSJFTFNFIj48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSIoWUpVaTZKUFt3UUV6KVVXXSx1KCI+PGZpZWxkIG5hbWU9IkNPTE9SIj4jZmZmZjAwPC9maWVsZD48ZmllbGQgbmFtZT0iRElTUExBWSI+VFJVRTwvZmllbGQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJmXjdzTVMzRXNXaXlAUXAtMXIpaCI+PGZpZWxkIG5hbWU9Ik5VTSI+MTAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iK19bO0lYdGxweS85ST9gc1RGV10iPjxmaWVsZCBuYW1lPSJOVU0iPjEwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0id0BleHd4Yi1saSNoU18oOF1ZO0siPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PC9ibG9jaz48L3N0YXRlbWVudD48L2Jsb2NrPjwveG1sPg==
ae95c6a352d3a1eb46e48267c0875632a5de774795fbafae223bedffbc622e61
--END BLOCKS--
"""


from PiStorms import PiStorms
import GroveDevices

psm = PiStorms()

groveButton_BBD1 = GroveDevices.Grove_Button("BBD1")


bool(psm.isKeyPressed())

while not (psm.screen.isTouched()):
  # If sensor is pressed, draw a red circle.
  # Otherwise draw a yellow circle.
  # This demo requires a Grove touch sensor.
  # Connect your Grove touch sensor to BBD1 port, or select a different port from the drop-down list.
  if groveButton_BBD1.isPressed():
    psm.screen.fillCircle(100, 100, 30, (255, 0, 0), display = True)
  else:
    psm.screen.fillCircle(100, 100, 30, (255, 255, 0), display = True)
