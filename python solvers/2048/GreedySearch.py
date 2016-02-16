'''
Created on Feb 6, 2016

@author: John_2
'''

from GameState import GameState
from random import randint
from Directions import *

class GreedySearch(object):
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
    
    def playGame(self):
        self.game.printState(self.game.gameArray)
        
        count = 0
        
        while (self.game.isGoing()):
            testBoard = self.game.copyArr()
            
            bestMove = self.search(testBoard, self.depth)
            print(bestMove[0])
            
            #self.game.printState(self.game.gameArray)
            self.game.takeMove(bestMove[0])
            self.game.printState(self.game.gameArray)
        pass
    
    
    'returns best move and the value of that move'
    'best move is only useful for the top-level call'
    def search(self, board, depth):
        #print("search level " + str(depth))
        
        if (depth == 0):
            return (Move.up, 0)
        
        bestMove = Move.up
        bestValue = -1
        
        move = Move.up
        moveValue = self.searchDirection(board, depth, move)
        #if (depth == self.depth):
        #    print("value of " + str(move) + " is " + str(moveValue) + " at level " + str(depth))
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.left
        moveValue = self.searchDirection(board, depth, move)
        #if (depth == self.depth):
        #    print("value of " + str(move) + " is " + str(moveValue) + " at level " + str(depth))
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
            
        move = Move.right
        moveValue = self.searchDirection(board, depth, move)
        #if (depth == self.depth):
        #    print("value of " + str(move) + " is " + str(moveValue) + " at level " + str(depth))
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.down
        moveValue = self.searchDirection(board, depth, move)
        #if (depth == self.depth):
        #    print("value of " + str(move) + " is " + str(moveValue) + " at level " + str(depth))
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        #if (depth == self.depth):
        #    print("moving " + str(bestMove) + " at level " + str(depth) + " for value " + str(bestValue))
        return (bestMove, bestValue)
    
    
    'returns the number of matches that a given move would make'
    'this only determines value of one move and no further searching'
    def valueOfMove(self, board, move):
        board = self.game.preRotate(move, board)
        
        value = 0
        for x in range(0, 4):
            value += self.game.countSlideDownMatches(x, board)
        
        board = self.game.postRotate(move, board)
        return value
    
    
    'returns the expected value of a given move searching with the given depth'
    def searchDirection(self, board, depth, move):
        testGame = GameState()
        testGame.setBoard(board)
        testGame.setBoard(testGame.copyArr())
        
        # if the move isn't valid, don't consider it
        if (not testGame.isValid(move)):
            return -1
        
        #determine the value for making the move at this level
        ourValue = self.valueOfMove(testGame.gameArray, move)
        
        #'using that as the starting board, check a lot of possibilities'
        afterMove = testGame.executeMove(move)
        testGame.setBoard(afterMove)
        ev2 = [[0 for x in range(4)] for x in range(4)]
        ev4 = [[0 for x in range(4)] for x in range(4)]
        
        options = 0
        searchValue = 0
        
        # determine the value of each cell
        for x in range (0, 4):
            for y in range (0, 4):
                trialBoard = testGame.copyArr()
                if (trialBoard[x][y] == 0):
                    options += 1
                    
                    trialBoard[x][y] = 2
                    ev2[x][y] = self.search(trialBoard, depth - 1)[1]
                    trialBoard[x][y] = 0
                    
                    trialBoard[x][y] = 4
                    ev4[x][y] = self.search(trialBoard, depth - 1)[1]
                    trialBoard[x][y] = 0
        
        
        # adjust those cells for their likelihood
        for x in range (0, 4):
            for y in range (0, 4):
                searchValue += (ev2[x][y] * 0.9) / options
                searchValue += (ev4[x][y] * 0.1) / options
        
        #print("ev of move " + str(move))
        #self.game.printState(ev2)
        
        return ourValue + searchValue
    
    
    
    def getScore(self):
        return self.game.getScore()
    
    def getMaxTile(self):
        return self.game.getMaxTile()
    
    def getMoves(self):
        return self.numMoves
    
    def printGame(self):
        self.game.printState()
        pass