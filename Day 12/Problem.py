def Findsum(nums,target):
    seen = {}
    for i in range(len(nums)):
        curr_num=nums[i]
        req_num= target - nums[i]
        if req_num in seen:
            return [seen[req_num],i]
        else:
            seen[nums[i]]=i

print(Findsum([2, 7, 11, 15],9))
print(Findsum([3, 2, 4],6))
print(Findsum([3, 3],6))
