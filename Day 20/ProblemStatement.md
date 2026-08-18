Day 20 — Problem: Contains Duplicate

Problem Statement

Given an integer array nums, determine whether any value appears at least twice in the array.

Return true if any duplicate value exists, otherwise return false.

Example 1

Input:
[1,2,3,1]

Output:
true

Explanation:
The value 1 appears more than once.

Example 2

Input:
[1,2,3,4]

Output:
false

Explanation:
Every element appears only once.

Example 3

Input:
[1,1,1,3,3,4,3,2,4,2]

Output:
true

Explanation:
Multiple values appear more than once.

Example 4

Input:
[5]

Output:
false

Constraints:

- 1 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9

Challenge:

- Solve the problem in O(n) time.
- Try to use O(n) extra space.
- Do not use nested loops.
- Do not compare every element with every other element.
- Try using a HashSet to efficiently track previously seen values.
- Return immediately when a duplicate is found.