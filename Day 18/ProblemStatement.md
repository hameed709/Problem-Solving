Day 18 — Problem: Best Time to Buy and Sell Stock

Problem Statement

You are given an array prices where prices[i] represents the price of a stock on the ith day.

You want to buy the stock on one day and sell it on a later day to maximize your profit.

Return the maximum profit you can achieve.

If no profit is possible, return 0.

Example 1

Input:
[7,1,5,3,6,4]

Output:
5

Explanation:
Buy on day 2 at price 1 and sell on day 5 at price 6.

Profit = 6 - 1 = 5

Example 2

Input:
[7,6,4,3,1]

Output:
0

Explanation:
The price keeps decreasing, so no profitable transaction is possible.

Example 3

Input:
[2,4,1,7]

Output:
6

Explanation:
Buy at price 1 and sell at price 7.

Profit = 7 - 1 = 6

Example 4

Input:
[1,2,3,4,5]

Output:
4

Explanation:
Buy at price 1 and sell at price 5.

Profit = 5 - 1 = 4

Constraints:

- 1 <= prices.length <= 100000
- 0 <= prices[i] <= 100000

Challenge:

- Solve the problem in O(n) time.
- Do not use nested loops.
- You can only buy and sell once.
- You must buy before you sell.
- Try using a single pass through the array.
- Track the minimum price seen so far and the maximum profit.