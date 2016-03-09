'''
Created on March 6, 2016

@author: John_2
'''

import math

class DataGroup(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.values = []
        pass
    
    
    def put(self, value):
        self.values = self.values + [value]
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
    
    
    def writeData(self, fileName):
        with open(fileName) as output:
            for val in self.values:
                output.write(str(val) + "\n")
        pass