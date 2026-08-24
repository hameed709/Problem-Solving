Day 26 — Problem: Container With Most Water

Problem Statement

Given an integer array height where height[i] represents the height of a vertical line at index i.

Choose two lines that, together with the x-axis, form a container that holds the most water.

Return the maximum amount of water the container can store.

Example 1

Input:
[1,8,6,2,5,4,8,3,7]

Output:
49

Explanation:
The lines at index 1 and index 8 form the container with maximum area.

Width = 8 - 1 = 7
Height = min(8,7) = 7

Area = 7 × 7 = 49

Example 2

Input:
[1,1]

Output:
1

Example 3

Input:
[4,3,2,1,4]

Output:
16

Explanation:
The first and last lines have height 4.

Width = 4
Height = 4

Area = 4 × 4 = 16

Example 4

Input:
[1,2,1]

Output:
2

Constraints:

- 2 <= height.length <= 100000
- 0 <= height[i] <= 10000

Challenge:

- Solve the problem in O(n) time.
- Do not use nested loops.
- Do not calculate the area of every possible pair.
- Try using the Two Pointer technique.
- Start with one pointer at the beginning and one at the end.
- Move the pointer with the smaller height.