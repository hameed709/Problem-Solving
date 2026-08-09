🚀 Day 11 — Daily Problem Solving Challenge
Today’s problem: Maximum Subarray Sum
🧩 Problem
Given an integer array, the goal is to find the contiguous subarray with the largest sum and return that maximum sum.
For example:
Input:
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6
The subarray [4, -1, 2, 1] produces the maximum sum:
4 + (-1) + 2 + 1 = 6
The challenge was to solve it in O(n) time without generating every possible subarray or using nested loops.
💡 My Approach
I used Kadane’s Algorithm.
While going through the array, I maintained two values:
curr → the maximum sum of a subarray ending at the current position
max_sum → the maximum sum found so far
For every element, I decide whether it is better to:
👉 Start a new subarray from the current element
or
👉 Continue the previous subarray
The key logic was:
curr = max(nums[i], curr + nums[i])
max_sum = max(max_sum, curr)
This allows the algorithm to make the decision at every element without checking every possible subarray.
⚠️ Important Edge Case
One thing I specifically had to make sure of was handling arrays containing only negative numbers.
For example:
[-3, -2, -5, -1]
The answer is:
-1
The algorithm should not incorrectly return 0, because the subarray must contain at least one element.
That's why I initialized both values using the first element:
curr = nums[0]
max_sum = nums[0]
📊 Complexity
⏱️ Time Complexity: O(n)
💾 Space Complexity: O(1)
No nested loops.
No generation of all possible subarrays.
Just a single pass through the array.
🧠 What I Learned
This problem helped me understand how a seemingly expensive subarray problem can be reduced to a single-pass solution by maintaining the right state.
The important part wasn't memorizing Kadane's Algorithm, but understanding why we can discard the previous sum when it becomes worse than starting fresh.
Another problem completed in my daily problem-solving challenge.

🔗 GitHub: https://lnkd.in/d8xrXrqd

#Day11 #DSA #ProblemSolving #Python #Algorithms #KadaneAlgorithm #CodingChallenge #100DaysOfCode #SoftwareEngineering

Link : https://lnkd.in/p/d3cR2zkz