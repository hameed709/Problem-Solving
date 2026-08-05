Day 7 — Problem: Longest Substring Without Repeating Characters

Problem Statement

Given a string s, find the length of the longest substring that contains no repeated characters.

A substring is a contiguous sequence of characters.

Return the length of the longest substring.

Example 1

Input:
"abcabcbb"

Output:
3

Explanation:
The longest substring without repeating characters is "abc".

Example 2

Input:
"bbbbb"

Output:
1

Explanation:
The longest substring is "b".

Example 3

Input:
"pwwkew"

Output:
3

Explanation:
The longest substring is "wke".

Example 4

Input:
""

Output:
0

Constraints:
- 0 <= s.length <= 10^5
- s consists of English letters, digits, symbols, and spaces.

Challenge:
Solve the problem in O(n) time.
Do not generate all possible substrings.
Use the Sliding Window technique for an optimal solution.