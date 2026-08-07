def sequence(nums):
    if not nums:
        return 0

    longest=0
    num_set=set(nums)

    for num in num_set:
        if num-1 not in num_set:
            current=num
            length=1
            while current+1 in num_set:
                current+=1
                length+=1
            longest=max(longest,length)

    return longest

print(sequence([100, 4, 200, 1, 3, 2]))
print(sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(sequence([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
print(sequence([]))