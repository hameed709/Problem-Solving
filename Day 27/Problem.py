def numSearching(arr,target):
    low=0
    high = len(arr)-1

    while low<=high:
        mid=(low+high)//2
        
        if arr[mid]==target:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=target and arr[mid]>=target:
                high =mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=target and arr[high]>=target:
                low=mid+1
            else:
                high = mid - 1 

    return -1

print(numSearching([4,5,6,7,0,1,2],0))
print(numSearching([4,5,6,7,0,1,2],3))
print(numSearching([1],0))
print(numSearching([6,7,8,1,2,3,4,5],3))
print(numSearching([3,4,5,1,2],4))
