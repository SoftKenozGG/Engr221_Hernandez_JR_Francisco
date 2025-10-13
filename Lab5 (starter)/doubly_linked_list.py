"""
Francisco Hernandez JR
doubly_linked_List.py
Implementation of a doubly linked list
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from double_node import DoubleNode 

class DoublyLinkedList():

    # Initialize an empty list with no nodes
    def __init__(self):
        self.__first_node = None
        self.__last_node = None

    # Check if the list is empty
    def is_empty(self):
        return self.__first_node == self.__last_node == None

    # If empty raise exception
    # If not empty return the value of the first node
    def first(self):
        if self.is_empty():
            raise Exception("Error: List is empty, no first node")
        return self.get_first_node().get_value()

    # Return the value of the first node without removing it
    def get_first_node(self):
        return self.__first_node

    # Return the value of the last node without removing it
    def get_last_node(self):
        return self.__last_node
    
    # Set the first node of the list
    def set_first_node(self, node):
        self.__first_node = node

    # Set the last node of the list
    def set_last_node(self, node):
        self.__last_node = node

    # Search for a node with the given value and return it
    # If not found, return None
    def find(self, value):
            current = self.__first_node
            while current != None:
                if current.get_value() == value:
                    return current
                current = current.get_next_node()
            return None

    # Insert a new node with the given value at the front of the list
    # If the list is empty, set both first and last node to the new node
    # If the list is not empty, update the pointers accordingly
    def insert_front(self, value):
        current = self.__first_node
        new_node = DoubleNode(value)
        if self.is_empty():
            self.__first_node = new_node
            self.__last_node = new_node
        else:
            new_node.set_next_node(current)
            current.set_previous_node(new_node)
            self.__first_node = new_node

    # Insert a new node with the given value at the back of the list
    # If the list is empty, set both first and last node to the new node
    # If the list is not empty, update the pointers accordingly
    def insert_back(self, value):
        current = self.__last_node
        new_node = DoubleNode(value)
        if self.is_empty():
            self.__first_node = new_node
            self.__last_node = new_node
        else:
            new_node.set_previous_node(current)
            current.set_next_node(new_node)
            self.__last_node = new_node

    # Insert a new node with the given value after the node with after_value
    # If after_value is not found, raise an exception
    # If after_value is the last node, insert at the back
    # Return True if inserted in the middle, False if inserted at the back
    def insert_after(self, value_to_add, after_value):
        new_node = DoubleNode(value_to_add)
        after_node = self.find(after_value)
        if after_node == None:
            raise Exception("Error: after_value not found in list")
        if after_node.is_last():
            self.insert_back(value_to_add)
            return False
        else:
            next_node = after_node.get_next_node()
            new_node.set_previous_node(after_node)
            new_node.set_next_node(next_node)
            after_node.set_next_node(new_node)
            next_node.set_previous_node(new_node)
            return True
    
    # Delete the first node of the list and return its value
    # If the list is empty, raise an exception
    def delete_first_node(self):
        if self.is_empty():
            raise Exception("Error: List is empty, cannot delete first node")
        del_node = self.first()
        if self.__first_node.get_next_node() is None:
            self.__first_node = None
            self.__last_node = None
        else:
            self.__first_node = self.__first_node.get_next_node()
            self.__first_node.set_previous_node(None)
        return del_node

    # Delete the last node of the list and return its value
    # If the list is empty, raise an exception
    def delete_last_node(self):
        if self.is_empty():
            raise Exception("Error: List is empty, cannot delete last node")
        if self.get_first_node() == self.get_last_node():
            del_node = self.__last_node.get_value()
            self.__last_node = None
            self.__first_node = None
            return del_node
        else:
            del_node = self.__last_node.get_value()
            self.__last_node = self.__last_node.get_previous_node()
            self.__last_node.set_next_node(None)
            return del_node

    # Delete the specified value in the list
    # If the list is empty, raise an exception
    # If value not found, raise exception
    def delete_value(self, value):
        if self.is_empty():
            raise Exception("Error: List is empty, cannot delete value")
        del_node = self.find(value)
        if del_node == None:
            raise Exception("Error: Value not found in list")
        if del_node == self.__first_node:
            return self.delete_first_node()
        elif del_node == self.__last_node:
            return self.delete_last_node()
        else:
            previous_node = del_node.get_previous_node()
            next_node = del_node.get_next_node()
            previous_node.set_next_node(next_node)
            next_node.set_previous_node(previous_node)
            return del_node.get_value()

    # Print each item in list starting from first node
    def forward_traverse(self):
        current = self.__first_node
        while current is not None:
            print(current.get_value())
            current = current.get_next_node()

    # Print each item in list starting from last node 
    def reverse_traverse(self):
        current = self.__last_node
        while current is not None:
            print(current.get_value())
            current = current.get_previous_node()

    # Overload the length function, and keep track of number of nodes in list
    def __len__(self):
        length = 0
        current = self.__first_node
        while current is not None:
            length += 1
            current = current.get_next_node()
        return length
    
    # Overload the string function, and print out a string from node list
    def __str__(self):
        result = "["
        current = self.__first_node
        while current is not None:
            result += str(current.get_value())
            if current.get_next_node() is not None:
                result += " <-> "
            current = current.get_next_node()
        result += "]"
        return result

if __name__ == "__main__":
    pass