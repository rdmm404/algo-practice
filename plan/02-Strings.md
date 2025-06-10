## Strings

### Study Questions (To Learn Patterns)

#### **1. Valid Palindrome**

- **Difficulty:** Easy
- **Description:** Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
- **Reason:** Introduces the two-pointer technique (from opposite ends) for string checking and highlights character manipulation/filtering.
- **Focus:** Understand how to preprocess the string (or handle character validation on the fly) and use two pointers to compare characters from both ends moving inwards.

#### **2. Valid Anagram**

- **Difficulty:** Easy
- **Description:** Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
- **Reason:** Demonstrates character frequency counting using a hash map or an integer array (for a fixed character set like ASCII).
- **Focus:** Learn how to count character occurrences in one string and then decrement counts based on the second string, or compare frequency maps.

#### **3. Longest Substring Without Repeating Characters**

- **Difficulty:** Medium
- **Description:** Given a string `s`, find the length of the longest substring without repeating characters.
- **Reason:** Classic application of the sliding window pattern with a hash set or hash map to keep track of characters currently in the window.
- **Focus:** Understand how the window expands (right pointer) and contracts (left pointer moves when a repeat is found), and how the auxiliary data structure helps detect repeats.

#### **4. Group Anagrams**

- **Difficulty:** Medium
- **Description:** Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
- **Reason:** Shows how to use a canonical representation (e.g., sorted string or character count tuple) as a key in a hash map to group anagrams.
- **Focus:** Explore different ways to generate a unique key for anagrams and use a hash map to collect strings sharing the same key.

#### **5. String to Integer (atoi)**

- **Difficulty:** Medium
- **Description:** Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).
- **Reason:** Focuses on careful string parsing, handling edge cases like whitespace, signs, overflow/underflow, and invalid characters.
- **Focus:** Pay attention to the step-by-step parsing logic: skipping leading whitespace, checking for sign, reading digits, and checking for integer overflow.

#### **6. Longest Palindromic Substring**

- **Difficulty:** Medium
- **Description:** Given a string `s`, return the longest palindromic substring in `s`.
- **Reason:** Introduces two common approaches: dynamic programming or the "expand from center" technique. The latter is often more intuitive for this problem.
- **Focus:** For "expand from center", understand how to check for palindromes of odd and even lengths by expanding outwards from each character (or pair of characters). For DP, understand the state `dp[i][j]` representing if `s[i...j]` is a palindrome.

#### **7. Valid Parentheses**

- **Difficulty:** Easy
- **Description:** Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
- **Reason:** Classic use case for a stack to match opening and closing parentheses. (Also a Stack problem, but fundamental for string parsing).
- **Focus:** Understand how to push opening brackets onto the stack and pop/check for matches when a closing bracket is encountered. Handle edge cases like an empty stack or mismatched brackets.

#### **8. Generate Parentheses**

- **Difficulty:** Medium
- **Description:** Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
- **Reason:** A good example of using backtracking to build valid string combinations based on specific rules (number of open vs. close parentheses).
- **Focus:** Understand the recursive backtracking approach: maintain counts for open and close parentheses, add '(' if open < n, add ')' if close < open.

#### **9. Minimum Window Substring**

- **Difficulty:** Hard
- **Description:** Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.
- **Reason:** A more advanced sliding window problem that requires careful management of character counts (for string `t`) within the current window of string `s`.
- **Focus:** Learn how to use hash maps to track required characters and current window characters, and how to expand/shrink the window to find the minimal valid substring.

#### **10. Reverse Words in a String**

- **Difficulty:** Medium
- **Description:** Given an input string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.
- **Reason:** Focuses on string manipulation, splitting by spaces, and then rejoining in reverse order. Highlights handling multiple spaces and leading/trailing spaces.
- **Focus:** Consider different approaches: splitting the string into words, reversing the list of words, and joining. Or, in-place reversal techniques if allowed/required.

### Practice Questions (To Apply Patterns)

#### **1. Reverse String**

- **Difficulty:** Easy
- **Description:** Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

#### **2. First Unique Character in a String**

- **Difficulty:** Easy
- **Description:** Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#### **3. Implement strStr()**

- **Difficulty:** Easy
- **Description:** Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#### **4. Longest Common Prefix**

- **Difficulty:** Easy
- **Description:** Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

#### **5. Palindromic Substrings**

- **Difficulty:** Medium
- **Description:** Given a string `s`, return the number of palindromic substrings in it.

#### **6. Word Break**

- **Difficulty:** Medium
- **Description:** Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

#### **7. Decode String**

- **Difficulty:** Medium
- **Description:** Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.

#### **8. Basic Calculator II**

- **Difficulty:** Medium
- **Description:** Given a string `s` which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero.

#### **9. Letter Combinations of a Phone Number**

- **Difficulty:** Medium
- **Description:** Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

#### **10. Simplify Path**

- **Difficulty:** Medium
- **Description:** Given a string `path`, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

#### **11. Zigzag Conversion**

- **Difficulty:** Medium
- **Description:** The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows. Write the code that will take a string and make this conversion given a number of rows.

#### **12. Find All Anagrams in a String**

- **Difficulty:** Medium
- **Description:** Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

#### **13. Text Justification**

- **Difficulty:** Hard
- **Description:** Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

#### **14. Regular Expression Matching**

- **Difficulty:** Hard
- **Description:** Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*`.

#### **15. Shortest Palindrome**

- **Difficulty:** Hard
- **Description:** You are given a string `s`. You can convert `s` to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can create by performing this transformation.

#### **16. Integer to Roman**

- **Difficulty:** Medium
- **Description:** Given an integer, convert it to a roman numeral.

#### **17. Roman to Integer**

- **Difficulty:** Easy
- **Description:** Given a roman numeral, convert it to an integer.

#### **18. Compare Version Numbers**

- **Difficulty:** Medium
- **Description:** Given two version numbers, `version1` and `version2`, compare them.

#### **19. Reorganize String**

- **Difficulty:** Medium
- **Description:** Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same. Return any possible rearrangement of `s` or return `""` if not possible.

#### **20. One Edit Distance**

- **Difficulty:** Medium
- **Description:** Given two strings `s` and `t`, return `true` if they are both one edit distance apart, otherwise return `false`. An edit distance of one means you can insert one character, delete one character, or replace one character to make the strings equal.
