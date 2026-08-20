def subArraySum(arr,k):
    prefixSum = 0
    count = 0
    seen = {0 : 1}
    for num in arr:
        prefixSum += num
        req = prefixSum - k
        if req in seen:
            count += seen[req]
        seen[prefixSum] = seen.get(prefixSum, 0) + 1
    return count

print(subArraySum([1,1,1],2))
print(subArraySum([1,2,3],3))
print(subArraySum([1,-1,0],0))
print(subArraySum([3,4,7,2,-3,1,4,2],7))