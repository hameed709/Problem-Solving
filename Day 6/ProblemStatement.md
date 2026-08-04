Day 6 — Problem: Group Anagrams

Problem Statement

Given an array of strings, group the words that are anagrams of each other.

Words are anagrams if they contain the same characters with the same frequency, but in a different order.

Return the groups in any order.

Example 1

Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Example 2

Input:
["abc", "bca", "cab", "xyz", "zyx"]

Output:
[["abc", "bca", "cab"], ["xyz", "zyx"]]

Example 3

Input:
["hello"]

Output:
[["hello"]]

Constraints:
- 1 <= strs.length <= 100
- 1 <= strs[i].length <= 100
- All strings contain only lowercase English letters.

Challenge:
Solve the problem without using any built-in anagram checking functions. Design an efficient solution that groups words correctly.