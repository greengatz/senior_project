'''

@author: John_2
'''

from GameState import *
from Directions import * 
import sys
import time
import datetime

global baseValue
baseValue = 0
global mergeValue
mergeValue = 2 # how much a single merge is worth
global openSquareBonus
openSquareBonus = 0.1 # how much an open square is worth
global nonMonotonicMult
nonMonotonicMult = 0.5 # multiplier applied to non-monotonic boards
global nonMonotonicPenalty
nonMonotonicPenalty = 1.5 # value reduced for a board being non-monotonic
global largeOnEdgeBonus
largeOnEdgeBonus = 0 # value bonus applied to boards with the largest tiles on the edges

global test
test = 1

def setWeights(newWeights):
    baseValue = newWeights[0]
    print(str(newWeights[0]))
    print(str(baseValue))
    mergeValue = newWeights[1]
    openSquareBonus = newWeights[2]
    nonMonotonicMult = newWeights[3]
    nonMonotonicPenalty = newWeights[4]
    largeOnEdgeBonus = newWeights[5]
    pass

def getWeights():
    return [baseValue, mergeValue, openSquareBonus, nonMonotonicMult, nonMonotonicPenalty, largeOnEdgeBonus]

def isMonotonic(a, b, c, d):
    result = False
    
    if a >= b and b >= c and c >= d:
        result = True
    
    if a <= b and b <= c and c <= d:
        result = True
    
    return result


def isLargeOnEdge(a, b, c, d):
    if (a > b and a > c) or (d > b and d > c):
        return True
    return False


def value(board, game, move):
    value = baseValue
    multiplier = 1
    
    # heuristic for making merges
    for x in range(0, 4):
        value += countSlideDownMatches(x, board)
    
    value = value * mergeValue
    
    # make the hypothetical move here
    board = game.executeMove(Move.down)
    
    # heuristic for large tiles on edges
    largeOnEdge = True
    for x in range(0, 4):
        largeOnEdge = largeOnEdge and isLargeOnEdge(board[x][0], board[x][1], board[x][2], board[x][3])
        largeOnEdge = largeOnEdge and isLargeOnEdge(board[0][x], board[1][x], board[2][x], board[3][x])
     
    if largeOnEdge:
        value = value + largeOnEdgeBonus
    
    # heuristic for open tile bonus
    for x in range(0, 4):
        for y in range(0, 4):
            if board[x][y] == 0:
                value += openSquareBonus
    
    # heuristic for monotonic rows/columns
    monotonicRows = True
    monotonicColumns = True
    for x in range(0, 4):
        monotonicRows = monotonicRows and isMonotonic(board[x][0], board[x][1], board[x][2], board[x][3])
        monotonicColumns = monotonicRows and isMonotonic(board[0][x], board[1][x], board[2][x], board[3][x])
    
    if not (monotonicColumns and monotonicRows):
        multiplier = multiplier * nonMonotonicMult
        #value = value - nonMonotonicPenalty
    
    return value * multiplier
