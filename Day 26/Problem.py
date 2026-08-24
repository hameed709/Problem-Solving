def containerWithMostWater(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0

    while left < right:
        height = min(arr[left], arr[right])
        width = right - left

        area = height * width
        max_area = max(max_area, area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return max_area


print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))
print(containerWithMostWater([1,1]))
print(containerWithMostWater([4,3,2,1,4]))
print(containerWithMostWater([1,2,1]))