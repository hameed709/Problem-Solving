Day 12 — Problem: Two Sum

Problem Statement

Given an array of integers nums and an integer target, find the indices of the two numbers that add up to the target.

You may assume that each input has exactly one solution.

You cannot use the same element twice.

Return the indices of the two numbers.

Example 1

Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9

Example 2

Input:
nums = [3, 2, 4]
target = 6

Output:
[1, 2]

Example 3

Input:
nums = [3, 3]
target = 6

Output:
[0, 1]

Constraints:

- 2 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid answer exists.

Challenge:

- Solve the problem in O(n) time.
- Do not use nested loops.
- Do not sort the array.
- Try using a HashMap to store previously seen numbers.