🚀 Day 10 of My Daily Problem-Solving Challenge
Today’s problem: Product of Array Except Self
The goal was to return an array where each element contains the product of every other element except the element at that index.
🧩 The Challenge
The solution had a few strict requirements:
• O(n) time complexity
• No division
• No nested loops
• Handle arrays containing zeroes
• Use O(1) extra space apart from the output array
💡 My Approach
I solved it using Prefix and Suffix Products.
In the first pass, I calculated the product of all elements to the left of each index.
Then, in the second pass, I traversed from right to left and multiplied each position by the product of all elements to its right.
This allowed me to build the final answer without using division or nested loops.
🧪 Test Cases
[1, 2, 3, 4] → [24, 12, 8, 6]
[-1, 1, 0, -3, 3] → [0, 0, 9, 0, 0]
[2, 3, 4, 5] → [60, 40, 30, 24]
📚 What I Learned
This problem helped me understand how prefix and suffix calculations can be combined to solve an array problem efficiently.
The interesting part was that zeroes don't require separate handling when the prefix/suffix approach is designed correctly.
Difficulty: Medium 🟡
Another problem solved. Another step forward in improving my problem-solving and understanding of time and space complexity.

🔗 GitHub Repository:https://lnkd.in/d5zQxrCb

#Day10 #ProblemSolving #DSA #Python #DataStructures #Algorithms #CodingChallenge #100DaysOfCode #LearningInPublic

Link : https://lnkd.in/p/ddweBktB