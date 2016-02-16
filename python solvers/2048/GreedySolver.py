'''
Created on Feb 1, 2016

@author: John_2
'''

from _overlapped import NULL
from GameState import GameState
from random import randint
from Directions import *

class GreedySolver(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.game = GameState()
        self.numMoves = 0
        pass
    
    def playGame(self):
        while (self.game.isGoing()):
            testBoard = self.game.copyArr()
            #self.game.printState(testBoard)
            
            bestOption = NULL
            bestValue = -1
            
            #down test
            option = Move.down
            if (self.game.isValid(option)):
                moveValue = 0
                testBoard = self.game.copyArr()
                testBoard = self.game.preRotate(option, testBoard)
            
                for x in range(0, 4):
                    moveValue += self.game.countSlideDownMatches(x, testBoard)
            
                if (moveValue > bestValue):
                    bestValue = moveValue
                    bestOption = option
                
            # left test
            option = Move.left
            if (self.game.isValid(option)):
                moveValue = 0
                testBoard = self.game.copyArr()
                testBoard = self.game.preRotate(option, testBoard)
            
                for x in range(0, 4):
                    moveValue += self.game.countSlideDownMatches(x, testBoard)
            
                if (moveValue > bestValue):
                    bestValue = moveValue
                    bestOption = option
                
            # up test
            option = Move.up
            if (self.game.isValid(option)):
                moveValue = 0
                testBoard = self.game.copyArr()
                testBoard = self.game.preRotate(option, testBoard)
            
                for x in range(0, 4):
                    moveValue += self.game.countSlideDownMatches(x, testBoard)
            
                if (moveValue > bestValue):
                    bestValue = moveValue
                    bestOption = option
            
            # right test
            option = Move.right
            if (self.game.isValid(option)):
                moveValue = 0
                testBoard = self.game.copyArr()
                testBoard = self.game.preRotate(option, testBoard)
            
                for x in range(0, 4):
                    moveValue += self.game.countSlideDownMatches(x, testBoard)
            
                if (moveValue > bestValue):
                    bestValue = moveValue
                    bestOption = option
            
            self.game.takeMove(bestOption)
        pass
    
    def getScore(self):
        return self.game.getScore()
    
    def getMaxTile(self):
        return self.game.getMaxTile()
    
    def getMoves(self):
        return self.numMoves
    
    def printGame(self):
        self.game.printState()
        pass