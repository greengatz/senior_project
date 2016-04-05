'''
Created on April 4, 2016

percentage guidelines: 
1.5% -> 40 possibilites searched
0.5% -> 80 possibilites searched - quick, 1 minute total
0.2% -> 350 possibilites searched - pretty quick, 2 seconds per move

@author: John
'''

from GameState import GameState
from random import randint
from Directions import *
import time
import datetime

class GreedySearchPercentageDepth(object):
    '''
    classdocs
    '''


    def __init__(self, threshold):
        '''
        Constructor
        '''
        self.game = GameState()
        self.numMoves = 0
        self.threshold = threshold
        pass
    
    
    'keeps searching for moves until the game is complete'
    def playGame(self):
        self.game.printState(self.game.gameArray)
        
        count = 0
        
        while (self.game.isGoing()):
            self.possibilities = 0
            moveStart = time.time()
            print("Starting move: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
            testBoard = self.game.copyArr()
            
            bestMove = self.search(testBoard, 1)
            moveEnd = time.time()
            totalTime = moveEnd - moveStart
            print(bestMove[0])
            print("time to search " + str(self.possibilities) + " possibilities moves: " + str(totalTime))
            print("time per possibility: " + str(totalTime / self.possibilities))
            
            
            # when at the end, all decisions might lead to an inevitable failure
            if (not self.game.isValid(bestMove)):
                pass
            
            #self.game.printState(self.game.gameArray)
            self.game.takeMove(bestMove[0])
            self.game.printState(self.game.gameArray)
            self.numMoves = self.numMoves + 1
        
        print(self.numMoves)
        pass
    
    
    'returns best move and the value of that move'
    'best move is only useful for the top-level call'
    def search(self, board, likelihood):
        if (likelihood < self.threshold):
            return (Move.up, 0)
        self.possibilities += 1
        
        bestMove = Move.up
        bestValue = -1
        
        move = Move.up
        moveValue = self.searchDirection(board, likelihood, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.left
        moveValue = self.searchDirection(board, likelihood, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
            
        move = Move.right
        moveValue = self.searchDirection(board, likelihood, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.down
        moveValue = self.searchDirection(board, likelihood, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
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
    
    
    'returns the expected value of a given move searching with the given likelihood'
    def searchDirection(self, board, likelihood, move):
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
        
        # determine which cells can have a new tile
        trialBoard = testGame.copyArr()
        for x in range (0, 4):
            for y in range (0, 4):
                if (trialBoard[x][y] == 0):
                    options += 1
        
        # determine the value of each cell
        for x in range (0, 4):
            for y in range (0, 4):
                trialBoard = testGame.copyArr()
                if (trialBoard[x][y] == 0):
                    cellChance = likelihood / options
                    
                    trialBoard[x][y] = 2
                    ev2[x][y] = cellChance * 0.9 * self.search(trialBoard, likelihood * cellChance * 0.9)[1]
                    trialBoard[x][y] = 0
                    
                    trialBoard[x][y] = 4
                    ev4[x][y] = cellChance * 0.9 * self.search(trialBoard, likelihood * cellChance * 0.1)[1]
                    trialBoard[x][y] = 0
        
        #print("ev of move " + str(move))
        #self.game.printState(ev2)
        
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