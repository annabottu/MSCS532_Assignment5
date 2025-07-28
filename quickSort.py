# this is a simple implementation of the QuickSort algorithm in Python.
# QuickSort is a divide-and-conquer algorithm that sorts an array by partitioning it into
# smaller sub-arrays. The steps are as follows: 
# 1. Choose a pivot element from the array.
# 2. Partition the array into three parts: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.
# 3. Recursively apply the same process to the sub-arrays of elements less than and greater than the pivot.
# 4. Combine the sorted sub-arrays and the pivot to get the final sorted array.
def quicksort(arr):
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Select a pivot (we use the last element for simplicity)
    pivot = arr[-1]

    # Step 2: Partition the array into three parts:
    # less than pivot, equal to pivot, and greater than pivot
    less = [x for x in arr[:-1] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    # Step 3: Recursively sort the less and greater subarrays
    return quicksort(less) + equal + quicksort(greater)

arr = [7,9,0,3,4,5,5,1,6,8,2]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
