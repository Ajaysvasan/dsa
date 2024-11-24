# Function to merge two subarrays
def merge(arr, l, m, r):
    # Sizes of two subarrays
    n1 = m - l + 1
    n2 = r - m

    # Temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into the main array
    i = 0  # Initial index of the first subarray
    j = 0  # Initial index of the second subarray
    k = l  # Initial index of the merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Recursive merge sort function
def mergeSort(arr, l, r):
    if l < r:
        # Find the middle point
        m = l + (r - l) // 2

        # Sort the first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # Merge the sorted halves
        merge(arr, l, m, r)

# Driver code
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

print("Given array is:")
print(" ".join(map(str, arr)))

mergeSort(arr, 0, n - 1)

print("\nSorted array is:")
print(" ".join(map(str, arr)))
