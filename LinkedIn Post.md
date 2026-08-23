🚀 Day 25 of my Problem-Solving Journey — 3Sum
Today’s problem was 3Sum, where the goal is to find all unique triplets in an array whose sum is 0.
🧩 Problem
Given an integer array, find all unique triplets:
nums[i] + nums[j] + nums[k] = 0
The challenge was to solve it in O(n²) without using three nested loops or returning duplicate triplets.
💡 Approach
I used:
🔹 Sorting — Sort the array first
🔹 Two Pointers — Fix one element and use left and right pointers to find the remaining two values
🔹 Duplicate Handling — Skip duplicate values for both the fixed element and the two-pointer search
The key idea was:
Sort → Fix one element → Two Pointers → Skip duplicates
📊 Complexity
⏱️ Time: O(n²)
💾 Extra Space: O(n) due to creating the sorted array
🧠 What I Learned
3Sum was a good reminder that improving an algorithm isn't always about adding more code. The real improvement came from recognizing that sorting gives us enough structure to eliminate an entire loop.
Handling duplicates correctly was also an important part of this problem.

💻 GitHub Repository: https://lnkd.in/dHw5_pCt

#100DaysOfCode #Day25 #ProblemSolving #DSA #Python #Algorithms #TwoPointers #LeetCode #CodingJourney #LearningInPublic

Link : https://lnkd.in/p/dMrCRvkU