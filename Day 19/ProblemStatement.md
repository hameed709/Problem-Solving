Day 19 — Problem: Find the Missing Number

Problem Statement

Given an array nums containing n distinct numbers taken from the range [0, n], find the one number that is missing from the array.

Example 1

Input:
[3,0,1]

Output:
2

Explanation:
The numbers should be [0,1,2,3].
The missing number is 2.

Example 2

Input:
[0,1]

Output:
2

Example 3

Input:
[9,6,4,2,3,5,7,0,1]

Output:
8

Example 4

Input:
[0]

Output:
1

Constraints:

- 1 <= nums.length <= 100000
- 0 <= nums[i] <= n
- All numbers in nums are unique.

Challenge:

- Solve the problem in O(n) time.
- Use O(1) extra space.
- Do not sort the array.
- Do not use a HashSet or HashMap.
- Try solving it using the XOR technique.