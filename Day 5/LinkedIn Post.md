🚀 Day 5 of My Daily Problem Solving Challenge

Today's challenge was Valid Anagram.

🧩 Problem Statement

Given two strings s and t, determine whether t is an anagram of s without using any built-in sorting functions.

Example:

"listen" & "silent" → ✅ True

"triangle" & "integral" → ✅ True

"hello" & "world" → ❌ False

💭 My Approach

I started with a straightforward idea: checking whether every character from the first string existed in the second. It worked for a few test cases, but I quickly realized it failed when duplicate characters were involved.

After debugging multiple edge cases, I shifted to a frequency-counting approach:

Count the occurrences of each character in the first string.

Decrease the count while traversing the second string.

Verify that every character count becomes zero.

🎯 Challenges I Faced

Mistakenly checking only for character presence instead of character frequency.

Assuming a sum of frequencies equal to zero meant the strings were anagrams.

Handling duplicate characters and edge cases correctly.

Learning why testing with edge cases is just as important as testing with happy-path examples.

📚 What I Learned

Choosing the right algorithm matters more than getting the first solution to work.

Edge cases expose flaws that normal test cases often hide.

Frequency maps (hash maps/dictionaries) are powerful for solving string problems efficiently.

Iterating, debugging, and refining an approach is where real learning happens.

This challenge was a great reminder that the first solution isn't always the correct one—but every iteration improves your problem-solving skills.

💻 GitHub: (https://lnkd.in/d9cAENvz)

#100DaysOfCode #ProblemSolving #Python #DataStructures #Algorithms #CodingChallenge #SoftwareEngineering #DeveloperJourney #LearningInPublic #Programming