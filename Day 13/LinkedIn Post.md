🚀 Day 13 — DSA Practice: Valid Parentheses
Today’s problem was Valid Parentheses, where the goal was to determine whether brackets are properly opened, closed, and nested.
🧠 Approach
I used a Stack-based approach:
Push every opening bracket onto the stack.
For every closing bracket, check whether it matches the most recently opened bracket.
If there is a mismatch or no corresponding opening bracket, return False.
At the end, the stack must be empty for the string to be valid.
💻 Complexity
⏱️ Time: O(n)
💾 Space: O(n)
🧪 Tested With
✅ ()
✅ ()[]{}
❌ (]
✅ ([{}])
❌ ([)]
✅ {[]}
This problem was a good reminder of why LIFO (Last In, First Out) is so useful when dealing with nested structures.
Another problem solved. Another concept strengthened. 🔥

🔗 GitHub Repository: https://lnkd.in/dWvRYnhA

#Day13 #DSA #DataStructures #Algorithms #Python #ProblemSolving #CodingJourney #100DaysOfCode

Link : https://lnkd.in/p/dfe2UppP