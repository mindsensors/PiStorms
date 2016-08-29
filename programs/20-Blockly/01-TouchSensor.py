#!/usr/bin/env python

# ATTENTION!
# Please do not manually edit the contents of this file
# Only use the web interface for editing
# Otherwise, the file may no longer be editable using the web interface, or you changes may be lost

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
#Learn more product option visit us @  http://www.mindsensors.com

"""
--BLOCKLY FILE--
--START BLOCKS--
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9InZhcmlhYmxlc19zZXQiIGlkPSI3IS5eI0JlcHBrUjRGTmFpQSwrVSIgeD0iLTM0OCIgeT0iLTMzNCI+PGZpZWxkIG5hbWU9IlZBUiI+dG91Y2hTZW5zb3I8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJWQUxVRSI+PGJsb2NrIHR5cGU9InNlbnNvcnNfZXYzdG91Y2giIGlkPSJRbX5RcTkwMltbYmRnVGQtQUdqcCI+PGZpZWxkIG5hbWU9InNlbnNvcl9zZWxlY3RvciI+QkFTMTwvZmllbGQ+PGNvbW1lbnQgcGlubmVkPSJ0cnVlIiBoPSI0MyIgdz0iMjA5Ij5DcmVhdGUgYSBUb3VjaCBTZW5zb3IgT2JqZWN0PC9jb21tZW50PjwvYmxvY2s+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0iY29udHJvbHNfd2hpbGVVbnRpbCIgaWQ9Im94MHpsI3hOOGlENEFOYFJfM2xxIj48ZmllbGQgbmFtZT0iTU9ERSI+VU5USUw8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJCT09MIj48YmxvY2sgdHlwZT0ic3lzdGVtX2tleXByZXNzZWQiIGlkPSJzOEp+TGpQakVjLzV6TC1TPyx9XiI+PC9ibG9jaz48L3ZhbHVlPjxzdGF0ZW1lbnQgbmFtZT0iRE8iPjxibG9jayB0eXBlPSJjb250cm9sc19pZiIgaWQ9IiN6anFkbl1QQi1BPTY4YXlfZWovIj48bXV0YXRpb24gZWxzZT0iMSI+PC9tdXRhdGlvbj48dmFsdWUgbmFtZT0iSUYwIj48YmxvY2sgdHlwZT0ic2Vuc29yc19pc3RvdWNocHJlc3NlZCIgaWQ9IkosSkpBcXl6c1p0I25VbzA3SWRhIj48dmFsdWUgbmFtZT0ic2Vuc29yIj48YmxvY2sgdHlwZT0idmFyaWFibGVzX2dldCIgaWQ9InNnI0l6LFRQQmBxWEFkblJGfk9pIj48ZmllbGQgbmFtZT0iVkFSIj50b3VjaFNlbnNvcjwvZmllbGQ+PC9ibG9jaz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48c3RhdGVtZW50IG5hbWU9IkRPMCI+PGJsb2NrIHR5cGU9InNjcmVlbl9kcmF3Y2lyY2xlIiBpZD0iIzV6Om45U2llYktTWjM6ZSotPTIiPjxmaWVsZCBuYW1lPSJDT0xPUiI+I2ZmMDAwMDwvZmllbGQ+PGZpZWxkIG5hbWU9IkRJU1BMQVkiPlRSVUU8L2ZpZWxkPjxjb21tZW50IHBpbm5lZD0idHJ1ZSIgaD0iMTA4IiB3PSIxNDAiPklmIHNlbnNvciBpcyBwcmVzc2VkLCBkcmF3IGEgUmVkIGNpcmNsZS4KZWxzZSBkcmF3IGEgWWVsbG93IGNpcmNsZS48L2NvbW1lbnQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJeeV4lNWtmUi1ZdWNkPUlsazIqbCI+PGZpZWxkIG5hbWU9Ik5VTSI+MTAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iS1pVXz12UC4tMy0oIWh3VywwR10iPjxmaWVsZCBuYW1lPSJOVU0iPjEwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iRnRUSkRJO0w5eXUyODk4dWg7RHMiPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PHN0YXRlbWVudCBuYW1lPSJFTFNFIj48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSJFNSsodVRucUpTZjJre35VO2YjfCI+PGZpZWxkIG5hbWU9IkNPTE9SIj4jZmZmZjAwPC9maWVsZD48ZmllbGQgbmFtZT0iRElTUExBWSI+VFJVRTwvZmllbGQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJMdmA6fnI/OTR1ZShZWVlTV3EvUSI+PGZpZWxkIG5hbWU9Ik5VTSI+MTAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iYENfVERdKjAxeWtod11SQWtMZFMiPjxmaWVsZCBuYW1lPSJOVU0iPjEwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iUFFDcH5aNHx9eDlIWH1kekZBI1oiPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PC9ibG9jaz48L3N0YXRlbWVudD48L2Jsb2NrPjwvbmV4dD48L2Jsb2NrPjwveG1sPg==
703b48342778a912447c6d16452350a62a021914f4c295eab860f8087e5ed63e
--END BLOCKS--
"""


import LegoDevices
from PiStorms import PiStorms

touchSensor = None

ev3touch_BAS1 = LegoDevices.EV3TouchSensor("BAS1")

psm = PiStorms()


# Create a Touch Sensor Object
touchSensor = ev3touch_BAS1
while not (bool(psm.isKeyPressed())):
  if touchSensor.isPressed():
    # If sensor is pressed, draw a Red circle.
    # else draw a Yellow circle.
    psm.screen.fillCircle(100, 100, 30, (255, 0, 0), display = True)
  else:
    psm.screen.fillCircle(100, 100, 30, (255, 255, 0), display = True)
