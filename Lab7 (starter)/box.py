"""
Author: Francisco Hernandez JR
Filename: box.py
Description: Box class for managing entries.
"""

import os, sys 

sys.path.append(os.path.dirname(__file__))

from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile='entries.txt'):
        # Open the file as read only
        with open(inputFile, 'r') as f:
            # Add each value in the file as an Entry to the Box
            for line in f:
                # Set the first word in the line as the nickname, and
                # the second as species
                nickname, species = line.split()
                # Add the new entry to the Box
                self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    Returns true if the Entry is successfully added to the Box, and
    false if the nickname already exists in the Box. """
    def add(self, nickname, species):
        # Check if the nickname already exists in the Box
        if self.nicknameMap.containsKey(nickname):
            return False  # Nickname already exists

        # Create a new Entry object
        new_entry = Entry(nickname, species)
        # Add the new Entry to the nicknameMap
        self.nicknameMap.put(nickname, new_entry)
        return True  # Successfully added 

    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """
    # find Entry By Nickname And Species
    def find(self, nickname, species):
        # Check if the nickname exists in the Box
        if self.nicknameMap.containsKey(nickname):
            # Get the entry associated with the nickname
            entry = self.nicknameMap.get(nickname)
            # Check if the species matches
            if entry._Entry__species == species:
                # Species matches, return the entry
                return entry
        # Entry not found, return None
        return None 

    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return an empty list if the Box is empty. """
    # find All Nicknames
    def findAllNicknames(self):
        # Initialize an empty list to store nicknames
        nicknames = []
        # Iterate through each bucket in the nicknameMap
        for bucket in self.nicknameMap.buckets:
            # Iterate through each entry in the bucket
            for entry in bucket:
                # Append the nickname (key) to the nicknames list
                nicknames.append(entry.getKey())
        # Return the list of nicknames
        return nicknames 

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return an empty list if the nickname is not in the Box. """
    # find Entry By Nickname
    def findEntryByNickname(self, nickname):
        # Check if the nickname exists in the Box
        if self.nicknameMap.containsKey(nickname):
            # Return the entry associated with the nickname
            return self.nicknameMap.get(nickname)
        # Nickname not found, return None
        return None 

    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    # remove By Nickname
    def removeByNickname(self, nickname):
        # Check if the nickname exists in the Box
        if self.nicknameMap.remove(nickname):
            # Successfully removed the entry
            return True
        # Nickname not found, return False
        return False 

    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    # remove Entry By Nickname And Species
    def removeEntry(self, nickname, species):
        # Check if the nickname exists in the Box
        if self.nicknameMap.containsKey(nickname):
            # Get the entry associated with the nickname
            entry = self.nicknameMap.get(nickname)
            # Check if the species matches
            if entry._Entry__species == species:
                # Species matches, remove the entry
                self.nicknameMap.remove(nickname)
                # Successfully removed the entry
                return True
        # Entry not found or species does not match, return False
        return False

if __name__ == '__main__':
    pass