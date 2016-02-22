'''
Created on Jan 11, 2016

@author: John_2
'''

from RandomSolver import RandomSolver
from GreedySolver import GreedySolver
from GreedySearch import GreedySearch
from GreedySearchNoRandom import GreedySearchNoRandom
from SearchSolver import SearchSolver
from Directions import *
from GameState import GameState
import sys
import time
import datetime

toRun = 1;
searchDepth = 2;

def playRandom(numTrials):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " random games\n")
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
        
        output.write("average score: " + str(totalScore / numTrials) + "\n")
        output.write("max tile: " + str(maxTile) + "\n")
    pass


def playGreedy(numTrials):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " greedy games\n")
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
        
        output.write("average score: " + str(totalScore / numTrials) + "\n")
        output.write("max tile: " + str(maxTile) + "\n")
    pass


def playGreedySearch(numTrials, depth=searchDepth):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " greedy search games with depth " + str(depth) + "\n")
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
        
        output.write("average score: " + str(totalScore / numTrials) + "\n")
        output.write("max tile: " + str(maxTile) + "\n")
    pass


'Greedy matching strategy, except it ignores all random possibilities'
def playGreedySearchNoRandom(numTrials, depth=searchDepth):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " greedy search without factoring randomization games with depth " + str(depth) + "\n")
        totalScore = 0
        maxTile = 0
        
        for x in range(0, numTrials):
            #print("game: " + str(x))
            solver = GreedySearchNoRandom(depth)
            solver.playGame()
            totalScore += solver.getScore()
            if(solver.getMaxTile() > maxTile):
                maxTile = solver.getMaxTile()
            solver = None
        
        output.write("average score: " + str(totalScore / numTrials) + "\n")
        output.write("max tile: " + str(maxTile) + "\n")
    pass


def playSearch(numTrials):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " searched games" + "\n")
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
        
        output.write("average score: " + str(totalScore / numTrials) + "\n")
        output.write("max tile: " + str(maxTile) + "\n")
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
    with open("output", "a") as output:
        output.write("\nStarting run at " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "\n")
    
    # validate number of args
    numArgs = len(sys.argv)
    if numArgs < 3:
        choice = "badChoice"
        runs = 0
    else:
        choice = sys.argv[1]
        runs = int(sys.argv[2])

    # use the correct solver based on input
    if choice == "random":
        playRandom(runs)
        
    elif choice == "greedy":
        playGreedy(runs)
        
    elif choice == "greedySearch":
        if numArgs < 4:
            print("bad usage, greedy search requires a 4th arg of search depth")
            print("ex.    thisProg.py greedySearch 10 3")
        else:
            inDepth = int(sys.argv[3])
            playGreedySearch(runs, inDepth)
    
    elif choice == "greedySearchNoRandom":
        if numArgs < 4:
            print("bad usage, greedy search requires a 4th arg of search depth")
            print("ex.    thisProg.py greedySearchNoRandom 10 3")
        else:
            inDepth = int(sys.argv[3])
            playGreedySearchNoRandom(runs, inDepth)
            
    elif choice == "human":
        playHuman()
        
    else:
        print("bad usage, invalid solver type")
        print("valid options: random, greedy, greedySearch, greedySearchNoRandom, human")
        print("ex.    thisProg.py <solver type> <num trials> <additional args if required>")
    
    with open("output", "a") as output:
        output.write("Ending run at " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "\n")
    pass
