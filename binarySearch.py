def binarySearch(arr, val):
    low, high = 0, len(arr)-1
    while(low <= high):
        mid = (low+high)//2
        if(arr[mid] < val):
            low = mid+1
        elif(arr[mid] > val):
            high = mid-1
        else:
            return True
    return False


print(binarySearch([0, 1, 2, 3, 4, 5, 6], 6))
