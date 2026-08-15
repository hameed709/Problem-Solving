Day 17 — Problem: Majority Element

Problem Statement

Given an array of integers nums, find the element that appears more than n / 2 times, where n is the length of the array.

You may assume that the majority element always exists in the array.

Example 1

Input:
[3,2,3]

Output:
3

Explanation:
3 appears 2 times out of 3 elements.

Example 2

Input:
[2,2,1,1,1,2,2]

Output:
2

Explanation:
2 appears 4 times out of 7 elements.

Example 3

Input:
[5]

Output:
5

Constraints:

- 1 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9
- The majority element always exists.

Challenge:

- Solve the problem in O(n) time.
- Try to solve it using O(1) extra space.
- Do not use sorting.
- Do not use a HashMap or dictionary to count frequencies.
- Try using the Boyer-Moore Voting Algorithm.