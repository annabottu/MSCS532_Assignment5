import random
# This is a simple implementation of the Randomized QuickSort algorithm in Python.
# Randomized QuickSort is a variation of the QuickSort algorithm that selects a random pivot
# element to improve performance on average, especially for cases where the input is already
# partially sorted or has many duplicate elements. The steps are as follows:
# 1. Randomly select a pivot element from the array.
# 2. Partition the array into three parts: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.
# 3. Recursively apply the same process to the sub-arrays of elements less than and greater than the pivot.
# 4. Combine the sorted sub-arrays and the pivot to get the final sorted array.
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    # Step 1: Randomly select a pivot
    pivot = random.choice(arr)

    # Step 2: Partition the array into three parts
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Step 3: Recursively sort the subarrays
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

arr = [7,9,0,3,4,5,5,1,6,8,2]
sorted_arr = randomized_quicksort(arr)
print("Sorted array:", sorted_arr)
