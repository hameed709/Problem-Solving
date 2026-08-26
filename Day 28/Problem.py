def findMin(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low+high)//2
        if arr[mid]>arr[high]:
            low = mid+1
        else:
            high = mid
    return arr[low]

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))
print(findMin([2,1]))
print(findMin([5,1,2,3,4]))
