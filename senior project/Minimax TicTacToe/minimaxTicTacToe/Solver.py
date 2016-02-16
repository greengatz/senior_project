'''
Created on Jan 25, 2016

@author: John_2
'''
from TTTGame import TTTGame
from Directions import *
from pip.index import Search
from _overlapped import NULL

class Solver(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print("starting new search")
        
        
        turn = Play.x
        initArray = [[Play.empty for x in range(3)] for x in range(3)]
        initArray[0][0] = Play.x
        initArray[0][1] = Play.o
        initArray[0][2] = Play.x
        
        initArray[1][0] = Play.o
        #initArray[1][1] = Play.x
        initArray[1][2] = Play.o
        
        #initArray[2][0] = Play.o
        #initArray[2][1] = Play.x
        #initArray[2][2] = Play.x
        
        
        self.game = TTTGame(initArray, turn)
        self.game.printState()
        pass
    
    def search(self, grid, turn):
        root = TTTGame(grid, turn)
        
        if (not root.isGoing()):
            return root.whoWon()
        
        xMove = NULL
        yMove = NULL
        exp = -1
        
        for x in range(0, 3):
            for y in range(0, 3):
                copy = TTTGame(self.copyGrid(grid), turn)
                #print(str(x) + ", " + str(y) + "    -   " + str(copy.isValid(x, y)))
                if(copy.isValid(x, y)):
                    copy.takeMove(x, y)
                    
                    #determine which was best
                    res = self.search(copy.getGrid(), copy.getTurn())

                    #if it is o's turn, we want lowest
                    #if it is x's turn, we want highest
                    adj = self.adjustValue(res, turn)

                    #our first search option is always the best choice at the time
                    if (adj >= exp):
                        xMove = x
                        yMove = y
                        exp = adj

        root.takeMove(xMove, yMove)
        return exp
        #root.printState()
    
    def adjustValue(self, val, turn):
        if(turn == Play.o and val == Play.o):
            return 1
        elif(turn == Play.o and val == Play.x):
            return -1
        elif(turn == Play.x and val == Play.x):
            return 1
        elif(turn == Play.x and val == Play.o):
            return -1
        elif(val == Play.empty):
            return 0
        return val * -1
    
    def copyGrid(self, grid):
        newGrid = [[Play.empty for x in range(3)] for x in range(3)]
        for x in range(0, 3):
            for y in range(0, 3):
                newGrid[x][y] = grid[x][y]
        return newGrid