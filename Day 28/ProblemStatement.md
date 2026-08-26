Day 28 — Problem: Find Minimum in Rotated Sorted Array

Problem Statement

Given a sorted array of distinct integers nums that has been rotated at an unknown position, find the minimum element in the array.

You must solve the problem in O(log n) time.

Example 1

Input:
[3,4,5,1,2]

Output:
1

Example 2

Input:
[4,5,6,7,0,1,2]

Output:
0

Example 3

Input:
[11,13,15,17]

Output:
11

Example 4

Input:
[2,1]

Output:
1

Example 5

Input:
[5,1,2,3,4]

Output:
1

Constraints:

- 1 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9
- All values in nums are distinct.
- nums is originally sorted in ascending order and then rotated.

Challenge:

- Solve the problem in O(log n) time.
- Do not use min().
- Do not sort the array.
- Do not scan every element.
- Use Binary Search.
- Compare the middle element with the rightmost element to determine which half contains the minimum.