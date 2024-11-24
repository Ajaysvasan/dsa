
def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if array[j]<array[minIndex]:
                minIndex = j
        if minIndex !=i:
            array[i],array[minIndex] = array[minIndex],array[i]
    return array
array = [5,10,2,26,8,6]

print(array)
print(selectionSort(array))