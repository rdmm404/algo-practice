## Binary Search

### Study Questions (To Learn Patterns)

#### **1. Binary Search**

- **Difficulty:** Easy
- **Description:** Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.
- **Reason:** The foundational problem. It establishes the core logic of binary search: repeatedly dividing the search interval in half.
- **Focus:** Understand the three main components: `low`, `high`, `mid` pointers. Pay close attention to the loop condition (`low <= high` vs `low < high`) and how `low` and `high` are updated. Consider integer overflow for `mid = (low + high) / 2`.

#### **2. Search a 2D Matrix**

- **Difficulty:** Medium
- **Description:** Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties: Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.
- **Reason:** Shows how binary search can be applied to a 2D structure that can be "flattened" conceptually into a 1D sorted array.
- **Focus:** Learn to map a 1D index (from binary search) to 2D coordinates (`row = mid / cols`, `col = mid % cols`) and vice-versa.

#### **3. Find Minimum in Rotated Sorted Array**

- **Difficulty:** Medium
- **Description:** Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.
- **Reason:** A classic variation where the standard binary search condition needs modification. The comparison is often between `nums[mid]` and `nums[high]` (or `nums[low]`) to decide which part of the array is sorted and where the pivot/minimum lies.
- **Focus:** Understand how the rotation creates two sorted subarrays. The key is to identify which half `mid` falls into and how that informs the search space reduction.

#### **4. Search in Rotated Sorted Array**

- **Difficulty:** Medium
- **Description:** There is an integer array `nums` sorted in ascending order (with distinct values), possibly rotated at an unknown pivot. Given `nums` and `target`, return the index of `target` if it is in `nums`, or -1 otherwise.
- **Reason:** Combines finding a pivot (or identifying the sorted half) with searching for the target. Requires careful conditional logic.
- **Focus:** Determine if `nums[mid]` is in the left sorted portion or right sorted portion. Then, check if the `target` lies within that sorted portion to narrow down the search.

#### **5. Find First and Last Position of Element in Sorted Array**

- **Difficulty:** Medium
- **Description:** Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If `target` is not found in the array, return `[-1, -1]`.
- **Reason:** Demonstrates using binary search twice (or a modified binary search) to find the leftmost and rightmost occurrences of an element.
- **Focus:** For finding the first occurrence, when `nums[mid] == target`, try to search further left (`high = mid - 1`). For the last occurrence, try to search further right (`low = mid + 1`).

#### **6. Median of Two Sorted Arrays**

- **Difficulty:** Hard
- **Description:** Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
- **Reason:** An advanced binary search application. The search is performed on the possible partitions of the smaller array to find the correct cut that divides all elements into two halves of equal length with left_half_max <= right_half_min.
- **Focus:** Understand the partitioning logic. The binary search is on the number of elements to take from the first array. The conditions for a valid partition (e.g., `maxLeftX <= minRightY` and `maxLeftY <= minRightX`) are crucial.

#### **7. Koko Eating Bananas**

- **Difficulty:** Medium
- **Description:** Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours. Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour. Return the minimum integer `k` such that she can eat all the bananas within `h` hours.
- **Reason:** "Binary search on answer." The possible values of `k` (eating speed) form a search space. For a given `k`, we can check if it's possible to eat all bananas in `h` hours.
- **Focus:** Identify the search range for `k` (e.g., from 1 to `max(piles)`). The `check(k)` function calculates the total hours needed for a given speed `k`. Adjust `low` and `high` based on whether `check(k)` meets the `h` hour constraint.

#### **8. Find Peak Element**

- **Difficulty:** Medium
- **Description:** A peak element is an element that is strictly greater than its neighbors. Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine `nums[-1] = nums[n] = -∞`.
- **Reason:** Binary search can be applied by comparing `nums[mid]` with `nums[mid+1]`. If `nums[mid] < nums[mid+1]`, a peak must exist on the right side (including `mid+1`). Otherwise, a peak must exist on the left side (including `mid`).
- **Focus:** Understand the logic for narrowing the search space. The condition `nums[mid] > nums[mid+1]` implies `mid` could be a peak or a peak is to its left. `nums[mid] < nums[mid+1]` implies a peak is to its right.

#### **9. Sqrt(x)**

- **Difficulty:** Easy
- **Description:** Given a non-negative integer `x`, compute and return the square root of `x`. Since the return type is an integer, the decimal part is truncated, and only the integer part of the result is returned.
- **Reason:** A straightforward application of binary search to find an integer `m` such that `m*m <= x`.
- **Focus:** The search space is `[0, x]`. For a `mid` value, check `mid*mid`. If it's equal to `x`, `mid` is the answer. If `mid*mid < x`, `mid` could be the answer, so store it and search in `[mid+1, high]`. If `mid*mid > x`, search in `[low, mid-1]`.

#### **10. Capacity To Ship Packages Within D Days**

- **Difficulty:** Medium
- **Description:** A conveyor belt has packages that must be shipped from one port to another within `D` days. The `i`-th package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship. Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `D` days.
- **Reason:** Another "binary search on answer" problem. The search space is the possible capacities of the ship.
- **Focus:** Determine the search range for capacity (e.g., `max(weights)` to `sum(weights)`). The `check(capacity)` function simulates loading packages and counts the number of days required. Adjust `low` and `high` based on this count.

### Practice Questions (To Apply Patterns)

#### **1. Guess Number Higher or Lower**

- **Difficulty:** Easy
- **Description:** We are playing the Guess Game. The game is as follows: I pick a number from 1 to `n`. You have to guess which number I picked. Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess. You call a pre-defined API `guess(int num)`.

#### **2. Search Insert Position**

- **Difficulty:** Easy
- **Description:** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#### **3. Arranging Coins**

- **Difficulty:** Easy
- **Description:** You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k` rows where the `i`-th row has exactly `i` coins. The last row of the staircase may be incomplete. Given `n`, return the number of complete rows of the staircase you will build.

#### **4. Valid Perfect Square**

- **Difficulty:** Easy
- **Description:** Given a positive integer `num`, write a function which returns `True` if `num` is a perfect square else `False`. Do not use any built-in library function such as `sqrt`.

#### **5. Find Smallest Letter Greater Than Target**

- **Difficulty:** Easy
- **Description:** You are given an array of characters `letters` that is sorted in non-decreasing order, and a character `target`. There are at least two different characters in `letters`. Return the smallest character in `letters` that is lexicographically greater than `target`. If such a character does not exist, return the first character in `letters`.

#### **6. Peak Index in a Mountain Array**

- **Difficulty:** Medium
- **Description:** An array `arr` is a mountain if the following properties hold: `arr.length >= 3` and there exists some `i` with `0 < i < arr.length - 1` such that `arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[arr.length - 1]`. Given a mountain array `arr`, return the index `i`.

#### **7. Search in Rotated Sorted Array II**

- **Difficulty:** Medium
- **Description:** There is an integer array `nums` sorted in non-decreasing order (not necessarily with distinct values). Before being passed to your function, `nums` is rotated at an unknown pivot index `k`. Given the array `nums` after the rotation and an integer `target`, return `true` if `target` is in `nums`, or `false` otherwise.

#### **8. Find Minimum in Rotated Sorted Array II**

- **Difficulty:** Hard
- **Description:** Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. The array may contain duplicates. Given the sorted rotated array `nums`, return the minimum element of this array.

#### **9. Time Based Key-Value Store**

- **Difficulty:** Medium
- **Description:** Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

#### **10. Minimum Speed to Arrive on Time**

- **Difficulty:** Medium
- **Description:** You are given a floating-point number `hour`, representing the amount of time you have to reach the office. To commute to the office, you must take `n` trains in sequential order. You are also given an integer array `dist` of length `n`, where `dist[i]` describes the distance (in kilometers) of the `i`-th train ride. Each train can only depart at an integer hour, so you may need to wait in between each train ride. Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible.

#### **11. Split Array Largest Sum**

- **Difficulty:** Hard
- **Description:** Given an array `nums` which consists of non-negative integers and an integer `m`, you can split the array into `m` non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these `m` subarrays.

#### **12. Find K-th Smallest Pair Distance**

- **Difficulty:** Hard
- **Description:** The distance of a pair of integers `a` and `b` is defined as the absolute difference between `a` and `b`. Given an integer array `nums` and an integer `k`, return the `k`-th smallest distance among all the pairs `nums[i]` and `nums[j]` where `0 <= i < j < nums.length`.

#### **13. Search a 2D Matrix II**

- **Difficulty:** Medium
- **Description:** Write an efficient algorithm that searches for a `target` value in an `m x n` integer matrix. The matrix has the following properties: Integers in each row are sorted in ascending from left to right. Integers in each column are sorted in ascending from top to bottom.

#### **14. H-Index II**

- **Difficulty:** Medium
- **Description:** Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`-th paper, return compute the researcher's h-index. The `citations` array is sorted in ascending order.

#### **15. Divide Two Integers**

- **Difficulty:** Medium
- **Description:** Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator. Return the quotient after dividing `dividend` by `divisor`.

#### **16. Find Right Interval**

- **Difficulty:** Medium
- **Description:** You are given an array of `intervals`, where `intervals[i] = [start_i, end_i]` and `intervals[i]` is unique. The right interval for an interval `i` is an interval `j` such that `start_j >= end_i` and `start_j` is minimized. Return an array of right interval indices for each interval `i`. If no such interval exists, store -1.

#### **17. Smallest Divisor Given a Threshold**

- **Difficulty:** Medium
- **Description:** Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer `divisor`, divide all the array elements by `divisor`, and sum the results of the division. Find the smallest `divisor` such that the result mentioned above is less than or equal to `threshold`.

#### **18. Minimum Number of Days to Make m Bouquets**

- **Difficulty:** Medium
- **Description:** You are given an integer array `bloomDay`, an integer `m` and an integer `k`. You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden. The garden consists of `n` flowers, the `i`-th flower will bloom in `bloomDay[i]` and then can be used in exactly one bouquet. Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets, return -1.

#### **19. Maximum Value at a Given Index in a Bounded Array**

- **Difficulty:** Medium
- **Description:** You are given three positive integers: `n`, `index`, and `maxSum`. You want to construct an array `nums` (0-indexed) that satisfies the following conditions: `nums.length == n`, `nums[i]` is a positive integer, `abs(nums[i] - nums[i+1]) <= 1`, the sum of all elements in `nums` does not exceed `maxSum`, and `nums[index]` is maximized. Return `nums[index]`.

#### **20. Heaters**

- **Difficulty:** Medium
- **Description:** Winter is coming! Your first job during the contest is to design a standard heater with a fixed warm radius to warm all the houses. Now, you are given positions of `houses` and `heaters` on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.
