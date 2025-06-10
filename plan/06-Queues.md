## Queues

### Study Questions (To Learn Patterns)

#### **1. Implement Stack using Queues**

- **Difficulty:** Easy
- **Description:** Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).
- **Reason:** Demonstrates how queues can simulate other data structures. Highlights the FIFO nature and how it can be manipulated (e.g., by transferring elements) to achieve LIFO.
- **Focus:** Understand the two main approaches: making `push` costly (O(n)) or making `pop` costly (O(n)) by re-arranging elements in the queues.

#### **2. Number of Recent Calls**

- **Difficulty:** Easy
- **Description:** You have a `RecentCounter` class which counts the number of recent requests within a certain time frame. Implement the `RecentCounter` class: `RecentCounter()` initializes the counter with zero recent requests. `int ping(int t)` adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
- **Reason:** A direct application of a queue to maintain a sliding window of time. Old requests outside the window are dequeued.
- **Focus:** Learn to add new elements to the queue and remove elements from the front that fall outside the `[t-3000, t]` window. The queue's size is the answer.

#### **3. Moving Average from Data Stream**

- **Difficulty:** Easy
- **Description:** Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
- **Reason:** Classic use of a queue to maintain a fixed-size sliding window. When the window is full, adding a new element requires removing the oldest.
- **Focus:** Understand how to use a queue to store window elements. Maintain the sum of elements in the window for efficient average calculation. When a new element arrives, enqueue it, and if the queue size exceeds the window size, dequeue and subtract the dequeued element from the sum.

#### **4. Walls and Gates**

- **Difficulty:** Medium
- **Description:** You are given an `m x n` grid `rooms` initialized with these three possible values: -1 (a wall or an obstacle), 0 (a gate), `INF` (an empty room). Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with `INF`.
- **Reason:** A great example of Breadth-First Search (BFS) starting from multiple sources (all gates simultaneously). The queue is essential for BFS level-order traversal.
- **Focus:** Understand how to initialize the queue with all gate locations. Then, perform BFS, updating distances for empty rooms layer by layer. This naturally finds the shortest distance.

#### **5. 01 Matrix**

- **Difficulty:** Medium
- **Description:** Given an `m x n` binary matrix `mat`, return the distance of the nearest 0 for each cell. The distance between two adjacent cells is 1.
- **Reason:** Similar to "Walls and Gates," this is a multi-source BFS problem. The queue stores cells to visit, and distances are updated layer by layer starting from all 0s.
- **Focus:** Initialize the queue with all cells containing 0. Perform BFS to explore neighbors, updating their distances if a shorter path (from a 0) is found. Mark visited cells or use the distance matrix itself to avoid re-processing.

#### **6. Design Circular Queue**

- **Difficulty:** Medium
- **Description:** Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO principle and the last position is connected back to the first position to make a circle.
- **Reason:** Focuses on the implementation details of a fixed-size queue using an array, including handling wrap-around logic for head and tail pointers.
- **Focus:** Understand how to use the modulo operator for circular array indexing. Manage `head`, `tail` pointers, and `size` (or use specific conditions for full/empty states) correctly.

#### **7. Task Scheduler** (Queue-based simulation approach)

- **Difficulty:** Medium
- **Description:** Given a characters array `tasks` representing tasks a CPU needs to do and a non-negative integer `n` (cooldown period). Return the least number of units of times that the CPU will take to finish all given tasks.
- **Reason:** While often solved with greedy approaches and priority queues, a simulation using a queue to manage task cooldowns is also a valid way to understand the process.
- **Focus:** If using a queue for cooldown, understand how tasks are added to a wait queue with their available time. The main loop simulates time, picking available tasks or idling.

#### **8. Dota2 Senate**

- **Difficulty:** Medium
- **Description:** In the world of Dota2, there are two parties: the Radiant and the Dire. The Dota2 senate consists of senators coming from two parties. Now the senate wants to decide on a change in the Dota2 game. The voting process goes in rounds. In each round, each senator can exercise one of the two rights: Ban one senator's right or Announce victory.
- **Reason:** A clever simulation problem that can be solved using queues to represent senators from each party. The greedy strategy involves banning the next opponent.
- **Focus:** Use two queues, one for Radiant and one for Dire, storing their original indices. In each round, compare the front of both queues. The senator with the smaller index (earlier turn) bans the other, and the banned senator is effectively removed, while the winning senator is re-queued for the next round (with an updated index to reflect their next turn).

#### **9. Sliding Window Maximum** (Deque-based solution)

- **Difficulty:** Hard
- **Description:** You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
- **Reason:** The optimal solution uses a Deque (Double-ended Queue) to maintain indices of elements in the current window, in decreasing order of their values. This allows O(1) lookup for the maximum.
- **Focus:** Understand how the deque stores indices. Before adding a new element's index, remove indices from the back of the deque that correspond to elements smaller than the current element. Also, remove indices from the front that are out of the current window. The front of the deque always holds the index of the maximum element in the window.

#### **10. Shortest Subarray with Sum at Least K**

- **Difficulty:** Hard
- **Description:** Given an integer array `nums` and an integer `k`, return the length of the shortest, non-empty, contiguous subarray of `nums` with sum at least `k`. If there is no such subarray, return -1.
- **Reason:** This problem uses a monotonic deque (specifically, increasing order of prefix sums) to efficiently find subarrays satisfying the condition. It's an advanced application of deques for optimization.
- **Focus:** First, calculate prefix sums. The deque will store indices `j` such that `prefix_sum[j]` are in increasing order. When considering `prefix_sum[i]`, we want to find the smallest `j < i` such that `prefix_sum[i] - prefix_sum[j] >= k`. The deque helps find this `j` efficiently.

### Practice Questions (To Apply Patterns)

#### **1. Implement Queue using Stacks**

- **Difficulty:** Easy
- **Description:** Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

#### **2. Time Needed to Buy Tickets**

- **Difficulty:** Easy
- **Description:** There are `n` people in a line queuing to buy tickets, where the `0`-th person is at the front of the line and the `(n - 1)`-th person is at the back of the line. You are given a 0-indexed integer array `tickets` of length `n` where `tickets[i]` is the number of tickets that the `i`-th person wants to buy. Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go to the back of the line (which happens instantaneously) in order to buy more tickets. If a person does not need to buy any more tickets, they leave the line. Return the time taken for the person at position `k` (0-indexed) to finish buying all their tickets.

#### **3. First Unique Character in a String** (Queue can be one way to track order)

- **Difficulty:** Easy
- **Description:** Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#### **4. Design Circular Deque**

- **Difficulty:** Medium
- **Description:** Design your implementation of the circular double-ended queue (deque).

#### **5. Reveal Cards In Increasing Order**

- **Difficulty:** Medium
- **Description:** You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The integer on the `i`-th card is `deck[i]`. You can order the deck in any order you want. Initially, all cards start face down (unrevealed) in one deck. You will do the following steps repeatedly until all cards are revealed: Take the top card of the deck, reveal it, and take it out of the deck. If there are still cards in the deck then put the next top card of the deck at the bottom of the deck. Return an ordering of the deck that would reveal the cards in increasing order.

#### **6. Keys and Rooms**

- **Difficulty:** Medium
- **Description:** There are `N` rooms and you start in room `0`. Each room has a distinct number in `0, 1, 2, ..., N-1`, and each room may have some keys to access the next room. Formally, each room `i` has a list of keys `rooms[i]`, and each key `rooms[i][j]` is an integer in `[0, 1, ..., N-1]` where `N = rooms.length`. A key `rooms[i][j] = v` opens the room with number `v`. Initially, all rooms are locked (except for room `0`). You can walk back and forth between rooms freely. Return `true` if and only if you can enter every room.

#### **7. Snakes and Ladders**

- **Difficulty:** Medium
- **Description:** You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n^2` in a Boustrophedon style starting from the bottom left of the board. You start at square `1`. In one move, you can move to a square `s` with a label `x` if `x` is in the range `[curr + 1, min(curr + 6, n^2)]`. If `board[r][c]` is not `-1`, you move to the square with label `board[r][c]`. Otherwise, you move to the square `s`. Return the least number of moves to reach the square `n^2`. If it is not possible, return `-1`.

#### **8. Rotting Oranges**

- **Difficulty:** Medium
- **Description:** You are given an `m x n` grid where each cell can have one of three values: `0` representing an empty cell, `1` representing a fresh orange, or `2` representing a rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

#### **9. Open the Lock**

- **Difficulty:** Medium
- **Description:** You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', ..., '9'. The wheels can rotate freely and wrap around. You are given a list of `deadends` dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it. Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

#### **10. Shortest Path in Binary Matrix**

- **Difficulty:** Medium
- **Description:** Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no clear path, return -1. A clear path in a binary matrix is a path from the top-left cell (i.e., `(0, 0)`) to the bottom-right cell (i.e., `(n - 1, n - 1)`) such that all visited cells are `0` and all adjacent cells of the path are 8-directionally connected.

#### **11. Minimum Knight Moves**

- **Difficulty:** Medium
- **Description:** In an infinite chessboard, a knight is placed at square `[0, 0]`. A knight has 8 possible moves. Given a target square `[x, y]`, return the minimum number of moves required to reach the target.

#### **12. Word Ladder**

- **Difficulty:** Hard
- **Description:** A transformation sequence from word `beginWord` to `word endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that every adjacent pair of words differs by a single letter, and every `si` is in `wordList`. `beginWord` does not need to be in `wordList`. `sk == endWord`. Given `beginWord`, `endWord`, and `wordList`, return the number of words in the shortest transformation sequence, or 0 if no such sequence exists.

#### **13. Find Bottom Left Tree Value** (BFS approach)

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, return the leftmost value in the last row of the tree.

#### **14. Binary Tree Level Order Traversal**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

#### **15. Binary Tree Zigzag Level Order Traversal**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

#### **16. Populating Next Right Pointers in Each Node**

- **Difficulty:** Medium
- **Description:** You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. Populate each `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `NULL`.

#### **17. Serialize and Deserialize Binary Tree** (BFS approach for serialization)

- **Difficulty:** Hard
- **Description:** Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Design an algorithm to serialize and deserialize a binary tree.

#### **18. Course Schedule II** (BFS/Kahn's algorithm for topological sort)

- **Difficulty:** Medium
- **Description:** There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

#### **19. The Maze**

- **Difficulty:** Medium
- **Description:** There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. Given the `maze`, the `start` coordinates, and the `destination` coordinates, return `true` if the ball can stop at the destination, otherwise return `false`.

#### **20. Design Front Middle Back Queue**

- **Difficulty:** Medium
- **Description:** Design a queue that supports `pushFront`, `pushMiddle`, `pushBack`, `popFront`, `popMiddle`, and `popBack` operations.
