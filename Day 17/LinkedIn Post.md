Day 17 — Majority Element 🗳️⚔️
Today’s problem introduced me to the Boyer–Moore Voting Algorithm.
The interesting part? No HashMap. No sorting. No extra array.
Just two variables:
candidate + count
The idea is simple:
🟢 Same element → increase the count
🔴 Different element → decrease the count
🔄 Count reaches 0 → choose a new candidate
The key insight I learned is that different elements effectively cancel each other out.
Since the majority element appears more than n/2 times, it cannot be completely cancelled. That’s why the final candidate is guaranteed to be the majority element.
Complexity
⏱️ Time: O(n)
💾 Space: O(1)
Another day, another algorithm added to the toolkit. 🚀
Day 17/30 🔥

🔗 GitHub: https://lnkd.in/dnke5uxq

#100DaysOfCode #DSA #Python #Algorithms #BoyerMoore #MajorityElement #CodingJourney #SoftwareEngineering #ProblemSolving #LearningInPublic

Link : https://lnkd.in/p/dHE5yEMx