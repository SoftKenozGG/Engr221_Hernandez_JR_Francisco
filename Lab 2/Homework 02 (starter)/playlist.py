"""
Author: Francisco Hernandez JR
Filename: playlist.py
Description: Implementation of a playlist as an array with duplicates
"""


import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from song import Song

class Playlist():
    # The constructor is run every time a new Playlist object is created
    # initial_songs is a list containing the Songs you can have in the playlist
    def __init__(self, initial_songs=None):
        # Stores the songs in the playlist
        # It is initially a list of songs of objects or None
        self.songs = initial_songs
        # The current number of songs in the playlist
        self.num_songs = len(initial_songs)
        # The maximum number of songs the playlist can have
        self.max_num_songs = len(initial_songs)

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
            self.max_num_songs = 1
            self.num_songs = 0

        # If the playlist is full, double its size
        if self.get_num_songs() == self.max_num_songs:
            self.new_max_num_songs = self.get_num_songs() * 2
            # Create a new list with double the size
            new_songs = [None] * self.new_max_num_songs
            # Copy over the songs from the old list to the new list
            for i in range(self.get_num_songs()):
                new_songs[i] = self.songs[i]
            self.songs = new_songs
            self.max_num_songs = self.new_max_num_songs

        # Insert the new song at the end of the playlist
        self.songs[self.get_num_songs()] = song

        # Update the length of the playlist
        self.num_songs += 1

    # Return the index of the given song title in the playlist,
    # or return -1 if the song is not in the playlist
    def search_by_title(self, song_title):
        # Only search the indices with songs
        for i in range(self.num_songs):
            # Check the value at the current index 
            if self.songs[i].title == song_title:
                # Return the index
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
                return 0
            elif idx == -1 and count > 0:
                return count

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
        return count

    # Print all songs in the playlist
    def traverse(self):
        for song in self.songs:
            print(song)

if __name__ == '__main__':
    # You can test your code here
    song = [Song("Golden", "HUNTR/X"),
            Song("Ordinary", "Alex Warren"),
            Song("What I Want", "Morgan Wallen ft. Tate McRae"),
            Song("Your Idol", "Saja Boys"),
            Song("Soda Pop", "Saja Boys")]
    p = Playlist(song)
    p.traverse()