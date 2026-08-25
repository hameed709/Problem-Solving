Day 27 — Search in Rotated Sorted Array 🔍
Today’s problem was Search in Rotated Sorted Array.
The challenge was to find a target in a rotated sorted array in O(log n) time — which means a normal linear search was out of the question.
💡 Key idea: Modified Binary Search
At every iteration:
Find the middle element.
Determine which half of the array is sorted.
Check whether the target lies within that sorted half.
If it does, search that half.
Otherwise, eliminate it and search the other half.
For example:
[4,5,6,7,0,1,2]
Searching for 0 → index 4.
The important insight I learned today:
Even though the array is rotated, at least one half around mid will always remain sorted.
⏱️ Time Complexity: O(log n)
💾 Space Complexity: O(1)
This problem was a good reminder that binary search isn't limited to perfectly sorted arrays — with the right logic, it can be adapted to more complex structures.
🚀 Day 27 — Problem Solving Challenge
I’m continuing to build consistency by solving one problem at a time and focusing on understanding the logic rather than just memorizing solutions.

💻 GitHub Repository: https://lnkd.in/dgGU8c9c

#100DaysOfCode #ProblemSolving #DSA #DataStructures #Algorithms #BinarySearch #Python #CodingChallenge #SoftwareEngineering #LearningInPublic

Link : https://lnkd.in/p/dNFDGBCK