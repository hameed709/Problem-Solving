Day 16 — Move Zeroes 🚀
Another problem added to the Daily Problem Solving Challenge!
Today’s problem was Move Zeroes — rearrange an array so that all 0s move to the end while keeping the relative order of the non-zero elements.
The interesting part wasn’t the problem itself, but understanding how to approach it efficiently.
I initially tried solving it using pop() and append(), then experimented with two pointers using left and right. That helped me understand an important lesson:
👉 Two Pointer isn't just about having two variables. The key is giving each pointer a clear responsibility.
For the final approach:
🔹 right scans through the array
🔹 left tracks where the next non-zero element should go
🔹 Non-zero elements are placed in their correct positions using swaps
🔹 No extra array is created
⏱️ Time Complexity: O(n)
💾 Space Complexity: O(1)
This problem was a good reminder that sometimes the biggest improvement isn't writing more code — it's finding a cleaner way to think about the problem. 🧠

🔗 GitHub: https://lnkd.in/dNJ5N4Rm

#Day16 #100DaysOfCode #DSA #Python #ProblemSolving #TwoPointers #CodingChallenge #DataStructures #Algorithms #LearningInPublic #SoftwareDevelopment

Link : https://lnkd.in/p/dZ3nrvJ8