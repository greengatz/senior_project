'''
Created on Feb 1, 2016

@author: John_2
'''

from GameState import GameState
from random import randint
from Directions import *
import sys
import time
import datetime

# (tileX, tileY, direction to move if empty)
tileOrder = [(0, 0, Move.left), (0, 1, Move.left), (0, 2, Move.left), (0, 3, Move.left)]
tileOrder += [(1, 3, Move.up), (1, 2, Move.right), (1, 1, Move.right), (1, 0, Move.right)]
tileOrder += [(2, 0, Move.up), (2, 1, Move.left), (2, 2, Move.left), (2, 3, Move.left)]
tileOrder += [(3, 3, Move.up), (3, 2, Move.right), (3, 1, Move.right), (3, 0, Move.right)]


    
def playPerfectGame():
    numMoves = 0
    game = GameState()
    startBoard = [[0 for x in range(4)] for x in range(4)]
    startBoard[tileOrder[0][0]][tileOrder[0][1]] = 2
    startBoard[tileOrder[1][0]][tileOrder[1][1]] = 2
    game.setBoard(startBoard)

    #while (game.isGoing()):
    #while game.isGoing():
    while numMoves < 50:
        print("\nStarting move: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        game.printState()
            
        takeMove(game)
        numMoves += 1
    pass
    
def takeMove(game):
    print("taking a move")
    
    destX = 0
    destY = 0
    
    # move plan:
    # look for a pair
    # if no pair, go by first tile found after white space
    # afterwards add the new tile
    
    
    #first try to find a pair to clean up the board
    pairFound = False
    for previousTile in range(14):
        currentTile = previousTile + 1
        
        prevVal = game.gameArray[tileOrder[previousTile][0]][tileOrder[previousTile][1]]
        curVal = game.gameArray[tileOrder[currentTile][0]][tileOrder[currentTile][1]]
        
        if curVal == prevVal:
            #print(str(tileOrder[previousTile][0]) + ", " + str(tileOrder[previousTile][1]))
            pairFound = True
            move = tileOrder[currentTile][2]
            print("found a pair!")
            break
    
    # what we dc if we don't find a pair
    if not pairFound:
        whiteSpace = False
        for currentTile in range(15):
            if whiteSpace and game.gameArray[tileOrder[currentTile][0]][tileOrder[currentTile][1]] != 0:
                move = tileOrder[currentTile][2]
                break
            
            if game.gameArray[tileOrder[currentTile][0]][tileOrder[currentTile][1]] == 0:                
                whiteSpace = True

    
    game.setBoard(game.executeMove(move))
    
    for currentTile in reversed(range(14)):
        previousTile = currentTile + 1
            
        if game.gameArray[tileOrder[currentTile][0]][tileOrder[currentTile][1]] != 0:
            #print(str(tileOrder[previousTile][0]) + ", " + str(tileOrder[previousTile][1]))
            destX = tileOrder[previousTile][0]
            destY = tileOrder[previousTile][1]
            break
        
    game.gameArray[destX][destY] = 4
    
    pass

    
if __name__ == '__main__':
    print("starting a perfect game")
    playPerfectGame()
    print("done")