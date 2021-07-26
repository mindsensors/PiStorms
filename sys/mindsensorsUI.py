#!/usr/bin/env python3
#
# Copyright (c) 2015 mindsensors.com
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
# July 2015  Henry     Initial Authoring
# Oct. 2015  Nitin     Editing and improved functionality
# Oct. 2015  Michael   Comments and documentation
# 10/18/15   Deepak    UI improvements
# 7/12/16    Roman     Touch screen record frame
# 10/7/16    Seth      Battery indicator, line methods
# 1/25/17    Seth      Additional dialog options

from PiStormsCom import PiStormsCom
from PiStormsCom_GRX import GRXCom
import time, os, sys, math
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap
import MS_ILI9341 as TFT
from Adafruit_ILI9341 import ILI9341_INVOFF
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import configparser

## @package mindsensorsUI
#  This module contains classes and functions necessary for use of LCD touchscreen on mindsensors.com products


## mindsensorsUI: this class provides functions for touchscreen LCD on mindsensors.com products for read and write operations.
#  There is no need to initialize this class unless using the LCD screen alone. Normal initialization will be performed automatically when instantiating a PiStorms object.
class mindsensorsUI():
    ## Constant to specify black color
    PS_BLACK = (0,0,0)
    ## Constant to specify blue color
    PS_BLUE = (0,0,255)
    ## Constant to specify red color
    PS_RED = (255,0,0)
    ## Constant to specify green color
    PS_GREEN = (0,255,0)
    ## Constant to specify cyan color
    PS_CYAN = (0,255,255)
    ## Constant to specify magenta color
    PS_MAGENTA = (255,0,255)
    ## Constant to specify yellow color
    PS_YELLOW = (255,255,0)
    ## Constant to specify white color
    PS_WHITE = (255,255,255)

    ## Constant to defualt screen width
    PS_SCREENWIDTH = 240
    ## Constant to defualt screen height
    PS_SCREENHEIGHT = 320

    ### @cond Doxygen_ignore_this
    ## Constant to specify terminal mode
    PS_MODE_TERMINAL = 0
    ## Constant to specify pop-up mode
    PS_MODE_POPUP = 1
    ## Constant to specify dead mode
    PS_MODE_DEAD = 2

    ## Dictionary of default emnpty terminal buffer
    terminalBuffer = [""]*20
    ## Variable of default terminal cursor position
    terminalCursor = 0
    ## Variable of default mode
    currentMode = 0
    ## Variable of default rotation
    currentRotation = 0
    ## Instance to initialize the display
    disp = TFT.ILI9341(24, rst=25, spi=SPI.SpiDev(0,0,max_speed_hz=64000000))
    ## Variable of default button text
    buttonText = ["OK","Cancel"]
    ## Variable of default pop-up text
    popupText = ["Do you wish to continue?"]

    ## Variable of default draw arrow state
    drawArrowsbool = False

    x = 0
    y = 0
    ### @endcond

    ## Initialize the UI device.
    #  @param self The object pointer.
    #  @param name The display title that will appear at the top of the LCD touchscreen. Optional, defaults to "PiStorms" (unused).
    #  @param rotation The rotation of the LCD touchscreen. Optional, defaults to 3 (standard rotation).
    #  @remark
    #  There is no need to use this function directly. To initialize the mindsensorsUI class in your program:
    #  @code
    #  from mindsensorsUI import mindsensorsUI
    #  ...
    #  screen = mindsensorsUI()
    #  @endcode
    def __init__(self, name = "PiStorms", rotation = 3):
        config = configparser.RawConfigParser()
        config.read("/usr/local/mindsensors/conf/msdev.cfg")
        if "GRX" in config.get('msdev', 'device'):
            self.comm = GRXCom
        else:
            self.comm = PiStormsCom()
        # note self.comm is only used to getTouchscreenCoordinates and to getKeyPressCount
        self.disp.begin()
        self.clearScreen()
        self.disp.command(ILI9341_INVOFF)

        if(rotation in range(4)):
            self.currentRotation = rotation
        self.refresh()
        self.myname = name
        #self.drawDisplay(name, display=False)

    ## Dumps the screen buffer
    #  @param self The object pointer.
    def dumpTerminal(self):
        self.terminalBuffer = [""]*20
        self.terminalCursor = 0
        if(self.getMode() == self.PS_MODE_TERMINAL):
            self.refresh()

    ## Sets the mode (Experienced users)
    #  @param self The object pointer.
    #  @param mode The new mode: PS_MODE_TERMINAL, PS_MODE_POPUP, or PS_MODE_DEAD. Optional, defaults to PS_MODE_TERMINAL.
    def setMode(self, mode = 0):
        if(mode<0 or mode>2):
            self.currentMode = self.PS_MODE_DEAD
        else:
            self.currentMode = mode
            self.refresh()

    ## Returns the value of the mode (Experienced users)
    #  @param self The object pointer.
    def getMode(self):
        return self.currentMode

    ## Draw a rectangle with rounded edges on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the rectangle.
    #  @param y The upper left y coordinate of the rectangle.
    #  @param width The width of the rectangle.
    #  @param height The height of the rectangle.
    #  @param radius The arc of the rectangle corners.
    #  @param fill The color of the inside of the rectangle. Optional, defaults to white.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    def fillRoundRect(self, x, y, width, height, radius, fill = (255,255,255), display = True):
        self.fillRect(x,y + radius,width, height-(radius*2), fill = fill, display = False)
        self.fillRect(x + radius, y, width - (radius*2), height, fill = fill, display = False)
        self.fillCircle(x + radius, y + radius, radius, fill = fill, display = False)
        self.fillCircle(x + width - radius, y + radius, radius, fill = fill, display = False)
        self.fillCircle(x + radius, y + height - radius, radius, fill = fill, display = False)
        self.fillCircle(x + width - radius,y + height - radius, radius, fill = fill, display = display)

    ## Calculates the x-coordinate of the screen upon rotation (INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param x x value in the current rotation's coordinate system
    #  @param y y value in the current rotation's coordinate system
    #  @return x value for the corresponding point in the display's coordinate system (for writing to TFT)
    def screenXFromImageCoords(self, x, y):
        cr = self.currentRotation
        if(cr == 0):
            return x
        if(cr == 1):
            return self.PS_SCREENWIDTH-y
        if(cr == 2):
            return self.PS_SCREENWIDTH-x
        if(cr == 3):
            return y

    ## Calculates the y-coordinate of the screen upon rotation (INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param x x value in the current rotation's coordinate system
    #  @param y y value in the current rotation's coordinate system
    #  @return y value for the corresponding point in the display's coordinate system (for writing to TFT)
    def screenYFromImageCoords(self, x, y):
        cr = self.currentRotation
        if(cr == 0):
            return y
        if(cr == 1):
            return x
        if(cr == 2):
            return self.PS_SCREENHEIGHT-y
        if(cr == 3):
            return self.PS_SCREENHEIGHT-x

    ## Calculates display x-coordinate from touchscreen values, adjusted for rotation (INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param x x value in the touchscreen's coordinate system (read from registers)
    #  @param y y value in the touchscreen's coordinate system (read from registers)
    #  @return x value for the corresponding point in the current rotation's coordinate system
    def TS_To_ImageCoords_X(self, x, y):
        cr = self.currentRotation
        if(cr == 0):
            return y
        if(cr == 1):
            return x
        if(cr == 2):
            return self.PS_SCREENWIDTH-y
        if(cr == 3):
            return self.PS_SCREENHEIGHT-x

    ## Calculates display y-coordinate from touchscreen values, adjusted for rotation (INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param x x value in the touchscreen's coordinate system (read from registers)
    #  @param y y value in the touchscreen's coordinate system (read from registers)
    #  @return y value for the corresponding point in the current rotation's coordinate system
    def TS_To_ImageCoords_Y(self, x, y):
        cr = self.currentRotation
        if(cr == 0):
            return x
        if(cr == 1):
            return self.PS_SCREENWIDTH-y
        if(cr == 2):
            return self.PS_SCREENHEIGHT-x
        if(cr == 3):
            return y

    ## Displays rotated text (INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param image The image used for creating text
    #  @param text The text to display on the screen
    #  @param position The position of the text as a set of x and y-coordinates
    #  @param angle The angle at which to rotate the text
    #  @param font The font of the text
    #  @param fill The color of the text. Optional, defaults to white.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    def draw_rotated_text(self, image, text, position, angle, font, fill=(255,255,255), display = True):
        draw = ImageDraw.Draw(image)
        width, height = draw.textsize(text, font=font)
        textimage = Image.new('RGBA', (width, height), (0,0,0,0))
        textdraw = ImageDraw.Draw(textimage)
        textdraw.text((0,0), text, font=font, fill=fill)
        if angle == - 90: textimage = textimage.transpose(Image.ROTATE_270)
        if angle == -180: textimage = textimage.transpose(Image.ROTATE_180)
        if angle == -270: textimage = textimage.transpose(Image.ROTATE_90)
        image.paste(textimage, position, textimage)
        if(display):
            self.disp.display()

    ## Determines the width of the screen based on rotation (Experienced users)
    #  @param self The object pointer.
    def screenWidth(self):
        if(self.currentRotation == 1 or self.currentRotation == 3):
            return 320
        else:
            return 240

    ## Determines the height of the screen based on rotation (Experienced users)
    #  @param self The object pointer.
    def screenHeight(self):
        if(self.currentRotation == 1 or self.currentRotation == 3):
            return 240
        else:
            return 320

    ## Prints a large title, intended for terminal mode.
    #  @param self The object pointer.
    #  @param name The display title that will appear at the top of the LCD touchscreen in cyan.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    def drawDisplay(self, name, display = True):
        self.drawAutoText(name, 0, 5, fill = (0,255,255), size = 30, display = display, align="center")

    ## Draw forward and back arrows on the screen
    #  @param self The object pointer.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    def drawArrows(self, display = True):
        self.drawButton(0, 0, width = 50, height = 40, text = "<", display = False)
        self.drawButton(self.screenWidth()-50, 0, width = 50, height = 40, text = ">", display = display)

    ## Determine if either on screen arrow button is pressed
    #  @param self The object pointer.
    def checkArrows(self):
        return(self.checkButton(0,0,50,50),self.checkButton(self.screenWidth()-50,0,50,50))

    ## Hide the on screen arrow buttons
    #  @param self The object pointer.
    #  @param refresh Choose to immediately refresh screen.
    def hideArrows(self, refresh = True):
        self.drawArrowsbool = False
        if(refresh):
            self.refresh()

    ## Show the on screen arrow buttons
    #  @param self The object pointer.
    #  @param refresh Choose to immediately refresh screen.
    def showArrows(self, refresh = True):
        self.drawArrowsbool = True
        if(refresh):
            self.refresh()

    ## Reads the x-coordinate of the touchscreen press
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  x = screen.TS_X()
    #  @endcode
    def TS_X(self):
        return self.x

    ## Reads the y-coordinate of the touchscreen press
    #  @param self The object pointer.
    #  To use this function in your program:
    #  @code
    #  ...
    #  y = screen.TS_Y()
    #  @endcode
    def TS_Y(self):
        return self.y

    ## Detects touchscreen presses and prevents false positives,
    #  updates self.x and self.y if pressed.
    #  @param self The object pointer.
    #  To use this function in your program:
    #  @code
    #  ...
    #  if (screen.isTouched())
    #      print "Touched at {},{}".format(screen.x, screen.y)
    #  @endcode
    def isTouched(self):
        x, y = self.comm.getTouchscreenCoordinates()
        if x == 0 and y == 0:
            return False
        self.x = x
        self.y = y
        return True

    ## Clears the LCD screen to defualt black
    #  @param self The object pointer.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.clearScreen()
    #  @endcode
    def clearScreen(self, display = True):
        self.disp.clear()
        if(display):
            self.disp.display()

    ## Draw a rectangle on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the rectangle.
    #  @param y The upper left y coordinate of the rectangle.
    #  @param width The width of the rectangle.
    #  @param height The height of the rectangle.
    #  @param fill The color of inside of the rectangle. Optional, defaults to white.
    #  @param outline The color of the outer edge of the rectangle. Optional, defaults to no outline.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.fillRect(100, 100, 75, 75, fill = (255,0,0), outline = (0,0,0))
    #  @endcode
    def fillRect(self, x, y, width, height, fill = (255,255,255), outline = None, display=True):
        draw = self.disp.draw()
        actx = self.screenXFromImageCoords(x,y)
        acty = self.screenYFromImageCoords(x,y)
        actx2 = self.screenXFromImageCoords(x + width,y + height)
        acty2 = self.screenYFromImageCoords(x + width,y + height)
        draw.rectangle((actx,acty,actx2,acty2), fill = fill, outline = outline)
        if(display):
            self.disp.display()

    ## Draw a filled circle on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param x The center x coordinate of the circle.
    #  @param y The center y coordinate of the circle.
    #  @param radius The radius of the circle.
    #  @param fill The color of the inside of the circle. Optional, defaults to white.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.fillCircle(100, 100, 15, fill = (255,0,0))
    #  @endcode
    def fillCircle(self, x, y, radius, fill = (255,255,255), display = True):
        draw = self.disp.draw()
        actx = self.screenXFromImageCoords(x,y)
        acty = self.screenYFromImageCoords(x,y)
        draw.ellipse((actx-radius,acty-radius,actx+radius,acty+radius), fill = fill)
        if(display):
            self.disp.display()

    ## Draw a circle on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param x The center x coordinate of the circle.
    #  @param y The center y coordinate of the circle.
    #  @param radius The radius of the circle.
    #  @param fill The color of the inside of the circle. Optional, defaults to None
    #  @param outline The color of the outer edge of the circle. Optional, defaults to Black
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  red circle with blue outline:
    #  screen.drawCircle(100, 100, 15, fill = (255,0,0), outline=(0,0,255))
    #  @endcode
    def drawCircle(self, x, y, radius, fill = None, outline = (0,0,0), display = True):
        draw = self.disp.draw()
        actx = self.screenXFromImageCoords(x,y)
        acty = self.screenYFromImageCoords(x,y)
        draw.ellipse((actx-radius,acty-radius,actx+radius,acty+radius), fill=fill, outline=outline)
        if(display):
            self.disp.display()

    ## Draw a bitmap image on the screen (.png files rcommended)
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the image.
    #  @param y The upper left y coordinate of the image.
    #  @param width The width of the image.
    #  @param height The width of the image.
    #  @param path The image file path. Optional, defaults to the popup background image.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.screen.fillBmp(30, 0, 240, 240, path = os.path.join(currentdir, "dog.png"))
    #  @endcode
    def fillBmp(self, x, y, width, height, path = "/usr/local/mindsensors/images/Pane1.png", display = True):
        buff = self.disp.buffer
        actx = self.screenXFromImageCoords(x,y)
        acty = self.screenYFromImageCoords(x,y)
        # if the caller only provided icon name, assume it is in our system repository
        if (path[0] != "/"):
            path = "/usr/local/mindsensors/images/" + path

        # if the image is missing, use a default X image.
        if (os.path.isfile(path)):
            image = Image.open(path)
        else:
            image = Image.open("/usr/local/mindsensors/images/missing.png")

        image = image.resize((int(width),int(height)), Image.ANTIALIAS)

        cr = self.currentRotation
        if(cr == 1):
            actx -= height
            image = image.transpose(Image.ROTATE_270)
        if(cr == 2):
            acty -= height
            actx -= width
            image = image.transpose(Image.ROTATE_180)
        if(cr == 3):
            acty -= width
            image = image.transpose(Image.ROTATE_90)

        buff.paste(image, (int(actx),int(acty)))
        if(display):
            self.disp.display()

    ## Draw a  image on the screen using supplied image data
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the image.
    #  @param y The upper left y coordinate of the image.
    #  @param width The width of the image.
    #  @param height The width of the image.
    #  @param image data
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.screen.fillBmp(40, 0, 240, 240, image)
    #  @endcode
    def fillImgArray(self, x, y, width, height, image, display = True):
        buff = self.disp.buffer
        actx = self.screenXFromImageCoords(x,y)
        acty = self.screenYFromImageCoords(x,y)

        image = Image.fromarray(image)

        image = image.resize((int(width),int(height)), Image.ANTIALIAS)

        cr = self.currentRotation
        if(cr == 1):
            actx -= height
            image = image.transpose(Image.ROTATE_270)
        if(cr == 2):
            acty -= height
            actx -= width
            image = image.transpose(Image.ROTATE_180)
        if(cr == 3):
            acty -= width
            image = image.transpose(Image.ROTATE_90)

        buff.paste(image, (actx,acty))
        if(display):
            self.disp.display()

    ## Rotates the screen orientation 90 degrees to the right (-90 degrees)
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.rotateRight()
    #  @endcode
    def rotateRight(self):
        self.currentRotation += 1
        if(self.currentRotation>3):
            self.currentRotation = 0
        self.refresh()

    ## Rotates the screen orientation 90 degrees to the left (90 degrees)
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.rotateLeft()
    #  @endcode
    def rotateLeft(self):
        self.currentRotation -= 1
        if(self.currentRotation<0):
            self.currentRotation = 3
        self.refresh()

    ## Displays text on the screen with adjusted position and rotation
    #  @param self The object pointer.
    #  @param text The text to display on the screen
    #  @param x The upper left x coordinate of the text. Optional, defaults to "left". Irrelevant if align is "center"
    #  @param y The upper left y coordinate of the text.
    #  @param fill The color of the text. Optional, defaults to white.
    #  @param size The pixel size of the text. Optional, defaults to 20.
    #  @param align The text alignment, "left" or "center" or "right". Optional, defaults to "left".
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.drawAutoText("Wow!", 10, 20, fill = (255,255,255), size = 25)
    #  @endcode
    def drawAutoText(self, text, x, y, fill = (255,255,255), size = 20, align="left", display = True):
        text = str(text)
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size)
        width, height = ImageDraw.Draw(self.disp.buffer).textsize(text, font=font)
        tempx = self.screenXFromImageCoords(x,y)
        tempy = self.screenYFromImageCoords(x,y)

        cr = self.currentRotation
        if align == "center":
            tempy = (self.screenWidth() - width)/2
            if cr == 1 or cr == 2:
                tempx = self.screenHeight() - height - y
            if cr == 0 or cr == 2:
                tempx, tempy = tempy, tempx
            if cr == 0:
                tempy = y
        elif align == "right":
            if cr == 0:
                tempx = self.screenWidth() - width - x
                tempy = y
            if cr == 1:
                tempx = self.screenHeight() - height - y
                tempy = self.screenWidth() - width - x
            if cr == 2:
                tempx, tempy = x, self.screenHeight() - height - y
            if cr == 3:
                tempy = x
        else:
            if cr == 1:
                tempx -= height
            if cr == 2:
                tempy -= height
                tempx -= width
            if cr == 3:
                tempy -= width

        angletemp = -90*self.currentRotation

        self.draw_rotated_text(self.disp.buffer, text, (int(tempx),int(tempy)), angletemp, font, fill, display = display)

    ## Set the cursor to a specific line of the of the screen
    #  @param self The object pointer.
    #  @param lineno The line number at which to set the cursor.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termGotoLine(5)
    #  @endcode
    def termGotoLine(self, lineno):
        self.terminalCursor = lineno

    ## Print to a specific line of the screen
    #  @param self The object pointer.
    #  @param lineno The line number at which to set the cursor.
    #  @param text The text to print to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termPrintAt(5, "Printing at line 5")
    #  @endcode
    def termPrintAt(self, lineno, text):
        self.terminalCursor = lineno
        self.fillRect(10, self.terminalCursor*20+42, 320, 19, (0,0,0), display = False)
        self.terminalBuffer[self.terminalCursor] =  str(text)
        self.refreshLine(self.terminalCursor)

    ## Print to the current line of the screen
    #  @param self The object pointer.
    #  @param text The text to print to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termPrint("Regular print, no newline")
    #  @endcode
    def termPrint(self, text):
        self.terminalBuffer[self.terminalCursor] += str(text)
        self.refreshLine(self.terminalCursor)

    ## Print to the current line and then go to the next line
    #  @param self The object pointer.
    #  @param text The text to print to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termPrintln("Hello, world!")
    #  @endcode
    def termPrintln(self, text):
        if(self.terminalCursor>9):
            self.terminalCursor = 0
            self.terminalBuffer = [""]*20
            self.refresh()
        self.termPrint(text)
        self.terminalCursor += 1

    ## Print new text in place of current line (Low Refresh Rate)
    #  @param self The object pointer.
    #  @param text The text to print to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termReplaceLastLine("Replaced!")
    #  @endcode
    def termReplaceLastLine(self, text):
        self.terminalBuffer[self.terminalCursor] = ""
        self.fillRect(10, self.terminalCursor*20+42, 320, 19, (0,0,0), display = False)
        self.termPrint(text)

    ## Refresh a screen line
    #  @param self The object pointer.
    #  @param lineNum The line number to refresh.
    #  @param display Choose to immediately push the drawing to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.refreshLine(1)
    #  @endcode
    def refreshLine(self, lineNum, display = True):
        if(self.currentMode == self.PS_MODE_TERMINAL):
            self.drawAutoText(self.terminalBuffer[lineNum], 10, lineNum*20 + 40, (255,255,255), display = display)

    ## Draw a labeled button on the screen (INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the rectangle.
    #  @param y The upper left y coordinate of the rectangle.
    #  @param width The width of the button.
    #  @param height The height of the button.
    #  @param prefix The button images filename prefix. Optional, defaults to "btns_"
    #  @param text The button label. Defaults to "OK"
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @param align The alignment for the button's text label.
    #  @param image An optional image to be included on the button, should be 32x32.
    #  @param imageX The x-coordinate of the optional image icon.
    #  @param imageY The y-coordinate of the optional image icon.
    def drawButton(self, x, y, width, height, prefix="btns_",text="OK", display=True, align="left", image=None, imageX=None, imageY=None):
        self.fillBmp(x, y, 14, height, prefix+"left.png", display=False)
        self.fillBmp(x+14, y, width-28, height, prefix+"center.png", display=False)
        self.fillBmp(x+width-14, y, 14, height, prefix+"right.png", display=False)

        textX = x+10
        if image:
            textX += 32
            imgY = imageY or y+((height-32)/2)
            imgX = imageX or x+4
            self.fillBmp(imgX, imgY, 32, 32, image, display=False)

        self.drawAutoText(text,textX, y+(height/2)-10, size=16, fill = (0,0,0), display=display, align=align)

    ## Refresh the screen (Slow)
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.refresh()
    #  @endcode
    def refresh(self):
        if(self.currentMode == self.PS_MODE_TERMINAL):
            self.clearScreen(False)
            if(self.drawArrowsbool):
                self.drawArrows(False)
            for i,_ in enumerate(self.terminalBuffer):
                self.refreshLine(i, display = False)
            self.disp.display()
        if(self.currentMode == self.PS_MODE_POPUP):
            xbuff = 20
            ybuff = 20
            try:
                self.fillBmp(xbuff,ybuff,self.screenWidth()-(2*xbuff),self.screenHeight()-(2*ybuff), "dialogbg.png", display = False)
            except:
                self.fillRect(xbuff,ybuff,self.screenWidth()-(2*xbuff),self.screenHeight()-(2*ybuff),fill = (127,127,127), outline = (255,255,255))

            numButts = len(self.buttonText)
            spacing = 10
            room = self.screenWidth()-(xbuff + ybuff)
            buttHeight = 50
            n = 0
            while(n<numButts):
                self.drawButton((room/numButts)*n + xbuff + spacing/2 + 10, self.screenHeight() - (ybuff + spacing + buttHeight), (room/numButts) - spacing - 20, buttHeight, prefix = "btns_", text=self.buttonText[n], display = False)
                """
                self.fillBmp((room/numButts)*n + xbuff + spacing/2, self.screenHeight() - (ybuff + spacing + buttHeight), (room/numButts) - spacing, buttHeight, path = "button.png", display = False)
                self.drawAutoText(self.buttonText[n],(room/numButts)*n + xbuff + spacing, self.screenHeight() - (ybuff + buttHeight), fill = (0,0,0), display = False)
                """
                n+= 1
            n = 0
            offset = 5
            if(self.currentRotation % 2 == 0): # portrait
                offset = 12
            while(n<len(self.popupText)):
                if ( n > 0 ):
                    offset = 10
                    if(self.currentRotation % 2 == 0): # portrait
                        offset = 24
                self.drawAutoText(self.popupText[n], xbuff + 10, ybuff + offset + (20*n), fill = (0,0,0), size = 15, display = False)

                n += 1
            self.disp.display()

    ## Determine if an on screen button is pressed
    #  @param self The object pointer.
    #  @param x The upper left x-coordinate of the button.
    #  @param y The upper left y-coordinate of the button.
    #  @param width The width of the button.
    #  @param height The height of the button.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  button = screen.checkButton(0, 0, 50, 50)
    #  @endcode
    def checkButton(self, x, y, width, height):
        if self.isTouched():
            tsx = self.TS_To_ImageCoords_X(self.x, self.y)
            tsy = self.TS_To_ImageCoords_Y(self.x, self.y)
            if tsx in range(int(x), int(x+width)) and tsy in range(int(y), int(y+height)):
                return True
        return False

    ## Determines if button in a pop-up window is pressed (Experienced users)
    #  @param self The object pointer.
    #  @param numButts How many buttons are being shown
    def checkDialogButtons(self, numButts):
        # see refresh method for value definitions
        xbuff = 20
        ybuff = 20
        spacing = 10
        room = self.screenWidth() - (xbuff + ybuff)
        buttHeight = 50
        y = self.screenHeight() - (ybuff + spacing + buttHeight)
        width = (room/numButts) - spacing - 20
        for n in range(numButts):
            x = (room/numButts)*n + xbuff + spacing/2 + 10
            if self.checkButton(x, y, width, buttHeight):
                return n
        return -1


    ## Display pop-up of a question on the screen
    #  @param self The object pointer.
    #  @param question The question that will pop-up on the screen. The first string will be the titlebar.
    #  @param options The possible answers to the question.
    #  @param touch Whether to check if the on screen buttons are pressed. Optional, defaults to True.
    #  @param goBtn Whether to check for the GO button to close the question. Optional, defaults to False.
    #  @param wrapText When True, long lines of text will be wrapped to fit in the popup. Optional, default to False.
    #  @code
    #  question = ["Title", "This is a very long line of text which will be wrapped to fit in the dialog box.", "Here's a second line. It will be wrapped, too. What do you think?"]
    #  options = ["No thanks", "Cool!"]
    #  answer = screen.askQuestion(question, options, wrapText=True)
    #  @endcode
    #  @note If goBtn is True, pressing GO will close the dialog and return -1
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  question = ["Color Picker", "Pick a color!"]
    #  options = ["Red", "Green", "Blue"]
    #  answer = screen.askQuestion(question, options)
    #  @endcode
    def askQuestion(self, question, options, touch=True, goBtn=False, wrapText=False):
        for i, line in enumerate(question):
            question[i] = str(line)
        if wrapText:
            wrap, maxlines = 48, 5
            if (self.currentRotation % 2 == 0): # portrait
                wrap, maxlines = 30, 9
            maxWidth = self.screenWidth()-60 # see fillBpm of dialogbg.png in refresh()
            getTextSize = ImageDraw.Draw(self.disp.buffer).textsize
            font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 15)
            def makeWrappedText():
                arr = '\n'.join([textwrap.fill(t, width=wrap) for t in question[1:]]).split('\n')
                self.popupText = [question[0]] + arr[:maxlines]
                if len(arr) > maxlines:
                    if self.popupText[maxlines][-1] == ".":
                        self.popupText[maxlines] += " ..."
                    else:
                        self.popupText[maxlines] += "..."
            def widestLine():
                return max([getTextSize(str, font=font)[0] for str in self.popupText])
            makeWrappedText()
            while (widestLine() > maxWidth):
                wrap -= 1
                makeWrappedText()
        else:
            self.popupText = question
        self.buttonText = options
        oldMode = self.currentMode
        self.setMode(self.PS_MODE_POPUP)
        if(len(options)>=4):
            print ("warning!, buttons may be too small to read")
        if(len(options)<=0 and not goBtn):
            print ("warning!, no options will leave this pop-up stuck")
        if goBtn:
            keyPressCount = self.comm.getKeyPressCount()
        while(True):
            if(goBtn and keyPressCount < self.comm.getKeyPressCount()):
                self.setMode(oldMode)
                return -1
            if(touch and self.isTouched()):
                n = self.checkDialogButtons(len(options))
                if(n != -1):
                    self.setMode(oldMode)
                    return n

    ## Display Pop-up of 'Yes' or 'No' question on the screen, returning True or False
    #  @param self The object pointer.
    #  @param question The question that will pop-up on the screen.
    #  @param touch Whether to check if on screen buttons are pressed. Optional, defaults to True.
    #  @param goBtn Whether to check for the GO button to close the question. Optional, defaults to False.
    #  @param wrapText When True, long lines of text will be wrapped to fit in the popup. Optional, default to False.
    #  @code
    #  question = ["Title", "This is a very long line of text which will be wrapped to fit in the dialog box.", "Cool?"]
    #  response = screen.askYesOrNoQuestion(question, wrapText=True)
    #  @endcode
    #  @note If goBtn is True, pressing GO will close the dialog and return False
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  question = ["Continue?", "Do you want to continue?"]
    #  response = screen.askYesOrNoQuestion(question)
    #  @endcode
    def askYesOrNoQuestion(self, question, touch=True, goBtn=False, wrapText=False):
        return self.askQuestion(question, ["Yes","No"], touch=touch, goBtn=goBtn, wrapText=wrapText) == 0

    ## Display pop-up of a message on the screen with a single option "OK"
    #  @param self The object pointer.
    #  @param message The message that will pop-up on the screen.
    #  @param touch Whether to check if on screen buttons are pressed. Optional, defaults to True.
    #  @param goBtn Whether to check for the GO button to close the question. Optional, defaults to True.
    #  @param wrapText When True, long lines of text will be wrapped to fit in the popup. Optional, default to False.
    #  @code
    #  message = ["Title", "This is a very long line of text which will be wrapped to fit in the dialog box.", "Other lines will be wrapped, too. Press OK to close this popup."]
    #  screen.showMessage(message, wrapText=True)
    #  @endcode
    #  @note If goBtn is True, pressing GO will close the dialog and return False
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  message = ["Complete", "The process has completed.", "Status: success"]
    #  screen.showMessage(message)
    #  @endcode
    def showMessage(self, message, touch=True, goBtn=True, wrapText=False):
        if type(message) is not list:
            message = ["Message", message]
        return self.askQuestion(message, ["OK"], touch=touch, goBtn=goBtn, wrapText=wrapText) == 0

    ## Display pop-up of a message on the screen with no exit options.
    #  This function will return right away. You may need to call `screen.setMode(screen.PS_MODE_TERMINAL)` to stop the popup later.
    #  @param self The object pointer.
    #  @param message The message that will pop-up on the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  message = ["Processing", "Processing, please wait..."]
    #  screen.forceMessage(message)
    #  @endcode
    def forceMessage(self, message):
        self.popupText = message
        self.buttonText = []
        oldMode = self.currentMode
        self.setMode(self.PS_MODE_POPUP)

    ## Draw a line on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param x1, y1, x2, y2 The x and y coordinates of each endpoint of the line.
    #  @param width The width of the line. Optional, defaults to 0.
    #  @param fill The color of line. Optional, defaults to white.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.drawLine(50, 50, 100, 100, width = 0, fill = (255,0,0))
    #  @endcode
    def drawLine(self, x1, y1, x2, y2, width = 0, fill = (255,255,255), display = True):
        draw = self.disp.draw()
        actx1 = self.screenXFromImageCoords(x1,y1)
        acty1 = self.screenYFromImageCoords(x1,y1)
        actx2 = self.screenXFromImageCoords(x2,y2)
        acty2 = self.screenYFromImageCoords(x2,y2)
        draw.line((actx1,acty1,actx2,acty2), fill = fill, width = width)
        if(display):
            self.disp.display()

    ## Draw a polyline on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param endpoints [x1, y1, x2, y2...] The x and y coordinates of each endpoint of the polyline.
    #  @param width The width of the polyline. Optional, defaults to 0.
    #  @param fill The color of polyline. Optional, defaults to white.
    #  @param display Choose to immediately push the drawing to the screen. Optional, defaults to True.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.drawLine([50, 50, 100, 50, 100, 100], width = 0, fill = (255,0,0))
    #  @endcode
    def drawPolyLine(self, endpoints, width = 0, fill = (255,255,255), display = True):
        assert len(endpoints) % 2 == 0, "endpoints must be an array of even length, containing *pairs* of integers"
        assert len(endpoints) >= 4, "endpoints must contain at least two coordinates to draw a line"
        draw = self.disp.draw()
        actendpts = []
        for (x,y) in [(endpoints[i*2],endpoints[i*2+1]) for i in range(len(endpoints)/2)]: # iterate over each pair of integers
            actendpts.append(self.screenXFromImageCoords(x,y)) # actual x-coordinate
            actendpts.append(self.screenYFromImageCoords(x,y)) # actual y-coordinate
        draw.line(actendpts, fill = fill, width = width)
        if(display):
            self.disp.display()


### @cond Doxygen_ignore_this
# the following code demonstrates screen rotation, popup menus, terminal printing, and custom buttons
if __name__ == '__main__':
    psb = mindsensorsUI("UI",2,Dev_PiStorms)
    psb.termPrintln("Starting test program...")

    try:
        confirmation = psb.askYesOrNoQuestion(["Confirmation Dialogue","Do you wish to continue?"])

        if(not confirmation):
            psb.termPrintln("Exiting Program...")
            sys.exit(0)

        #while(psb.isKeyPressed() == True):
        while(True):
            if(psb.getMode() != psb.PS_MODE_TERMINAL):
                psb.setMode(psb.PS_MODE_TERMINAL)
                psb.termPrintln("Re-activated refresh")
            psb.termPrintln("Main Menu reached")
            demomode = psb.askQuestion(["Mode Selector","Select demonstration mode"],["Rotate","Button","Print"])
            if(demomode == 0):

                psb.termPrintln("Screen rotation demo...")
                exit = 0
                while(exit == 0):
                    answerChoices = ["Left","Right","Exit"]
                    answer = psb.askQuestion(["Rotate Screen?","Pick a direction to rotate,","or press EXIT to exit."],answerChoices)
                    psb.termPrintln("User selected: " + answerChoices[answer])

                    if(answer == 0):
                        psb.rotateLeft()
                    if(answer == 1):
                        psb.rotateRight()
                    if(answer == 2):
                        exit = 1
            elif(demomode == 1):
                psb.termPrintln("Starting custom button demo...")
                psb.termPrintln("Killing refresh...")
                psb.setMode(psb.PS_MODE_DEAD)#prevent library drawing on top of our buttons
                exit = 0
                psb.drawButton(50,125,text = "Exit")
                buttonOld = True
                while(exit == 0):

                    buttonNew = psb.checkButton(50,50)
                    if(buttonNew != buttonOld):

                        buttonOld = buttonNew
                        if(buttonNew):
                            psb.drawButton(50,50,text = "ButtonPressed")
                        else:
                            psb.drawButton(50,50,text = "Button")
                    if(psb.checkButton(50,125)):
                        exit = 1
            else:
                x = 0
                xq = time.time()
                psb.termPrintln("Printing test beginning...")
                time.sleep(2)
                while(x<50):
                    psb.termPrintln("Test loop #" + str(x))

                    x += 1
                psb.termPrintln("Printing test complete! (" + str(int(math.floor((time.time()-xq)*1000))) + " ms)")
                time.sleep(2)
                psb.dumpTerminal()
    except KeyboardInterrupt:
        print ("\nQuitting...")
        psb.setMode(psb.PS_MODE_TERMINAL)
        psb.termPrintln("Exiting Program...")
        sys.exit(0)
### @endcond
