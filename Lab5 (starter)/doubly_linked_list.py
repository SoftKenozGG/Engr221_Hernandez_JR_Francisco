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
        pass

    def first(self):
        pass
    
    def get_first_node(self):
        pass

    def get_last_node(self):
        pass
    
    def set_first_node(self, node):
        pass

    def set_last_node(self, node):
        pass

    def find(self, value):
        pass

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