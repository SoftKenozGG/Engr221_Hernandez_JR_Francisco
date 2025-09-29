"""
WRITE YOUR PROGRAM HEADER HERE
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from double_node import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__first_node = None
        self.__last_node = None 

    def is_empty(self):
        return self.__first_node == None

    def first(self):
        if self.is_empty():
            raise Exception("Error: List is empty, cannot return first  value")
        return self.__first_node
    
    def get_first_node(self):
        return self.__first_node

    def get_last_node(self):
        return self.__last_node
    
    def set_first_node(self, node):
        self.__first_node = node

    def set_last_node(self, node):
        self.__last_node = node

    def find(self, value):
        node = self.get_first_node()

        while node != None:
            if node.

    def insert_front(self, value):
        pass

    def insert_back(self, value):
        pass

    def insert_after(self, value_to_add, after_value):
        pass
    
    def delete_first_node(self):
        pass
    
    def delete_last_node(self):
        pass
    
    def delete_value(self, value):
        pass

    def forward_traverse(self):
        pass

    def reverse_traverse(self):
        pass

    def __len__(self):
        pass
    
    def __str__(self):
        pass
    
if __name__ == "__main__":
    pass