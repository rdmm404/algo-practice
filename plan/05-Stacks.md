## Stacks

### Study Questions (To Learn Patterns)

#### **1. Valid Parentheses**

- **Difficulty:** Easy
- **Description:** Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
- **Reason:** The most fundamental stack problem. It clearly demonstrates the LIFO (Last-In, First-Out) principle for matching opening and closing brackets.
- **Focus:** Understand how to push opening brackets onto the stack and pop/check for matches when a closing bracket is encountered. Handle edge cases like an empty stack or mismatched brackets.

#### **2. Min Stack**

- **Difficulty:** Easy
- **Description:** Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
- **Reason:** Introduces the concept of augmenting a stack to support additional operations efficiently. Common solutions involve using a second stack to track minimums or storing `(value, current_min)` pairs.
- **Focus:** Analyze the trade-offs of different approaches to maintain the minimum element. Understand how push and pop operations affect the minimum tracking.

#### **3. Evaluate Reverse Polish Notation**

- **Difficulty:** Medium
- **Description:** Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.
- **Reason:** A direct application of stacks for expression evaluation. Operands are pushed onto the stack, and when an operator is encountered, operands are popped, the operation is performed, and the result is pushed back.
- **Focus:** Learn how to process tokens: push numbers, and when an operator appears, pop the required number of operands, compute, and push the result.

#### **4. Daily Temperatures**

- **Difficulty:** Medium
- **Description:** Given a list of daily `temperatures`, return a list `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.
- **Reason:** Excellent example of a monotonic stack (specifically, a decreasing stack). It's used to find the next greater element for each temperature.
- **Focus:** Understand how the stack stores indices of temperatures in decreasing order. When a warmer temperature is found, pop elements from the stack and calculate the waiting days.

#### **5. Implement Queue using Stacks**

- **Difficulty:** Easy
- **Description:** Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).
- **Reason:** Shows how one data structure can be simulated using another. Involves using one stack for enqueuing and another for dequeuing (by transferring elements).
- **Focus:** Grasp the "amortized O(1)" complexity for dequeue operations. Understand when and how elements are moved between the two stacks to maintain FIFO order.

#### **6. Basic Calculator**

- **Difficulty:** Hard
- **Description:** Given a string `s` representing a valid expression, implement a basic calculator to evaluate it and return the result of the evaluation. The expression string may contain open `(` and closing `)` parentheses, the plus `+` or minus sign `-`, non-negative integers and empty spaces.
- **Reason:** A more complex expression parsing problem that often uses two stacks: one for numbers and one for operators, or a single stack to handle parentheses and intermediate results.
- **Focus:** Learn how to handle operator precedence (implicitly through parentheses here) and signs. The use of a stack to manage intermediate calculations, especially when parentheses are involved, is key.

#### **7. Next Greater Element I**

- **Difficulty:** Easy
- **Description:** The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array. You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`. For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is -1.
- **Reason:** Introduces the "Next Greater Element" pattern using a monotonic stack. The stack helps efficiently find the NGE for elements in `nums2`.
- **Focus:** Understand how to iterate `nums2` and use a stack to keep track of elements for which NGE hasn't been found yet. A HashMap can store NGE results for quick lookup for `nums1` elements.

#### **8. Simplify Path**

- **Difficulty:** Medium
- **Description:** Given a string `path`, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
- **Reason:** Uses a stack to handle directory navigation components like `.` (current directory), `..` (parent directory), and actual directory names.
- **Focus:** Learn how to split the path by `/` and process each component: ignore `.` and empty strings, pop for `..` (if stack is not empty), and push valid directory names. Finally, reconstruct the path from the stack.

#### **9. Decode String**

- **Difficulty:** Medium
- **Description:** Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.
- **Reason:** Effectively uses stacks (often two: one for counts and one for strings/characters being built) to handle nested encoded strings.
- **Focus:** Understand how to push numbers and partial strings onto stacks when `[` is encountered, and how to pop, repeat, and concatenate when `]` is found.

#### **10. Trapping Rain Water** (Stack-based solution)

- **Difficulty:** Hard
- **Description:** Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
- **Reason:** While there are DP and two-pointer solutions, a stack-based solution is also common and insightful. It processes bars and calculates trapped water when a bar taller than the stack top is encountered.
- **Focus:** Understand how the stack stores indices of bars in increasing order. When a bar `current` is taller than `stack.top()`, it forms a container. Pop `stack.top()`, calculate water trapped with `min(height[current], height[stack.top()]) - height[popped_bar]`.

### Practice Questions (To Apply Patterns)

#### **1. Implement Stack using Queues**

- **Difficulty:** Easy
- **Description:** Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

#### **2. Backspace String Compare**

- **Difficulty:** Easy
- **Description:** Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `#` means a backspace character.

#### **3. Baseball Game**

- **Difficulty:** Easy
- **Description:** You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores. You are given a list of strings `ops`, where `ops[i]` is the `i`-th operation you must apply to the record.

#### **4. Next Greater Element II**

- **Difficulty:** Medium
- **Description:** Given a circular integer array `nums` (i.e., `nums[nums.length - 1]`'s next element is `nums[0]`), return the next greater number for every element in `nums`.

#### **5. Remove All Adjacent Duplicates In String**

- **Difficulty:** Easy
- **Description:** You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them. We repeatedly make duplicate removals on `s` until we no longer can. Return the final string after all such duplicate removals have been made.

#### **6. Asteroid Collision**

- **Difficulty:** Medium
- **Description:** We are given an array `asteroids` of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions.

#### **7. Online Stock Span**

- **Difficulty:** Medium
- **Description:** Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day. The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

#### **8. Remove K Digits**

- **Difficulty:** Medium
- **Description:** Given string `num` representing a non-negative integer, and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

#### **9. Score of Parentheses**

- **Difficulty:** Medium
- **Description:** Given a balanced parentheses string `S`, compute the score of the string based on the following rule: `()` has score 1, `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings. `(A)` has score `2 * A`.

#### **10. Largest Rectangle in Histogram**

- **Difficulty:** Hard
- **Description:** Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

#### **11. Maximal Rectangle**

- **Difficulty:** Hard
- **Description:** Given a `rows x cols` binary `matrix` filled with 0's and 1's, find the largest rectangle containing only 1's and return its area. (Hint: Can be solved by reducing to "Largest Rectangle in Histogram" for each row).

#### **12. Car Fleet**

- **Difficulty:** Medium
- **Description:** There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away. You are given two integer arrays `position` and `speed`, both of length `n`. Return the number of car fleets that will arrive at the destination.

#### **13. Sum of Subarray Minimums**

- **Difficulty:** Medium
- **Description:** Given an array of integers `arr`, find the sum of `min(b)` for every (contiguous) subarray `b` of `arr`. Since the answer may be large, return the answer modulo \(10^9 + 7\).

#### **14. Validate Stack Sequences**

- **Difficulty:** Medium
- **Description:** Given two integer arrays `pushed` and `popped` each with distinct values, return `true` if this could have been the result of a sequence of push and pop operations on an initially empty stack, or `false` otherwise.

#### **15. Minimum Remove to Make Valid Parentheses**

- **Difficulty:** Medium
- **Description:** Given a string `s` of `(` , `)` and lowercase English characters. Your task is to remove the minimum number of parentheses `(` or `)`, in any positions, so that the resulting parentheses string is valid and return any valid string.

#### **16. Basic Calculator II**

- **Difficulty:** Medium
- **Description:** Given a string `s` which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero. (No parentheses, but involves operator precedence).

#### **17. Exclusive Time of Functions**

- **Difficulty:** Medium
- **Description:** On a single-threaded CPU, we execute a program containing `n` functions. Each function has a unique ID between `0` and `n-1`. Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. You are given a list of logs, where `logs[i]` represents the `i`-th log message formatted as a string `"{function_id}:{"start" | "end"}:{timestamp}"`. Return the exclusive time of each function.

#### **18. Remove Outermost Parentheses**

- **Difficulty:** Easy
- **Description:** A valid parentheses string is primitive if it is nonempty, and there does not exist a way to split it into `s = A + B`, with `A` and `B` nonempty valid parentheses strings. Given a valid parentheses string `s`, consider its primitive decomposition: `s = P_1 + P_2 + ... + P_k`, where `P_i` are primitive valid parentheses strings. Return `s` after removing the outermost parentheses of every primitive string in the primitive decomposition of `s`.

#### **19. Crawler Log Folder**

- **Difficulty:** Easy
- **Description:** The Leetcode file system keeps a log each time a user performs a change folder operation. The operations are described below: `../` : Move to the parent folder. If already in the main folder, remain in the same folder. `./` : Remain in the same folder. `x/` : Move to the child folder named `x`. You are given a list of strings `logs` where `logs[i]` is the operation performed by the user at the `i`-th step. Return the minimum number of operations needed to go back to the main folder after the change folder operations.

#### **20. Number of Visible People in a Queue**

- **Difficulty:** Hard
- **Description:** There are `n` people standing in a queue, and they are numbered from `0` to `n - 1` in left to right order. You are given an array `heights` of distinct integers where `heights[i]` represents the height of the `i`-th person. A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the `i`-th person can see the `j`-th person if `i < j` and `min(heights[i], heights[j]) > max(heights[i+1], ..., heights[j-1])`. Return an array `answer` of length `n` where `answer[i]` is the number of people the `i`-th person can see to their right in the queue.
