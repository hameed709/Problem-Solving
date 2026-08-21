Day 23 — Problem: Find All Duplicates in an Array

Problem Statement

Given an integer array nums of length n where each integer is in the range [1, n], find all the values that appear exactly twice.

Return the values that appear twice.

The order of the result does not matter.

Example 1

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

Explanation:
2 appears twice and 3 appears twice.

Example 2

Input:
[1,1,2]

Output:
[1]

Example 3

Input:
[1]

Output:
[]

Example 4

Input:
[2,2,3,1,3,4]

Output:
[2,3]

Constraints:

- n == nums.length
- 1 <= n <= 100000
- 1 <= nums[i] <= n
- Each integer appears once or twice.

Challenge:

- Solve the problem in O(n) time.
- Try to use O(1) extra space apart from the output array.
- Do not use a HashSet or HashMap.
- Do not sort the array.
- Try using the array indices as markers.
- Make sure each duplicate value is added only once.