'''
Created on Jan 6, 2016

@author: John_2
'''
from practice.counter import MyClass


print("hello world")
counter = MyClass()

while counter.isDone():
    print(counter.getNum())


print("done")
