Day 22 — Problem: Subarray Sum Equals K

Problem Statement

Given an integer array nums and an integer k, find the total number of continuous subarrays whose sum equals k.

A subarray must contain at least one element.

Example 1

Input:
nums = [1,1,1]
k = 2

Output:
2

Explanation:
The subarrays [1,1] starting at index 0 and index 1 have a sum of 2.

Example 2

Input:
nums = [1,2,3]
k = 3

Output:
2

Explanation:
The subarrays [1,2] and [3] have a sum of 3.

Example 3

Input:
nums = [1,-1,0]
k = 0

Output:
3

Explanation:
The subarrays [1,-1], [0], and [1,-1,0] have a sum of 0.

Example 4

Input:
nums = [3,4,7,2,-3,1,4,2]
k = 7

Output:
4

Constraints:

- 1 <= nums.length <= 20000
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

Challenge:

- Solve the problem in O(n) time.
- Do not use nested loops.
- Do not generate all possible subarrays.
- The array may contain positive, negative, and zero values.
- Try using Prefix Sum + HashMap.
- Store the frequency of previously seen prefix sums.