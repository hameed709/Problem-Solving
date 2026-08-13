Day 15 — Problem: Rotate Array

Problem Statement

Given an integer array nums, rotate the array to the right by k steps.

Rotating the array means that elements at the end of the array move to the beginning.

Example 1

Input:
nums = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]

Explanation:
After 1 rotation:
[7,1,2,3,4,5,6]

After 2 rotations:
[6,7,1,2,3,4,5]

After 3 rotations:
[5,6,7,1,2,3,4]

Example 2

Input:
nums = [-1,-100,3,99]
k = 2

Output:
[3,99,-1,-100]

Example 3

Input:
nums = [1,2]
k = 5

Output:
[2,1]

Explanation:
Rotating 5 times is the same as rotating 1 time because:

5 % 2 = 1

Constraints:

- 1 <= nums.length <= 100000
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^9

Challenge:

- Solve the problem in O(n) time.
- Do not use nested loops.
- Do not create another array of size n.
- Try solving it using the Array Reversal technique.
- Handle cases where k is greater than the length of the array.
- Target extra space: O(1).