## Arrays (Including Two Pointers, Sliding Window and other efficient array traversal approaches)

### Study Questions (To Learn Patterns)

#### **1. Two Sum**

- **Difficulty:** Easy
- **Description:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
- **Reason:** Introduces the common pattern of using a hash map to store complements for O(1) lookups, significantly optimizing search in an array.
- **Focus:** Understand how the hash map stores `(value, index)` pairs and how checking for `target - current_value` in the map leads to an efficient solution.

#### **2. Best Time to Buy and Sell Stock**

- **Difficulty:** Easy
- **Description:** You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
- **Reason:** Demonstrates a simple greedy approach or a variation of Kadane's algorithm by keeping track of the minimum price seen so far and calculating potential profit.
- **Focus:** Observe how iterating through the array once, maintaining the minimum buy price and maximum profit, solves the problem efficiently.

#### **3. Product of Array Except Self**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must write an algorithm that runs in O(n) time and without using the division operation.
- **Reason:** Excellent for understanding prefix and suffix products. The solution involves two passes to calculate products to the left and right of each element.
- **Focus:** Grasp the concept of constructing prefix product and suffix product arrays (or using constant space by iterating and updating a result array).

#### **4. Container With Most Water**

- **Difficulty:** Medium
- **Description:** You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water.
- **Reason:** Classic example of the two-pointer technique (opposite ends) where the search space is intelligently reduced.
- **Focus:** Understand why moving the pointer of the shorter line is the optimal strategy to potentially find a larger area.

#### **5. 3Sum**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.
- **Reason:** Combines sorting with the two-pointer technique (applied after fixing one element) to find triplets. Also highlights handling duplicates.
- **Focus:** Learn how sorting enables the two-pointer approach and how to efficiently skip duplicate elements to avoid redundant triplets.

#### **6. Maximum Subarray**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
- **Reason:** Introduces Kadane's algorithm, a dynamic programming approach (or greedy) for finding the maximum sum subarray in O(n) time.
- **Focus:** Understand the logic of maintaining `current_max_sum` and `global_max_sum`, and when to reset `current_max_sum`.

#### **7. Rotate Array**

- **Difficulty:** Medium
- **Description:** Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.
- **Reason:** Explores different in-place array manipulation techniques, such as using reversal or cyclic replacements.
- **Focus:** Analyze the time and space complexity of different rotation methods, especially the three-reversal technique for O(1) space.

#### **8. Merge Sorted Array**

- **Difficulty:** Easy
- **Description:** You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively. Merge `nums2` into `nums1` as one sorted array. The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`.
- **Reason:** Demonstrates the two-pointer technique for merging, often starting from the end of the arrays to utilize available space in `nums1`.
- **Focus:** Understand how to merge in-place by comparing elements from the end of both arrays and placing the larger one at the end of `nums1`.

#### **9. Minimum Size Subarray Sum**

- **Difficulty:** Medium
- **Description:** Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray of which the sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.
- **Reason:** A great example of a variable-size sliding window pattern. The window expands to meet a condition and shrinks to find the minimum size.
- **Focus:** Learn how to manage the window sum, expand the window by adding elements from the right, and shrink it from the left while the condition (sum >= target) holds.

#### **10. Find All Numbers Disappeared in an Array**

- **Difficulty:** Easy
- **Description:** Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.
- **Reason:** Showcases an in-place modification technique (cyclic sort idea or using index negation/marking) to find missing numbers in O(1) extra space (excluding the result array).
- **Focus:** Understand how to use the array itself as a hash map by marking visited numbers using their values as indices.

#### **11. Next Permutation**

- **Difficulty:** Medium
- **Description:** Implement the next lexicographical permutation of a given list of numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order). The replacement must be in-place and use only constant extra memory.
- **Reason:** A classic array manipulation problem requiring careful observation of patterns to find the next lexicographically greater permutation.
- **Focus:** Understand the algorithm: find the first decreasing element from the right, swap it with the smallest element to its right that is larger than it, and then reverse the suffix.

#### **12. Sort Colors (Dutch National Flag problem)**

- **Difficulty:** Medium
- **Description:** Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
- **Reason:** Illustrates the Dutch National Flag algorithm, a three-pointer approach (low, mid, high) for partitioning an array into three sections in a single pass.
- **Focus:** Understand the roles of the `low`, `mid`, and `high` pointers and the conditions under which they are moved or elements are swapped.

### Practice Questions (To Apply Patterns)

#### **1. Contains Duplicate**

- **Difficulty:** Easy
- **Description:** Given an integer array `nums`, return `true` if any value appears at least twice in the array, and `false` if every element is distinct.

#### **2. Squares of a Sorted Array**

- **Difficulty:** Easy
- **Description:** Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#### **3. Move Zeroes**

- **Difficulty:** Easy
- **Description:** Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

#### **4. Remove Duplicates from Sorted Array**

- **Difficulty:** Easy
- **Description:** Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and return the new length.

#### **5. Majority Element**

- **Difficulty:** Easy
- **Description:** Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times.

#### **6. Subarray Sum Equals K**

- **Difficulty:** Medium
- **Description:** Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

#### **7. Kth Largest Element in an Array**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` and an integer `k`, return the `k`-th largest element in the array.

#### **8. Find the Duplicate Number**

- **Difficulty:** Medium
- **Description:** Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive. There is only one repeated number in `nums`, return this repeated number.

#### **9. Search in Rotated Sorted Array**

- **Difficulty:** Medium
- **Description:** There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k`. Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or -1 if it is not in `nums`.

#### **10. Longest Consecutive Sequence**

- **Difficulty:** Medium
- **Description:** Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

#### **11. Merge Intervals**

- **Difficulty:** Medium
- **Description:** Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. (Also an Interval problem, but good for array sorting/manipulation)

#### **12. Task Scheduler**

- **Difficulty:** Medium
- **Description:** Given a characters array `tasks` representing tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle. However, there is a non-negative integer `n` that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks. Return the least number of units of times that the CPU will take to finish all the given tasks.

#### **13. Sliding Window Maximum**

- **Difficulty:** Hard
- **Description:** You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

#### **14. First Missing Positive**

- **Difficulty:** Hard
- **Description:** Given an unsorted integer array `nums`, return the smallest missing positive integer.

#### **15. Trapping Rain Water**

- **Difficulty:** Hard
- **Description:** Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

#### **16. Median of Two Sorted Arrays**

- **Difficulty:** Hard
- **Description:** Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

#### **17. Shortest Unsorted Continuous Subarray**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order. Return the shortest such subarray and output its length.

#### **18. Max Chunks To Make Sorted**

- **Difficulty:** Medium
- **Description:** You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`. We split `arr` into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array. Return the largest number of chunks we can make to sort the array.

#### **19. Find Peak Element**

- **Difficulty:** Medium
- **Description:** A peak element is an element that is strictly greater than its neighbors. Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

#### **20. Game of Life**

- **Difficulty:** Medium
- **Description:** According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970." Given a `m x n` grid `board` where each cell is either 0 (dead) or 1 (live), write a function to compute the next state (after one update) of the board according to the rules of the Game of Life. The update is done in-place.
