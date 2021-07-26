#!/usr/bin/env python3

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
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9ImNvbnRyb2xzX3doaWxlVW50aWwiIGlkPSJYLkM0WiU2RXJwKHhhUiVdLUVFUSIgeD0iNTYiIHk9IjY5Ij48ZmllbGQgbmFtZT0iTU9ERSI+VU5USUw8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJCT09MIj48YmxvY2sgdHlwZT0ic3lzdGVtX2tleXByZXNzZWQiIGlkPSI7ZHBEcnkjMVVNLERyQGBTJTs3XSI+PC9ibG9jaz48L3ZhbHVlPjxzdGF0ZW1lbnQgbmFtZT0iRE8iPjxibG9jayB0eXBlPSJtb3RvcnNfc2V0c3BlZWQiIGlkPSJfaz1nc1pHMnJocDVLRmwpZzRGOCI+PGZpZWxkIG5hbWU9Im1vdG9yX3NlbGVjdG9yIj5CQU0xPC9maWVsZD48dmFsdWUgbmFtZT0iU1BFRUQiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIhNEQodmFxal8jSD8lL2t4IVg2eSI+PGZpZWxkIG5hbWU9Ik5VTSI+NTA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PG5leHQ+PGJsb2NrIHR5cGU9InN5c3RlbV9zbGVlcCIgaWQ9Ijc/dF5TKXBLbmx2IyhLN0pDKVRBIj48dmFsdWUgbmFtZT0iVElNRSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlRGKkl9Y3kyZmpiKjc3a2Z7RHJaIj48ZmllbGQgbmFtZT0iTlVNIj4xPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjxuZXh0PjxibG9jayB0eXBlPSJtb3RvcnNfc2V0c3BlZWQiIGlkPSIoMTR8Q11NW2JMeWdwc0VZKkVWdCI+PGZpZWxkIG5hbWU9Im1vdG9yX3NlbGVjdG9yIj5CQU0xPC9maWVsZD48dmFsdWUgbmFtZT0iU1BFRUQiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJQLnlFLTh7NnV5bzEock5saHNlNSI+PGZpZWxkIG5hbWU9Ik5VTSI+MDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0ic3lzdGVtX3NsZWVwIiBpZD0iY2BAP0ZjWHUre2xnbW8rX0p7enciPjx2YWx1ZSBuYW1lPSJUSU1FIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iSC5Ed2UqYVleKUBCbzIlVXpUKVoiPjxmaWVsZCBuYW1lPSJOVU0iPjE8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L3N0YXRlbWVudD48L2Jsb2NrPjwveG1sPg==
184e880526960bd774d2be11aadd04c103d1c18b1cfb9bf66e80c527d4a8051e
--END BLOCKS--
"""


from PiStorms import PiStorms
import time

psm = PiStorms()


while not bool(psm.isKeyPressed()):
  psm.BAM1.setSpeed(50)
  time.sleep(1)
  psm.BAM1.setSpeed(0)
  time.sleep(1)
