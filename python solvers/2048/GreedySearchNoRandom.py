'''
Created on Feb 6, 2016

@author: John_2
'''

from GameState import GameState
from random import randint
from ValueCalculator import value
from Directions import *

class GreedySearchNoRandom(object):
    '''
    classdocs
    '''


    def __init__(self, inDepth):
        '''
        Constructor
        '''
        self.game = GameState()
        self.numMoves = 0
        self.depth = inDepth
        pass
    
    
    'keeps searching for moves until the game is complete'
    def playGame(self):
        self.game.printState(self.game.gameArray)
        
        count = 0
        
        while (self.game.isGoing()):
            testBoard = self.game.copyArr()
            
            bestMove = self.search(testBoard, self.depth)
            print(bestMove[0])
            
            # when at the end, all decisions might lead to an inevitable failure
            if (not self.game.isValid(bestMove)):
                pass
            
            #self.game.printState(self.game.gameArray)
            self.game.takeMove(bestMove[0])
            self.game.printState(self.game.gameArray)
        pass
    
    
    'returns best move and the value of that move'
    'best move is only useful for the top-level call'
    def search(self, board, depth):    
        if (depth == 0):
            return (Move.up, 0)
        
        bestMove = Move.up
        bestValue = -1
        
        move = Move.up
        moveValue = self.searchDirection(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.left
        moveValue = self.searchDirection(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
            
        move = Move.right
        moveValue = self.searchDirection(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.down
        moveValue = self.searchDirection(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        return (bestMove, bestValue)
    
    
    'returns the number of matches that a given move would make'
    'this only determines value of one move and no further searching'
    def valueOfMove(self, board, move):
        return value(self.game.preRotate(move, board), self.game, move)
    
    
    'returns the expected value of a given move searching with the given depth'
    'this ignores the new tiles appearing, which saves tons on complexity'
    def searchDirection(self, board, depth, move):
        testGame = GameState()
        testGame.setBoard(board)
        testGame.setBoard(testGame.copyArr())
        
        # if the move isn't valid, don't consider it
        if (not testGame.isValid(move)):
            return -1
        
        # determine the value for making the move at this level
        ourValue = self.valueOfMove(testGame.gameArray, move)
        
        # using that as the starting board, check the child's options
        afterMove = testGame.executeMove(move)
        #testGame.setBoard(afterMove)
        
        #trialBoard = testGame.copyArr()
        searchValue = self.search(afterMove, depth - 1)[1]
        
        return ourValue + searchValue
    
    
    'generic methods of every solver'
    def getScore(self):
        return self.game.getScore()
    
    def getMaxTile(self):
        return self.game.getMaxTile()
    
    def getMoves(self):
        return self.numMoves
    
    def printGame(self):
        self.game.printState()
        pass