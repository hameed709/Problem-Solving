Day 13 — Problem: Valid Parentheses

Problem Statement

Given a string s containing only the characters '(', ')', '{', '}', '[' and ']', determine whether the input string is valid.

A string is valid if:

- Every opening bracket has a corresponding closing bracket of the same type.
- Brackets are closed in the correct order.
- Every closing bracket has a corresponding opening bracket.

Example 1

Input:
"()"

Output:
true

Example 2

Input:
"()[]{}"

Output:
true

Example 3

Input:
"(]"

Output:
false

Example 4

Input:
"([{}])"

Output:
true

Example 5

Input:
"([)]"

Output:
false

Example 6

Input:
"{[]}"

Output:
true

Constraints:

- 1 <= s.length <= 100000
- s consists only of '(', ')', '{', '}', '[' and ']'.

Challenge:

- Solve the problem in O(n) time.
- Do not repeatedly scan the string.
- Use a Stack-based approach.
- Make sure nested brackets are handled correctly.