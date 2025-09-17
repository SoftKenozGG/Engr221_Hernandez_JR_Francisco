"""
Name: Francisco Hernandez JR
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

def insertion_sort(list_to_sort):   
    for indx in range(len(list_to_sort)):
        j = indx
        while j > 0 and list_to_sort[j-1] > list_to_sort[j]:
            temp = list_to_sort[j-1]
            list_to_sort[j-1]=list_to_sort[j]
            list_to_sort[j]=temp
            j -= 1
        print(indx)
        print(list_to_sort[indx])
        print(list_to_sort)
        print(len(list_to_sort))

def bubble_sort(list_to_sort):
    j = 0
    for i in len(list_to_sort) -1-i:
        if list_to_sort[j] > list_to_sort[j+1]:
            list_to_sort[j] = list_to_sort[j+1]
        print(list_to_sort)
    pass

def create_random_list(length):
    """ Returns a list of the given length with random values.
        Input: 
            length (int) - Desired length of the list """
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def get_runtime(function_to_run, list_length):
    """ Returns the duration (in seconds) that it took for 
        function_to_run to sort a list of length list_length.
        Input: 
            function_to_run (function) - Name of the function
            list_length (int) - Length of the list to sort """
    # Create a new list to sort
    list_to_sort = create_random_list(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time

if __name__ == '__main__':
    insertion_sort([7,5,9,10,3,2,1,13,12,4,2,2,2,1,2,3,5,4,31,90,67,6])
    #print(get_runtime(insertion_sort, 100000))