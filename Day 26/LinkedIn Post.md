Day 26 — Container With Most Water 🌊
Today’s problem was Container With Most Water.
Given an array of heights, the goal is to choose two lines that form a container capable of holding the maximum amount of water.
💡 Key Insight
A brute-force approach would check every possible pair, resulting in O(n²) time.
Instead, I used the Two Pointer technique:
Start with one pointer at the beginning.
Start another pointer at the end.
Calculate the current area.
Move the pointer with the smaller height.
Continue until both pointers meet.
The important formula is:
Area = min(left height, right height) × width
The reason for moving the smaller pointer is simple: the shorter line limits the container's height. Moving the taller line only reduces the width without giving us a chance to overcome that limitation.
📌 Example
[1,8,6,2,5,4,8,3,7]

Maximum Area = 49
The lines at indices 1 and 8 give:
Width  = 8 - 1 = 7
Height = min(8, 7) = 7

Area = 7 × 7 = 49
⚡ Complexity
Time: O(n)
Space: O(1)
This problem was a good reminder that optimizing an algorithm isn't just about writing less code — it's about understanding why certain possibilities can safely be eliminated.
Another problem solved. 🚀
Day 26 ✅

💻 GitHub Repository: https://lnkd.in/diTP5AJU

#100DaysOfCode #Python #DSA #DataStructures #Algorithms #TwoPointers #ProblemSolving #CodingJourney #SoftwareEngineering #LearningInPublic

Link : https://lnkd.in/p/dp4NDpwr