🚀Day 15 — Rotate Array 🔄
Today’s problem looked simple at first:
Rotate an array to the right by k steps.
My first approach was straightforward: move the last element to the beginning repeatedly.
It worked for the examples, but there was a problem. 👀
insert(0, ...) is expensive, and repeating it k times doesn't satisfy the O(n) requirement.
So I went back, experimented with slicing and reversal, and eventually reached the Array Reversal technique.
The final approach:
🔹 Reverse the entire array
🔹 Reverse the first k elements
🔹 Reverse the remaining elements
For example:
[1,2,3,4,5,6,7], k = 3
➡️ Reverse everything
[7,6,5,4,3,2,1]
➡️ Reverse the first 3
[5,6,7,4,3,2,1]
➡️ Reverse the remaining
[5,6,7,1,2,3,4] ✅
The biggest takeaway wasn't just the final solution.
It was realizing that a brute-force-looking operation can sometimes be completely transformed by changing how you look at the problem.
📌 Complexity:
Time: O(n)
Extra Space: O(1)
Another day, another problem solved by actually thinking through it instead of immediately looking up the solution. 💻🔥

🔗 GitHub Repository: https://lnkd.in/dNjCR6qZ

#Day15 #100DaysOfCode #CodingChallenge #Python #DSA #DataStructures #Algorithms #ProblemSolving #LearningInPublic #SoftwareEngineering #CodingJourney 🚀

Link : https://lnkd.in/p/duTRysCD