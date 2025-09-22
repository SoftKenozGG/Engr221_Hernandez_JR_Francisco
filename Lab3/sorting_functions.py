"""
Name: Francisco Hernandez JR
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

# Sorts a list using the insertion sort algorithm
def insertion_sort(list_to_sort):   
    # Run through 1 to len(list_to_sort)
    for indx in range(len(list_to_sort)):
        j = indx
        # Move elements of list_to_sort[0..i-1], that are
        # greater than list_to_sort[i], to one position ahead
        while j > 0 and list_to_sort[j-1] > list_to_sort[j]:
            # save the value at index j
            arr = list_to_sort[j]
            # swap the values at index j and j-1
            list_to_sort[j] = list_to_sort[j-1]
            # save the value at index j-1
            list_to_sort[j-1] = arr
            j -= 1
    return list_to_sort

def bubble_sort(list_to_sort):

    n = len(list_to_sort)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already sorted, so no need to check them
        for j in range(0, n - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                # Swap if the element found is greater than the next element
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                swapped = True
        
        # If no two elements were swapped, the list is already sorted
        if not swapped:
            break
    return list_to_sort

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
    print(get_runtime(insertion_sort, 10000))
    print(get_runtime(bubble_sort, 10000))