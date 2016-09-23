# Tic Tac Toe

import random
import os,sys,inspect,time,thread
import socket,fcntl,struct    

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms

psm = PiStorms()
psm.led(1,0,0,0)
psm.led(2,0,0,0)


'''
exit = False
while not exit:
    if psm.screen.checkButton(0,0,320,240):
        psm.led(2,255,0,0)
    else:
        psm.led(2,0,0,0)
    
    if(psm.isKeyPressed() == True): # if the GO button is pressed
            exit = True
'''

def drawLines():
    #210x210, 55px side border, 15px vertical border,  70px squares
    psm.screen.fillRect(124,15, 2,210)
    psm.screen.fillRect(196,15, 2,210)
    psm.screen.fillRect(55,84, 210,2)
    psm.screen.fillRect(55,154, 210,2)

def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    
    k = { 'X': {
            'x': [76,150,224],
            'y': [28,103,177],
            's': 36 },
          'O': {
            'x': [69,143,216],
            'y': [20,92,167],
            's': 52 }
    }
    
    for y in range(3):
        for x in range(3):
            c = board[x+1+y*3]
            if c != ' ':
                psm.screen.drawAutoText(c, k[c]['x'][x], k[c]['y'][2-y], size = k[c]['s'])

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the
    # computer's letter as the second.
    psm.screen.fillRect(0,0, 360,240, (0,0,0))
    psm.screen.drawAutoText('Do you want to be X or O?', 13,10, size=26)
    psm.screen.fillRect(11,55, 144,182, (255,0,0))
    psm.screen.fillRect(166,54, 147,180, (0,0,255))
    psm.screen.drawAutoText('X', 74,127, size=36)
    psm.screen.drawAutoText('O', 224,121, size=42)

    letter = ''
    while not letter:
        if psm.screen.checkButton(11,55, 144,182):
            letter = 'X'
        elif psm.screen.checkButton(166,54, 147,180):
            letter = 'O'
        if(psm.isKeyPressed() == True):
            raise SystemExit()
    if letter == 'X':
        psm.led(2,255,0,0)
    elif letter == 'O':
        psm.led(1,0,0,255)
        
    time.sleep(1) # missing 'GO' quit check
    psm.led(1,0,0,0)
    psm.led(2,0,0,0)
    psm.screen.fillRect(0,0, 360,240, (0,0,0))

    # the first element in the tuple is the player's letter, the second is the
    # computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise
    # it returns False.
    
    #psm.screen.fillRect(0,0, 360,240, (0,0,0))
    return psm.screen.askYesOrNoQuestion(['Do you want to play again?'])

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that
    # player has won.
    # We use bo instead of board and le instead of letter so we don't have to
    # type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his or her move.
    #psm.screen.termPrintAt(9, 'What is your next move?')
 
    move = 0
    while not (move >= 1 and move <= 10):# or not isSpaceFree(board, int(move)):
        for y in range(3):
            for x in range(3):
                 if psm.screen.checkButton(55+x*70, y*70, 70,70):
                    #psm.led(2,128*x,128*y,255)
                    move = x+1+(2-y)*3 #  like a number pad, not x+1+y*3
    return move

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and
    # return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return
    # False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    drawLines()
    drawBoard(theBoard)
    psm.screen.termPrintAt(9, 'The ' + turn + ' will go first.')
    time.sleep(1)
    gameIsPlaying = True
    
    while gameIsPlaying:
        if (turn == 'player' and playerLetter == 'X') or (turn == 'computer' and computerLetter == 'X'):
            psm.led(2,255,0,0)
        if (turn == 'player' and playerLetter == 'O') or (turn == 'computer' and computerLetter == 'O'):
            psm.led(1,0,0,255)
        if turn == 'player':
            psm.screen.termPrintAt(9, 'Player\'s turn...')
        else:
            psm.screen.termPrintAt(9, 'Computer\'s turn...')
        drawBoard(theBoard)
        
        if turn == 'player':
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            turn = 'computer'
        else:
            time.sleep(1)
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            turn = 'player'
                
        psm.led(1,0,0,0)
        psm.led(2,0,0,0)
        drawBoard(theBoard)
        
        if isWinner(theBoard, playerLetter):
            psm.screen.termPrintAt(9, 'Hooray! You have won the game!')
            time.sleep(2)
            gameIsPlaying = False
        if isWinner(theBoard, computerLetter):
            psm.screen.termPrintAt(9, 'The computer has beaten you!')
            time.sleep(2)
            gameIsPlaying = False
        
        if gameIsPlaying and isBoardFull(theBoard):
            psm.screen.termPrintAt(9, 'The game is a tie!')
            time.sleep(2)
            gameIsPlaying = False
        
    if not playAgain():
        break
