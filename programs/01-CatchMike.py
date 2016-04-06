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

#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/

# History:
# Date      Author      Comments
# 08/11/15  Andrew     Initial Authoring
# 10/14/15  Nitin      performance imporvements
#
#Demo Code for the PiStorms and Raspberry Pi
# initial setup code

import os,sys,inspect,time,thread,random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
from PiStorms import PiStorms

# starts an instance of PiStorms
psm = PiStorms()

### setup variables ###
# exit is used to eventually exit the main running loop
# score will keep track of the player's current score
# dispScore tracks the displayed score
exit = False
score = 1
dispScore = -1

# turns the leds off from any previous program
psm.led(1,0,0,0)
psm.led(2,0,0,0)

# sets screen to a white background
psm.screen.fillRect(0, 0, 320, 240)

# initial loading screen
psm.screen.fillBmp(110, 20, 100, 100, path = currentdir+'/'+"faceAwesome.png")
psm.screen.drawAutoText("Hi I am Mike!", 15, 140, fill=(0, 0, 0), size = 30)
psm.screen.drawAutoText("Catch me if you can!!", 15, 170, fill=(0, 0, 0), size = 30)
psm.screen.drawAutoText("(Press Go button to quit)", 15, 210, fill=(0, 0, 0), size = 15)

# display loading screen for 4 seconds, then white background
time.sleep(4)
psm.screen.fillRect(0, 0, 320, 240)

# function to flash the leds equivalent to player's current score
def ledFlash(num):
    quit = False # used to quit the loop later
    x = 0 # tracks loop iterations
    while(not quit):
        if(x % 2 == 0): # if the number of loop iterations modulo 2 = 0, then:
            psm.led(1,255,0,0) # flash LED 1 red
            time.sleep(0.06) # for 6/100ths of a second
        if(x % 2 == 1): # if the number of loop iterations modulo 2 = 1, then:
            psm.led(2,255,0,0) #flash LED 2 red
            time.sleep(0.06) # for 6/100ths of a second
        psm.led(1,0,0,0) # set both LEDs to off
        psm.led(2,0,0,0)
        time.sleep(0.01) # wait 1/100th of a second
        x += 1 # increment loop iteration count
        if(x >= num): # if the loop iteration count is higher than the input, then:
            x = 0 # set loop iteration to 0
            quit = True # quit becomes true and the loop is escaped

### main running loop ###
# moves "Mike" (the smiley face) around the screen to random locations
# tracks the players score
miliseconds = int(round(time.time()*1000)) 
psm.resetKeyPressCount

while(not exit):
    randX = random.randint(0, 245)  # selects a random x coordinate for Mike
                                    # max of 245 so he will not appear off the screen (screen x value is 320, so 320 - Mike's width (75) = 245)
    randY = random.randint(0, 115)  # selects a random y coordinate for Mike
                                    # max of 115 so he will not appear off the screen (screen y value is 240, but the score display starts at yvalue of 190, so 190 - Mike's height (75) = 115)
                                    
    psm.screen.fillBmp(randX, randY, 95-score, 95-score, path = currentdir+'/'+"faceAwesome.png") # display Mike at the random coordinates
    miliseconds = int(round(time.time()*1000)) 
    while (int(round(time.time()*1000)) - miliseconds)< (150+1000/score):
        if(psm.screen.checkButton(randX - (score), randY - (score), 95-score, 95-score)): # if an invisible box drawn around Mike's position is tapped, then:
            psm.screen.fillRect(0,0,320,320) # white screen
            psm.screen.drawAutoText("You got me!", 15, 140, fill=(0, 0, 0), size = 45) # draw text
            score += 1 # increment player's score
            if score < 5 : 
                ledFlash(score) # run the ledFlash function using the players current score as the input
            psm.screen.fillRect(0,0,320,320) # back to white screen
    psm.screen.fillRect(randX, randY, 95-score, 95-score) # cover up Mike after each drawing of him
    
    if(dispScore != score): # if the displayed score does not equal the player's current score, then redraw the score count
        if score > 50 :
            exit = True 
            psm.screen.drawAutoText("Congratulations You Win:", 15, 190, fill=(0, 0, 0), size = 35) # draw "score:"    
        else :
            psm.screen.drawAutoText("score:", 15, 190, fill=(0, 0, 0), size = 25) # draw "score:"
            psm.screen.drawAutoText(str(score-1), 100, 190, fill=(0, 0, 0), size = 25) # draw the player's score
            dispScore = score # log the change of score to the variable "dispScore"
        
    #print psm.isKeyPressed()
    #if(psm.isKeyPressed() == True): # if the GO button is pressed
    if(psm.isKeyPressed() == 1): # if the GO button is pressed    
        time.sleep(0.5)
        exit = True # escape loop
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        exit = True 
    else:
        pass