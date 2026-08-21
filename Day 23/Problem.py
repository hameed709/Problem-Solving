def findDuplicate(arr):
    result = []

    for num in arr:
        index = abs(num) -1
        if arr[index] < 0 :
            result.append(abs(num))
        else:
            arr[index] = -arr[index]

    return result

print(findDuplicate([4,3,2,7,8,2,3,1]))
print(findDuplicate([1,1,2]))
print(findDuplicate([1]))
print(findDuplicate([2,2,3,1,3,4]))