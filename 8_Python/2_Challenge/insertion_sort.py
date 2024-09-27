# Inserion sort is less predictable algorithm and is mostly used
# The insertion sort always sees backward for a value if it is greater 
# than current value.
# If it is greater then it swaps
# In this algorithm we use 1 FOR loop and 1 WHILE loop.
# The FOR loop move forward and the WHILE loop moves backward to see
# if the previous value is greater than the current value.


array = [21, 54, 87, 32, 5, 68, 44, 7, 10]

for current in range(1, len(array)):
    i = current
    while i > 0:
        if array[i-1]>array[i]:
            array[i], array[i-1] = array[i-1], array[i]
        i -= 1
    
print(array)

# Insertion Sort looks for the bigger value behind
# The best and worst case are found in insertion sort algorithm
# If the array is partially unsorted then the (comparisions and swaps)
# will be less otherwise it will be many comparisions
# If the array is already sorted then (n-1) comparisions
# If the array is unsorted then (n^2-n)/2 comparisions