Day 8 — Problem: Longest Palindromic Substring

Problem Statement

Given a string s, find the longest substring that is a palindrome.

A palindrome is a string that reads the same forward and backward.

Return the longest palindromic substring.

Example 1

Input:
"babad"

Output:
"bab"

Explanation:
"aba" is also a valid answer.

Example 2

Input:
"cbbd"

Output:
"bb"

Example 3

Input:
"a"

Output:
"a"

Example 4

Input:
"forgeeksskeegfor"

Output:
"geeksskeeg"

Constraints:
- 1 <= s.length <= 1000
- s consists of English letters and digits.

Challenge:
Solve the problem in O(n²) time without generating all possible substrings.
Try using the Expand Around Center technique instead of brute force.