Day 11 — Problem: Maximum Subarray Sum

Problem Statement

Given an integer array nums, find the contiguous subarray with the largest sum and return that maximum sum.

A subarray must contain at least one element.

Example 1

Input:
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6

Explanation:
The subarray [4, -1, 2, 1] has the maximum sum:

4 + (-1) + 2 + 1 = 6

Example 2

Input:
[1]

Output:
1

Example 3

Input:
[5, 4, -1, 7, 8]

Output:
23

Explanation:
The entire array has the maximum sum:

5 + 4 - 1 + 7 + 8 = 23

Example 4

Input:
[-3, -2, -5, -1]

Output:
-1

Constraints:

- 1 <= nums.length <= 100000
- -10^4 <= nums[i] <= 10^4

Challenge:

- Solve the problem in O(n) time.
- Do not use nested loops.
- Do not generate all possible subarrays.
- Try solving it using Kadane's Algorithm.
- Handle arrays containing only negative numbers correctly.