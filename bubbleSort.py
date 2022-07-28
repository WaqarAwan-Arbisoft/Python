def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubbleSort([27, 0, 71, 70, 27, 63, 90]))
