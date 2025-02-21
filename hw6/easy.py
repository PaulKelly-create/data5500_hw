#I didn't understand what an array was so I asked Chat What is an array in Python and it explained what an array is, and that it is mostly lists
#I made a function for caculating a given list, or array
def calculate_sum(arr):
    # Make the sum vairaible so that we can add on to it
    total_sum = 0
    
    # Iterate through each element of the array or list and add them to total sum
    for num in arr:
        total_sum += num
    
    # Return the total sum
    return total_sum

# Example for an array and adding it all up
arr = [1, 2, 1, 2, 1]
result = calculate_sum(arr)
print("Sum of array elements:", result)

#Chat help me understand the big O notation of this code
# For big O notation asked chat about it and what it is, I actually did the medium before the easy so I learned about it there
# The time complexity of this function is O(n), where n is the number of elements in the array.
# Chat also talked about the space complexity being O(1) because we only use a fixed amount of extra space regardless of input size which is interesting