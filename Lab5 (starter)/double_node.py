"""
WRITE YOUR PROGRAM HEADER HERE
"""

class DoubleNode():

    def __init__(self, value, next=None, previous=None):
        self.__value = value
        self.__next_node = next
        self.__previous_node = previous 

    #####
    # Methods
    #####
        
    def is_first(self):
        pass
        
    def is_last(self):
        pass

    #####
    # Getters
    #####

    def get_value(self):
        pass
    
    def get_next_node(self):
        pass

    def get_previous_node(self):
        pass

    #####
    # Setters
    #####

    def set_value(self, new_value):
        pass

    def set_next_node(self, new_next):
        pass

    def set_previous_node(self, new_previous):
        pass

    #####
    # Helpers
    #####

    def __check_valid_node(self, node):
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True
    
    def __str__(self):
        pass

if __name__ == "__main__":
    pass