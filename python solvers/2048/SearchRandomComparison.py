'''
Created on Feb 6, 2016

@author: John_2
'''

from GameState import GameState
from random import randint
from Directions import *
import time
import datetime

class SearchRandomComparison(object):
    '''
    classdocs
    '''


    def __init__(self, inDepth, zeroes):
        '''
        Constructor
        '''
        self.game = GameState()
        self.numMoves = 0
        self.depth = inDepth
        self.zeroes = zeroes
        self.disagreements = 0
        self.comparisons = 0
        pass
    
    
    'keeps searching for moves until the game is complete'
    def playGame(self):
        self.game.printState(self.game.gameArray)
        
        count = 0
        disagreements = 0
        comparisons = 0
        
        while (self.game.isGoing()):
            print("\nStarting move: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
            
            bestMove = self.searchRandom(self.game.copyArr(), self.depth)
            print(bestMove[0])
            
            if self.enoughZeroes():
                self.comparisons += 1
                noRandomMove = self.searchNoRandom(self.game.copyArr(), self.depth)
                if not noRandomMove == bestMove:
                    self.disagreements += 1
            
            
            # when at the end, all decisions might lead to an inevitable failure
            if (not self.game.isValid(bestMove)):
                pass
            
            #self.game.printState(self.game.gameArray)
            self.game.takeMove(bestMove[0])
            self.game.printState(self.game.gameArray)
            self.numMoves = self.numMoves + 1
        
        print(self.numMoves)
        pass
    
    
    'determines whether or not a comparison should occur based on how full the board is'
    'number of required 0s is determined at solver creation'
    def enoughZeroes(self):
        numZeroes = 0
        
        # count number of 0-tiles
        for x in range (0, 4):
            for y in range (0, 4):
                if self.game.gameArray[x][y] == 0:
                    numZeroes += 1
        
        if numZeroes >= self.zeroes:
            return True
        return False
    
    
    'returns best move and the value of that move factoring in random tiles'
    'best move is only useful for the top-level call'
    def searchRandom(self, board, depth):
        if (depth == 0):
            return (Move.up, 0)
        
        bestMove = Move.up
        bestValue = -1
        
        move = Move.up
        moveValue = self.searchDirectionRandom(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.left
        moveValue = self.searchDirectionRandom(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
            
        move = Move.right
        moveValue = self.searchDirectionRandom(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.down
        moveValue = self.searchDirectionRandom(board, depth, move)
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
    
    
    'returns the expected value of a given move searching with the given depth factoring in random tiles'
    def searchDirectionRandom(self, board, depth, move):
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
                    ev2[x][y] = self.searchRandom(trialBoard, depth - 1)[1]
                    trialBoard[x][y] = 0
                    
                    trialBoard[x][y] = 4
                    ev4[x][y] = self.searchRandom(trialBoard, depth - 1)[1]
                    trialBoard[x][y] = 0
        
        
        # adjust those cells for their likelihood
        for x in range (0, 4):
            for y in range (0, 4):
                searchValue += (ev2[x][y] * 0.9) / options
                searchValue += (ev4[x][y] * 0.1) / options
        
        #print("ev of move " + str(move))
        #self.game.printState(ev2)
        
        return ourValue + searchValue
    
    
    'returns best move and the value of that move'
    'best move is only useful for the top-level call'
    def searchNoRandom(self, board, depth):    
        if (depth == 0):
            return (Move.up, 0)
        
        bestMove = Move.up
        bestValue = -1
        
        move = Move.up
        moveValue = self.searchDirectionNoRandom(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.left
        moveValue = self.searchDirectionNoRandom(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
            
        move = Move.right
        moveValue = self.searchDirectionNoRandom(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        move = Move.down
        moveValue = self.searchDirectionNoRandom(board, depth, move)
        if (moveValue > bestValue):
            bestMove = move
            bestValue = moveValue
        
        return (bestMove, bestValue)


    'returns the expected value of a given move searching with the given depth'
    'this ignores the new tiles appearing, which saves tons on complexity'
    def searchDirectionNoRandom(self, board, depth, move):
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
        searchValue = self.searchNoRandom(afterMove, depth - 1)[1]
        
        return ourValue + searchValue


    'class specific stats'
    def getComparisons(self):
        return self.comparisons
    
    def getDisagreements(self):
        return self.disagreements

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