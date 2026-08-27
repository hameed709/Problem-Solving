Day 29 — Simple Challenge: Frequency of the Most Frequent Element

Given an integer array nums, return the maximum frequency of any element after performing the following operation any number of times:

Choose an element and increase it by 1.

You can perform the operation at most k times.

Example 1
nums = [1,2,4]
k = 5

Output:
3

Example 2
nums = [1,4,8,13]
k = 5

Output:
2


Example 3
nums = [3,9,6]
k = 2

Output:
1


🎯 Target
Time: O(n log n)
Space: O(1) extra space if you sort in place.

Hint

Sort the array first.