from GameState import GameState
from random import randint
from Directions import *

class SearchSolver(object):
    '''
    classdocs
    '''


    def __init__(self, inDepth):
        '''
        Constructor
        '''
        self.depth = inDepth
        self.game = GameState()
        self.numMoves = 0
        pass
    
    
    def playGame(self):
        while (self.game.isGoing()):
            self.startSearch(self.game.copyArr(), self.depth)
            break
        pass
    
    
    # determines the move with the highest ev with the given search depth
    def startSearch(self, board, depth):
        bestOption = None
        bestVal = -1
        
        # base case, depth == 0
        # in this case, estimate rest of the way greedy?
        if (depth == 0):
            return (Move.up, 0)
        
        upVal = self.estimateValue(depth - 1, board, Move.up)
        print(upVal)
        if (upVal > bestVal):
            bestOption = Move.up
        
        rightVal = self.estimateValue(depth - 1, board, Move.right)
        if (rightVal > bestVal):
            bestOption = Move.right
        
        return (bestOption, bestVal)
    
    
    def estimateValue(self, depth, board, move):
        ev2 = [[0 for x in range(4)] for x in range(4)]
        ev4 = [[0 for x in range(4)] for x in range(4)]
        ev = 0
        numOptions = 0
        
        # go through all options
        if(self.game.isValid(move)): 
            baseGameUp = GameState()
            baseGameUp.setBoard(board)
            baseGameUp.executeMove(move)
            
            for x in range (0, 4):
                for y in range (0, 4):
                    if(baseGameUp.gameArray[x][y] == 0):
                        numOptions += 2
                        
                        # per cell ev expecting 4
                        pretendBoard2 = baseGameUp.copyArr()
                        pretendGame2 = GameState()
                        pretendBoard2[x][y] = 2
                        pretendGame2.setBoard(pretendBoard2)
                        searchEv = self.startSearch(pretendGame2.copyArr(), depth - 1)
                        ev2[x][y] = searchEv[1]
                        pretendGame4 = None
                    
                        # per cell ev expecting 4
                        pretendBoard4 = baseGameUp.copyArr()
                        pretendGame4 = GameState()
                        pretendBoard4[x][y] = 4
                        pretendGame4.setBoard(pretendBoard4)
                        searchEv = self.startSearch(pretendGame4.copyArr(), depth - 1)
                        ev4[x][y] = searchEv[1]
                        pretendGame4 = None
                    
                        pass
        return ev
    
    
    def getScore(self):
        return self.game.getScore()
    
    def getMaxTile(self):
        return self.game.getMaxTile()
    
    def getMoves(self):
        return self.numMoves
    
    def printGame(self):
        self.game.printState()
        pass