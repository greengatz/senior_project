'''
Created on Jan 11, 2016

@author: John_2
'''

from RandomSolver import RandomSolver
from GreedySolver import GreedySolver
from GreedySearch import GreedySearch
from SearchSolver import SearchSolver
from Directions import *
from GameState import GameState

toRun = 1;
searchDepth = 2;

def playRandom(numTrials):
    print("running " + str(numTrials) + " random games")
    totalScore = 0
    maxTile = 0
    
    for x in range(0, numTrials):
        #print("game: " + str(x))
        solver = RandomSolver()
        solver.playGame()
        totalScore += solver.getScore()
        if(solver.getMaxTile() > maxTile):
            maxTile = solver.getMaxTile()
        solver = None
    
    print("average score: " + str(totalScore / numTrials))
    print("max tile: " + str(maxTile))
    pass


def playGreedy(numTrials):
    print("running " + str(numTrials) + " greedy games")
    totalScore = 0
    maxTile = 0
    
    for x in range(0, numTrials):
        #print("game: " + str(x))
        solver = GreedySolver()
        solver.playGame()
        totalScore += solver.getScore()
        if(solver.getMaxTile() > maxTile):
            maxTile = solver.getMaxTile()
        solver = None
    
    print("average score: " + str(totalScore / numTrials))
    print("max tile: " + str(maxTile))
    pass


def playGreedySearch(numTrials, depth=searchDepth):
    print("running " + str(numTrials) + " greedy search games with depth " + str(depth))
    totalScore = 0
    maxTile = 0
    
    for x in range(0, numTrials):
        #print("game: " + str(x))
        solver = GreedySearch(depth)
        solver.playGame()
        totalScore += solver.getScore()
        if(solver.getMaxTile() > maxTile):
            maxTile = solver.getMaxTile()
        solver = None
    
    print("average score: " + str(totalScore / numTrials))
    print("max tile: " + str(maxTile))
    pass


def playSearch(numTrials):
    print("running " + str(numTrials) + " searched games")
    totalScore = 0
    maxTile = 0
    
    for x in range(0, numTrials):
        #print("game: " + str(x))
        solver = SearchSolver(searchDepth)
        solver.playGame()
        totalScore += solver.getScore()
        if(solver.getMaxTile() > maxTile):
            maxTile = solver.getMaxTile()
        solver = None
    
    print("average score: " + str(totalScore / numTrials))
    print("max tile: " + str(maxTile))
    pass


def playHuman():
    print("human is playing the game")
    aGame = GameState();
    
    'game loop'
    while aGame.isGoing():
        aGame.printState()
        entered = input("enter a move")
        key = entered[0]
        if key == 'q':
            break
        elif key == 'w':
            aGame.takeMove(Move.up)
        elif key == 'a':
            aGame.takeMove(Move.left)
        elif key == 's':
            aGame.takeMove(Move.down)
        elif key == 'd':
            aGame.takeMove(Move.right)
    
    print("game over")
    aGame.printState()
    pass


if __name__ == '__main__':
    playGreedy(toRun)
    pass
