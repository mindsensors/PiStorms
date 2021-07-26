#!/usr/bin/env python
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
# Date         Author          Comments
# June 2016    Roman Bohuk     Initial Authoring
# July 2017    Seth Tenembaum  Add alternate skin for GRX

import Adafruit_ILI9341
import os
import datetime
from PIL import Image, ImageDraw
from fcntl import flock, LOCK_EX, LOCK_UN
import configparser

class ILI9341(Adafruit_ILI9341.ILI9341):
    def __init__(self, dc, spi, rst=None, gpio=None, width=Adafruit_ILI9341.ILI9341_TFTWIDTH,
        height=Adafruit_ILI9341.ILI9341_TFTHEIGHT):
        Adafruit_ILI9341.ILI9341.__init__(self, dc, spi, rst, gpio, width,
        height)
        self.touch_record_path = "/tmp/pistormstouchrecord"
        self.record_path = "/tmp/pistormsrecord"
        config = configparser.RawConfigParser()
        config.read("/usr/local/mindsensors/conf/msdev.cfg")
        if "GRX" in config.get('msdev', 'device'):
            self.background_path = "/usr/local/mindsensors/images/artwork-for-grx-images.png"
        else:
            self.background_path = "/usr/local/mindsensors/images/artwork-for-images.png"
        self.x = -1
        self.y = -1
        self.store = False
        self.mutex = open("/var/lock/ili9341", "w+")
        # allow lock to be modified without sudo permissions
    #    os.chown("/var/lock/ili9341", 1000, 1000) # pi's UID, GID

    # PIL.ImageDraw.Draw creates an object that draws in-place, so the mutex is required
    def draw(self):
        flock(self.mutex, LOCK_EX)
        r = super(ILI9341, self).draw()
        flock(self.mutex, LOCK_UN)
        return r

    def save(self, path=None, img=None, extension="PNG", includeBg=False):
        """Writes the buffer to a file"""
        # If no path is specified, store the file in the current folder with timestamp
        tstamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S%f')[:-3]
        path = "/var/tmp/ps_images/%s.%s" % (tstamp, extension) if path is None else path
        # If no PIL Image specified, store the whole screen
        dat = self.getBuffer() if img is None else img
        dat = self.mergeBackground() if includeBg else dat
        # Save to file
        dat.save(path, extension)

    def getBuffer(self):
        """Gets the copy of a buffer"""
        return self.buffer.transpose(Image.ROTATE_270)

    def getSectionBounds(self, left, upper, right, lower):
        """Gets the section of the screen"""
        return self.getBuffer().crop((left, upper, right, lower))

    def getSection(self, x, y, width, height):
        """Gets the section of the screen with same parameters as mindensorsUI"""
        return self.get_section_bounds(x, y, x + width, y + height)

    def getPixel(self, x, y):
        """Gets the RGB of a pixel"""
        return self.getBuffer().getpixel((x, y))

    def recordFileExists(self):
        return os.path.isfile(self.record_path)

    def recordTouchFileExists(self):
        return os.path.isfile(self.touch_record_path)

    def startRecording(self, frames="-", includeBg=True):
        with open(self.record_path, "w+") as f: f.write(frames + "\n" + str(int(includeBg)))

    def startTouchRecording(self, frames="-"):
        with open(self.touch_record_path, "w+") as f: f.write(frames + "\n1")

    def stopRecording(self):
        if self.recordFileExists(): os.remove(self.record_path)

    def stopTouchRecording(self):
        if self.recordTouchFileExists(): os.remove(self.touch_record_path)

    def readRecordingCount(self):
        if self.recordFileExists():
            with open(self.record_path, "r") as f:
                return f.read().split("\n")
        else: return ["",""]

    def readTouchRecordingCount(self):
        if self.recordTouchFileExists():
            with open(self.touch_record_path, "r") as f:
                return f.read().split("\n")
        else: return ["",""]

    def isTakingFrames(self, fileContents):
        return fileContents == "-" or fileContents.isdigit()

    def isStoringWithBg(self, fileContents):
        return str(fileContents) == "1"

    def decrementRecordingCount(self, fileContents, includeBgIn):
        toWrite = ""
        if fileContents == "-": toWrite = "-"
        elif fileContents.isdigit():
            temp = int(fileContents)-1
            toWrite = str(temp) if temp > 0 else ""
        if toWrite == "": self.stopRecording()
        else: self.startRecording(toWrite, includeBgIn)

    def decrementTouchRecordingCount(self, fileContents, includeBgIn):
        toWrite = ""
        if fileContents == "-": toWrite = "-"
        elif fileContents.isdigit():
            temp = int(fileContents)-1
            toWrite = str(temp) if temp > 0 else ""
        if toWrite == "": self.stopTouchRecording()
        else: self.startTouchRecording(toWrite, includeBgIn)

    def display(self, image=None):
        flock(self.mutex, LOCK_EX)
        content = self.readRecordingCount()
        if len(content) == 2 and self.isTakingFrames(content[0]):
            self.decrementRecordingCount(content[0],self.isStoringWithBg(content[1]))
            if self.isStoringWithBg(content[1]): self.save(includeBg=True)
            else: self.save(includeBg=False)
        if image is None: image = self.buffer
        self.set_window()
        pixelbytes = list(Adafruit_ILI9341.image_to_data(image))
        self.data(pixelbytes)
        if self.store and self.isTakingFrames(self.readTouchRecordingCount()[0]):
            image = Image.new('RGBA',(568, 428))
            draw = ImageDraw.Draw(image)
            draw.ellipse((122+320-self.y, 12+self.x, 152+320-self.y, 42+self.x), fill = 'red', outline ='red')
            self.save(img=image)
            self.store = False
            self.x, self.y = -1, -1
        flock(self.mutex, LOCK_UN)

    def mergeBackground(self):
        bg = Image.open(self.background_path)
        bg.paste(self.getBuffer(), (137, 27))
        return bg
