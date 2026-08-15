def findMajority(nums):
    count = 0
    curr = None
    for num in nums:
        if count == 0:
            curr = num
        if curr ==num:
            count+=1
        else:
            count-=1
    return curr

print(findMajority([3,2,3]))
print(findMajority([2,2,1,1,1,2,2]))
print(findMajority([5]))