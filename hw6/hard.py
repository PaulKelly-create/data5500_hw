#worked with chat a little bit on this one but not much, mostly on the big O notation
# made another function to find the max distance of any two numbers in an array/list
def max_dif(arr):
    #need to check if there is fewer than 2 elements so this works
    if len(arr) <2:
        return None
    # start the min and max varaibles to the first element of the array/list
    min_num = max_num = arr[0]

    #find the min and max values in the list/array
    for num in arr:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    #now get the max difference between largest and smallest numbers in the list/array
    return max_num - min_num

#for testing the code seeing that the function works
arr = [3, 10, 5, 8, 9, 4, 3]
result = max_dif(arr)
print("Maximum difference:", result)

#Chat help me understand the big O notation of this code
# for big O notation it is O(n), where n is the number of elements in the array because it iterates the array once to find both min and max
# also looked at space complexity, O(1) for this, becasue we only use a constant amount of space for min and max numbers regardless of input size

