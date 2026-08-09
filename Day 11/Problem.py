def maxSubArray(nums):
    curr=nums[0]
    max_sum=nums[0]

    for i in range(1,len(nums)):
        curr=max(nums[i],curr+nums[i])
        max_sum=max(max_sum,curr)

    return max_sum

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([1]))
print(maxSubArray([5, 4, -1, 7, 8]))
print(maxSubArray([-3, -2, -5, -1]))