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
#  August 20, 2015  Andrew Miller     Initial Authoring
#  September 22, 2016  Seth Tenembaum     Additional Functionality

from PiStorms import PiStorms

#Demo Code for the PiStorms and Raspberry Pi

#initial setup code
import os,sys,inspect,time,thread, random,time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
#sys.path.insert(0,parentdir)

#starts an instance of PiStorms
psm = PiStorms()

class Sam:
    '''
    Hello! I'm Sam, the emotional robot.
    I  have my own blog page, check it out here!
    http://www.mindsensors.com/blog/how-to/sam-the-emotional-robot
    My left arm is conencted to BAM1, right in BBM2. My eyes are at BBS2.
    '''

    STARTLE_DELAY = 1 # after you startle me, I won't be startled again for this many seconds
    NOTICE_SOMEONE_DISTANCE = 2000 # the maximum distance, in millimeters, that Sam will display "Hm, is someone there?"
    NOTICE_SOMEONE_DELAY = 1 # higher reduces flicker and filters false sensor values, but decreases responsiveness (1 or 2 reccomended)
    TIMES_TO_WAVE = 2 # when waving, how many times to oscillate my arm
    NOTICE_WAVING_DISTANCE = 1000 # maximum distance, in millimeters, to look for someone waving
    NOTICE_WAVE_DELAY = 2 # after waving, how many seconds to wait before looking for a wave again
    WAVE_LENGTH = 0.5 # how long, in seconds, a hand must be seen or not seen to count as a wave
    MIN_WAVES = 3 # how many waves to look for before waving back


    class Reaction(object):
        '''
        Display an emoticon for a set amount of time,
        then draw a exclamation and comment
        '''
        def __init__(self, image, imageDelay, exclamation, exclamationOffset, exclamationSize,
                     comment, commentOffset, commentSize, dialogDelay):
            self.image = image # emotion (or any arbitrary image) to display fullscreen at 320x240
            self.imageDelay = imageDelay # how long to leave the image on screen
            self.exclamation = exclamation # the large text to print at the top of the screen
            self.exclamationOffset = exclamationOffset # how far from the left edge of the screen to wriet the text, used for centering
            self.exclamationSize = exclamationSize
            self.comment = comment # a smaller text to print below the exclamation
            self.commentOffset = commentOffset
            self.commentSize = commentSize
            self.dialogDelay = dialogDelay # how long to leave the text on screen

        def display(self):
            psm.screen.fillBmp(0, 0, 320, 240, path = currentdir + '/reactionImages/' + self.image)
            time.sleep(self.imageDelay)
            psm.screen.fillRect(0, 0, 320, 240) # clear the image
            psm.screen.drawAutoText(self.exclamation, self.exclamationOffset, 30, fill=(0, 0, 0), size = self.exclamationSize)
            psm.screen.drawAutoText(self.comment, self.commentOffset, 140, fill=(0, 0, 0), size = self.commentSize)
            #time.sleep(self.dialogDelay) # call in startled() instead so the overwritten method in LongReaction can draw its second line
            #psm.screen.fillRect(0, 0, 320, 240) # clear dialog

    class LongReaction(Reaction):
        '''
        Display an emoticon for a set amount of time,
        then draw a exclamation and two lines of comments
        '''
        def __init__(self, image, imageDelay, exclamation, exclamationOffset, exclamationSize,
                     comment, commentOffset, commentSize, comment2, commentOffset2, commentSize2, dialogDelay):
            super(self.__class__, self).__init__(image, imageDelay, exclamation, exclamationOffset, exclamationSize,
                     comment, commentOffset, commentSize, dialogDelay)
            self.comment2 = comment2 # a second line of smaller text to print below the first
            self.commentOffset2 = commentOffset2
            self.commentSize2 = commentSize2

        def display(self):
            super(self.__class__, self).display()
            psm.screen.drawAutoText(self.comment2, self.commentOffset2, 180, fill=(0, 0, 0), size = self.commentSize2)


    REACTIONS = [
        Reaction("frightened.png", 1,  "Sorry,", 75, 70,  "you scared me", 67, 30, 2),
        Reaction("exhausted.png", 1,   "Whew,", 65, 70,   "You scared me there", 25, 30, 2),
        Reaction("shocked.png", 1,     "Yikes!", 70, 70,  "Didn't see you there", 35, 30, 2),
        Reaction("eyeRoll.png", 1,     "Oh,", 100, 70,    "a human", 85, 40, 1.2),
        LongReaction("eyeRoll.png", 1, "Really?", 50, 70, "Are you trying to", 55, 30, "scare me again?", 52, 30, 2),
        LongReaction("wink.png", 1,    "Again?", 55, 70,  "Have you tried", 60, 30,    "Blockly programming?", 15, 30,   3),
    ]

    def __init__(self, pistorms):
        self.psm = pistorms
        self.RIGHT_ARM = psm.BBM2 # my right, your left when facing me
        self.LEFT_ARM = psm.BAM1
        # set to function, invoke `self.eyes()` for value
        self.eyes = psm.BBS2.distanceUSEV3 # in millimeters!
        self.lastSawSomeone = time.time()
        self.seeWavingNow = False
        self.wavesSeen = 0
        self.lastWave = time.time()

        self.drawGreeting()
        self.RIGHT_ARM.runSecs(secs=1, speed=20, brakeOnCompletion=True) # lower arms
        self.LEFT_ARM.runSecs(secs=1, speed=20, brakeOnCompletion=True)
        time.sleep(1) # wait for motors to finish
        self.RIGHT_ARM.resetPos()
        self.LEFT_ARM.resetPos()
        self.lastStartledAt = time.time()
        psm.untilKeyPress(self.mainLoop)
        self.psm.led(1, 0,0,0) # turn off LEDs after the main loop
        self.psm.led(2, 0,0,0)

    def mainLoop(self):
        if self.eye,s() < 500 and time.time() - self.lastStartledAt > self.STARTLE_DELAY:
            self.startled()
            self.lastStartledAt = time.time()
        elif self.checkWaving():
            self.wave()
            self.lastStartledAt = time.time() # don't get startled right after waving at someone
        else:
            self.isSomeoneThere()

    def startled(self):
        # quickly flash LEDs between red and green, twice
        for i in range(2):
            self.psm.led(1, 255, 0, 0) # red
            self.psm.led(2, 255, 0, 0)
            time.sleep(.1)
            self.psm.led(1, 0, 255, 0) # green
            self.psm.led(2, 0, 255, 0)
            time.sleep(.1)

        # throw arms backward and hold them there
        self.RIGHT_ARM.runDegs(-130, brakeOnCompletion = True)
        self.LEFT_ARM.runDegs(-130, brakeOnCompletion = True)

        reaction = random.choice(self.REACTIONS)
        reaction.display()
        time.sleep(reaction.dialogDelay)

        # slowly lower arms back to resting position
        self.RIGHT_ARM.runSecs(secs = 3, speed = 20, brakeOnCompletion = True)
        self.LEFT_ARM.runSecs(secs = 3, speed = 20, brakeOnCompletion = True)
        time.sleep(3)

        # reset LEDs to a restful blue
        self.psm.led(1,0,0,255)
        self.psm.led(2,0,0,255)

        self.drawGreeting()

    def drawGreeting(self):
        # clear the screen of any unwanted text by filling the screen with a white rectangle
        self.psm.screen.fillRect(0, 0, 320, 240)
        self.psm.led(1, 0, 0, 255) # blue
        self.psm.led(2, 0, 0, 255)
        self.psm.screen.drawAutoText("Hello", 80, 30, fill = (255, 0, 0), size = 70)
        self.psm.screen.drawAutoText("I am Sam", 70, 140, fill = (255, 0, 0), size = 45)

    def isSomeoneThere(self):
        if self.eyes() < self.NOTICE_SOMEONE_DISTANCE:
            self.psm.screen.drawAutoText("Hm, someone there?", 30, 195, fill=(0, 0, 255), size = 30)
            self.lastSawSomeone = time.time()
        elif time.time() - self.lastSawSomeone > self.NOTICE_SOMEONE_DELAY: # don't flicker
            self.psm.screen.fillRect(30, 195, 320, 240)

    def wave(self):
        self.RIGHT_ARM.runDegs(-130, speed = 50, brakeOnCompletion = True)
        time.sleep(0.5)

        for i in range(self.TIMES_TO_WAVE):
            self.RIGHT_ARM.runDegs(40, speed = 70, brakeOnCompletion = True)
            time.sleep(0.25)
            self.RIGHT_ARM.runDegs(-40, speed = 70, brakeOnCompletion = True)
            time.sleep(0.25)

        time.sleep(0.5)
        self.RIGHT_ARM.runSecs(secs=3, speed=20, brakeOnCompletion=True)
        time.sleep(3)

    def checkWaving(self):
        if self.wavesSeen > self.MIN_WAVES:
            #self.wave()
            self.seeWavingNow = False
            self.wavesSeen = 0
            self.lastWave = time.time() + self.NOTICE_WAVE_DELAY
            return True

        timeDiff = time.time() - self.lastWave
        if timeDiff > 4:
            self.wavesSeen = 0
        # do I see a hand now (and wasn't just seeing one)?
        if not self.seeWavingNow and self.eyes() < self.NOTICE_WAVING_DISTANCE and timeDiff > self.WAVE_LENGTH:
            self.seeWavingNow = True
            self.wavesSeen = self.wavesSeen + 1
            self.lastWave = time.time()
        # was I seeing a hand and don't anymore?
        if self.seeWavingNow and self.eyes() > self.NOTICE_WAVING_DISTANCE and timeDiff > self.WAVE_LENGTH:
            self.seeWavingNow = False
            self.wavesSeen = self.wavesSeen + 1 # if commented: only count a wave as a hand entering view
            self.lastWave = time.time()

        return False


'''
Display, in huge numbers, the current reading of the ultrasonic sensor
'''
def ultrasonicDebug():
    def printDistance():
        psm.screen.fillRect(0, 0, 320, 240)
        psm.screen.drawAutoText(str(psm.BBS2.distanceUSEV3()), 10, 50, fill=(0, 0, 255), size = 120)
        #print psm.BBS2.distanceUSEV3() # if you want to print the values, maybe redirect the output to a file
    psm.untilKeyPress(printDistance)


Sam(psm) # while loop will halt execution here

