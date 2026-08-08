def arrayProduct(nums):
    n=len(nums)
    answer = [1]*n
    prefix = 1

    for i in range(n):
        answer[i]=prefix
        prefix *=nums[i]

    suffix=1
    for i in range(n-1,-1,-1):
        answer[i]*=suffix
        suffix *=nums[i]

    return answer


print(arrayProduct([1, 2, 3, 4]))
print(arrayProduct([-1, 1, 0, -3, 3]))
print(arrayProduct([2, 3, 4, 5]))