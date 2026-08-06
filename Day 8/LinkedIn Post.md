🚀 Day 8 of My Daily Problem Solving Challenge
Today's challenge was Longest Palindromic Substring.
The goal was to find the longest substring in a given string that reads the same forwards and backwards, while solving it efficiently in O(n²) time using the Expand Around Center technique instead of generating every possible substring.
At first, my instinct was to search for the palindrome from the middle of the string. That worked for a few examples, but it quickly fell apart once I tested more cases. The biggest lesson was realizing that the longest palindrome isn't necessarily centered in the middle of the string.
The key insight was:
Every character can be the center of an odd-length palindrome.
Every pair of adjacent characters can be the center of an even-length palindrome.
Expanding outward from every possible center guarantees that we don't miss the longest palindrome.
This problem was a great reminder that the first idea isn't always the correct one. Sometimes the challenge is not writing code—it's changing the way you think about the problem.
📚 Difficulty
Medium
💡 What I Learned
Expand Around Center algorithm
Handling both odd and even length palindromes
Pointer expansion using left and right indices
The importance of validating assumptions with edge cases
Every day I solve one problem, learn something new, and become a better problem solver. Consistency is the goal.

💻 GitHub Repository:https://lnkd.in/dM4zg-yD

#100DaysOfCode #ProblemSolving #DataStructures #Algorithms #Python #CodingChallenge #SoftwareEngineering #Programming #LearningInPublic #DSA

Link : https://lnkd.in/p/dTB3W9yj