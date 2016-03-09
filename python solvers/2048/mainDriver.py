'''
Created on Jan 11, 2016

@author: John_2
'''

from RandomSolver import RandomSolver
from GreedySolver import GreedySolver
from GreedySearch import GreedySearch
from RegionSearch import RegionSearch
from GreedySearchNoRandom import GreedySearchNoRandom
from SearchSolver import SearchSolver
from SearchRandomComparison import SearchRandomComparison
from Directions import *
from GameState import GameState
from Histogram import DataGroup
import sys
import time
import datetime


def recordData(solver, tile, score):
    score.put(solver.getScore())
    tile.put(solver.getMaxTile())
    pass


def printRunData(tile, score, output):
    output.write("SCORE")
    output.write("---max : " + str(score.getMax()))
    output.write("   ---mean : " + str(score.getMean()))
    output.write("   ---std : " + str(score.getStd()) + "\n")
    output.write("TILE")
    output.write("---max : " + str(tile.getMax()))
    output.write("   ---mean : " + str(tile.getMean()))
    output.write("   ---std : " + str(tile.getStd()) + "\n")
    pass


def playRandom(numTrials):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " random games\n")
        tile = DataGroup()
        score = DataGroup()
        
        for x in range(0, numTrials):
            solver = RandomSolver()
            solver.playGame()
            recordData(solver, tile, score)
            solver = None
        
        printRunData(tile, score, output)
    pass


def playGreedy(numTrials):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " greedy games\n")
        tile = DataGroup()
        score = DataGroup()
        
        for x in range(0, numTrials):
            solver = GreedySolver()
            solver.playGame()
            recordData(solver, tile, score)
            solver = None
        
        printRunData(tile, score, output)
    pass


def playGreedySearch(numTrials, depth):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " greedy search games with depth " + str(depth) + "\n")
        tile = DataGroup()
        score = DataGroup()
        
        for x in range(0, numTrials):
            solver = GreedySearch(depth)
            solver.playGame()
            recordData(solver, tile, score)
            solver = None
        
        printRunData(tile, score, output)
    pass


def playRegionSearch(numTrials, depth):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " region-based search games with depth " + str(depth) + "\n")
        tile = DataGroup()
        score = DataGroup()
        
        for x in range(0, numTrials):
            solver = RegionSearch(depth)
            solver.playGame()
            recordData(solver, tile, score)
            solver = None
        
        printRunData(tile, score, output)
    pass


'Greedy matching strategy, except it ignores all random possibilities'
def playGreedySearchNoRandom(numTrials, depth):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " greedy search without factoring randomization games with depth " + str(depth) + "\n")
        tile = DataGroup()
        score = DataGroup()
        
        for x in range(0, numTrials):
            solver = GreedySearchNoRandom(depth)
            solver.playGame()
            recordData(solver, tile, score)
            solver = None
        
        printRunData(tile, score, output)
    pass


'Greedy matching strategy, except it ignores all random possibilities'
def playSearchRandomComparison(numTrials, depth, zeroLevel):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " search comparisons with depth " + str(depth) + "\n")
        output.write("the required number of 0s for a comparison is " + str(zeroLevel) + "\n")
        tile = DataGroup()
        score = DataGroup()
        disagreements = 0
        comparisons = 0
        
        for x in range(0, numTrials):
            solver = SearchRandomComparison(depth, zeroLevel)
            solver.playGame()
            recordData(solver, tile, score)
            disagreements += solver.getDisagreements()
            comparisons += solver.getComparisons()
            solver = None
        
        printRunData(tile, score, output)
        output.write("comparisons: " + str(comparisons) + "\ndisagreements: " + str(disagreements) + "\n")
    pass


def playSearch(numTrials):
    with open("output", "a") as output:
        output.write("running " + str(numTrials) + " searched games" + "\n")
        tile = DataGroup()
        score = DataGroup()
        
        for x in range(0, numTrials):
            #print("game: " + str(x))
            solver = SearchSolver(searchDepth)
            solver.playGame()
            recordData(solver, tile, score)
            solver = None
        
        printRunData(tile, score, output)
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
        print(sys.argv[2])
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
    
    elif choice == "regionSearch":
        if numArgs < 4:
            print("bad usage, region search requires a 4th arg of search depth")
            print("ex.    thisProg.py regionSearch 10 3")
        else:
            inDepth = int(sys.argv[3])
            playRegionSearch(runs, inDepth)
    
    elif choice == "searchRandomComparison":
        if numArgs < 5:
            print("bad usage, greedy search requires a 4th arg of search depth and a 5th argument of required 0s on board")
            print("ex.    thisProg.py searchRandomComparison 10 3 8")
        else:
            inDepth = int(sys.argv[3])
            zeroLevel = int(sys.argv[4])
            playSearchRandomComparison(runs, inDepth, zeroLevel)
            
    elif choice == "human":
        playHuman()
        
    else:
        print("bad usage, invalid solver type")
        print("valid options: random, greedy, greedySearch, greedySearchNoRandom, human, searchRandomComparison")
        print("ex.    thisProg.py <solver type> <num trials> <additional args if required>")
    
    with open("output", "a") as output:
        output.write("Ending run at " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "\n")
    pass
