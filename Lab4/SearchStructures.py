"""
WRITE YOUR PROGRAM HEADER HERE
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.items = []

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        return len(self.items) == 0

    # For a Stack, this should "push" item to the top of the Stack
    def add(self, item):
        self.items += [item]

    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        x = self.items[len(self.items)- 1]
        del self.items[len(self.items)-1]
        return x
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.items = []

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        return len(self.items) == 0

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        self.items += [item]

    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        x = self.items[len(self.items)- len(self.items)]
        del self.items[len(self.items)-len(self.items)]
        return x
    
    