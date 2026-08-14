Day 16 — Problem: Move Zeroes

Problem Statement

Given an integer array nums, move all 0's to the end of the array while maintaining the relative order of the non-zero elements.

You must modify the array in-place.

Example 1

Input:
[0,1,0,3,12]

Output:
[1,3,12,0,0]

Example 2

Input:
[0]

Output:
[0]

Example 3

Input:
[1,0,2,0,3,0,4]

Output:
[1,2,3,4,0,0,0]

Example 4

Input:
[1,2,3,4]

Output:
[1,2,3,4]

Constraints:

- 1 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9

Challenge:

- Solve the problem in O(n) time.
- Modify the array in-place.
- Do not create another array.
- Maintain the relative order of all non-zero elements.
- Try using the Two Pointer technique.
- Minimize the number of unnecessary swaps.