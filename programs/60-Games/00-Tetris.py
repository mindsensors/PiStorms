#!/usr/bin/env python
#
# Copyright (c) 2015 mindsensors.com and Kevin Chabowski
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
# Date       Author           Comments
# 2010       Kevin Chabowski  Initial Pygame implementation
# Sept 2016  Seth  Tenembaum  Initial PiStorms adaptation

import os,sys,inspect,time,thread
import socket,fcntl,struct

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from PiStorms import PiStorms

psm = PiStorms(rotation = 2)


from random import randrange as rand
import pygame, sys

# The configuration
cell_size = 18
cols = 13
rows = 18
maxfps = 30
msPerTick = float(1000) / maxfps

colors = [
    (0,   0,   0  ),
    (0,   255, 255), # I: cyan
    (0,   0,   255), # J: blue
    (255, 165, 0  ), # L: orange
    (255, 255, 0  ),  # O: yellow
    (0,   255, 0  ), # S: lime
    (128, 0,   128), # T: yellow
    (255, 0,   0  ), # Z: red
]

# Define the shapes of the single parts
tetris_shapes = [
    [[1, 1, 1, 1]], # I
    
    [[2, 2, 2], # J
     [0, 0, 2]],
    
    [[3, 3, 3], # L
     [3, 0, 0]],
    
    [[4, 4], # O
     [4, 4]],
    
    [[0, 5, 5], # S
     [5, 5, 0]],
    
    [[6, 6, 6], # T
     [0, 6, 0]],
    
    [[7, 7, 0], # Z
     [0, 7, 7]]
]

def rotate_clockwise(shape):
    return [ [ shape[y][x]
            for y in xrange(len(shape)) ]
        for x in xrange(len(shape[0]) - 1, -1, -1) ]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                if cell and board[ cy + off_y ][ cx + off_x ]:
                    return True
            except IndexError:
                return True
    return False

def remove_row(board, row):
    del board[row]
    return [[0 for i in xrange(cols)]] + board

def join_matrixes(mat1, mat2, mat2_off):
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy+off_y-1 ][cx+off_x] += val
    return mat1

def new_board():
    board = [ [ 0 for x in xrange(cols) ]
            for y in xrange(rows) ]
    board += [[ 1 for x in xrange(cols)]]
    return board

class TetrisApp(object):
    
    class InputDelay(object):
        def __init__(self, maxExecutionsPerSecond = 1, holdEnabled = True):
            self.timeLastExecuted = time.time()
            self.currentState = False
            self.maxRateMs = float(1000) / maxExecutionsPerSecond
            self.canHold = holdEnabled
        
        def canExec(self):
            if self.currentState == self.canHold and time.time() - self.timeLastExecuted > self.maxRateMs:
                self.timeLastExecuted = time.time()
                return True
            else:
                return False
        
        def set(self, state):
            self.currentState = state
        
    
    def __init__(self):
        pygame.init()
        pygame.joystick.Joystick(0).init()
        self.screen = psm.screen
        self.init_inputs()
        self.init_game()

    def init_inputs(self): # initialize input timing/delays
        self.inputs = {}
        self.inputs['moveLeft'] = TetrisApp.InputDelay(maxExecutionsPerSecond = 20)
        self.inputs['moveRight'] = TetrisApp.InputDelay(maxExecutionsPerSecond = 20)
        self.inputs['spin'] = TetrisApp.InputDelay(maxExecutionsPerSecond = 5, holdEnabled = False)
        self.inputs['drop'] = TetrisApp.InputDelay(maxExecutionsPerSecond = 30)
        self.inputs['instaDrop'] = TetrisApp.InputDelay(holdEnabled = False)
        self.inputs['pause'] = TetrisApp.InputDelay(holdEnabled = False)
    
    def new_stone(self):
        self.stone = self.nextStone
        self.nextStone = tetris_shapes[rand(len(tetris_shapes))]
        self.stone_x = int(cols / 2 - len(self.stone[0])/2)
        self.stone_y = 0
        
        if check_collision(self.board, self.stone, (self.stone_x, self.stone_y)):
            self.gameover = True
    
    def init_game(self):
        self.board = new_board()
        self.nextStone = [[0]] # avoid AttributeError
        self.new_stone()
        self.new_stone()
        self.level = 1
        self.score = 0
        self.lines = 0
        self.newStoneDelay = 1
        self.nextStoneAt = time.time() + self.newStoneDelay
        self.gameover = False
        self.paused = False
    
    def draw_matrix(self, matrix, offset, refresh = False):
        off_x, off_y  = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    self.screen.fillRect(
                            (off_x+x) * cell_size,
                            (off_y+y) * cell_size,
                            cell_size, cell_size,
                            fill = colors[val],
                            display = False)
        if refresh:
            self.screen.fillRect(0,0,0,0,display=True)
            # `self.screen.refresh()` doesn't work for some reason, maybe fillRect writes to a different buffer?
    
    def add_cl_lines(self, n):
        linescores = [0, 40, 100, 300, 1200]
        self.lines += n
        self.score += linescores[n] * self.level
        if self.lines >= self.level*6:
            self.level += 1
            newdelay = 1-0.05*(self.level-1)
            self.newStoneDelay = 0.1 if newdelay < 0.1 else newdelay
    
    def move(self, delta_x):
        if not self.gameover and not self.paused:
            new_x = self.stone_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > cols - len(self.stone[0]):
                new_x = cols - len(self.stone[0])
            if not check_collision(self.board, self.stone, (new_x, self.stone_y)):
                self.stone_x = new_x
    
    def drop(self, manual = False):
        if not self.gameover and not self.paused:
            self.score += 1 if manual else 0
            self.stone_y += 1
            if check_collision(self.board, self.stone, (self.stone_x, self.stone_y)):
                self.board = join_matrixes(self.board, self.stone, (self.stone_x, self.stone_y))
                self.new_stone()
                cleared_rows = 0
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = remove_row(self.board, i)
                            cleared_rows += 1
                            break
                    else:
                        break
                self.add_cl_lines(cleared_rows)
                return True
        return False
    
    def insta_drop(self):
        if not self.gameover and not self.paused:
            while(not self.drop(True)):
                pass
    
    def rotate_stone(self):
        if not self.gameover and not self.paused:
            new_stone = rotate_clockwise(self.stone)
            if not check_collision(self.board, new_stone, (self.stone_x, self.stone_y)):
                self.stone = new_stone
    
    def toggle_pause(self):
        self.paused = not self.paused
    
    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False
    
    def quit_game(self):
        psm.led(1, 0, 0, 0)
        psm.led(2, 0, 0, 0)
        raise SystemExit("Exiting...")
    
    def run(self):
        while True:
            tickStart = time.time()
            
            # 320 for both width and height to handle both orientations
            self.screen.fillRect(0, 0, 320, 320, fill = (0,0,0), display = False)
            
            if self.gameover:
                self.screen.drawAutoText("Game Over!", 15, 15, fill = (255,255,255), size = 35, display = False)
                self.screen.drawAutoText("Your score: %d" % self.score, 15, 70, fill = (255,255,255), size = 28, display = False)
                self.screen.drawAutoText("Press start to", 15, 130, fill = (255,255,255), size = 24, display = False)
                self.screen.drawAutoText("start another game.", 15, 160, fill = (255,255,255), size = 24, display = True)
            elif self.paused:
                self.screen.drawAutoText("Paused", 20, 60, fill = (255,255,255), size = 60, display = False)
                self.screen.drawAutoText("Press the center", 35, 160, fill = (255,255,255), size = 24, display = False)
                self.screen.drawAutoText("button to resume.", 32, 190, fill = (255,255,255), size = 24, display = True)
            else:
                self.draw_matrix(self.stone, (self.stone_x, self.stone_y))
                self.draw_matrix(self.board, (0,0), refresh = True)
                colorIndex = [c for c in self.nextStone[0] if c != 0][0] # get color number of piece (not 0 or empty space)
                psm.led(1, *(colors[colorIndex]))
                psm.led(2, *(colors[colorIndex]))
            
            if time.time() >= self.nextStoneAt:
                self.drop()
                self.nextStoneAt = self.nextStoneAt + self.newStoneDelay
            
            for event in pygame.event.get():
                joystick = pygame.joystick.Joystick(0)
                
                self.inputs['moveLeft'].set(joystick.get_axis(0) < -0.7 or joystick.get_button(0))
                self.inputs['moveRight'].set(joystick.get_axis(0) > 0.7 or joystick.get_button(2))
                self.inputs['spin'].set(joystick.get_axis(1) < -0.7 or joystick.get_button(3)) # joystick up or triangle
                self.inputs['drop'].set(joystick.get_axis(1) > 0.7 or joystick.get_button(1))
                self.inputs['instaDrop'].set(
                    joystick.get_button(4) or joystick.get_button(5) or # all triggers
                    joystick.get_button(6) or joystick.get_button(7) or
                    joystick.get_button(10) or joystick.get_button(11) # joystick pressed in
                )
                self.inputs['pause'].set(joystick.get_button(12)) # center "dG" button
                if joystick.get_button(8): # select
                    self.quit_game()
                if joystick.get_button(9): # start
                    self.start_game()
            
            if self.inputs['moveLeft'].canExec():
                self.move(-1)
            if self.inputs['moveRight'].canExec():
                self.move(1)
            if self.inputs['spin'].canExec():
                self.rotate_stone()
            if self.inputs['drop'].canExec():
                self.drop(manual = True)
            if self.inputs['instaDrop'].canExec():
                self.insta_drop()
            if self.inputs['pause'].canExec():
                self.toggle_pause()
            if psm.isKeyPressed(): # GO button pressed
                self.quit_game()
            
            elapsed = time.time() - tickStart
            if elapsed < msPerTick: # if we've finished this frame faster than the amount of time this frame should take
                time.sleep((msPerTick - elapsed) / 1000) # sleep the rest of that time


if __name__ == '__main__':
    App = TetrisApp()
    App.run()
