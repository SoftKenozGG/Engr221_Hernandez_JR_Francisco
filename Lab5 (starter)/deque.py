"""
WRITE YOUR PROGRAM HEADER HERE
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from doubly_linked_list import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList()

    def is_empty(self):
        pass
    
    def __len__(self):
        pass
    
    def __str__(self):
        pass

    def peek_left(self):
        pass

    def peek_right(self):
        pass

    def insert_left(self, value):
        pass
        
    def insert_right(self, value): 
        pass

    def remove_left(self): 
        pass

    def remove_right(self):
        pass
    
if __name__ == "__main__":
    pass