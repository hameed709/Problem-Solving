def Interval(nums):
    result = []
    intervals = sorted(nums)
    curr = intervals[0]
    for interval in intervals[1:]:
        next = interval
        if next[0] <= curr[-1]:
            curr = [curr[0],max(curr[1],next[1])]
        else:
            result.append(curr)
            curr = next
    result.append(curr)
    return result


print(Interval([[1,3],[2,6],[8,10],[15,18]]))
print(Interval([[1,4],[4,5]]))
print(Interval([[1,10],[2,3],[4,5],[6,8]]))
print(Interval([[1,2],[3,4],[5,6]]))
print(Interval([[1,9]]))