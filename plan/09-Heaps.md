## Heaps (Priority Queues)

### Study Questions (To Learn Patterns)

#### **1. Kth Largest Element in an Array**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` and an integer `k`, return the `k`-th largest element in the array.
- **Reason:** Classic application of a min-heap of size `k`. The heap stores the `k` largest elements encountered so far.
- **Focus:** Understand why a min-heap is used. When iterating through numbers, if a number is larger than the heap's top (smallest among the k largest), pop the top and push the current number. The final top is the k-th largest.

#### **2. Top K Frequent Elements**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.
- **Reason:** Combines frequency counting (using a HashMap) with a min-heap to find the top `k` frequent elements. The heap stores pairs of `(frequency, element)`.
- **Focus:** First, count frequencies. Then, iterate through the frequency map. Use a min-heap of size `k` ordered by frequency. If an element's frequency is greater than the heap's top frequency, adjust the heap.

#### **3. Merge K Sorted Lists**

- **Difficulty:** Hard
- **Description:** You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.
- **Reason:** A min-heap is perfect for keeping track of the smallest current element among all `k` lists.
- **Focus:** Store `(value, list_index, node_reference)` or just `(value, node_reference)` in the min-heap (if nodes are comparable or a custom comparator is used). Extract min, add to result, and if the extracted node has a next, add it to the heap.

#### **4. Find Median from Data Stream**

- **Difficulty:** Hard
- **Description:** The median is the middle value in an ordered integer list. Design a data structure that supports adding new numbers and finding the median of all elements seen so far.
- **Reason:** The two-heap approach (a max-heap for the lower half and a min-heap for the upper half) is a canonical solution for this.
- **Focus:** Maintain two heaps such that their sizes differ by at most 1. The max-heap stores the smaller half of numbers, and the min-heap stores the larger half. The median is either the top of the larger heap (if sizes differ) or the average of tops (if sizes are equal). Balance the heaps after each insertion.

#### **5. K Closest Points to Origin**

- **Difficulty:** Medium
- **Description:** Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.
- **Reason:** Use a max-heap of size `k` to store the `k` closest points found so far. The heap is ordered by distance from the origin.
- **Focus:** Calculate the squared Euclidean distance to avoid `sqrt`. If the current point's distance is less than the heap's top (largest distance among the k closest), pop and push the current point.

#### **6. Task Scheduler**

- **Difficulty:** Medium
- **Description:** Given a characters array `tasks` representing tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle. However, there is a non-negative integer `n` that represents the cooldown period between two same tasks. Return the least number of units of times that the CPU will take to finish all the given tasks.
- **Reason:** A greedy approach using a max-heap (for task frequencies) and a queue (for tasks in cooldown) is common.
- **Focus:** Use a max-heap to pick the most frequent available task. After processing, if it still has counts, put it in a temporary list/wait queue with its next available time. Decrement cooldowns in the wait queue. Add tasks back to the heap when their cooldown is over.

#### **7. Reorganize String**

- **Difficulty:** Medium
- **Description:** Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same. Return any possible rearrangement of `s` or return `""` if not possible.
- **Reason:** A greedy approach using a max-heap based on character frequencies. Always try to append the most frequent character that is different from the previously appended character.
- **Focus:** Build a frequency map. Use a max-heap to store `(count, char)`. In each step, extract the top. If it's different from the last char added to result, append it, decrement its count, and add back to heap if count > 0. If it's same, extract the second top, use it, and put both back.

#### **8. Meeting Rooms II**

- **Difficulty:** Medium
- **Description:** Given an array of meeting time `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.
- **Reason:** Sort intervals by start times. Use a min-heap to store the end times of meetings currently in progress. This heap represents the rooms occupied and when they become free.
- **Focus:** Iterate through sorted intervals. If the current meeting's start time is >= heap's top (earliest end time), it means a room is free; pop from heap. Push the current meeting's end time to the heap. The heap's max size during this process is the answer.

#### **9. Sliding Window Median**

- **Difficulty:** Hard
- **Description:** The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values. Given an array `nums` and an integer `k`, return the median of the sliding window.
- **Reason:** Extends the "Find Median from Data Stream" idea to a sliding window. Requires efficient addition and removal from the two heaps.
- **Focus:** Maintain two heaps (max-heap for left, min-heap for right). When the window slides, add the new element and remove the outgoing element. Removal from a heap is tricky (usually O(log n) if direct access or O(n) to find and remove, but can be optimized with lazy removal or by storing indices). Rebalance heaps.

#### **10. The Skyline Problem**

- **Difficulty:** Hard
- **Description:** A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
- **Reason:** A sweep-line algorithm combined with a max-heap (or sorted data structure like `TreeMap` in Java, `multiset` in C++) to keep track of the current maximum height of active buildings.
- **Focus:** Represent buildings as start and end events `(coordinate, height, type)`. Sort these events. When processing events, if it's a start event, add height to max-heap. If it's an end event, remove height. If current max height in heap changes, it's a critical point for the skyline.

### Practice Questions (To Apply Patterns)

#### **1. Last Stone Weight**

- **Difficulty:** Easy
- **Description:** You are given an array of integers `stones` where `stones[i]` is the weight of the `i`-th stone. We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Rules for smashing are given. Return the weight of the last remaining stone, or 0 if no stones remain.

#### **2. Kth Smallest Element in a Sorted Matrix**

- **Difficulty:** Medium
- **Description:** Given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the `k`-th smallest element in the matrix.

#### **3. Sort Characters By Frequency**

- **Difficulty:** Medium
- **Description:** Given a string `s`, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

#### **4. Network Delay Time**

- **Difficulty:** Medium
- **Description:** You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target. We will send a signal from a given node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. If it is impossible for all `n` nodes to receive the signal, return -1. (Dijkstra's algorithm often uses a min-priority queue).

#### **5. Ugly Number II**

- **Difficulty:** Medium
- **Description:** An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. Given an integer `n`, return the `n`-th ugly number.

#### **6. Find K Pairs with Smallest Sums**

- **Difficulty:** Medium
- **Description:** You are given two integer arrays `nums1` and `nums2` sorted in ascending order and an integer `k`. Define a pair `(u, v)` which consists of one element from the first array and one element from the second array. Return the `k` pairs `(u1, v1), (u2, v2), ..., (uk, vk)` with the smallest sums.

#### **7. Path With Minimum Effort**

- **Difficulty:** Medium
- **Description:** You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)`. You can move up, down, left, or right, and you wish to find a route that requires the minimum effort. A route's effort is the maximum absolute difference in heights between two consecutive cells of the route. Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

#### **8. Furthest Building You Can Reach**

- **Difficulty:** Medium
- **Description:** You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`. You start your journey from building 0 and move to the next building by possibly using bricks or ladders. While moving from building `i` to building `i+1` (0-indexed), if `heights[i] >= heights[i+1]`, you do not need a ladder or bricks. If `heights[i] < heights[i+1]`, you can either use one ladder or `(heights[i+1] - heights[i])` bricks. Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

#### **9. Process Tasks Using Servers**

- **Difficulty:** Medium
- **Description:** You are given two 0-indexed integer arrays, `servers` and `tasks`, of lengths `n` and `m` respectively. `servers[i]` is the weight of the `i`-th server, and `tasks[j]` is the time needed to process the `j`-th task. You are also given an integer `k`. You assign tasks to servers starting from the 0-th task. When the `j`-th task arrives, it is assigned to a server that is free and has the smallest weight. If several servers are free and have the same smallest weight, it is assigned to the server with the smallest index. If no server is free, the task waits in a queue until a server becomes free. Return an array `ans` of length `m`, where `ans[j]` is the index of the server the `j`-th task will be assigned to.

#### **10. Minimum Cost to Connect Sticks**

- **Difficulty:** Medium
- **Description:** You have some number of sticks with positive integer lengths. These lengths are given as an array `sticks`, where `sticks[i]` is the length of the `i`-th stick. You can connect any two sticks of lengths `X` and `Y` into one stick by paying a cost of `X + Y`. This results in a new stick of length `X + Y`. Your goal is to connect all the sticks into one stick with minimum cost. Return the minimum cost.

#### **11. IPO**

- **Difficulty:** Hard
- **Description:** Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. You are given `n` projects where the `i`-th project has a pure profit `profits[i]` and a minimum capital of `capital[i]` is needed to start it. Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital. Pick a list of at most `k` distinct projects from given projects to maximize your final capital, and return the final maximized capital.

#### **12. Swim in Rising Water**

- **Difficulty:** Hard
- **Description:** You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`. The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim. You start at the top-left square `(0, 0)`. Return the least time until you can reach the bottom-right square `(n - 1, n - 1)`.

#### **13. Design Search Autocomplete System**

- **Difficulty:** Hard
- **Description:** Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

#### **14. Employee Free Time**

- **Difficulty:** Hard
- **Description:** We are given a list `schedule` of employees, which represents the working time for each employee. Each employee has a list of non-overlapping `Intervals`, and these intervals are in sorted order. Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

#### **15. Reduce Array Size to The Half**

- **Difficulty:** Medium
- **Description:** You are given an integer array `arr`. You can choose a set of integers and remove all the occurrences of these integers in the array. Return the minimum size of the set so that at least half of the integers of the array are removed.

#### **16. Maximum Performance of a Team**

- **Difficulty:** Hard
- **Description:** You are given two integers `n` and `k` and two integer arrays `speed` and `efficiency` both of length `n`. There are `n` engineers. `speed[i]` and `efficiency[i]` represent the speed and efficiency of the `i`-th engineer respectively. Choose at most `k` different engineers to form a team with the maximum performance. The performance of a team is the sum of their speeds multiplied by the minimum efficiency among them. Return the maximum performance of a team.

#### **17. Single-Threaded CPU**

- **Difficulty:** Medium
- **Description:** You are given `n` tasks, represented by a 2D integer array `tasks` where `tasks[i] = [enqueueTime_i, processingTime_i]` means that the `i`-th task will be available to process at `enqueueTime_i` and will take `processingTime_i` to process. You have a single-threaded CPU that can process at most one task at a time and will act as follows: If the CPU is idle and there are available tasks, the CPU will choose the task with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index. Once a task is started, the CPU will process the entire task without stopping. The CPU can finish a task then start a new one instantly. Return the order in which the CPU will process the tasks.

#### **18. Minimum Number of Refueling Stops**

- **Difficulty:** Hard
- **Description:** A car travels from a starting position to a destination which is `target` miles east of the starting position. Along the way, there are gas stations. You are given an array `stations` where `stations[i] = [position_i, fuel_i]` indicates that the `i`-th gas station is `position_i` miles east of the starting position and has `fuel_i` liters of gas. The car starts with an infinite tank of gas, which is initially empty. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car. Return the minimum number of refueling stops the car must make to reach its destination. If it cannot reach the destination, return -1.

#### **19. Car Pooling**

- **Difficulty:** Medium
- **Description:** There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west). You are given the integer `capacity` and an array `trips` where `trip[i] = [numPassengers_i, from_i, to_i]` indicates that the `i`-th trip has `numPassengers_i` passengers and the locations to pick them up and drop them off are `from_i` and `to_i` respectively. The locations are given as the number of kilometers due east from the car's initial location. Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or `false` otherwise. (Can be solved with a min-heap of drop-off events or by processing events sorted by location).

#### **20. Find Kth Largest XOR Coordinate Value**

- **Difficulty:** Medium
- **Description:** You are given a 2D `matrix` of size `m x n`, consisting of non-negative integers. You are also given an integer `k`. The value of coordinate `(a, b)` of the matrix is the XOR sum of all `matrix[i][j]` where `0 <= i <= a < m` and `0 <= j <= b < n`. Return the `k`-th largest value (1-indexed) of all coordinate values.
