def reversal(nums,start,stop):
    while start < stop :
        nums[start],nums[stop] = nums[stop],nums[start]

        start+=1
        stop-=1

    return nums

def arrayReversal(nums,k):
    n = len(nums)
    k %=n
    nums.reverse()
    reversal(nums,0,k-1)
    reversal(nums,k,n-1)
    return nums

print(arrayReversal([1,2,3,4,5,6,7],3))
print(arrayReversal([-1,-100,3,99],2))
print(arrayReversal([1,2],5))