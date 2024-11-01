# define a merge sort function that takes in one array
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # check if array length is less than or equal to 1, if so return array as is

    # define mid as half array length
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    # divide the array into left array and right array, 
    # recursively call the merge sort algorithm with the left array and the right array and store the result in left and right sorted arrays
    sorted_right_array = merge_sort(right_arr)
    sorted_left_array = merge_sort(left_arr)
    # return the merge function and to it pass two arrays the sorted right and left arrays
    return merge(sorted_left_array, sorted_right_array)

# define a merge function that takes in 2 arrays
def merge(left, right):
# initialize an empty array, sorted_array to store sorted elements
    sorted_array = []
    # initialize counters, i and j at value, 0
    i = j = 0
    # write a while loop that checks that both the left and right arrays have a length greater than zero
    while i < len(left) and j < len(right):
        # in the loop check for which elements at index i and j for left and right respectively is smaller (if else)
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
            # append the smaller element to the  sorted_array
        else:
            sorted_array.append(right[j])
            j += 1
            # increment counter for respective smaller element array

    # extend the sorted elements with any remaining values past the counters 
    sorted_array.extend(right[j:])
    sorted_array.extend(left[i:])
    # return the sorted array
    return sorted_array


# test with a unsorted array
array = [5, 3, 2, 7, 8]
# print out the sorted array
sorted_array = merge_sort(array)
print(sorted_array)