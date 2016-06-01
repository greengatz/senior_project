import cma
from numpy import ndarray
from numpy import array
from GreedySearch import GreedySearch
import ValueCalculator as vc
import numpy as np

baseValue = 0.09
mergeValue = 1.95 # how much a single merge is worth
openSquareBonus = 0.45 # how much an open square is worth
nonMonotonicMult = 0.70 # multiplier applied to non-monotonic boards
nonMonotonicPenalty = 1.0 # value reduced for a board being non-monotonic
largeOnEdgeBonus = 0.35 # value bonus applied to boards with the largest tiles on the edges

scalar = 0.8

numTrialsPerCall = 1
searchDepth = 3

def objectiveFunc(x, *args):
    # do 10 runs
    # average the results
    # return 100 / avg (function is minimizing, we want max)
    allScores = 0

    setWeights(x)

    for i in range(numTrialsPerCall):
        solver = GreedySearch(searchDepth)
        solver.playGame()
        allScores += solver.getScore()

    scoreAvg = allScores / numTrialsPerCall

    if scoreAvg == 0:
        return [np.float(100)]

    return [np.float(100 / scoreAvg)]

def setWeights(newWeights):
    vc.baseValue = newWeights[0]
    vc.mergeValue = newWeights[1]
    vc.openSquareBonus = newWeights[2]
    vc.nonMonotonicMult = newWeights[3]
    vc.nonMonotonicPenalty = newWeights[4]
    vc.largeOnEdgeBonus = newWeights[5]
    pass

if __name__ == '__main__':
    x = np.zeros(6)
    x[0] = baseValue
    x[1] = mergeValue
    x[2] = openSquareBonus
    x[3] = nonMonotonicMult
    x[4] = nonMonotonicPenalty
    x[5] = largeOnEdgeBonus
    
    print(str(vc.getWeights()))
    setWeights(x)
    print(str(vc.getWeights()))

    es = cma.CMAEvolutionStrategy(x, scalar).optimize(objectiveFunc)

    print(es.result_pretty())

