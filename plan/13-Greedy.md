## Greedy Algorithms

### Study Questions (To Learn Patterns)

#### **1. Best Time to Buy and Sell Stock**

- **Difficulty:** Easy
- **Description:** You are given an array `prices`. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
- **Reason:** A simple greedy choice: keep track of the minimum price seen so far and calculate the maximum profit if sold today.
- **Focus:** Understand that at each step, the decision (buy, sell, or wait) is made based on current information to maximize immediate or overall gain without needing to look back or exhaustively search.

#### **2. Jump Game**

- **Difficulty:** Medium
- **Description:** You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return `true` if you can reach the last index, or `false` otherwise.
- **Reason:** Greedy approach: at each step, try to reach the farthest possible position.
- **Focus:** Maintain a variable `max_reach` representing the farthest index reachable so far. Iterate through the array, updating `max_reach`. If the current index `i` exceeds `max_reach`, you're stuck.

#### **3. Gas Station**

- **Difficulty:** Medium
- **Description:** There are `n` gas stations along a circular route, where the amount of gas at the `i`-th station is `gas[i]`. You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i`-th station to its next `(i + 1)`-th station. You begin the journey with an empty tank at one of the gas stations. Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
- **Reason:** If the total gas is less than total cost, it's impossible. Otherwise, a solution exists. The greedy insight is that if you start at `A` and run out of gas before reaching `B`, then no station between `A` and `B` (inclusive of A) can be a starting point.
- **Focus:** Calculate `diff[i] = gas[i] - cost[i]`. If `sum(diff) < 0`, return -1. Iterate, maintaining `current_tank` and `start_index`. If `current_tank` drops below zero, try starting from the next station.

#### **4. Merge Intervals**

- **Difficulty:** Medium
- **Description:** Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
- **Reason:** Greedy choice after sorting: Sort intervals by start times. Iterate through sorted intervals, merging with the previous merged interval if they overlap.
- **Focus:** The sorting step is crucial. Then, compare the current interval's start with the previous merged interval's end.

#### **5. Task Scheduler**

- **Difficulty:** Medium
- **Description:** Given a characters array `tasks` and a cooldown `n`. Return the least number of units of times that the CPU will take to finish all given tasks.
- **Reason:** Greedy strategy: at each step, schedule the most frequent task that is not in cooldown. If no such task, be idle.
- **Focus:** Use a frequency map and a max-priority queue for task counts. A wait queue can manage cooldowns. The core idea is to prioritize tasks that are high in frequency to minimize idle slots.

#### **6. Minimum Number of Arrows to Burst Balloons**

- **Difficulty:** Medium
- **Description:** There are some spherical balloons spread in a 2D space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. An arrow shot vertically up from an x-coordinate bursts all balloons whose horizontal diameters include that x-coordinate. Find the minimum number of arrows that must be shot to burst all balloons.
- **Reason:** Sort balloons by their end coordinates. The greedy choice is to shoot an arrow at the end coordinate of the current balloon, as this position has the best chance of bursting subsequent overlapping balloons.
- **Focus:** After sorting by end points, iterate. If the current balloon's start is beyond the last arrow's position, a new arrow is needed. Update arrow position to current balloon's end.

#### **7. Non-overlapping Intervals**

- **Difficulty:** Medium
- **Description:** Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
- **Reason:** Similar to Activity Selection Problem. Sort intervals by end times. The greedy choice is to pick the interval that finishes earliest, as it leaves maximum room for other intervals.
- **Focus:** Sort by end times. Keep track of the end time of the last selected non-overlapping interval. Iterate; if the current interval's start is >= last end time, select it and update last end time. Count selected intervals; `total - selected` is the number to remove.

#### **8. Partition Labels**

- **Difficulty:** Medium
- **Description:** You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. Return a list of integers representing the size of these parts.
- **Reason:** Greedy approach. For each character, find its last occurrence in the string. Iterate through the string, maintaining the `end` of the current partition (max of last occurrences of characters seen so far in this partition). When the current index `i` reaches `end`, a partition is complete.
- **Focus:** First, precompute the last occurrence index for each character. Then, iterate through the string with `start` and `current_max_last_occurrence` pointers.

#### **9. Reorganize String**

- **Difficulty:** Medium
- **Description:** Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same. Return any possible rearrangement or `""`.
- **Reason:** Greedy: at each step, append the most frequent character that is different from the last appended character. A max-heap helps manage frequencies.
- **Focus:** Use a max-heap for `(frequency, char)`. Pop the most frequent. If it's different from the previous char, append it. If same, pop the second most frequent, append it, and put both back (if counts > 0).

#### **10. Candy**

- **Difficulty:** Hard
- **Description:** There are `N` children standing in a line. Each child is assigned a rating value. You are giving candies to these children subjected to the following requirements: Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. What is the minimum candies you must give?
- **Reason:** Two-pass greedy approach. First pass (left to right): ensure `ratings[i] > ratings[i-1] => candies[i] > candies[i-1]`. Second pass (right to left): ensure `ratings[i] > ratings[i+1] => candies[i] > candies[i+1]`. Take the max from both passes for each child.
- **Focus:** Initialize candies to 1 for everyone. The two passes correctly handle local greedy choices that combine to a global optimum.

### Practice Questions (To Apply Patterns)

#### **1. Assign Cookies**

- **Difficulty:** Easy
- **Description:** Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child `i` has a greed factor `g[i]`, and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign cookie `j` to child `i`, and child `i` will be content. Your goal is to maximize the number of content children and output the maximum number.

#### **2. Lemonade Change**

- **Difficulty:** Easy
- **Description:** At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time. Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5. Return `true` if you can provide every customer with the correct change, or `false` otherwise. You initially have no change.

#### **3. Best Time to Buy and Sell Stock II**

- **Difficulty:** Medium
- **Description:** You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`-th day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.

#### **4. Jump Game II**

- **Difficulty:** Medium
- **Description:** You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`. Each element `nums[i]` represents the maximum length of a forward jump from index `i`. Return the minimum number of jumps to reach `nums[n - 1]`.

#### **5. Remove K Digits**

- **Difficulty:** Medium
- **Description:** Given string `num` representing a non-negative integer, and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

#### **6. Broken Calculator**

- **Difficulty:** Medium
- **Description:** There is a broken calculator that has the integer `startValue` displayed on it. In one operation, you can multiply the displayed number by 2, or subtract 1 from the displayed number. Given two integers `startValue` and `target`, return the minimum number of operations to display `target` on the calculator.

#### **7. Bag of Tokens**

- **Difficulty:** Medium
- **Description:** You have an initial `power` and an initial `score` of 0. You also have a bag of `tokens` where `tokens[i]` is the value of the `i`-th token. Your goal is to maximize your total `score` by playing these tokens in any order. In one move, you can play an unplayed token in one of the two ways: face-up or face-down. If your current `power` is at least `tokens[i]`, you may play token `i` face-up, losing `tokens[i]` power and gaining 1 `score`. If your current `score` is at least 1, you may play token `i` face-down, gaining `tokens[i]` power and losing 1 `score`. Return the maximum `score` you can achieve.

#### **8. Two City Scheduling**

- **Difficulty:** Medium
- **Description:** A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCost_i, bCost_i]`, the cost of flying the `i`-th person to city A is `aCost_i`, and the cost of flying the `i`-th person to city B is `bCost_i`. Return the minimum cost to fly every person to a city such that exactly `n` people arrive in each city.

#### **9. Minimum Domino Rotations For Equal Row**

- **Difficulty:** Medium
- **Description:** In a row of dominoes, `tops[i]` and `bottoms[i]` represent the top and bottom halves of the `i`-th domino. A domino `(a, b)` can be rotated to be `(b, a)`. Return the minimum number of rotations so that all the values in `tops` are the same, or all the values in `bottoms` are the same. If it cannot be done, return -1.

#### **10. Boats to Save People**

- **Difficulty:** Medium
- **Description:** You are given an array `people` where `people[i]` is the weight of the `i`-th person, and an infinite number of boats where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`. Return the minimum number of boats to carry every given person.

#### **11. Maximum Units on a Truck**

- **Difficulty:** Easy
- **Description:** You are assigned to put some amount of boxes onto one truck. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxes_i, numberOfUnitsPerBox_i]`. You are also given an integer `truckSize`, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`. Return the maximum total number of units that can be put on the truck.

#### **12. Wiggle Subsequence**

- **Difficulty:** Medium
- **Description:** A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. Given an integer array `nums`, return the length of the longest wiggle subsequence of `nums`.

#### **13. Queue Reconstruction by Height**

- **Difficulty:** Medium
- **Description:** You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [h_i, k_i]` represents the `i`-th person of height `h_i` with `k_i` other people in front who have a height greater than or equal to `h_i`. Reconstruct and return the queue.

#### **14. Course Schedule III**

- **Difficulty:** Hard
- **Description:** There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where `courses[i] = [duration_i, lastDay_i]` indicates that the `i`-th course should be taken continuously for `duration_i` days and must be finished before or on `lastDay_i`. You will start on the 1st day. Return the maximum number of courses that you can take.

#### **15. Earliest Possible Day of Full Bloom**

- **Difficulty:** Hard
- **Description:** You have `n` flower seeds. Every seed must be planted. You are given two 0-indexed integer arrays `plantTime` and `growTime`, of length `n` each. `plantTime[i]` is the number of days it takes you to plant the `i`-th seed. `growTime[i]` is the number of days it takes the `i`-th seed to grow after it is planted. You can only plant one seed per day, but you can plant the seeds in any order. Return the earliest day that all seeds are blooming.

#### **16. Minimum Deletions to Make Character Frequencies Unique**

- **Difficulty:** Medium
- **Description:** A string `s` is called good if there are no two different characters in `s` that have the same frequency. Given a string `s`, return the minimum number of characters you need to delete to make `s` good.

#### **17. Car Pooling** (Greedy with sorting events)

- **Difficulty:** Medium
- **Description:** There is a car with `capacity` empty seats. The vehicle only drives east. You are given `capacity` and an array `trips` where `trip[i] = [numPassengers_i, from_i, to_i]`. Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or `false` otherwise.

#### **18. Patching Array**

- **Difficulty:** Hard
- **Description:** Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array such that any number in the range `[1, n]` (inclusive) can be formed by the sum of some elements in the array. Return the minimum number of patches required.

#### **19. Split Array into Consecutive Subsequences**

- **Difficulty:** Medium
- **Description:** You are given an integer array `nums` that is sorted in non-decreasing order. Determine if it is possible to split `nums` into one or more subsequences such that both of the following conditions are true: Each subsequence is a consecutive increasing sequence (i.e., each integer is exactly one more than the previous integer). All subsequences have a length of 3 or more. Return `true` if you can split `nums` according to the above conditions, or `false` otherwise.

#### **20. Find Latest Group of Size M**

- **Difficulty:** Medium
- **Description:** You are given an array `arr` which is a permutation of `[1, 2, ..., n]`. You are also given an integer `m`. You are going to perform `n` operations. In the `i`-th operation (1-indexed), you will mark the cell `arr[i]` as 1. Return the latest step at which there exists a group of ones of length `m`. A group of ones is a contiguous substring of 1s that is not extendable in either direction. If no such group exists, return -1.
