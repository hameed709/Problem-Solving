def arrayIntersection(arr1,arr2):
    intersection = set()
    arr2_set = set(arr2)
    for num in arr1:
        if num in arr2_set:
            intersection.add(num)
    return list(intersection)

print(arrayIntersection([1,2,2,1],[2,2]))
print(arrayIntersection([4,9,5],[9,4,9,8,4]))
print(arrayIntersection([1,2,3],[4,5,6]))
print(arrayIntersection([1,1,1,2,2],[1,1,2,3]))