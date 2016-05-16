'''

@author: John_2
'''

from GameState import *
from Directions import * 
import sys
import time
import datetime
import cma


baseValue = 0
mergeValue = 2 # how much a single merge is worth
openSquareBonus = 0.1 # how much an open square is worth
nonMonotonicMult = 0.5 # multiplier applied to non-monotonic boards
nonMonotonicPenalty = 1.5 # value reduced for a board being non-monotonic
largeOnEdgeBonus = 0 # value bonus applied to boards with the largest tiles on the edges

if __name__ == '__main__':
    print("test")