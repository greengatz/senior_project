'''
Created on Jan 25, 2016

@author: John_2
'''

from Directions import *


def testArray(state, type):
    for x in range(0, 3):
        if (state[x][0] == state[x][1] and state[x][1] == state[x][2] and state[x][0] == type):
            return True
        elif (state[0][x] == state[1][x] and state[1][x] == state[2][x] and state[0][x] == type):
            return True
    if (state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[0][0] == type):
        return True
    elif (state[2][0] == state[1][1] and state[1][1] == state[0][2] and state[2][0] == type):
        return True
    return False

class TTTGame(object):
    '''
    classdocs
    '''


    '''
    X O X
    O X 
    O X 
    '''
    def __init__(self, initArray = [[Play.empty for x in range(3)] for x in range(3)], initPlay = Play.x):
        '''
        Constructor
        '''
        self.gameArray = initArray
        self.turn = initPlay
        pass
    
    
    
    def printState(self):
        print(str(self.turn) + "'s turn")
        for x in range(0, 3):
            for y in range(0, 3):
                print(str(self.gameArray[x][y]) + " ", end="")
            print(" ")
        pass
    
    
    def getGrid(self):
        return self.gameArray
    
    
    def getTurn(self):
        return self.turn
    
    
    def takeMove(self, x, y):
        if(self.isValid(x, y)):
            self.gameArray[x][y] = self.turn
            self.swapMove()
        else:
            print("invalid move chosen")
    
    def isValid(self, x, y):
        if(self.gameArray[x][y] == Play.empty):
            return True
        return False
    
    def swapMove(self):
        if(self.turn == Play.x):
            self.turn = Play.o
        else:
            self.turn = Play.x
    
    
    def isGoing(self):
        if (testArray(self.gameArray, Play.x) or testArray(self.gameArray, Play.o)):
            return False
        
        for x in range(0, 3):
            for y in range(0, 3):
                if (self.gameArray[x][y] == Play.empty):
                    return True
        return False
    
    
    def whoWon(self):
        if (testArray(self.gameArray, Play.x)):
            return Play.x
        elif (testArray(self.gameArray, Play.o)):
            return Play.o
        else:
            return Play.empty