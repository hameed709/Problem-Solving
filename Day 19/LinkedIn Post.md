🚀 Day 19 
Today’s problem: Find the Missing Number 🔢
Given an array containing n distinct numbers from the range [0, n], the goal is to find the missing number.
For example:
[3, 0, 1] → 2
The interesting part? We had to solve it in O(n) time, using O(1) extra space, without sorting or using a HashSet/HashMap.
💡 My approach: XOR
The key XOR properties are:
x ^ x = 0
x ^ 0 = x
So, if we XOR all numbers from 0 to n with all the numbers present in the array, every existing number appears twice and cancels out.
That leaves only the missing number. 🎯

⚡ Complexity
Time: O(n)
Space: O(1)
No sorting
No HashSet / HashMap
Another day, another algorithm added to the toolkit. 🧠💻
The goal isn't just to solve problems — it's to understand why the solution works and recognize the pattern when a similar problem appears.

🔗 GitHub: https://lnkd.in/dkHuPNjB

#Day19 #30DaysOfDSA #DSA #DataStructuresAndAlgorithms #Python #CodingChallenge #ProblemSolving #Algorithms #LearningInPublic #100DaysOfCode

Link : https://lnkd.in/p/dXRydzsd