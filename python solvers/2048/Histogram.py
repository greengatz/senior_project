import math
from ast import increment_lineno

class DataGroup(object):

    def __init__(self):
        self.values = []
        self.histo = []
        pass
    
    
    def contains(self, value):
        for val in self.histo:
            if val[0] == value:
                return True
        return False
    
    
    def increment(self, value):
        for x in range(len(self.histo)):
            if self.histo[x][0] == value:
                newTuple = (value, self.histo[x][1] + 1)
                del self.histo[x]
                self.histo = self.histo + [newTuple]
                
    
    
    def add(self, value):
        self.histo = self.histo + [(value, 1)]
    
    
    def put(self, value):
        self.values = self.values + [value]
        if self.contains(value):
            self.increment(value)
        else:
            self.add(value)
        pass
    
    
    def getMean(self):
        sum = 0
        
        for val in self.values:
            sum += val
        
        sum /= len(self.values)
        return sum
    
    
    def getStd(self):
        mean = self.getMean()
        diffsSquared = 0
        
        for val in self.values:
            diff = val - mean
            diffsSquared += (diff * diff)
        
        return math.sqrt(diffsSquared)
    
    
    def getMax(self):
        return max(self.values)
    
    
    def getHisto(self):
        retStr = ""
        for val in self.histo:
            retStr = retStr + str(val[0]) + "-" + str(val[1]) + "\n";
        return retStr
    
    
    def writeData(self, fileName):
        with open(fileName) as output:
            for val in self.values:
                output.write(str(val) + "\n")
        pass