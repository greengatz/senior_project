'''
This depth test goes for 65535 moves, which is the max possible board with only getting 4s

128k 64k 32k 16k
8k   4k  2k  1024
512  256 128 64
32   16  8   2

Results: 
-limit is just under 1000 frames
-python handles recursion poorly
-can be raised for threads that are created
    -this isn't as bad as it sounds, just start by making a new thread with huge limit
-memory shouldn't be an issue, if we go up to 64mb then in the worst case each frame can have 1kb
    -this should be more than enough memory

TL;DR: Memory is fine, needs to be run in a new thread, the bottleneck is computation
'''

from GameState import GameState
import sys
import time
import datetime

TEST_DEPTH = 65535

def search(state, level):
    if level % 100 == 0:
        print(str(level))
    if level == TEST_DEPTH:
        pass
    
    newState = GameState()
    newState.setBoard(state.copyArr())
    search(newState, level + 1)
    pass

if __name__ == '__main__':
    print("Starting run at " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "\n")
    print("Running a depth test of " + str(TEST_DEPTH) + " moves")
    
    firstState = GameState()
    
    try:
        search(firstState, 0)
    except RecursionError:
        print("Recursion limit reached")
        

    print("Ending run at " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "\n")
    pass
