🚀 Day 22 of my Problem-Solving Journey
Today’s problem: Subarray Sum Equals K 🎯
Given an integer array and a target k, the goal is to find the total number of continuous subarrays whose sum equals k.
At first glance, a brute-force approach seems straightforward — generate every possible subarray and calculate its sum.
But that would take O(n²) time. ❌
Instead, I used the Prefix Sum + HashMap approach. 🧠
The key idea:
👉 If the current prefix sum is prefixSum, we need to check whether we previously encountered:
prefixSum - k
If we did, that previous prefix sum represents a subarray ending at the current position whose sum is exactly k.
I also learned why storing the frequency of prefix sums is important rather than simply checking whether a sum exists. The same prefix sum can occur multiple times, and each occurrence can represent a different valid subarray.
Complexity
⏱️ Time: O(n)
💾 Space: O(n)
The solution also handles arrays containing positive numbers, negative numbers, and zeros.
🔥 Another important step in my problem-solving journey — understanding why the optimization works instead of simply memorizing the pattern.
Day 22 completed. 📈

🔗 GitHub: https://lnkd.in/dDnvazFi

#ProblemSolving #DSA #Python #Algorithms #CodingJourney #100DaysOfCode #LeetCode #PrefixSum #HashMap #LearningInPublic

Link : https://lnkd.in/p/dJi9RjsR