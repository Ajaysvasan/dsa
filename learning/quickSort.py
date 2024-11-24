# Function to partition the array
def partition(array, low, high):
    # Select the pivot (last element in the array)
    pivot = array[high]
    i = low - 1  # Pointer for the smaller element

    # Traverse through the array
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1  # Increment the smaller element pointer
            # Swap elements to ensure smaller ones are on the left
            array[i], array[j] = array[j], array[i]

    # Place the pivot element in its correct position
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1  # Return the partition index

# Function to implement Quick Sort
def quickSort(array, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(array, low, high)

        # Recursively sort elements before and after the partition
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# Driver code
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array:")
print(data)

# Perform Quick Sort
quickSort(data, 0, len(data) - 1)   

print("\nSorted Array in Ascending Order:")
print(data)
