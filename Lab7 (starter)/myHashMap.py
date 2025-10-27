"""
Author: Francisco Hernandez JR
Filename: myHashMap.py
Description: Implementing a hash map.
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self):
        # Double the number of buckets
        self.capacity *= 2 
        # Make a copy of the current contents in the buckets
        old_buckets = self.buckets 
        # Create a new set of buckets that's twice as big as the old one
        self.buckets = [[] for _ in range(self.capacity)]
        # Reset the size to 0 before re-adding entries
        self.size = 0
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in old_buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        # Turn the key into a hash value
        keyHash = hash(key)

        # Check if key is None
        if key is None:
            raise Exception("Key cannot be None")
        
        # Check if resize is needed
        if (self.size) / self.capacity > self.load_factor:
            self.resize()
        
        # Find the appropriate bucket for the key
        bucket_index = keyHash % self.capacity
        bucket = self.buckets[bucket_index]

        # Check if the key already exists in the bucket
        for entry in bucket:
            if entry.getKey() == key:
                return False  # Key already exists

        # If key does not exist, add new entry
        new_entry = self.MyHashMapEntry(key, value)
        bucket.append(new_entry)
        # Increment the size of the map
        self.size += 1
        return True

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
        # Check if key is None
        if key is None:
            raise Exception("Key cannot be None")
        
        # Turn the key into a hash value
        keyHash = hash(key)

        # Find the appropriate index for the bucket
        bucket_index = keyHash % self.capacity
        # Find the bucket
        bucket = self.buckets[bucket_index]

        # Search for the key in the bucket
        for entry in bucket:
            # If the key is found, replace its value
            if entry.getKey() == key:
                entry.setValue(newValue)
                # Successfully replaced the value
                return True
        
        # Key was not found
        return False

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        # Check if key is None
        if key is None:
            raise Exception("Key cannot be None")
        
        # Turn the key into a hash value
        keyHash = hash(key)

        # Find the appropriate index for the bucket
        bucket_index = keyHash % self.capacity
        # Find the bucket
        bucket = self.buckets[bucket_index]

        # Search for the key in the bucket
        for i in range(len(bucket)):
            entry = bucket[i]
            # If the key is found, remove the entry
            if entry.getKey() == key:
                del bucket[i]
                # Decrement the size of the map
                self.size -= 1
                # Successfully removed the entry
                return True
        
        # Key was not found
        return False

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        # Check if key is None
        if key is None:
            raise Exception("Key cannot be None")
        
        # If the key does not exist, add it
        if self.containsKey(key) == False:
            self.put(key, value)        
        else:
            # Try to replace the value if the key exists
            self.replace(key, value)
        


    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        # Check if key is None
        if key is None:
            raise Exception("Key cannot be None")
        
        # Turn the key into a hash value
        keyHash = hash(key)

        # Find the appropriate index for the bucket
        bucket_index = keyHash % self.capacity
        # Find the bucket
        bucket = self.buckets[bucket_index]

        # Search for the key in the bucket
        for entry in bucket:
            # If the key is found, return its value
            if entry.getKey() == key:
                return entry.getValue()
        
        # Key was not found
        return None

    """
    Return the number of key, value pairs in this MyHashMap. """
    # Return the size of the map
    def get_size(self):
        return self.size

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    # Check if the size is 0
    def isEmpty(self):
        # Return true if the size is 0
        return self.size == 0

    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        # Check if key is None
        if key is None:
            raise Exception("Key cannot be None")
        
        # Turn the key into a hash value
        keyHash = hash(key)

        # Find the appropriate index for the bucket
        bucket_index = keyHash % self.capacity
        # Find the bucket
        bucket = self.buckets[bucket_index]

        # Search for the key in the bucket
        for entry in bucket:
            # If the key is found, return true
            if entry.getKey() == key:
                return True
        
        # Key was not found
        return False

    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        keys_list = []
        # Iterate through each bucket
        for bucket in self.buckets:
            # If the bucket is not empty
            if bucket != []:
                # Iterate through each entry in the bucket
                for entry in bucket:
                    # Append the key to the keys_list
                    keys_list.append(entry.getKey())
        return keys_list

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key 
            self.value = value 

        def getKey(self):
            return self.key 
        
        def getValue(self):
            return self.value 
        
        def setValue(self, new_value):
            self.value = new_value 

if __name__ == "__main__":
    pass