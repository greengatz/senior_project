'''
Created on Jan 6, 2016

@author: John_2
'''

class MyClass(object):
    '''
    classdocs
    '''
    hiddenNum = 0

    def __init__(self):
        '''
        Constructor
        '''
        self.hiddenNum = 0
    
    def getNum(self):
        self.hiddenNum += 1;
        return self.hiddenNum
        
    def isDone(self):
        return self.hiddenNum < 10