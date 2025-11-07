"""
Author: Francisco Hernandez JR
Filename: binarySearchTree.py
Description: Implementing a Binary Search Tree.
"""

class BinarySearchTree:
    """ The Binary Search Tree inserts, searches, deletes 
        nodes for a balanced BST """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        # Checks if the tree is empty by checking if the root is None
        return self.__root == None
    
    def getRoot(self):
        # Returns the root node of the tree
        return self.__root

    def search(self, goalKey):
        # Searches for a node with the given key in the BST.
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        # A recursive helper method to search for a node with the given key.
        if node == None:
            return None
        elif goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        elif goalKey > node.key:
            return self.__searchHelp(node.right, goalKey)
        return node

        
    def lookup(self, goal):
        """ TODO: LOOKUP DOCSTRING HERE """
        return self.search(goal)

    def findSuccessor(self, subtreeRoot):
        """ TODO: FINDSUCCESSOR DOCSTRING HERE """
        return self.__findSuccessorHelp(subtreeRoot)
    pass
    
    def __findSuccessorHelp(self, node):
        """ TODO: __FINDSUCCESSOR DOCSTRING HERE """
        # The successor is the smallest key in the left subtree
        current = node.left
        while current.left != None and current != None:
            current = current.left
        return current
    
    def delete(self, deleteKey):
        """ TODO: DELETE DOCSTRING HERE """
        if self.search(deleteKey):
            return self.__deleteHelp(self.__root, deleteKey)
        raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ TODO: __DELETEHELP DOCSTRING HERE """
        """A recursive helper method to delete() method,
           which deletes the node with the given key from the BST."""
        if node is None:
            return node
        if deleteKey < node.key:
            node.left = self.__deleteHelp(node.left, deleteKey)
        elif deleteKey > node.key:
            node.right = self.__deleteHelp(node.right, deleteKey)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: Get the inorder successor (smallest in the left subtree)
            temp = self.__findSuccessorHelp(node)
            # Copy the inorder successor's content to this node
            node.key = temp.key
            node.value = temp.value
            # Delete the inorder successor
            node.left = self.__deleteHelp(node.left, temp.key)    
        return node

    def traverse(self) -> None:
        # Traverses the tree in-order and prints the keys and values.
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        # A recursive helper method to traverse the tree in-order.
        if node != None:
            self.__traverseHelp(node.left)
            print("({}, {})".format(node.key, node.value))
            self.__traverseHelp(node.right)

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    pass