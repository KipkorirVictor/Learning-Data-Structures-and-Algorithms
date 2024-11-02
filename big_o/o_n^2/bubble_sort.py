
def bubble_sort(arr):
    n =len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
    

unsorted_array = [24, 23, 26, 67, 88, 27, 64, 89,]
sorted_array = bubble_sort(unsorted_array)
print(sorted_array)