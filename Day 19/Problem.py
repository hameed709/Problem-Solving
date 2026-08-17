def findNum(nums):
    n=len(nums)
    missingNum = n
    for i in range(n):
        missingNum ^= i
        missingNum ^=nums[i]

    return missingNum

print(findNum([3,0,1]))
print(findNum([0,1]))
print(findNum([9,6,4,2,3,5,7,0,1]))
print(findNum([0]))