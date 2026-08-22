def maxProduct(arr):
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    for num in arr:
        if num > largest :
            second_largest = largest
            largest =num
        elif num > second_largest:
            second_largest = num
        if num < smallest:
            second_smallest =smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    maximumProduct = max(largest*second_largest,smallest*second_smallest) 
    return maximumProduct

print(maxProduct([3,4,5,2]))
print(maxProduct([-10,-3,5,6]))
print(maxProduct([-10,-3,5,2]))
print(maxProduct([-5,-2,-1]))
print(maxProduct([-1,0,2,3]))