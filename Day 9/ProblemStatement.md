Day 9 — Problem: Longest Consecutive Sequence

Problem Statement

Given an unsorted array of integers, find the length of the longest sequence of consecutive numbers.

A consecutive sequence contains numbers that follow each other without gaps.

Your algorithm must run in O(n) time.

Example 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
4

Explanation:
The longest consecutive sequence is [1, 2, 3, 4].

Example 2

Input:
[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Output:
9

Explanation:
The longest consecutive sequence is
[0,1,2,3,4,5,6,7,8].

Example 3

Input:
[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]

Output:
7

Explanation:
The longest consecutive sequence is
[3,4,5,6,7,8,9].

Constraints:

- 0 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9

Challenge:

- Solve the problem in O(n) time.
- Do not sort the array.
- Use a HashSet or HashMap for an optimal solution.