## Bit Manipulation

### Study Questions (To Learn Patterns)

#### **1. Single Number**

- **Difficulty:** Easy
- **Description:** Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
- **Reason:** Classic XOR property: `x ^ x = 0` and `x ^ 0 = x`. XORing all numbers together will cancel out pairs, leaving the single number.
- **Focus:** Understand the XOR properties and how they apply to finding the unique element.

#### **2. Number of 1 Bits (Hamming Weight)**

- **Difficulty:** Easy
- **Description:** Write a function that takes an unsigned integer and returns the number of '1' bits it has.
- **Reason:** Introduces basic bit counting techniques.
- **Focus:** Learn two common methods:
  1.  Loop and check the last bit (`n & 1`), then right shift (`n >>= 1`).
  2.  Brian Kernighan's algorithm: `n = n & (n - 1)` repeatedly, which removes the rightmost set bit in each step. Count steps.

#### **3. Counting Bits**

- **Difficulty:** Easy
- **Description:** Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of 1's in the binary representation of `i`.
- **Reason:** Can be solved with DP and bit manipulation. `dp[i] = dp[i / 2] + (i % 2)` or `dp[i] = dp[i & (i-1)] + 1`.
- **Focus:** Understand the relationship between the number of set bits in `i` and `i/2` (right shift) or `i & (i-1)` (removes last set bit).

#### **4. Reverse Bits**

- **Difficulty:** Easy
- **Description:** Reverse bits of a given 32-bit unsigned integer.
- **Reason:** Demonstrates bit-by-bit construction of the reversed number.
- **Focus:** Iterate 32 times. In each iteration, take the last bit of the input, append it to the result (by left shifting result and ORing the bit), and then right shift the input.

#### **5. Missing Number**

- **Difficulty:** Easy
- **Description:** Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.
- **Reason:** Can be solved using XOR. XOR all numbers from `0` to `n` together, then XOR this result with all numbers in the `nums` array. The final result is the missing number.
- **Focus:** Similar to "Single Number". The expected set of numbers `[0...n]` is XORed with the actual set `nums`. Paired numbers cancel out.

#### **6. Power of Two**

- **Difficulty:** Easy
- **Description:** Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.
- **Reason:** A number is a power of two if it's positive and has only one bit set in its binary representation. This means `n & (n - 1)` will be 0.
- **Focus:** Understand that `n & (n - 1)` unsets the least significant bit. If `n` is a power of two, it has only one set bit, so this operation results in 0. Handle `n <= 0`.

#### **7. Sum of Two Integers**

- **Difficulty:** Medium
- **Description:** Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.
- **Reason:** Simulates binary addition using bitwise operators: XOR for sum without carry, AND followed by left shift for carry.
- **Focus:** `sum = a ^ b` (bits that don't cause a carry). `carry = (a & b) << 1` (bits that cause a carry, shifted left). Repeat until carry is 0.

#### **8. Single Number II**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element and return it.
- **Reason:** More advanced bit manipulation. One common approach is to count set bits at each position (0 to 31). For each bit position, the sum of bits modulo 3 will give the bit of the single number.
- **Focus:** Iterate through each bit position. For each position, count how many numbers in `nums` have that bit set. If `count % 3 == 1`, then the single number has that bit set. Construct the result. Another approach uses two bitmasks (`ones`, `twos`).

#### **9. Bitwise AND of Numbers Range**

- **Difficulty:** Medium
- **Description:** Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.
- **Reason:** The bitwise AND of a range of numbers results in their common prefix in binary representation.
- **Focus:** Find the common prefix. One way is to repeatedly right-shift `left` and `right` until they are equal. The number of shifts indicates how many trailing zeros the result will have. Left-shift the common prefix back. Alternatively, `right &= (right - 1)` until `right <= left`. The final `right` is the answer.

#### **10. Subsets** (Bitmasking approach)

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` of unique elements, return all possible subsets (the power set).
- **Reason:** Each number from `0` to `2^n - 1` can represent a subset. The `i`-th bit of the number corresponds to the `i`-th element of `nums`. If the bit is set, include the element.
- **Focus:** Iterate from `0` to `(1 << n) - 1`. For each integer `i` (mask), check its bits. If the `j`-th bit of `i` is set, include `nums[j]` in the current subset.

### Practice Questions (To Apply Patterns)

#### **1. Binary Gap**

- **Difficulty:** Easy
- **Description:** Given a positive integer `n`, find and return the longest distance between any two adjacent 1's in the binary representation of `n`. If there are no two adjacent 1's, return 0.

#### **2. Complement of Base 10 Integer**

- **Difficulty:** Easy
- **Description:** The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation. Given an integer `n`, return its complement.

#### **3. Hamming Distance**

- **Difficulty:** Easy
- **Description:** The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers `x` and `y`, return the Hamming distance between them.

#### **4. Power of Four**

- **Difficulty:** Easy
- **Description:** Given an integer `n`, return `true` if it is a power of four. Otherwise, return `false`.

#### **5. Find the Difference**

- **Difficulty:** Easy
- **Description:** You are given two strings `s` and `t`. String `t` is generated by random shuffling string `s` and then add one more letter at a random position. Return the letter that was added to `t`. (Can use XOR).

#### **6. Single Number III**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

#### **7. Maximum Product of Word Lengths**

- **Difficulty:** Medium
- **Description:** Given a string array `words`, return the maximum value of `length(word[i]) * length(word[j])` where the two words do not share common letters. If no such two words exist, return 0. (Use bitmasks to represent character sets of words).

#### **8. Total Hamming Distance**

- **Difficulty:** Medium
- **Description:** The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given an integer array `nums`, return the sum of Hamming distances between all the pairs of the integers in `nums`.

#### **9. Encode and Decode TinyURL** (Bit manipulation is not primary, but good to think about unique ID generation)

- **Difficulty:** Medium
- **Description:** TinyURL is a URL shortening service where you enter a URL and it returns a short URL. Design a class to implement `encode` and `decode`.

#### **10. Find Kth Bit in Nth Binary String**

- **Difficulty:** Medium
- **Description:** Given two positive integers `n` and `k`, the binary string `S_n` is formed as follows: `S_1 = "0"`, `S_i = S_{i-1} + "1" + reverse(invert(S_{i-1}))` for `i > 1`. Return the `k`-th bit in `S_n`.

#### **11. Minimum Flips to Make a OR b Equal to c**

- **Difficulty:** Medium
- **Description:** Given 3 positives numbers `a`, `b` and `c`. Return the minimum flips required in some bits of `a` and `b` to make `(a OR b) == c`. (Flip is changing 0 to 1 and 1 to 0).

#### **12. Number of Steps to Reduce a Number to Zero**

- **Difficulty:** Easy
- **Description:** Given an integer `num`, return the number of steps to reduce it to zero. In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

#### **13. Convert a Number to Hexadecimal**

- **Difficulty:** Easy
- **Description:** Given an integer `num`, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

#### **14. Gray Code** (Can be solved with bit manipulation formula `i ^ (i >> 1)`)

- **Difficulty:** Medium
- **Description:** An n-bit gray code sequence is a sequence of \(2^n\) integers. Given an integer `n`, return any valid n-bit gray code sequence.

#### **15. Divide Two Integers** (Bit manipulation for repeated subtraction/multiplication by 2)

- **Difficulty:** Medium
- **Description:** Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.

#### **16. Maximum XOR for Each Query**

- **Difficulty:** Medium
- **Description:** You are given a sorted array `nums` of `n` non-negative integers and an integer `maximumBit`. You want to perform `n` queries. For the `i`-th query (0-indexed), you first find the XOR sum of all elements currently in the array. Then, you find a non-negative integer `k < 2^maximumBit` such that XOR sum `XOR k` is maximized. Lastly, you remove the last element from the current array. Return an array `answer`, where `answer[i]` is the `k` chosen for the `i`-th query.

#### **17. Prime Number of Set Bits in Binary Representation**

- **Difficulty:** Easy
- **Description:** Given two integers `left` and `right`, return the count of numbers in the inclusive range `[left, right]` having a prime number of set bits in their binary representation.

#### **18. Smallest Sufficient Team**

- **Difficulty:** Hard
- **Description:** In a project, you have a list of required skills `req_skills`, and a list of people. The `i`-th person `people[i]` contains a list of skills that person has. Consider a sufficient team: a set of people such that for every required skill in `req_skills`, there is at least one person in the team who has that skill. We can represent these skills by integers. Return a list of people (represented by their indices) that form the smallest sufficient team. (Bitmask DP).

#### **19. XOR Queries of a Subarray**

- **Difficulty:** Medium
- **Description:** You are given an array `arr` of positive integers. You are also given an array `queries` where `queries[i] = [Li, Ri]`. For each query `i`, you have to find the XOR sum of elements from index `Li` to `Ri` (inclusive). Return an array containing the result for all queries. (Prefix XORs).

#### **20. Number of Valid Words for Each Puzzle**

- **Difficulty:** Hard
- **Description:** Given an array of `words` and an array of `puzzles`. For each `puzzle`, count how many words are valid. A word is valid if: 1. `word` contains the first letter of `puzzle`. 2. For each letter in `word`, that letter is in `puzzle`. (Use bitmasks to represent character sets).
