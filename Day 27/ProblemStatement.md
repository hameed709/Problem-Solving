Day 27 — Problem: Search in Rotated Sorted Array

Problem Statement

Given a sorted array of distinct integers nums that has been rotated at an unknown position, and an integer target, return the index of target if it exists in the array.

If target does not exist, return -1.

You must solve the problem in O(log n) time.

Example 1

Input:
nums = [4,5,6,7,0,1,2]
target = 0

Output:
4

Example 2

Input:
nums = [4,5,6,7,0,1,2]
target = 3

Output:
-1

Example 3

Input:
nums = [1]
target = 0

Output:
-1

Example 4

Input:
nums = [6,7,8,1,2,3,4,5]
target = 3

Output:
5

Example 5

Input:
nums = [3,4,5,1,2]
target = 4

Output:
1

Constraints:

- 1 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9
- All values in nums are distinct.
- nums is originally sorted in ascending order and then rotated.
- -10^9 <= target <= 10^9

Challenge:

- Solve the problem in O(log n) time.
- Do not use linear search.
- Do not sort the array again.
- Use the Binary Search technique.
- Identify which half of the array is sorted.
- Decide which half may contain the target and eliminate the other half.