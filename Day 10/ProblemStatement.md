Day 10 — Problem: Product of Array Except Self

Problem Statement

Given an array of integers nums, return an array answer such that:

answer[i] is equal to the product of all elements of nums except nums[i].

The solution should handle arrays containing zeroes.

You must solve the problem without using division.

Example 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Explanation:
- For index 0: 2 × 3 × 4 = 24
- For index 1: 1 × 3 × 4 = 12
- For index 2: 1 × 2 × 4 = 8
- For index 3: 1 × 2 × 3 = 6


Example 2

Input:
[-1, 1, 0, -3, 3]

Output:
[0, 0, 9, 0, 0]

Explanation:
For index 2, excluding 0:

(-1) × 1 × (-3) × 3 = 9


Example 3

Input:
[2, 3, 4, 5]

Output:
[60, 40, 30, 24]


Constraints:

- 2 <= nums.length <= 100000
- -30 <= nums[i] <= 30

Challenge:

- Solve the problem in O(n) time.
- Do not use division.
- Do not use nested loops.
- Try to solve it using prefix and suffix products.
- Use O(1) extra space apart from the output array.