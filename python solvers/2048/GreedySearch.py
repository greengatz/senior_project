from GameState import GameState
from random import randint
from Directions import *
from ValueCalculator import value
import time
import datetime

class GreedySearch(object):
    fourCorners = {(0, 0), (0, 3), (3, 0), (3, 3)}
    possibilities = {Move.down, Move.left, Move.up, Move.right}
    
    enterCorner = 0
    maxInCornerMultiplier = 1.0
    cornerBonusScaledByMax = 0.8
    moveDownPenalty = 0.0

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
        count = 0
        
        while (self.game.isGoing()):
            print("\nStarting move: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
            testBoard = self.game.copyArr()
            
            bestMove = self.search(testBoard, self.depth)
            print(bestMove[0])
            
            self.game.printState(self.game.gameArray)
            wasSuccessful = self.game.takeMove(bestMove[0])
            self.numMoves = self.numMoves + 1
            if not wasSuccessful:
                break
        
        self.game.printState(self.game.gameArray)
        print("number of moves in game: " + str(self.numMoves))
        
        pass
    
    
    'returns best move and the value of that move'
    'best move is only useful for the top-level call'
    def search(self, board, depth):
        bestMove = Move.up
        bestValue = -1
        
        for move in self.possibilities:
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
    def searchDirection(self, board, depth, move):
        testGame = GameState()
        testGame.setBoard(board)
        testGame.setBoard(testGame.copyArr())
        
        # if the move isn't valid, don't consider it
        if (not testGame.isValid(move)):
            return -1
        
        # determine the value for making the move at this level
        ourValue = self.valueOfMove(testGame.gameArray, move)
        
        # if we have reached bottom depth, stop searching and return the heuristic value
        if depth == 1:
            return ourValue
        
        # using that as the starting board, check a lot of possibilities
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
                    
                    trialBoard[x][y] = 4
                    ev4[x][y] = self.search(trialBoard, depth - 1)[1]
                    trialBoard[x][y] = 0
        
        
        # adjust those cells for their likelihood
        for x in range (0, 4):
            for y in range (0, 4):
                searchValue += (ev2[x][y] * 0.9) / options
                searchValue += (ev4[x][y] * 0.1) / options
        
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
