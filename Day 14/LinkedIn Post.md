🚀 Day 14 — Merge Intervals
Today’s problem was Merge Intervals 📚
The tricky part for me wasn't the syntax — it was figuring out how to maintain the current interval while checking the next one in a single loop.
Once that clicked, the logic became much clearer:
🔹 Sort the intervals
🔹 Compare the current and next interval
🔹 Merge if they overlap
🔹 Continue until the end
I also made a mistake while merging overlapping intervals by directly using the next interval's end value. That broke cases where the current interval already extended further.
The fix? 👉 Keep the maximum end value.
Another small but important lesson in understanding how to think about a problem before writing the code. 🧠💻
⏱️ Time Complexity: O(n log n)

🔗 GitHub Repo: https://lnkd.in/dZ9z_T8Z

#DSA #Python #Algorithms #ProblemSolving #100DaysOfCode

Link : https://lnkd.in/p/d_iYVx5v