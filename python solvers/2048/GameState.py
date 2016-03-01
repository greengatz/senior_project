'''
Created on Jan 11, 2016

@author: John
'''

from Directions import *
import random
from random import randrange

class GameState(object):
    '''
    This will be passed to a solver, which will use information regarding
    game state to determine the move.
    '''

    def __init__(self):
        '''
        Constructor
        
        Initializes the gameboard and adds two tiles to it.
        '''
        self.gameArray = [[0 for x in range(4)] for x in range(4)]
        self.addRandomTile()
        self.addRandomTile()
        self.score = 0
        
        pass
    
    
    'check game state'
    def isGoing(self):
        return self.isValid(Move.up) or self.isValid(Move.right) or self.isValid(Move.down) or self.isValid(Move.left)
    
    
    'determines if a move would progress the game'
    def isValid (self, move, board=None):
        if board == None:
            board = self.copyArr()
        
        isValid = False
        
        board = self.preRotate(move, board)
        for x in range(0, 4):
            isValid = isValid or self.canSlideDown(x, move, board)
        board = self.postRotate(move, board)
        
        return isValid


    'says if the given column can slide down'
    def canSlideDown(self, column, move, board):
        foundTile = False
        
        for i in range(0, 3):
            if board[i][column] != 0:
                foundTile = True
            
            if foundTile and (board[i][column] == 0 or board[i + 1][column] == 0):
                return True
            if board[i][column] == board[i + 1][column] and board[i][column] != 0:
                return True
        
        return False
    
    
    'determines if the current game state is different the given one'
    'TODO this method seems unnecessary, probably remove it'
    def isSame(self, testArr):
        for x in range(0, 4):
                for y in range(0, 4):
                    if testArr[y][x] != self.gameArray[y][x]:
                        return False
        return True
    
    
    'tries to take a move, if it is invalid it fails and announces it'
    def takeMove (self, move):
        if not self.isValid(move):
            print("invalid move chosen")
            return
        
        self.gameArray = self.executeMove(move)
        self.addRandomTile()
        return
    
    
    'creates a copy of our game state'
    def copyArr (self):
        newArr = [[0 for x in range(4)] for x in range(4)]
        
        for x in range(0, 4):
                for y in range(0, 4):
                    newArr[y][x] = self.gameArray[y][x] 
                    
        return newArr
    
    
    'slides the tiles in the column down'
    def slideDown (self, column, board):     
        x = 2
        y = 0
        limit = 3
        scoreIncrease = 0

        while (x >= 0):
            if (board[x][column] != 0):
                y = x + 1
                while (y <= limit):
                    # if we find a match
                    if (board[x][column] == board[y][column]):
                        board[y][column] += board[x][column]
                        scoreIncrease += board[y][column]
                        board[x][column] = 0
                        limit = y - 1
                        y = 5
                    
                    # if we find the next tile can't match
                    elif (board[x][column] != board[y][column] and board[y][column] != 0):
                        temp = board[x][column]
                        board[x][column] = 0
                        board[y - 1][column] = temp
                        limit = y - 1
                        y = 5
                    
                    # if we are at end of column
                    elif (board[y][column] == 0 and y == limit):
                        board[y][column] = board[x][column]
                        board[x][column] = 0
                        y = 5
                    
                    # no choice found, keep searching
                    y += 1
            x = x - 1
        
        return scoreIncrease
    
    
    'rotates the board so a move will be down'
    def preRotate (self, move, board):
        if (move == Move.up):
            board = self.rotateClockwise(board)
            board = self.rotateClockwise(board)
        elif (move == Move.right):
            board = self.rotateClockwise(board)
        elif (move == Move.down):
            pass
        elif (move == Move.left):
            board = self.rotateClockwise(board)
            board = self.rotateClockwise(board)
            board = self.rotateClockwise(board)
        
        return board
    
    
    'rotates the board to its initial orientation after the move'
    def postRotate (self, move, board):
        if (move == Move.up):
            board = self.rotateClockwise(board)
            board = self.rotateClockwise(board)
        elif (move == Move.right):
            board = self.rotateClockwise(board)
            board = self.rotateClockwise(board)
            board = self.rotateClockwise(board)
        elif (move == Move.down):
            pass
        elif (move == Move.left):
            board = self.rotateClockwise(board)
            
        return board
    
    
    'moves the tiles based on the chosen move'
    def executeMove (self, move, board=None):
        if (board == None):
            board = self.copyArr()
            incrScore = True
        
        toIncr = 0
        board = self.preRotate(move, board)
        for x in range(0, 4):
            toIncr = self.slideDown(x, board)
        board = self.postRotate(move, board)
        
        if incrScore:
            self.score += toIncr
        
        return board
    
    
    'returns the games state'
    def getState(self):
        return self.gameArray
    
    
    'rename x and y'
    def printState(self, board = None):
        if (board == None):
            board = self.gameArray
        
        for x in range(0, 4):
            print(str(board[x][0]) + " " + str(board[x][1]) + " " + str(board[x][2]) + " " + str(board[x][3]))
            print(" ")
        pass
    
    
    'adds a random tile to the board'
    def addRandomTile(self):
        tileToAdd = 2
        if(randrange(0, 10) == 0):
            tileToAdd = 4
        
        openSlots = 0;
        
        'determine where the tile can go'
        for x in range(0, 4):
            for y in range(0, 4):
                if self.gameArray[x][y] == 0:
                    openSlots += 1
        
        'determine where the tile will go'
        threshold = 1 / openSlots
        test = random.random() # done this way to avoid overhead in calling random
        
        for x in range(0, 4):
            for y in range(0, 4):
                threshold = 1 / openSlots
                test = random.random()

                if self.gameArray[x][y] == 0:
                    if test <= threshold:
                        self.gameArray[x][y] = tileToAdd
                        return
                    else:
                        openSlots = openSlots - 1
        
        print("ERROR: NO TILE ADDED")
        self.printState()
        return
    
    
    'returns the total score on the table'
    def getScore(self):
        return self.score
    
    'sets the score, useful for replicating gamestates'
    def setScore(self, newScore):
        self.score = newScore
    
    'returns the highest tile on the board'
    def getMaxTile(self):
        tile = 0
        for x in range(0, 4):
            for y in range(0, 4):
                if(self.gameArray[x][y] > tile):
                    tile = self.gameArray[x][y]
        return tile
    
    
    'takes in a board, returns a copy of it rotated clockwise'
    def rotateClockwise(self, board = None):
        if (board == None):
            board = self.gameArray
        
        newArr = [[0 for x in range(4)] for x in range(4)]
        
        for x in range(0, 4):
                for y in range(0, 4):
                    newArr[y][x] = board[3 - x][y] 
                    
        return newArr
    
    
    'tells how many matches can be made with that column'
    def countSlideDownMatches(self, column, board):
        matchCount = 0
        x = 0
        y = 0
        
        while (x < 4):
            for y in range(x + 1, 4):
                #print ("checking " + str(x) + " against " + str(y))
                if (board[x][column] == board[y][column] and board[x][column] != 0):
                    matchCount += 1
                    x = y
                    #print("merge, x is " + str(x))
                    break
                elif (board[x][column] != board[y][column] and board[y][column] != 0):
                    break
            x += 1
                
        return matchCount
    
    
    'method to allow easy board control to help with testing'
    def setBoard(self, board):
        self.gameArray = board
        pass
