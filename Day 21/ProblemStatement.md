Day 21 — Problem: Intersection of Two Arrays

Problem Statement

Given two integer arrays nums1 and nums2, find the unique elements that appear in both arrays.

Each element in the result should appear only once.

The order of the result does not matter.

Example 1

Input:
nums1 = [1,2,2,1]
nums2 = [2,2]

Output:
[2]

Explanation:
The value 2 appears in both arrays.

Example 2

Input:
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

Output:
[4,9]

Example 3

Input:
nums1 = [1,2,3]
nums2 = [4,5,6]

Output:
[]

Example 4

Input:
nums1 = [1,1,1,2,2]
nums2 = [1,1,2,3]

Output:
[1,2]

Constraints:

- 1 <= nums1.length, nums2.length <= 100000
- -10^9 <= nums1[i], nums2[i] <= 10^9

Challenge:

- Solve the problem in O(n + m) time.
- Do not use nested loops.
- The result must contain only unique values.
- Try using a HashSet for an efficient solution.
- Do not sort the arrays.