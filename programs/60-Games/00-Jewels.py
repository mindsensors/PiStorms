#!/usr/bin/env python
#
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
#Learn more product option visit us @  http://www.mindsensors.com/

import os,sys,inspect,time,thread,random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

from PiStorms import PiStorms
psm = PiStorms()

board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
score = 0
def generate_board():
	j = 0
	for row in board:
		i = 0
		for place in row:
			rand = random.randint(1,4)
			row[i] = rand
			i += 1
		print board[j]
		j += 1
	return board


def triplets(board):
	replacedR = []
	replacedC = []
	tripletCount = 0
	row = 0
	column = 0
	totalR = len(board)
	totalC = len(board[0])
	while row <= totalR-1:
		column = 0
		while column <= totalC-1:
			adjR = [row-2, row-1, row, row+1, row+2]
			adjC = [column-2, column-1, column, column+1, column+2]
			placeVal = board[row][column]
			triplet = str(placeVal)+str(placeVal)+str(placeVal)
			vert = ""
			v = 0
			for R in adjR:
				if R<0 or R>4:
					adjR[v] = 0
				vert += str(board[v][column])
				v += 1
			horiz = ""
			h = 0
			for C in adjC:
				if C<0 or C>4:
					adjC[h] = 0
				horiz += str(board[row][h])
				h += 1

			if (triplet in vert) or (triplet in horiz):
				tripletCount += 1
				replace = str(random.randint(1,4))+str(random.randint(1,4))+str(random.randint(1,4))
				vert = vert.replace(triplet,replace)
				horiz = horiz.replace(triplet,replace)
				v = 0
				for R in adjR:
					board[R][column] = int(vert[v])
					v += 1
				h = 0
				for C in adjC:
					board[row][C] = int(horiz[h])
					h += 1
			column += 1
		row += 1
	print "Triplets:", tripletCount
	return board, tripletCount

def switch(board, x1, y1, x2, y2):
	if ((x1+1==x2)or(x1-1==x2))^((y1+1==y2)or(y1-1==y2)):
		first = board[y1][x1]
		second = board[y2][x2]
		board[y1][x1] = second
		board[y2][x2] = first
		print "Switched", x1, y1, "and", x2, y2
		return True
	else:
		print "*****Invalid switch*****"
		return False

	#make it normal color
	j = 0
	for row in board:
		print board[j]
		j += 1


'''
board = generate_board()
triplets(board)
j = 0
for row in board:
	print board[j]
	j += 1
doSwitch = raw_input("Do you want to switch tiles? (y/n)")
while (doSwitch != "n"): #and (tripletCount != 0)
	if doSwitch == "y":
		j = 0
		for row in board:
			print board[j]
			j += 1
		switch(board)
		triplets(board)
	else:
		print "Please type  \"y\" or \"n\""
	j = 0
	for row in board:
		print board[j]
		j += 1
	triplets(board)
	doSwitch = raw_input("Do you want to switch tiles? (y/n)")'''


def checkButton(board):

	r = 0
	p = 0
	t0 = time.clock()
	touch = []
	for row in board:
		p = 0
		for place in row:
			touched =  psm.screen.checkButton((p*48), (r*40), width = 40, height = 48)
			if touched:
				touch.append(r)
				touch.append(p)
			p += 1
		r += 1
	return touch

def printBoard(board):
	r = 0
	p = 0
	for row in board:
		p = 0
		for place in row:
			#psm.screen.drawButton((p*48), (r*40), width = 40, height = 48, text=str(board[r][p]), display=False)
			if board[r][p] == 1:
				img = "GemRed.png"
			elif board[r][p] == 2:
				img = "GemBlue.png"
			elif board[r][p] == 3:
				img = "GemGreen.png"
			elif board[r][p] == 4:
				img = "GemYellow.png"
			elif board[r][p] == 5:
				img = "GemBlack.png"
			psm.screen.fillBmp((p*48), (r*40), width = 40, height = 48, path = currentdir+'/'+img)
			p += 1
		r += 1

board = generate_board()
board = triplets(board)[0]
board = triplets(board)[0]
board = triplets(board)[0]
board = triplets(board)[0]
printBoard(board)

scoreMessage = "Score:" + str(score)
psm.screen.drawButton(235, 0, width = 85, height = 96, text=scoreMessage, display=True)
psm.screen.termPrintAt(9, "Touch a jewel")

doExit = False
touches = [[0,0]] #[[r1, p1], [r2, p2]] <-> [[y1, x1], [y2, x2]]
print "start loop"
while (not doExit):
	a = 0
	touch = checkButton(board)
	if (touch !=  []) and (touch != touches[-1]):
		touches.append(touch)
		a = 1
	if (len(touches) == 2) and (a == 1):
		psm.screen.termPrintAt(9, "Touch another jewel")
	elif (len(touches) == 3) and (a == 1):
		psm.screen.termPrintAt(9, "Switching")
		didSwitch = switch(board, touches[1][1], touches[1][0], touches[2][1], touches[2][0])
		#printBoard(board)
		if didSwitch:
			print""
			time.sleep(0.2)
			p = touches[1][1]
			r = touches[1][0]
			if board[r][p] == 1:
				img = "GemRed.png"
			elif board[r][p] == 2:
				img = "GemBlue.png"
			elif board[r][p] == 3:
				img = "GemGreen.png"
			elif board[r][p] == 4:
				img = "GemYellow.png"
			elif board[r][p] == 5:
				img = "GemBlack.png"
			psm.screen.fillBmp((p*48), (r*40), width = 40, height = 48, path = currentdir+'/Gem.png')
			time.sleep(0.1)
			psm.screen.fillBmp((p*48), (r*40), width = 40, height = 48, path = currentdir+'/'+img)
			p = touches[2][1]
			r = touches[2][0]
			if board[r][p] == 1:
				img = "GemRed.png"
			elif board[r][p] == 2:
				img = "GemBlue.png"
			elif board[r][p] == 3:
				img = "GemGreen.png"
			elif board[r][p] == 4:
				img = "GemYellow.png"
			elif board[r][p] == 5:
				img = "GemBlack.png"
			psm.screen.fillBmp((p*48), (r*40), width = 40, height = 48, path = currentdir+'/Gem.png')
			time.sleep(0.1)
			psm.screen.fillBmp((p*48), (r*40), width = 40, height = 48, path = currentdir+'/'+img)
		touches = [[0,0]]
		tripReturn = triplets(board)
		print tripReturn
		board = tripReturn[0]
		score += 5 * tripReturn[1]
		scoreMessage = "Score:" + str(score)
		psm.screen.drawButton(235, 0, width = 85, height = 96, text=scoreMessage, display=True)
		board = triplets(board)[0]
		board = triplets(board)[0]
		board = triplets(board)[0]
		board = triplets(board)[0]
		printBoard(board)
		psm.screen.termPrintAt(9, "Touch a jewel")
		j = 0
		for row in board:
			print board[j]
			j += 1
	if(psm.isKeyPressed()):
			psm.screen.clearScreen()
			psm.screen.termPrintAt(9, "Exiting to menu")
			time.sleep(0.5)
			doExit = True

