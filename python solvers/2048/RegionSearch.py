'''
predicts value based on assuming what region of the board the next tile will appear in

@author: John_2
'''

from GameState import GameState
from random import randint
from random import randrange
from Directions import *
import time
import datetime

class RegionSearch(object):
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
            print("\nStarting move: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
            testBoard = self.game.copyArr()
            
            bestMove = self.search(testBoard, self.depth)
            print(bestMove[0])
            
            
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
        
        options = 0
        searchValue = 0
        
        
        # arrays
        ev2 = [[0 for x in range(2)] for x in range(2)]
        ev4 = [[0 for x in range(2)] for x in range(2)]
        optionsInRegion = [[0 for x in range(2)] for x in range(2)]
        
        # determine value of the region
        for x in range (0, 2): # location of region
            for y in range (0, 2):
                trialBoard = testGame.copyArr()
                validLocs = []
                for rx in range (0, 2): # location within region
                    for ry in range (0, 2):
                        locX = (x * 2) + rx
                        locY = (y * 2) + ry
                        
                        # take all 0s into account for likelihood
                        if (trialBoard[locX][locY] == 0):
                            optionsInRegion[x][y] += 1
                            options += 1
                            validLocs += [(locX, locY)]
                
                # find a cell in the region to test
                possibilities = optionsInRegion[x][y]
                for loc in validLocs:
                    rand = randrange(0, 100)
                    
                    # randomly select one cell in the region to care about
                    if rand < ((1 / possibilities) * 100): # test whether or not this is the cell we care about
                        trialBoard[loc[0]][loc[1]] = 2
                        ev2[x][y] = self.search(trialBoard, depth - 1)[1]
                        
                        trialBoard[loc[0]][loc[1]] = 4
                        ev4[x][y] = self.search(trialBoard, depth - 1)[1]
                        trialBoard[loc[0]][loc[1]] = 0
                        break
                    possibilities -= 1
                
                # reset our locations for the next region    
                validLocs.clear()
        
        # adjust those region evs for their likelihood
        for x in range (0, 2):
            for y in range (0, 2):
                searchValue += (ev2[x][y] * 0.9) * (optionsInRegion[x][y] / options)
                searchValue += (ev4[x][y] * 0.1) * (optionsInRegion[x][y] / options)
        
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