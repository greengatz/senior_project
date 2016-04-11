'''
Created on Feb 1, 2016

@author: John_2
'''

from GameState import GameState
from random import randint
from Directions import *
import sys
import time
import datetime

class GreedySolver(object):
    '''
    classdocs
    '''
    fourCorners = {(0, 0), (0, 3), (3, 0), (3, 3)}
    possibilities = {Move.down, Move.left, Move.up, Move.right}
    
    stayInCorner = 0.5
    enterCorner = 1.5
    moveDownMultiplier = 0.8


    def __init__(self):
        '''
        Constructor
        '''
        self.game = GameState()
        self.numMoves = 0
        print("test")
        pass
    
    def playGame(self):
        while (self.game.isGoing()):
            testBoard = self.game.copyArr()
            
            print("\nStarting move: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
            self.game.printState(testBoard)
            
            bestOption = None
            bestValue = -1
            possibilities = {Move.down, Move.left, Move.up, Move.right}
            
            moveValue = 0
            
            for option in possibilities:
                if (self.game.isValid(option)):
                    moveVal = self.testDir(option)
                    if (moveValue > bestValue):
                        bestValue = moveValue
                        bestOption = option
            
            print(bestOption)
            self.game.takeMove(bestOption)
        pass
    
    
    def testDir(self, direction):
        testBoard = self.game.copyArr()
        self.game.preRotate(direction, testBoard)
        testGame = GameState()
        testGame.setBoard(testBoard)
        dirVal = 0
        
        for x in range(0, 4):
            dirVal += self.game.countSlideDownMatches(x, testBoard)
        
        # check if the largest tile is in a corner before the move
        # if it isn't, moving it to the corner is worth a lot
        inCorner = False
        maxTile = testGame.getMaxTile()
        for corner in self.fourCorners:
            if testGame.gameArray[corner[0]][corner[1]] == maxTile:
                inCorner = True
        
        # check where it is after the move
        maxTile = testGame.getMaxTile()
        testGame.executeMove(Move.down)
        for corner in self.fourCorners:
            if testGame.gameArray[corner[0]][corner[1]] == maxTile:
                if not inCorner:
                    dirVal += self.enterCorner
                else:
                    dirVal += self.stayInCorner
        
        # penalty for moving down
        if direction == Move.down:
            dirVal *= self.moveDownMultiplier

        return dirVal
    
    
    def getScore(self):
        return self.game.getScore()
    
    def getMaxTile(self):
        return self.game.getMaxTile()
    
    def getMoves(self):
        return self.numMoves
    
    def printGame(self):
        self.game.printState()
        pass