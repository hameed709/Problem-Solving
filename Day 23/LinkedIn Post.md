Day 23 — Find All Duplicates in an Array 🔍
Day 23 of my problem-solving journey.
Today's problem was Find All Duplicates in an Array.
The challenge was to find all values that appear exactly twice while:
⏱️ Maintaining O(n) time
💾 Using O(1) extra space apart from the output
❌ No HashSet / HashMap
❌ No sorting
💡 Key Insight
Since every number is in the range [1, n], each value can be mapped directly to an array index:
value → value - 1
I used the sign of the value as a marker:
Positive → number hasn't been seen yet
Negative → number has already been seen
When I encounter a number whose corresponding index is already negative, I've found a duplicate.
Example
For:
[4,3,2,7,8,2,3,1]
The duplicate values are:
[2,3]
This problem helped me understand an important technique:
Sometimes the input array itself can be used as extra memory.
📊 Complexity
Time: O(n)
Extra Space: O(1), excluding the output array
Another day, another algorithmic pattern learned. 🚀

🔗 GitHub: https://lnkd.in/d4HamrX5

#Day23 #100DaysOfCode #ProblemSolving #DSA #Python #Algorithms #CodingJourney #LearningInPublic

Link : https://lnkd.in/p/dkyV_tXe