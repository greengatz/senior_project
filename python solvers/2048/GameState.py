'''
Created on Jan 11, 2016

whitespace to test committing through egit

@author: John_2
'''

from Directions import *
import random
from random import randrange
from unittest.test.testmock.testmock import Something
from _overlapped import NULL

class GameState(object):
    '''
    classdocs
    
    This will be passed to a game controller, which will use information regarding
    game state to determine the move.
    '''

    '4 x 4 array of the game'
    #gameArray = [[0 for x in range(4)] for x in range(4)]


    ''
    def __init__(self):
        '''
        Constructor
        
        TODO add 2 random tiles
        '''
        self.gameArray = [[0 for x in range(4)] for x in range(4)]
        #self.addRandomTile()
        #self.addRandomTile()
        
        self.gameArray[3][0] = 2
        self.gameArray[3][2] = 2
        self.gameArray[3][3] = 2
        
        pass
    
    
    'TODO - check game state'
    def isGoing(self):
        return self.isValid(Move.up) or self.isValid(Move.right) or self.isValid(Move.down) or self.isValid(Move.left)
    
    
    'determines if a move would progress the game'
    def isValid (self, move):
        return not self.isSame(self.executeMove(move))
    
    'determines if the current game state is different the given one'
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

        while (x >= 0):
            if (board[x][column] != 0):
                y = x + 1
                while (y <= limit):
                    # if we find a match
                    if (board[x][column] == board[y][column]):
                        board[y][column] += board[x][column]
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
    def executeMove (self, move, board=NULL):
        if (board == NULL):
            board = self.copyArr()
        
        board = self.preRotate(move, board)
        for x in range(0, 4):
            self.slideDown(x, board)
        board = self.postRotate(move, board)
        
        return board
    
    
    'returns the games state'
    def getState(self):
        return self.gameArray
    
    
    'TODO rename x and y'
    def printState(self, board = NULL):
        if (board == NULL):
            board = self.gameArray
        
        for x in range(0, 4):
            for y in range(0, 4):
                print(str(board[x][y]) + " ", end="")
            print(" ")
        pass
    
    
    'TODO rename x and y'
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
        for x in range(0, 4):
            for y in range(0, 4):
                if self.gameArray[x][y] == 0:
                    threshold = 1 / openSlots
                    if  random.random() <= threshold:
                        self.gameArray[x][y] = tileToAdd
                        return
                    else:
                        openSlots -= 1
        
        print("ERROR: NO TILE ADDED")
        self.printState()
        return
    
    
    'returns the total score on the table'
    def getScore(self):
        score = 0
        for x in range(0, 4):
            for y in range(0, 4):
                score += self.gameArray[x][y]
        return score
    
    
    'returns the highest tile on the board'
    def getMaxTile(self):
        tile = 0
        for x in range(0, 4):
            for y in range(0, 4):
                if(self.gameArray[x][y] > tile):
                    tile = self.gameArray[x][y]
        return tile
    
    
    'takes in a board, returns a copy of it rotated clockwise'
    def rotateClockwise(self, board = NULL):
        if (board == NULL):
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
    
    'allows easy board control'
    def setBoard(self, board):
        self.gameArray = board
        pass