Day 24 — Problem: Product of Two Numbers

Problem Statement

Given an integer array nums, find the two distinct elements whose product is the maximum.

Return the maximum product.

You may assume the array contains at least two elements.

Example 1

Input:
[3,4,5,2]

Output:
20

Explanation:
The two largest positive numbers are 4 and 5.

4 × 5 = 20

Example 2

Input:
[-10,-3,5,6]

Output:
30

Explanation:
The two smallest negative numbers are -10 and -3.

(-10) × (-3) = 30

Example 3

Input:
[-10,-3,5,2]

Output:
30

Example 4

Input:
[-5,-2,-1]

Output:
10

Explanation:
(-5) × (-2) = 10

Example 5

Input:
[-1,0,2,3]

Output:
6

Constraints:

- 2 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9

Challenge:

- Solve the problem in O(n) time.
- Do not sort the array.
- Do not use nested loops.
- Do not generate all possible pairs.
- Try solving it in a single pass.
- Carefully handle both positive and negative numbers.
- Think about the two largest values and the two smallest values.