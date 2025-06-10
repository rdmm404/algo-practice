## Dynamic Programming (1D & 2D)

### Study Questions (To Learn Patterns)

#### **1. Climbing Stairs**

- **Difficulty:** Easy
- **Description:** You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
- **Reason:** Classic introduction to DP. The number of ways to reach step `i` is the sum of ways to reach step `i-1` and step `i-2`. This is the Fibonacci sequence.
- **Focus:** Understand the recurrence relation: `dp[i] = dp[i-1] + dp[i-2]`. Identify base cases: `dp[0]=1` (or `dp[1]=1`), `dp[1]=1` (or `dp[2]=2`) depending on 0 or 1-based indexing. Learn both top-down (memoization) and bottom-up (tabulation) approaches.

#### **2. House Robber**

- **Difficulty:** Medium
- **Description:** You are a professional robber planning to rob houses along a street. Each house has a certain amount of money. If you rob two adjacent houses, the alarm will contact the police. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
- **Reason:** Introduces the choice pattern in 1D DP: at each house `i`, you either rob it (and can't rob `i-1`) or don't rob it (and take the max from `i-1`).
- **Focus:** Recurrence: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. `dp[i]` is the max money robbed up to house `i`. Base cases for `dp[0]` and `dp[1]`.

#### **3. Longest Increasing Subsequence**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, return the length of the longest strictly increasing subsequence.
- **Reason:** A common DP pattern where `dp[i]` represents the length of the LIS ending at index `i`.
- **Focus:** To calculate `dp[i]`, iterate `j` from `0` to `i-1`. If `nums[i] > nums[j]`, then `dp[i]` can be `dp[j] + 1`. Take the maximum of these possibilities. The final answer is the maximum value in the `dp` array. Also, be aware of the O(n log n) solution using patience sorting/binary search.

#### **4. Coin Change**

- **Difficulty:** Medium
- **Description:** You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
- **Reason:** Unbounded knapsack type problem. `dp[i]` is the minimum coins to make amount `i`.
- **Focus:** Recurrence: `dp[i] = min(dp[i - coin_value] + 1)` for all `coin_value` in `coins` such that `i - coin_value >= 0`. Initialize `dp` array with infinity, `dp[0] = 0`.

#### **5. Unique Paths**

- **Difficulty:** Medium
- **Description:** A robot is located at the top-left corner of an `m x n` grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?
- **Reason:** Basic 2D DP. `dp[i][j]` is the number of paths to reach cell `(i, j)`.
- **Focus:** Recurrence: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. Base cases: `dp[0][j] = 1` and `dp[i][0] = 1` (or handle boundaries).

#### **6. Edit Distance**

- **Difficulty:** Hard
- **Description:** Given two strings `word1` and `word2`, return the minimum number of operations (insert, delete, or replace a character) required to convert `word1` to `word2`.
- **Reason:** Classic 2D DP problem. `dp[i][j]` is the edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`.
- **Focus:** If `word1[i-1] == word2[j-1]`, then `dp[i][j] = dp[i-1][j-1]`. Otherwise, `dp[i][j] = 1 + min(dp[i-1][j] (delete), dp[i][j-1] (insert), dp[i-1][j-1] (replace))`. Base cases for empty strings.

#### **7. Longest Common Subsequence**

- **Difficulty:** Medium
- **Description:** Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.
- **Reason:** Fundamental 2D DP. `dp[i][j]` is the LCS of `text1[0...i-1]` and `text2[0...j-1]`.
- **Focus:** If `text1[i-1] == text2[j-1]`, then `dp[i][j] = 1 + dp[i-1][j-1]`. Else, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

#### **8. Word Break**

- **Difficulty:** Medium
- **Description:** Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
- **Reason:** 1D DP. `dp[i]` is true if the prefix `s[0...i-1]` can be segmented.
- **Focus:** To calculate `dp[i]`, iterate `j` from `0` to `i-1`. If `dp[j]` is true and `s[j...i-1]` is in `wordDict`, then `dp[i]` is true. `dp[0]` is true (empty string).

#### **9. Decode Ways**

- **Difficulty:** Medium
- **Description:** A message containing letters from A-Z is being encoded to numbers using the mapping A->1, B->2, ..., Z->26. Given a string `s` containing only digits, return the number of ways to decode it.
- **Reason:** 1D DP. `dp[i]` is the number of ways to decode the prefix `s[0...i-1]`.
- **Focus:** `dp[i]` can be formed from `dp[i-1]` (if `s[i-1]` is a valid single digit decode) and/or `dp[i-2]` (if `s[i-2...i-1]` is a valid two-digit decode). Handle leading zeros carefully.

#### **10. Maximum Subarray** (DP approach)

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
- **Reason:** Kadane's algorithm is a greedy DP. `dp[i]` is the maximum subarray sum ending at index `i`.
- **Focus:** `dp[i] = max(nums[i], nums[i] + dp[i-1])`. The answer is the maximum value in the `dp` array.

#### **11. Palindromic Substrings**

- **Difficulty:** Medium
- **Description:** Given a string `s`, return the number of palindromic substrings in it.
- **Reason:** 2D DP. `dp[i][j]` is true if `s[i...j]` is a palindrome.
- **Focus:** If `s[i] == s[j]`, then `dp[i][j]` depends on `dp[i+1][j-1]` (for length > 2) or is true (for length 1 or 2). Iterate by increasing substring length. Count true values in `dp`.

#### **12. Best Time to Buy and Sell Stock with Cooldown**

- **Difficulty:** Medium
- **Description:** You are given an array `prices`. Design an algorithm to find the maximum profit. You may complete as many transactions as you like (buy one and sell one share of the stock), but you need to observe a cooldown period of one day after selling. You may not engage in multiple transactions simultaneously.
- **Reason:** State machine DP. Define states like `s0` (can buy), `s1` (can sell/holding), `s2` (cooldown).
- **Focus:** `s0[i] = max(s0[i-1], s2[i-1])` (rest or end of cooldown). `s1[i] = max(s1[i-1], s0[i-1] - prices[i])` (rest or buy). `s2[i] = s1[i-1] + prices[i]` (sell).

#### **13. Partition Equal Subset Sum**

- **Difficulty:** Medium
- **Description:** Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
- **Reason:** 0/1 Knapsack type problem. Check if a subset sum equal to `totalSum / 2` can be formed. `dp[i]` is true if sum `i` can be formed.
- **Focus:** If `totalSum` is odd, return false. Target sum is `totalSum / 2`. `dp[j] = dp[j] || dp[j - num]` for each `num` in `nums`. Iterate `j` downwards to use each number once.

#### **14. Minimum Path Sum**

- **Difficulty:** Medium
- **Description:** Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.
- **Reason:** 2D DP, similar to Unique Paths but minimizing sum. `dp[i][j]` is the min sum to reach `(i,j)`.
- **Focus:** `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`. Handle boundary conditions for the first row and first column.

#### **15. Regular Expression Matching**

- **Difficulty:** Hard
- **Description:** Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*`.
- **Reason:** Complex 2D DP. `dp[i][j]` is true if `s[0...i-1]` matches `p[0...j-1]`.
- **Focus:** Handle cases for `p[j-1]` being a normal char, `.`, or `*`. If `p[j-1]` is `*`: it can match zero occurrences of `p[j-2]` (`dp[i][j-2]`) or one/more occurrences (`s[i-1]` matches `p[j-2]` and `dp[i-1][j]`).

### Practice Questions (To Apply Patterns)

#### **1. Min Cost Climbing Stairs**

- **Difficulty:** Easy
- **Description:** You are given an integer array `cost` where `cost[i]` is the cost of `i`-th step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor.

#### **2. House Robber II**

- **Difficulty:** Medium
- **Description:** You are a professional robber. Houses are arranged in a circle. This means the first house is the neighbor of the last one. Otherwise, the rules are the same as House Robber I. Return the maximum amount of money you can rob.

#### **3. Triangle**

- **Difficulty:** Medium
- **Description:** Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number of the row below.

#### **4. Maximum Product Subarray**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

#### **5. Longest Palindromic Substring** (DP approach)

- **Difficulty:** Medium
- **Description:** Given a string `s`, return the longest palindromic substring in `s`.

#### **6. Unique Paths II**

- **Difficulty:** Medium
- **Description:** You are given an `m x n` integer array `grid`. There is a robot on an `m x n` grid. The robot is initially located at the top-left corner. The robot tries to move to the bottom-right corner. The robot can only move either down or right at any point in time. An obstacle is marked as 1 and an empty space is marked as 0. Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

#### **7. Combination Sum IV**

- **Difficulty:** Medium
- **Description:** Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`. The answer can be very large, so return it modulo \(10^9 + 7\). (Order matters, so it's permutations of sums).

#### **8. Perfect Squares**

- **Difficulty:** Medium
- **Description:** Given an integer `n`, return the least number of perfect square numbers that sum to `n`.

#### **9. Best Time to Buy and Sell Stock** (DP approach)

- **Difficulty:** Easy
- **Description:** You are given an array `prices`. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit.

#### **10. Interleaving String**

- **Difficulty:** Medium
- **Description:** Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

#### **11. Maximal Square**

- **Difficulty:** Medium
- **Description:** Given an `m x n` binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

#### **12. Target Sum**

- **Difficulty:** Medium
- **Description:** You are given an integer array `nums` and an integer `target`. You want to build an expression out of `nums` by adding one of the symbols `+` and `-` before each integer in `nums` and then concatenate all the integers. Return the number of different expressions that you can build, which evaluates to `target`.

#### **13. Delete Operation for Two Strings**

- **Difficulty:** Medium
- **Description:** Given two strings `word1` and `word2`, return the minimum number of steps required to make `word1` and `word2` the same. In one step, you can delete exactly one character in either string.

#### **14. Coin Change II**

- **Difficulty:** Medium
- **Description:** You are given an integer array `coins` representing coins of different denominations and an integer `amount`. Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0. (This is about combinations, order doesn't matter).

#### **15. Wildcard Matching**

- **Difficulty:** Hard
- **Description:** Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `?` and `*`. `?` matches any single character. `*` matches any sequence of characters (including the empty sequence).

#### **16. Burst Balloons**

- **Difficulty:** Hard
- **Description:** You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon has a number painted on it represented by an array `nums`. You are asked to burst all the balloons. If you burst the `i`-th balloon, you will get `nums[left] * nums[i] * nums[right]` coins. Here `left` and `right` are adjacent indices of `i`. After the burst, `left` and `right` become adjacent. Return the maximum coins you can collect by bursting the balloons wisely.

#### **17. Minimum Falling Path Sum**

- **Difficulty:** Medium
- **Description:** Given an `n x n` array of integers `matrix`, return the minimum sum of any falling path through `matrix`. A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right.

#### **18. Knight Dialer**

- **Difficulty:** Medium
- **Description:** The chess knight has a unique movement pattern. A phone keypad has numbers on it. Given an integer `n`, return how many distinct phone numbers of length `n` we can dial. You are allowed to place the knight on any numeric cell initially and then you should perform `n - 1` jumps to dial a number of length `n`. All jumps should be valid knight jumps.

#### **19. Number of Longest Increasing Subsequence**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, return the number of longest increasing subsequences.

#### **20. Best Time to Buy and Sell Stock III (at most two transactions)**

- **Difficulty:** Hard
- **Description:** You are given an array `prices`. You may complete at most two transactions. You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again). Return the maximum profit you can achieve.
