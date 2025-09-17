"""
Author: Francisco Hernandez JR
Filename: nodupesplaylist.py
Description: Implementation of a playlist as an array without duplicates
"""


import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from song import Song

class NoDupesPlaylist():
    # The constructor is run every time a new NoDupesPlaylist object is created
    # initial_songs is a list containing the Songs you can have in the playlist
    #Checks to see if playlist has duplicates
    def __init__(self, initial_songs=None):
        #initialize the nodupe playlist
        new_song_list = []
        self.max_num_songs = 0
        self.num_songs = 0

        #Runs through the initial songs and checks for duplicates
        for item in initial_songs:
            isDuplicate = False
            for  uniqueItem in new_song_list:
                #Returns true if duplicate is found and breaks loop
                if item == uniqueItem:
                    isDuplicate = True
                    break
            #If no duplicate is found, adds song to new list
            if not isDuplicate:
                new_song_list += [item]
        #Sets the songs to the new list without duplicates
        self.songs = new_song_list
        #Updates the number of songs and max number of songs
        self.num_songs = len(self.songs)
        self.max_num_songs = len(self.songs)

    ###########
    # Methods #
    ###########

    # Return the number of songs in the playlist
    def get_num_songs(self):
        return self.num_songs 
    
    # Return the current songs list
    def get_songs(self):
        return self.songs 
    
    # Return the song at index idx or
    # Return None if idx is outside of bounds
    def get_song_at_idx(self, idx):
        if 0 <= idx and idx < self.num_songs:
            return self.songs[idx]
    
    # Set index idx to the given song
    # Do not change anything if idx is outside of bounds
    def set_song_at_idx(self, idx, song):
        if 0 <= idx and idx < self.num_songs:
            self.songs[idx] = song 

    # Insert a song to the end of the playlist
    def insert_song(self, song):

         # If the playlist is empty, initialize it with size 1
        if self.get_num_songs() == 0:
            self.songs = [None] * 1
            self.max_num_songs = 0
            self.num_songs = 0

        #Make sure there are no duplicates
        if self.search_by_title(song.title) == -1:
            
            # If the playlist is full, add one to size
            if self.get_num_songs() == self.max_num_songs:
                new_max_num_songs = self.max_num_songs + 1
                new_songs = [None] * new_max_num_songs
            else:
                # Create a new list with the new size
                new_songs = [None] * self.max_num_songs

                # Copy over the songs from the old list to the new list
            for i in range(self.get_num_songs()):
                new_songs[i] = self.songs[i]
            
            # Update the playlist to the new list and size  
            self.songs = new_songs
            # Update the max size
            self.max_num_songs = new_max_num_songs
            # Insert the new song at the end of the playlist
            self.songs[self.get_num_songs()] = song

            self.num_songs += 1
            # Update the length of the playlist


    # Return the index of the given song title in the playlist,
    # or return -1 if the song is not in the playlist
    def search_by_title(self, song_title):
        # Only search the indices with songs
        for i in range(self.get_num_songs()):
            # Check the value at the current index 
            if self.songs[i].title == song_title:
                # Return the index if we found the song
                return i 
            
        # If we got here, we did not find the song so return -1
        return -1
    
    # Delete all occurrences of a song title in the playlist
    # Returns the number of occurrences deleted if the song was deleted, or 0 if not
    def delete_by_title(self, song_title):
        # Initialize a counter for the number of occurrences deleted
        count = 0

        for i in range(self.get_num_songs()):
            # Find the index of the song to delete
            idx = self.search_by_title(song_title)

            # If the song was not found, we cannot delete it
            if idx == -1 and count == 0:
                return False
            elif idx == -1 and count > 0:
                return True

            # If the song is found, delete it
            if self.songs[i].title == song_title:
                
                # Then shift all the remaining songs in the playlist
                for j in range(i, self.get_num_songs() - 1):
                    self.songs[j] = self.songs[j+1]
                    
                # Set the last song to None since we shifted everything
                self.songs[self.get_num_songs() - 1] = None
                # Decrement the number of songs
                self.num_songs -= 1
                # Increment the counter
                count += 1
        
        # Otherwise, proceed by decrementing the size of the playlist
        self.num_songs -= 1

        # Return the number of occurrences deleted
        return True

    # Print all songs in the playlist
    def traverse(self):
        for song in self.songs:
            print(song)

if __name__ == '__main__':
    # You can test your code here
    song = [Song("Golden", "HUNTR/X"),
            Song("Ordinary", "Alex Warren"),
            Song("Golden", "HUNTR/X"),
            Song("What I Want", "Morgan Wallen ft. Tate McRae"),
            Song("Your Idol", "Saja Boys"),
            Song("Soda Pop", "Saja Boys"),
            Song("What I Want", "Morgan Wallen ft. Tate McRae"),
            Song("What I Want", "Morgan Wallen ft. Tate McRae"),
            Song("Golden", "HUNTR/X")]
    p = NoDupesPlaylist(song)
    p.traverse()
    print(p.get_num_songs())
    p.insert_song(Song("Soda Pop", "Saja Boys"))
    p.insert_song(Song("Soda Pop", "Saja Boys"))
    p.insert_song(Song("What I Want", "Morgan Wallen ft. Tate McRae"))
    p.traverse()
