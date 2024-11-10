# Develop selection sort algorithm
# Details of the working of this algorithm are as follows:
# array = [12, 9, 4, 2, 5]
# We run a for loop from 0 to length of array
# minimum-index is the index at the element in the 0 position as starting value (current_index)
# Then we run another loop from the index 1 to the length of array to find another minimum in the rest of the
# array by checking if any element in the reset of the array is less than element in the minimum_index and then
# we update the minimum_index to the index of that lesser value
# then in the outer loop we always to swapping between the current_index and the minimum_index
# Selection sort is an predictable algorithm which always loog for the 
# minimum value and do sorting and scanning the whole array

array = [12, 9, 4, 2, 5]

for current in range(0, len(array)):
    min_index = current
    for i in range(current+1, len(array)):
        if(array[i]<array[min_index]):
            min_index = i
    array[min_index], array[current] = array[current], array[min_index]

print(array)

# Selection sort = Minimum index (looks for minimum value in an array)
# Working is element 12 is current element
# Comparisions are as follows (9,12), (4,12), and so on
# if the ith element is smaller than current element then we update the min_index
# We always do swap min_index element and current element and move the number in the sorted sequence

# If the length of the array is (n) then the selection sort does the (n) accesses and (n-1) comparisions.
# The array with 4 elements will do 6 comparisions and 3 swaps = (n-1)
# The formula for calculating the number of comparision is (n^2-n)/2