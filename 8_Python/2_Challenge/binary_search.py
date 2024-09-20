# Develop the binary search algorithm

# Binary search algorithm works on the principal of lo, mid, and high index selection in the array
# Every time in the while loop we update the lo, mid, and high index by comparing it with the target value
# Binary search only works when the array is already sorted

array = [10, 15, 17, 54, 66, 78, 79, 81, 95, 102, 121, 135]
target = 17

lo = 0
high = len(array)-1

while lo<high:
    mid = int((lo + high)/2)
    
    if array[mid] > target:
        high = mid - 1
    
    elif array[mid] < target:
        lo = mid + 1

    elif array[mid] == target:
        print("Target value found:", array[mid])
        break