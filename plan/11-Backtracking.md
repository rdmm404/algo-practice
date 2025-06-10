## Backtracking

### Study Questions (To Learn Patterns)

#### **1. Subsets**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets.
- **Reason:** Fundamental backtracking problem. For each element, we have two choices: either include it in the current subset or not.
- **Focus:** Understand the recursive structure. The parameters for the recursive function typically include the current index being considered, the current subset being built, and the list to store results.

#### **2. Permutations**

- **Difficulty:** Medium
- **Description:** Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.
- **Reason:** Classic backtracking problem for generating all orderings. Involves picking an unused element at each step.
- **Focus:** Maintain a `used` array or similar mechanism to track which elements have been included in the current permutation. At each step of building the permutation, iterate through all numbers. If a number is not used, add it to the current permutation and recurse. Backtrack by removing it and marking it as unused.

#### **3. Combination Sum**

- **Difficulty:** Medium
- **Description:** Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order. The same number may be chosen from `candidates` an unlimited number of times.
- **Reason:** Demonstrates backtracking where elements can be reused. The key is how to manage the `target` sum and the starting index for picking candidates to avoid duplicates and ensure all combinations are found.
- **Focus:** In the recursive call, when an element `candidates[i]` is chosen, the next recursive call can also start from index `i` (allowing reuse). The target sum is reduced. Base cases: target is 0 (add combination), target < 0 (invalid path).

#### **4. Letter Combinations of a Phone Number**

- **Difficulty:** Medium
- **Description:** Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given.
- **Reason:** Maps digits to characters and then uses backtracking to form all possible strings by picking one character for each digit.
- **Focus:** The recursive function takes the current index of the input `digits` string and the `current_combination` string. For the digit at the current index, iterate through its mapped letters, append each letter to `current_combination`, and recurse for the next digit.

#### **5. Generate Parentheses**

- **Difficulty:** Medium
- **Description:** Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
- **Reason:** Backtracking with constraints: the number of open parentheses used must not exceed `n`, and the number of close parentheses used must not exceed the number of open parentheses used.
- **Focus:** The recursive function maintains counts of `open_brackets_used` and `close_brackets_used`. Add '(' if `open_brackets_used < n`. Add ')' if `close_brackets_used < open_brackets_used`. Base case: length of string is `2*n`.

#### **6. N-Queens**

- **Difficulty:** Hard
- **Description:** The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Given an integer `n`, return all distinct solutions to the n-queens puzzle.
- **Reason:** A classic constraint satisfaction problem solved with backtracking. At each row, try placing a queen in a valid column.
- **Focus:** The state includes the current row being considered and the placement of queens in previous rows. Need an efficient way to check if placing a queen at `(row, col)` is valid (i.e., no other queen in the same column or diagonals). Store the board configuration or just column placements.

#### **7. Word Search**

- **Difficulty:** Medium
- **Description:** Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
- **Reason:** DFS/backtracking on a grid. Start DFS from any cell that matches the first letter of the `word`.
- **Focus:** The recursive function takes current `(row, col)`, and current `index` in `word`. Mark visited cells (e.g., by temporarily changing `board[row][col]`) to avoid reuse. Explore 4-directional neighbors. Backtrack by unmarking the cell.

#### **8. Palindrome Partitioning**

- **Difficulty:** Medium
- **Description:** Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.
- **Reason:** Backtracking where each step involves finding a palindromic prefix of the remaining string.
- **Focus:** The recursive function takes the `start_index` of the string to be partitioned. Iterate `i` from `start_index` to `len(s)-1`. If `s[start_index...i]` is a palindrome, add it to the current partition and recurse for the rest of the string `s[i+1...]`.

#### **9. Subsets II (contains duplicates)**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.
- **Reason:** Variation of "Subsets" that requires handling duplicates in the input array to avoid generating duplicate subsets in the output.
- **Focus:** Sort the input array `nums` first. In the recursive step, if considering `nums[i]`, and `i > start_index` and `nums[i] == nums[i-1]`, skip `nums[i]` to avoid duplicates that would arise from picking the same number from different positions when it's a duplicate.

#### **10. Permutations II (contains duplicates)**

- **Difficulty:** Medium
- **Description:** Given a collection of numbers `nums` that might contain duplicates, return all possible unique permutations in any order.
- **Reason:** Variation of "Permutations" that needs to handle duplicates in `nums` to produce unique permutations.
- **Focus:** Sort `nums`. Use a `used` boolean array. In the loop for choosing the next number, if `i > 0 && nums[i] == nums[i-1] && !used[i-1]`, skip `nums[i]`. This ensures that for a sequence of identical numbers, they are picked in their original relative order.

### Practice Questions (To Apply Patterns)

#### **1. Combinations**

- **Difficulty:** Medium
- **Description:** Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`. You may return the answer in any order.

#### **2. Combination Sum II (candidates may have duplicates, each number used once)**

- **Difficulty:** Medium
- **Description:** Given a collection of candidate numbers `candidates` (which might contain duplicates) and a target number `target`, find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination.

#### **3. Beautiful Arrangement**

- **Difficulty:** Medium
- **Description:** Suppose you have `n` integers labeled `1` through `n`. A permutation of those `n` integers `perm` (1-indexed) is considered a beautiful arrangement if for every `i` (1 <= `i` <= `n`), either `perm[i]` is divisible by `i` or `i` is divisible by `perm[i]`. Given an integer `n`, return the number of beautiful arrangements.

#### **4. Word Search II**

- **Difficulty:** Hard
- **Description:** Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. (Often involves Trie + Backtracking).

#### **5. Sudoku Solver**

- **Difficulty:** Hard
- **Description:** Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the given rules.

#### **6. Restore IP Addresses**

- **Difficulty:** Medium
- **Description:** A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros. Given a string `s` containing only digits, return all possible valid IP addresses that can be formed by inserting dots into `s`.

#### **7. Path Sum II** (Already listed under Trees, but good backtracking practice)

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values in the path equals `targetSum`.

#### **8. Gray Code**

- **Difficulty:** Medium
- **Description:** An n-bit gray code sequence is a sequence of \(2^n\) integers where: Every integer is in the inclusive range \([0, 2^n - 1]\), The first integer is 0, An integer appears no more than once in the sequence, The binary representation of every pair of adjacent integers differs by exactly one bit, and The binary representation of the first and last integers differs by exactly one bit. Given an integer `n`, return any valid n-bit gray code sequence.

#### **9. Expression Add Operators**

- **Difficulty:** Hard
- **Description:** Given a string `num` that contains only digits and an integer `target`, return all possibilities to add the binary operators `+`, `-`, or `*` between the digits of `num` so that the resultant expression evaluates to the `target` value.

#### **10. Split a String Into the Max Number of Unique Substrings**

- **Difficulty:** Medium
- **Description:** Given a string `s`, return the maximum number of unique substrings that `s` can be split into. You can split `s` into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, all the substrings in the split list must be unique.

#### **11. Combination Sum III**

- **Difficulty:** Medium
- **Description:** Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true: Only numbers `1` through `9` are used. Each number is used at most once. Return a list of all possible valid combinations.

#### **12. Factor Combinations**

- **Difficulty:** Medium
- **Description:** Numbers can be regarded as products of their factors. For example, 8 = 2 x 2 x 2; = 2 x 4. Write a function that takes an integer `n` and return all possible combinations of its factors. Factors should be greater than 1 and less than `n`.

#### **13. Letter Case Permutation**

- **Difficulty:** Easy
- **Description:** Given a string `s`, you can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create.

#### **14. Word Break II**

- **Difficulty:** Hard
- **Description:** Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

#### **15. Matchsticks to Square**

- **Difficulty:** Medium
- **Description:** You are given an integer array `matchsticks` where `matchsticks[i]` is the length of the `i`-th matchstick. You want to use all the matchsticks to form one square. You cannot break any stick, but you can link them up, and each matchstick must be used exactly one time. Return `true` if you can form this square and `false` otherwise.

#### **16. Optimal Account Balancing**

- **Difficulty:** Hard
- **Description:** You are given an array `transactions` where `transactions[i] = [from_i, to_i, amount_i]` indicates that person `from_i` gave `amount_i` to person `to_i`. Return the minimum number of transactions required to settle the debt.

#### **17. Find Minimum Time to Finish All Jobs**

- **Difficulty:** Hard
- **Description:** You are given an integer array `jobs`, where `jobs[i]` is the amount of time it takes to complete the `i`-th job. There are `k` workers. All jobs are assigned to the workers. Each job must be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to minimize the maximum working time among all the workers. Return the minimum possible maximum working time.

#### **18. Maximum Length of a Concatenated String with Unique Characters**

- **Difficulty:** Medium
- **Description:** You are given an array of strings `arr`. A string `s` is formed by the concatenation of a subsequence of `arr` that has unique characters. Return the maximum possible length of `s`.

#### **19. Number of Squareful Arrays**

- **Difficulty:** Hard
- **Description:** An array is squareful if the sum of every pair of adjacent elements is a perfect square. Given an integer array `nums`, return the number of permutations of `nums` that are squareful. Two permutations `perm1` and `perm2` are different if there is some index `i` such that `perm1[i] != perm2[i]`.

#### **20. Generalized Abbreviation**

- **Difficulty:** Medium
- **Description:** A word's generalized abbreviation can be formed by replacing some number of non-overlapping substrings with their lengths. For example, "word" can be abbreviated as "word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4". Given a string `word`, return a list of all possible generalized abbreviations.
