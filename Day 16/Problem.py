def moveZeros(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1

    return nums

print(moveZeros([0,1,0,3,12]))
print(moveZeros([0]))
print(moveZeros([1,0,2,0,3,0,4]))
print(moveZeros([1,2,3,4]))