Day 28 — Find Minimum in Rotated Sorted Array 🔍
Today’s problem was Find Minimum in Rotated Sorted Array.
Given a sorted array that has been rotated at an unknown position, the goal is to find the minimum element in O(log n) time.
💡 Approach
I used Binary Search.
The key comparison is:
arr[mid] vs arr[high]
If arr[mid] > arr[high], the minimum must be on the right side, so:
low = mid + 1
Otherwise, the minimum is at mid or on the left side, so:
high = mid
The search continues until low == high, which gives the index of the minimum element.
Example
Input:
[4,5,6,7,0,1,2]
Output:
0
Complexity
⏱️ Time: O(log n)
💾 Space: O(1)
No min(), no sorting, and no scanning through the entire array.
This problem was a good reminder that in rotated-array problems, the real skill is identifying which half can safely be eliminated.

💻 GitHub Repository: https://lnkd.in/ddHFWHn6

#Day28 #100DaysOfCode #DSA #DataStructures #Algorithms #BinarySearch #Python #ProblemSolving #CodingJourney #LeetCode

Link : https://lnkd.in/p/dX5cZcBS