Day 24 — Product of Two Numbers 🚀
Today’s problem was Product of Two Numbers.
🧩 Problem
Given an integer array, find the maximum product that can be obtained by multiplying any two distinct elements.
The tricky part is handling negative numbers.
For example:
[-10, -3, 5, 6]
The answer is:
(-10) × (-3) = 30
So simply finding the two largest numbers isn't enough.
💡 Key Insight
The maximum product can only come from one of two possibilities:
The two largest numbers
The two smallest numbers
Why?
Because two large positive numbers can produce the maximum positive product, while two large-magnitude negative numbers can also produce a large positive product.
So, in a single pass, I tracked:
largest
second_largest
smallest
second_smallest
Then compared:
largest × second_largest
with
smallest × second_smallest
⚡ Complexity
Time: O(n)
Space: O(1)
No sorting.
No nested loops.
No generating all possible pairs.
📚 What I learned
Today's problem reinforced an important algorithmic pattern:
Instead of checking every possibility, identify the small set of values that can actually influence the final answer.
This is another step toward becoming better at problem-solving, optimization, and algorithmic thinking.
Day 24✅

🔗 GitHub: https://lnkd.in/dxg_EHvk

#100DaysOfCode #Python #DSA #ProblemSolving #Algorithms #CodingJourney #LearningInPublic

Link : https://lnkd.in/p/d93Tt6NA