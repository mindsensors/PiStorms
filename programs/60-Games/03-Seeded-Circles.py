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


from PiStorms import PiStorms
import random, time

psm = PiStorms()

#
# To exit this program, press & hold GO button and touch the screen
#

psm.screen.termPrintAt(1, "To Exit: press & hold GO button")
psm.screen.termPrintAt(2, "and touch the screen.")
time.sleep(4)

while not (bool(psm.isKeyPressed()) and psm.screen.isTouched()):
  if ( psm.screen.isTouched() ):
    x = psm.screen.TS_X()
    y = psm.screen.TS_Y()
    tsx = psm.screen.TS_To_ImageCoords_X(x,y)
    tsy = psm.screen.TS_To_ImageCoords_Y(x,y)

    isTouched = True
    tFactor = 2
  else:
    isTouched = False
    tFactor = 0

  if (isTouched):
    x = tsx
    y = tsy
  else:
    x = (random.randint(30, 300))
    y = (random.randint(30, 300))
  psm.screen.fillCircle(x, y,
               (random.randint(10, 35+(tFactor*30))),
               (0, 0, random.randint(150,255)),
               display = True)
  if (isTouched):
    x = tsx
    y = tsy
  else:
    x = (random.randint(30, 300))
    y = (random.randint(30, 300))
  psm.screen.fillCircle(x, y,
               (random.randint(10, 35+(tFactor*30))),
               (random.randint(150,255), 0, 0),
               display = True)
  if (isTouched):
    x = tsx
    y = tsy
  else:
    x = (random.randint(30, 250))
    y = (random.randint(30, 250))
  psm.screen.fillCircle(x, y,
               (random.randint(10, 20+(tFactor*30))),
               ((random.randint(50,255), random.randint(50,255), 0)),
               display = True)
  if (isTouched):
    x = tsx
    y = tsy
  else:
    x = (random.randint(30, 300))
    y = (random.randint(30, 300))
  psm.screen.fillCircle(x, y,
               (random.randint(10, 20+(tFactor*30))),
               (51, 255, 51),
               display = True)
  if (isTouched):
    x = tsx
    y = tsy
  else:
    x = (random.randint(80, 300))
    y = (random.randint(70, 300))
  psm.screen.fillCircle(x, y,
               (random.randint(20, 40+(tFactor*30))),
               (random.randint(110,151), random.randint(150,204), random.randint(60,255)),
               display = True)
