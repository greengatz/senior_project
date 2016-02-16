'''
Created on Jan 18, 2016

@author: John_2
'''
from _overlapped import NULL
from GameState import GameState
from random import randint
from Directions import *

class RandomSolver(object):
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
            'pick a move'
            move = randint(1, 4)
            'execute move'
            if (self.game.isValid(Move(move))):
                self.game.takeMove(Move(move))
                self.numMoves += 1
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