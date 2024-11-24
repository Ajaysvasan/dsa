def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1 
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key

array = [10,8,2,9,1]
insertionSort(array)
print(array)