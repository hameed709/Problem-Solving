def find3Sum(arr):
    arr_sorted = sorted(arr)
    n = len(arr)
    result = []
    for i in range(n):
        num = arr_sorted[i]
        if i>0 and num == arr_sorted[i-1]:
            continue

        left = i + 1
        right = n - 1
        while left < right:
            sum3 = num + arr_sorted[left] + arr_sorted[right]
            if sum3 < 0:
                left += 1
            elif sum3 > 0:
                right -= 1
            else:
                result.append([num,arr_sorted[left],arr_sorted[right]])
                while left < right and arr_sorted[left] == arr_sorted[left + 1]:
                    left += 1
                while left < right and arr_sorted[right] == arr_sorted[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

print(find3Sum([-1,0,1,2,-1,-4]))
print(find3Sum([0,1,1]))
print(find3Sum([0,0,0]))
print(find3Sum([-2,0,1,1,2]))