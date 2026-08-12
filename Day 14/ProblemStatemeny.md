Day 14 — Problem: Merge Intervals

Problem Statement

Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.

Return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1

Input:
[[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]

Explanation:
The intervals [1,3] and [2,6] overlap, so they are merged into [1,6].

Example 2

Input:
[[1,4],[4,5]]

Output:
[[1,5]]

Explanation:
The intervals [1,4] and [4,5] overlap at 4, so they are merged.

Example 3

Input:
[[1,10],[2,3],[4,5],[6,8]]

Output:
[[1,10]]

Example 4

Input:
[[1,2],[3,4],[5,6]]

Output:
[[1,2],[3,4],[5,6]]

Constraints:

- 1 <= intervals.length <= 10000
- intervals[i].length == 2
- 0 <= start <= end <= 10000

Challenge:

- Solve the problem efficiently.
- Sort the intervals based on their starting values.
- Merge overlapping intervals in a single pass after sorting.
- Do not compare every interval with every other interval.
- Target time complexity: O(n log n).