Day 25 — Problem: 3Sum

Problem Statement

Given an integer array nums, find all unique triplets [nums[i], nums[j], nums[k]] such that:

nums[i] + nums[j] + nums[k] = 0

The indices i, j, and k must be different.

The solution must not contain duplicate triplets.

Return all valid triplets.

Example 1

Input:
[-1,0,1,2,-1,-4]

Output:
[[-1,-1,2],[-1,0,1]]

Example 2

Input:
[0,1,1]

Output:
[]

Example 3

Input:
[0,0,0]

Output:
[[0,0,0]]

Example 4

Input:
[-2,0,1,1,2]

Output:
[[-2,0,2],[-2,1,1]]

Constraints:

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Challenge:

- Solve the problem in O(n²) time.
- Do not use three nested loops.
- Do not generate all possible triplets.
- Do not return duplicate triplets.
- Try using sorting + the Two Pointer technique.
- Carefully handle duplicate values.