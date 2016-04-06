#!/usr/bin/env python
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

from mindsensors_i2c import mindsensors_i2c
import time, math ,os
import Image
import ImageDraw
import ImageFont
import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import sys,os
from threading import Thread, Lock

## @package mindsensorsUI
#  This module contains classes and functions necessary for use of LCD touchscreen on mindsensors.com products
 
Dev_PiStorms = 1
Dev_SensorShield = 2


## mindsensorsUI: this class provides functions for touchscreen LCD on mindsensors.com products for read and write operations.
#  There is no need to initialize this class unless using the LCD screen alone. Normal initialization will be performed automatically with initialization of the Device on which the screen is used.
class mindsensorsUI():

    ## Default Device I2C Address 
    PS_ADDRESS = 0x34 
    ## Touchscreen X-axis Register. Will return an unsigned integer reading (0-340) 
    PS_TSX = 0xE3
    ## Touchscreen Y-axis Register. Will return an unsigned integer reading (0-440) 
    PS_TSY = 0xE5
    
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
    
    ### @cond
    #PS_XMIN = 0x5A
    #PS_XMAX = 0x5C
    #PS_YMIN = 0x5E
    #PS_YMAX = 0x60
    ## Constant to specify terminal mode
    PS_MODE_TERMINAL = 0
    ## Constant to specify pop-up mode
    PS_MODE_POPUP = 1
    ## Constant to specify dead mode
    PS_MODE_DEAD = 2
    
    ## Dictionary of default emnpty terminal buffer
    terminalBuffer = ["","","","","","","","","","","","","","","","","","","",""]
    ## Variable of default terminal cursor position
    terminalCursor = 0
    ## Variable of default mode
    currentMode = 0;
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
    
    touchIgnoreX = 0
    touchIgnoreY = 0
    ### @endcond
    
    ## Initialize the PiStorms motor and sensor ports
    #  @param self The object pointer.
    #  @param name The display title that will appear at the top of the LCD touchscreen.
    #  @param rotation The rotation of the LCD touchscreen.
    #  @param device The device on which the LCD touchscreen is used.
    #  @remark
    #  There is no need to use this function directly. To initialize the mindsensorsUI class in your program:
    #  @code
    #  from mindsensorsUI import mindsensorsUI
    #  ...
    #  screen = mindsensorsUI()
    #  @endcode    
    def __init__(self,name = "PiStorms", rotation = 3,device = Dev_PiStorms ):
        if  device == Dev_SensorShield :
            self.PS_ADDRESS =  0x16
            self.PS_TSX =  0x56
            self.PS_TSY =  0x58
        self.i2c = mindsensors_i2c(self.PS_ADDRESS >> 1)
        self.disp.begin()
        self.clearScreen()
        self.mutex = Lock()
        try:
            self.touchIgnoreX = self.TS_X()
            self.touchIgnoreY = self.TS_Y()
            self.calibrateTouched()
        except:
            pass
            
        if(rotation > 0 and rotation < 4):
            self.currentRotation = rotation
        self.refresh()
        self.myname = name
        self.drawDisplay(name,display = False)
    
    ### @cond
    ## Dumps the screen buffer
    #  @param self The object pointer.
    def dumpTerminal(self):
        self.terminalBuffer = ["","","","","","","","","","","","","","","","","","","",""]
        self.terminalCursor = 0
        if(self.getMode() == self.PS_MODE_TERMINAL):
            self.refresh()
    
    
    ## Sets the mode(Experienced users)
    #  @param self The object pointer. 
    def setMode(self, mode = 0):
        if(mode<0 or mode>2):
            self.currentMode = self.PS_MODE_DEAD
        else:
            self.currentMode = mode
            self.refresh()
    
    ## Returns the value of the mode(Experienced users)
    #  @param self The object pointer.
    def getMode(self):
        return self.currentMode
        
    def calibrateTouched(self):
        self.touchIgnoreX = self.TS_X()
        self.touchIgnoreY = self.TS_Y()
        
    ## Draw a rectangle with rounded edges on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the rectangle.
    #  @param y The upper left y coordinate of the rectangle.
    #  @param width The width of the rectangle.
    #  @param height The height of the rectangle.
    #  @param radius The arc of the rectangle corners.
    #  @param fill The color of the inside of the rectangle.
    #  @param display Choose to immediately push the drawing to the screen.
    def fillRoundRect(self, x, y, width, height, radius, fill = (255,255,255),display = True):
        self.fillRect(x,y + radius,width, height-(radius*2), fill = fill,display = False)
        self.fillRect(x + radius, y, width - (radius*2), height, fill = fill,display = False)
        self.fillCircle(x + radius, y + radius, radius, fill = fill,display = False)
        self.fillCircle(x + width - radius, y + radius, radius, fill = fill,display = False)
        self.fillCircle(x + radius, y + height - radius, radius, fill = fill,display = False)
        self.fillCircle(x + width - radius,y + height - radius, radius, fill = fill, display = display)
        
    ## Calculates the x-coordinate of the screen upon rotation(INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param x The x-coordinate.
    #  @param y The y-coordinate.    
    def screenXFromImageCoords(self,x = 0,y = 0):
        currentRotation = self.currentRotation
        if(currentRotation == 0):
            return x
        if(currentRotation == 1):
            return self.PS_SCREENWIDTH-y
        if(currentRotation == 2):
            return self.PS_SCREENWIDTH-x
        if(currentRotation == 3):
            return y
    
    ## Calculates the y-coordinate of the screen upon rotation(INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param x The x-coordinate.
    #  @param y The y-coordinate.   
    def screenYFromImageCoords(self,x = 0,y = 0):
        cr = self.currentRotation
        if(cr == 0):
            return y
        if(cr == 1):
            return x
        if(cr == 2):
            return self.PS_SCREENHEIGHT-y
        if(cr == 3):
            return self.PS_SCREENHEIGHT-x

    def TS_To_ImageCoords_Y(self, x, y):
        cr = self.currentRotation
        if(cr == 0):
            return y
        if(cr == 3):
            return x

    def TS_To_ImageCoords_X(self, x, y):
        cr = self.currentRotation
        if(cr == 0):
            return x
        if(cr == 3):
            return self.PS_SCREENHEIGHT-y
            
    ## Displays rotated text (INTERNAL USE ONLY)
    #  @param self The object pointer.
    #  @param image The image used for creating text
    #  @param text The text to display on the screen
    #  @param position The position of the text as a set of x and y-coordinates
    #  @param angle The angle at which to rotate the text
    #  @param font The font of the text
    #  @param fill The color of the text
    #  @param display Choose to immediately push the drawing to the screen.
    def draw_rotated_text(self, image, text, position, angle, font, fill=(255,255,255), display = True):
        draw = ImageDraw.Draw(image)
        width, height = draw.textsize(text, font=font)
        textimage = Image.new('RGBA', (width, height), (0,0,0,0))
        textdraw = ImageDraw.Draw(textimage)
        textdraw.text((0,0), text, font=font, fill=fill)
        rotated = textimage.rotate(angle, expand=1)
        image.paste(rotated, position, rotated)
        if(display):
            self.disp.display()
            
    ## Determines the width of the screen based on rotation (experienced users)
    #  @param self The object pointer.
    def screenWidth(self):
        if(self.currentRotation == 1 or self.currentRotation == 3):
            return 320
        else:
            return 240
    
    ## Determines the height of the screen based on rotation (experienced users)
    #  @param self The object pointer.
    def screenHeight(self):
        if(self.currentRotation == 1 or self.currentRotation == 3):
            return 240
        else:
            return 320
    
    ## Prints the name text on the screen
    #  @param self The object pointer.
    #  @param name The display title that will appear at the top of the LCD touchscreen.
    #  @param display Choose to immediately push the drawing to the screen.
    def drawDisplay(self, name,display = True):
        self.drawAutoText(name,50,0,fill = (0,255,255), size = 40, display = display)
        
    ## Draw a labeled button on the screen
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the rectangle.
    #  @param y The upper left y coordinate of the rectangle.
    #  @param width The width of the button.
    #  @param height The height of the button.
    #  @param text The button label.
    #  @param display Choose to immediately push the drawing to the screen.
    # disabled by Deepak
    #def drawButton(self,x,y,width = 150,height = 50, text = "OK", display = True):
    #    self.fillBmp(x,y,width,height,path = "/usr/local/mindsensors_images/button.png", display = False)
    #    self.drawAutoText(text, x + 10,y + 15, fill = (0,0,0), display = display)
    
    ## Draw forward and back arrows on the screen
    #  @param self The object pointer.
    #  @param display Choose to immediately push the drawing to the screen.
    def drawArrows(self,display = True):
        self.drawButton(0,0,width = 50,height = 40, text = "<",display = False)
        self.drawButton(self.screenWidth()-50,0,width = 50,height = 40, text = ">",display = display)
    
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
    
    ## Determines if button in a pop-up window is pressed (experienced users)
    #  @param self The object pointer.
    #  @param xbuff The x-coordinate buffer.
    #  @param ybuff The y-coordinate buffer.
    #  @param buttHeight The height of the button.
    def calculateButton(self, xbuff, ybuff, buttHeight):
        n = 0
        while(n < len(self.buttonText)):
            numButts = len(self.buttonText)
            room = self.screenWidth()-(xbuff + ybuff)
            xlb = (room/numButts)*n + xbuff
            ylb = self.screenHeight() - (ybuff + buttHeight)
            xub = xlb + (room/numButts)
            yub = ylb + buttHeight
            
            axlb = self.screenXFromImageCoords(xlb,ylb)
            aylb = self.screenYFromImageCoords(xlb,ylb)
            axub = self.screenXFromImageCoords(xub,yub)
            ayub = self.screenYFromImageCoords(xub,yub)
            
            
            if(axub<axlb):
                tempx = axub
                axub = axlb
                axlb = tempx
            if(ayub<aylb):
                tempy = ayub
                ayub = aylb
                aylb = tempy
            
            tsx = self.TS_X()
            tsy = self.TS_Y()
            #print str(tsy) + " " + str(aylb) + " " + str(ayub)
            if(tsx<axub and tsx>axlb and tsy>aylb and tsy<ayub):
                return n
        
        
            n += 1
        return -1
    ### @endcond
    
    ## Reads the x-coordinate of the touchscreen press
    #  @param self The object pointer.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  x = screen.TS_X()
    #  @endcode 
    def TS_X(self):
        return self.i2c.readInteger(self.PS_TSY)
    
    ## Reads the y-coordinate of the touchscreen press
    #  @param self The object pointer.
    #  To use this function in your program:
    #  @code
    #  ...
    #  y = screen.TS_Y()
    #  @endcode 
    def TS_Y(self):
        return self.i2c.readInteger(self.PS_TSX)
    
    ## Detects touchscreen presses and prevents false positives 
    #  @param self The object pointer.
    #  To use this function in your program:
    #  @code
    #  ...
    #  touch = screen.isTouched()
    #  @endcode 
    def isTouched(self):
        firstTry = self.touchIgnoreX == self.TS_X() and self.touchIgnoreY == self.TS_Y()
        secondTry = self.touchIgnoreX == self.TS_X() and self.touchIgnoreY == self.TS_Y()
        thirdTry = self.touchIgnoreX == self.TS_X() and self.touchIgnoreY == self.TS_Y()
        return (not firstTry) and (not secondTry) and (not thirdTry)
    
    ## Clears the LCD screen to defualt black
    #  @param self The object pointer.
    #  @param display Choose to immediately push the drawing to the screen.
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.clearScreen(True)
    #  @endcode 
    def clearScreen(self,display = True):
        self.disp.clear()
        if(display):
            self.disp.display()
    
    ## Draw a rectangle on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the rectangle.
    #  @param y The upper left y coordinate of the rectangle.
    #  @param width The width of the rectangle.
    #  @param height The height of the rectangle.
    #  @param fill The color of inside of the rectangle.
    #  @param outline The color of the outer edge of the rectangle.
    #  @param display Choose to immediately push the drawing to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.fillRect(100, 100, 75, 75, fill = (255,0,0), None, True)
    #  @endcode    
    def fillRect(self, x, y, width, height, fill = (255,255,255), outline = None,display=True):
        draw = self.disp.draw()
        actx = self.screenXFromImageCoords(x,y)
        acty = self.screenYFromImageCoords(x,y)
        actx2 = self.screenXFromImageCoords(x + width,y + height)
        acty2 = self.screenYFromImageCoords(x + width,y + height)
        draw.rectangle((actx,acty,actx2,acty2), fill = fill, outline = outline)
        if(display):
            self.disp.display()
    
    ## Draw a circle on the screen (rotated to screen)
    #  @param self The object pointer.
    #  @param x The center x coordinate of the circle.
    #  @param y The center y coordinate of the circle.
    #  @param radius The radius of the circle.
    #  @param fill The color of the inside of the circle.
    #  @param display Choose to immediately push the drawing to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.fillCircle(100, 100, 15, fill = (255,255,255), True)
    #  @endcode    
    def fillCircle(self, x, y, radius, fill = (255,255,255),display = True):
        draw = self.disp.draw()
        actx = self.screenXFromImageCoords(x,y)
        acty = self.screenYFromImageCoords(x,y)
        draw.ellipse((actx-radius,acty-radius,actx+radius,acty+radius), fill = fill)
        if(display):
            self.disp.display()
    
    ## Draw a bitmap image on the screen (.png files rcommended)
    #  @param self The object pointer.
    #  @param x The upper left x coordinate of the image.
    #  @param y The upper left y coordinate of the image.
    #  @param width The width of the image.
    #  @param height The width of the image.
    #  @param path The image file path.
    #  @param display Choose to immediately push the drawing to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.screen.fillBmp(30, 0, 240, 240, path = currentdir+'/'+"dog.png", True)
    #  @endcode    
    def fillBmp(self, x, y, width, height, path = "/usr/local/mindsensors_images/Pane1.png",display = True):

        self.mutex.acquire()

        try:
            buff = self.disp.buffer
            actx = self.screenXFromImageCoords(x,y)
            acty = self.screenYFromImageCoords(x,y)
            # if the caller only provided icon name, assume it is in our system repository
            if ( path[0] != "/" ):
                path = "/usr/local/mindsensors_images/" + path
            image = Image.open(path)
            non_transparent = Image.new('RGBA',image.size,(255,255,255,255))
            #changed by Deepak.
            non_transparent.paste(image,(0,0))
            
            tempimage = image
            
            tempimage = tempimage.resize((width,height),Image.ANTIALIAS)
            tempimage = tempimage.rotate(-90*self.currentRotation)
            
            cr = self.currentRotation
            if(cr == 1):
                actx -= height
            if(cr == 2):
                acty -= height
                actx -= width
            if(cr ==3):
                acty -= width
            
            
            #changed by Deepak.
            buff.paste(tempimage,(actx,acty))
            if(display):
                self.disp.display()
        finally:
            self.mutex.release()
    
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
    #  @param x The upper left x coordinate of the text.
    #  @param y The upper left y coordinate of the text.
    #  @param fill The color of the text
    #  @param size The pixel size of the text
    #  @param display Choose to immediately push the drawing to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.drawAutoText(self.terminalBuffer[lineNum], 10, 20, fill = (255,255,255), 25, True)
    #  @endcode    
    def drawAutoText(self,text,x,y,fill = (255,255,255), size = 20, display = True, align="left"):
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size)
        linew,lineh = font.getsize(text)
        width, height = ImageDraw.Draw(self.disp.buffer).textsize(text, font=font)
        tempx = self.screenXFromImageCoords(x,y)
        tempy = self.screenYFromImageCoords(x,y)
        cr = self.currentRotation
        if(cr == 1):
            tempx -= height
        if(cr == 2):
            tempy -= height
            tempx -= width
        if(cr ==3):
            tempy -= width
            if ( align == "center" ):
                tempy -= linew/2
        angletemp = 0
        angletemp -= 90*self.currentRotation
        
        self.draw_rotated_text(self.disp.buffer,text,(tempx,tempy),angletemp,font,fill, display = display)
    
    ## Set the cursor to a specific line of the of the screen
    #  @param self The object pointer.
    #  @param lineno The line number at which to set the cursor.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termGotoLine(5)
    #  @endcode    
    def termGotoLine(self,lineno):
        self.terminalCursor = lineno
    
    ## Print to a specific line of the screen
    #  @param self The object pointer.
    #  @param lineno The line number at which to set the cursor.
    #  @param text The text to print to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termPrintAt(5, "Print At Line 5")
    #  @endcode    
    def termPrintAt(self,lineno,text):
        self.terminalCursor = lineno
        self.fillRect(10,self.terminalCursor*20+42,320,19,(0,0,0), display = False)
        self.terminalBuffer[self.terminalCursor] =  str(text)
        self.refreshLine(self.terminalCursor)        
    
    ## Print to the current line of the screen
    #  @param self The object pointer.
    #  @param text The text to print to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termPrint("Print Now")
    #  @endcode    
    def termPrint(self,text):
        self.terminalBuffer[self.terminalCursor] = self.terminalBuffer[self.terminalCursor] + str(text)
        self.refreshLine(self.terminalCursor)
    
    ## Print to the current line of the screen followed by a line feed
    #  @param self The object pointer.
    #  @param text The text to print to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.termPrintln("Print Now")
    #  @endcode    
    def termPrintln(self,text):
        if(self.terminalCursor>9):
            self.terminalCursor = 0
            self.terminalBuffer = ["","","","","","","","","","","","","","","","","","","",""]
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
    #  screen.termReplaceLastLine("Print Now")
    #  @endcode    
    def termReplaceLastLine(self,text):
        self.terminalBuffer[self.terminalCursor] = ""
        #self.fillRect(10,self.terminalCursor*20 + 40,320,self.terminalCursor*20 + 35,(0,0,0), display = False)
        #self.fillRect(10,self.terminalCursor*15 + 40,320,self.terminalCursor*15 + 35,(0,0,0), display = False)
        self.fillRect(10,self.terminalCursor*20+42,320,19,(0,0,0), display = False)
        self.termPrint(text)
    
    ## Refresh a screen line 
    #  @param self The object pointer.
    #  @param text The text to print to the screen.
    #  @param display Choose to immediately push the drawing to the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  screen.refreshLine(1,True)
    #  @endcode    
    def refreshLine(self,lineNum, display = True):
        if(self.currentMode == self.PS_MODE_TERMINAL):
            self.drawAutoText(self.terminalBuffer[lineNum],10,lineNum*20 + 40, (255,255,255), display = display)
    
    ## drawButton
    def drawButton(self, x, y, width, height, prefix="btns_",text="OK", display=True, align="left"):
        self.fillBmp(x, y, 14, height, prefix+"left.png", display=display)
        self.fillBmp(x+14, y, width-28, height, prefix+"center.png", display=display)
        self.fillBmp(x+width-14, y, 14, height, prefix+"right.png", display=display)
        self.drawAutoText(text,x + 10, y+(height/2)-10, fill = (0,0,0), display=display, align=align)


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
            self.drawDisplay("",False)
            if(self.drawArrowsbool):
                self.drawArrows(False)
            temp = 0
            while(temp < len(self.terminalBuffer)):
                if(self.terminalBuffer[temp] != ""):
                    self.refreshLine(temp, display = False)
                temp += 1
            self.disp.display()
        if(self.currentMode == self.PS_MODE_POPUP):
            xbuff = 20
            ybuff = 20
            #self.fillRect(xbuff,ybuff,self.screenWidth()-(2*xbuff),self.screenHeight()-(2*ybuff),fill = (127,127,127), outline = (255,255,255))
            self.fillBmp(xbuff,ybuff,self.screenWidth()-(2*xbuff),self.screenHeight()-(2*ybuff), "dialogbg.png", display = False)
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
            while(n<len(self.popupText)):
                if ( n > 0 ):
                    offset = 10
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
    #  button = screen.checkButton(0,0,50,50)
    #  @endcode    
    def checkButton(self,x,y,width = 150,height = 50):
        if(self.isTouched()):
            axlb = self.screenXFromImageCoords(x,y)
            aylb = self.screenYFromImageCoords(x,y)
            axub = self.screenXFromImageCoords(x + width,y + height)
            ayub = self.screenYFromImageCoords(x + width,y + height)
            
            
            if(axub<axlb):
                tempx = axub
                axub = axlb
                axlb = tempx
            if(ayub<aylb):
                tempy = ayub
                ayub = aylb
                aylb = tempy
                
            tsx = self.TS_X()
            tsy = self.TS_Y()
            
            tsx2 = self.TS_X()
            tsy2 = self.TS_Y()
            
            if(tsx != tsx2):
                tsx = self.TS_X()
            if(tsy != tsy2):
                tsy = self.TS_Y()
            if(tsx<axub and tsx>axlb and tsy>aylb and tsy<ayub):
                return True
        return False
    
    ## Display pop-up of a question on the screen
    #  @param self The object pointer.
    #  @param question The question that will pop-up on the screen.
    #  @param options The possible answers to the question.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  answer = screen.askQuestion(["Continue?"],["Yes","No"])
    #  @endcode    
    def askQuestion(self, question = ["Continue?"], options = ["Yes","No"]):
        self.popupText = question
        self.buttonText = options
        oldMode = self.currentMode
        self.setMode(self.PS_MODE_POPUP)
        if(len(options)>5):
            print "warning!, buttons may be too small to read"
        while(True):
            if(self.isTouched()):
                tempthis = self.calculateButton(20,20,50) #check four times in a row, and only return if all four readings were the same
                tempthis2 = self.calculateButton(20,20,50)
                tempthis3 = self.calculateButton(20,20,50)
                tempthis4 = self.calculateButton(20,20,50)
                if(tempthis != -1 and tempthis == tempthis2 and tempthis2 == tempthis3 and tempthis3 == tempthis4):
                    self.setMode(oldMode)
                    return tempthis
    
    ## Display Pop-up of 'Yes' or 'No' question on the screen
    #  @param self The object pointer.
    #  @param question The question that will pop-up on the screen.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  ...
    #  answer = screen.askYesOrNoQuestion(["Continue?"])
    #  @endcode    
    def askYesOrNoQuestion(self, question = ["Continue?"]):
        return self.askQuestion(question,["Yes","No"]) == 0
    
                
                
if __name__ == '__main__':#following code demonstrates screen rotation, popup menus, terminal printing, and custom buttons

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
        print "\nQuitting..."
        psb.setMode(psb.PS_MODE_TERMINAL)
        psb.termPrintln("Exiting Program...")
        sys.exit(0)
       
