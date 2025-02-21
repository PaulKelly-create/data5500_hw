#again made a function to go through a list but this time to find the second largest number in that list or array
def second_largest(arr):
    #Keep track of the largest and the second largest variables in array/list
    largest = second_largest = float('-inf')
    # Asked chat about this, what -inf is, it sets it to negative infinity initailly so that you can then find the next largest number

    #go through each element in list
    for num in arr:
        #keep updating largest and second larget numbers
        if num >largest:
            second_largest = largest
            largest = num
        #largest does not look like a word anymore which is crazy
        elif num > second_largest and num != largest:
            second_largest = num
        
        #making it so if second largest is still -inf there is no valid second largest
    if second_largest == float('-inf'):
        return None
    
    return second_largest

#example list to see if code works
arr = [5, 3, 7, 2, 9]
result = second_largest(arr)
print("Second largest number:", result)

#Chat help me understand the big O notation of this code
# Asked chat what the time complexity meant and learned about O(1) O(n) and O(n^2)
# Time complexity: O(n)
# We go through each element of the array once, so the running time is linear with respect to the number of elements.

