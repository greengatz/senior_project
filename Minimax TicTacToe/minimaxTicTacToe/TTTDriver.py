'''
Created on Jan 25, 2016

@author: John_2
'''
from Solver import *
from Directions import *

if __name__ == '__main__':
    print("running TTT minimax")
    
    solver = Solver()
    
    print(str(solver.search(solver.game.getGrid(), solver.game.getTurn())))
    solver.game.swapMove() #always follows
    solver.game.printState()
    
    print(str(solver.search(solver.game.getGrid(), solver.game.getTurn())))
    solver.game.swapMove() #always follows
    solver.game.printState()
    
    print(str(solver.search(solver.game.getGrid(), solver.game.getTurn())))
    solver.game.swapMove() #always follows
    solver.game.printState()
    
    pass