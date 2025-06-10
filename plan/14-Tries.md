## Tries

### Study Questions (To Learn Patterns)

#### **1. Implement Trie (Prefix Tree)**

- **Difficulty:** Medium
- **Description:** A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. Implement the `Trie` class: `Trie()` initializes the trie object. `void insert(String word)` inserts the string `word` into the trie. `boolean search(String word)` returns `true` if the string `word` is in the trie. `boolean startsWith(String prefix)` returns `true` if there is a previously inserted string `word` that has the `prefix`.
- **Reason:** This is the foundational problem for understanding Trie implementation. It covers the basic structure (nodes with children pointers and an `isEndOfWord` flag) and core operations.
- **Focus:** Understand the structure of a TrieNode (typically an array/map for children and a boolean for end of word). Trace how `insert`, `search`, and `startsWith` traverse the trie character by character.

#### **2. Word Search II**

- **Difficulty:** Hard
- **Description:** Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells. The same letter cell may not be used more than once in a word.
- **Reason:** Combines Trie with DFS/backtracking. Build a Trie from the `words` list. Then, perform DFS on the `board`. As you traverse the board, also traverse the Trie. If a path in the board forms a word in the Trie, add it to results.
- **Focus:** The Trie helps to efficiently check if the current path on the board corresponds to a prefix of any word in the dictionary, pruning the search space significantly. When a word is found, mark it in the Trie (e.g., set `word` field in TrieNode to null or use another flag) to avoid adding duplicates if the same word can be formed multiple ways.

#### **3. Design Add and Search Words Data Structure**

- **Difficulty:** Medium
- **Description:** Design a data structure that supports adding new words and finding if a string matches any previously added string. Implement the `WordDictionary` class: `WordDictionary()` initializes the object. `void addWord(String word)` adds `word` to the data structure. `boolean search(String word)` returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `.` where dots can be matched with any letter.
- **Reason:** Extends the basic Trie search to handle wildcards (`.`). This requires a modified search function that backtracks or explores multiple children when a `.` is encountered.
- **Focus:** The `search` function needs to be recursive. If the current character in the search `word` is a `.` , iterate through all non-null children of the current Trie node and recursively call search on them for the rest of the `word`.

#### **4. Maximum XOR of Two Numbers in an Array**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums`, return the maximum XOR result of `nums[i] XOR nums[j]` where `0 <= i <= j < n`.
- **Reason:** A clever application of Tries with binary representations of numbers. For each number, traverse the Trie of previously inserted numbers to find a number that maximizes the XOR sum by trying to pick opposite bits at each position.
- **Focus:** Insert binary representations of numbers into a Trie (e.g., 32 bits). When searching for max XOR for a number `x`, traverse the Trie. At each bit position, try to go to the child node representing the opposite bit of `x`'s current bit. If not possible, take the same bit. Build the XOR sum bit by bit.

#### **5. Replace Words**

- **Difficulty:** Medium
- **Description:** In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another". Given a `dictionary` consisting of many roots and a `sentence` consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length. Return the sentence after the replacement.
- **Reason:** Use a Trie to store the dictionary roots. For each word in the sentence, traverse the Trie to find the shortest prefix that is a root.
- **Focus:** Insert all roots into a Trie. For each word in the sentence, iterate through its prefixes. For each prefix, check if it exists as a complete word (root) in the Trie. If found, replace the sentence word with this shortest root and move to the next sentence word.

#### **6. Word Squares**

- **Difficulty:** Hard
- **Description:** Given an array of unique strings `words`, return all the word squares you can build from `words`. A sequence of strings forms a valid word square if the `k`-th row and `k`-th column read the same string, where `0 <= k < max(numRows, numColumns)`.
- **Reason:** Backtracking problem where a Trie is used to efficiently find words with a specific prefix. When building the square row by row, the columns formed so far dictate the required prefixes for the next words.
- **Focus:** Build a Trie of all words. Use backtracking to build the square. If `k` rows are filled, the `j`-th character of the `(k+1)`-th row must match the `(k+1)`-th character of the `j`-th row. This forms a prefix for the `(k+1)`-th word. Use the Trie to find all words starting with this prefix.

#### **7. Concatenated Words**

- **Difficulty:** Hard
- **Description:** Given an array of strings `words` (without duplicates), return all the concatenated words in the given list of `words`. A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
- **Reason:** For each word, check if it can be formed by concatenating other words from the list. A Trie of all words can help efficiently check if prefixes are valid words. This often combines Trie with DP or DFS.
- **Focus:** Insert all words into a Trie. For each `word` in `words`, use DFS/DP to check if it can be segmented into other words present in the Trie. Ensure the concatenated word is formed by at least two shorter words.

#### **8. Palindrome Pairs** (Trie-based solution)

- **Difficulty:** Hard
- **Description:** Given a list of unique `words`, return all pairs of distinct indices `(i, j)` in the given list, so that the concatenation of the two words `words[i] + words[j]` is a palindrome.
- **Reason:** A Trie can be used to efficiently search for words that, when appended or prepended to a given word, form a palindrome. Store words (or their reverses) in a Trie.
- **Focus:** For each word `w1`, consider splitting it into `prefix + suffix`.
  1.  If `suffix` is a palindrome, search for `reverse(prefix)` in the Trie.
  2.  If `prefix` is a palindrome, search for `reverse(suffix)` in the Trie (if `suffix` is not empty).
      Store indices of words in Trie nodes. Special handling for empty strings.

#### **9. Design Search Autocomplete System**

- **Difficulty:** Hard
- **Description:** Design a search autocomplete system. For each character typed (except '#'), return the top 3 historical hot sentences that have the same prefix.
- **Reason:** A Trie can store all sentences. Each Trie node can store information about sentences passing through it (or ending at it) and their frequencies/hotness.
- **Focus:** Each Trie node represents a prefix. Store sentences (or references to them) and their counts/scores in the Trie nodes. When a prefix is typed, traverse to the corresponding Trie node and retrieve/sort the sentences associated with that node and its descendants.

#### **10. Shortest Unique Prefix** (Conceptual, often seen in variations)

- **Difficulty:** Medium (Conceptual)
- **Description:** Given a list of words, find the shortest unique prefix for each word. If a word itself is a prefix of another word (e.g., "apple", "apply"), its unique prefix might be the word itself.
- **Reason:** A Trie can help. During insertion or a separate traversal, count how many words pass through each node. A unique prefix ends at a node (or just before a node) where the path becomes unique to that word, or at a node with a count of 1.
- **Focus:** Augment Trie nodes to store a frequency count (number of words passing through/ending at this prefix). To find the shortest unique prefix for a word, traverse the Trie. The prefix is unique up to the point where the node count becomes 1.

### Practice Questions (To Apply Patterns)

#### **1. Longest Word in Dictionary**

- **Difficulty:** Easy
- **Description:** Given an array of strings `words` representing an English Dictionary, return the longest word in `words` that can be built one character at a time by other words in `words`. If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

#### **2. Map Sum Pairs**

- **Difficulty:** Medium
- **Description:** Design a map that allows you to store key-value pairs and supports two operations: `insert(key, val)` and `sum(prefix)`. `insert` adds a key-value pair to the map. If the key already existed, the original key-value pair will be overridden to the new one. `sum` returns the sum of all values of keys that have the given `prefix`.

#### **3. Index Pairs of a String**

- **Difficulty:** Easy
- **Description:** Given a string `text` and an array of strings `words`, return an array of all index pairs `[i, j]` so that the substring `text[i...j]` is in `words`.

#### **4. Stream of Characters**

- **Difficulty:** Hard
- **Description:** Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of `words`.

#### **5. Search Suggestions System**

- **Difficulty:** Medium
- **Description:** You are given an array of strings `products` and a string `searchWord`. Design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested products should have common prefix with `searchWord`. If there are more than three products with a common prefix return the three lexicographically minimums products.

#### **6. Maximum XOR With an Element From Array**

- **Difficulty:** Hard
- **Description:** You are given two 0-indexed integer arrays `nums` and `queries`, where `queries[i] = [xi, mi]`. For the `i`-th query, find the maximum XOR value of `xi` and any element of `nums` that is less than or equal to `mi`. If all elements in `nums` are larger than `mi`, then the answer is -1.

#### **7. Count Pairs With XOR in a Range**

- **Difficulty:** Hard
- **Description:** Given a 0-indexed integer array `nums` and two integers `low` and `high`, return the number of pairs `(i, j)` such that `i < j` and `low <= (nums[i] XOR nums[j]) <= high`.

#### **8. Number of Matching Subsequences**

- **Difficulty:** Medium
- **Description:** Given a string `s` and an array of strings `words`, return the number of `words[i]` that is a subsequence of `s`. (Trie can be one way to optimize checking multiple words, though other approaches exist).

#### **9. Camelcase Matching**

- **Difficulty:** Medium
- **Description:** Given an array of strings `queries` and a string `pattern`, return a boolean array `answer` where `answer[i]` is `true` if `queries[i]` matches `pattern`, and `false` otherwise. A query word `queries[i]` matches `pattern` if you can insert lowercase English letters into `pattern` so that it equals `queries[i]`.

#### **10. Remove Sub-Folders from the Filesystem**

- **Difficulty:** Medium
- **Description:** Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing. If a `folder[i]` is located within another `folder[j]`, it is called a sub-folder of it. The format of a path is one or more concatenated strings of the form: `/` followed by one or more lowercase English letters.

#### **11. Concatenated Words** (Practice)

- **Difficulty:** Hard
- **Description:** Given an array of strings `words` (without duplicates), return all the concatenated words in the given list of `words`.

#### **12. Word Search II** (Practice)

- **Difficulty:** Hard
- **Description:** Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.

#### **13. Implement Magic Dictionary**

- **Difficulty:** Medium
- **Description:** Design a magic dictionary to determine if a given word can be changed to match a word in the dictionary by changing exactly one character.

#### **14. Longest Common Suffix Queries**

- **Difficulty:** Hard
- **Description:** You are given two arrays of strings `wordsContainer` and `wordsQuery`. For each `wordsQuery[i]`, find the string from `wordsContainer` that has the longest common suffix with `wordsQuery[i]`. If there are ties, choose the string with the smallest index in `wordsContainer`. If there is no common suffix, choose the string with the smallest index in `wordsContainer`. Return an array of integers `ans`, where `ans[i]` is the index of the chosen string in `wordsContainer` for `wordsQuery[i]`. (Hint: Use a Trie of reversed words).

#### **15. Find All People With Secret**

- **Difficulty:** Hard
- **Description:** You are given an integer `n` indicating there are `n` people numbered from `0` to `n - 1`. You are also given a 0-indexed 2D integer array `meetings` where `meetings[i] = [xi, yi, timei]` indicates that person `xi` and person `yi` have a meeting at `timei`. A person may attend multiple meetings at the same time. Finally, you are given an integer `firstPerson`. Person `0` has a secret and initially shares the secret with `firstPerson` at time `0`. This secret is then shared every time a meeting takes place with a person that already knows the secret. More formally, for every meeting, if a person `xi` knows the secret at `timei`, then they will share the secret with person `yi` at `timei` as well, and vice versa. The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame. Return a list of all people that know the secret after all the meetings have taken place. You may return the answer in any order. (While not purely Trie, graph traversal is key; Trie could organize meetings by time if needed, but usually sorting is enough).

#### **16. Prefix and Suffix Search**

- **Difficulty:** Hard
- **Description:** Design a special dictionary that searches the words in it by a prefix and a suffix. Implement the `WordFilter` class: `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary. `f(string prefix, string suffix)` Returns the index of the word in the dictionary that has the `prefix` and the `suffix`. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1. (Hint: Store `suffix#word` in a Trie).

#### **17. Palindrome Pairs** (Practice)

- **Difficulty:** Hard
- **Description:** Given a list of unique `words`, return all pairs of distinct indices `(i, j)` in the given list, so that the concatenation of the two words `words[i] + words[j]` is a palindrome.

#### **18. Design File System**

- **Difficulty:** Medium
- **Description:** You are asked to design a file system that allows you to create new paths and assign them a value. The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. You are also given a `createPath(path, value)` function, which creates all intermediate directories if they do not exist.

#### **19. Autocomplete System using Trie** (Conceptual, similar to Design Search Autocomplete System)

- **Difficulty:** Hard
- **Description:** Design an autocomplete system. When a user types a character, the system should return a list of suggested words that start with the characters typed so far. The suggestions should be sorted by frequency (most frequent first). If frequencies are the same, sort lexicographically.

#### **20. Count Substrings That Differ by One Character**

- **Difficulty:** Medium
- **Description:** Given two strings `s` and `t`, find the number of ways you can choose a non-empty substring of `s` and replace a single character by a different character such that the resulting substring is a substring of `t`. (Trie can be used to store substrings of t for efficient lookup, though other DP/hashing solutions exist).
