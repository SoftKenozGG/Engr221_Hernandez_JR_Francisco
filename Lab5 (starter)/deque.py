"""
Francisco Hernandez JR
deque.py
Implementation of a deque using a doubly linked list
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from doubly_linked_list import DoublyLinkedList

#Implement a deque using a doubly linked list
class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList()

    # Returns True if the deque is empty, False otherwise
    def is_empty(self):
        return self.__values.is_empty()
    
    # Returns the number of elements in the deque
    def __len__(self):
        return len(self.__values)
    
    # Returns a string representation of the deque
    def __str__(self):
        return self.__values.__str__()

    # Returns the value at the left end of the deque without removing it
    def peek_left(self):
        return self.__values.get_first_node().get_value()

    # Returns the value at the right end of the deque without removing it
    def peek_right(self):
        return self.__values.get_last_node().get_value()
    
    #Inserts a value at the left end of the deque
    def insert_left(self, value):
        self.__values.insert_front(value)
        
    #Inserts a value at the right end of the deque
    def insert_right(self, value): 
        self.__values.insert_back(value)

    #Removes and returns the value at the left end of the deque
    def remove_left(self): 
        return self.__values.delete_first_node()

    #Removes and returns the value at the right end of the deque
    def remove_right(self):
        return self.__values.delete_last_node()
    
if __name__ == "__main__":
    pass