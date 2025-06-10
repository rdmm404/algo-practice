## HashMaps & HashSets

### Study Questions (To Learn Patterns)

#### **1. Two Sum**

- **Difficulty:** Easy
- **Description:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
- **Reason:** The quintessential HashMap problem. It demonstrates storing elements and their indices for quick lookups of complements.
- **Focus:** Understand how `value -> index` mapping in a HashMap allows O(1) average time complexity for finding the complement `target - nums[i]`.

#### **2. Contains Duplicate**

- **Difficulty:** Easy
- **Description:** Given an integer array `nums`, return `true` if any value appears at least twice in the array, and `false` if every element is distinct.
- **Reason:** A basic application of HashSet to efficiently check for the existence of an element before adding it, thus detecting duplicates.
- **Focus:** Observe how adding elements to a HashSet and checking its return value (or size before/after insertion) can identify duplicates in O(n) time.

#### **3. Group Anagrams**

- **Difficulty:** Medium
- **Description:** Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
- **Reason:** Shows using a HashMap where the key is a canonical representation of a string (e.g., sorted string or character count array) and the value is a list of anagrams.
- **Focus:** Learn to derive a unique key for items that should be grouped together (anagrams in this case) and use the HashMap to aggregate these items.

#### **4. Valid Sudoku**

- **Difficulty:** Medium
- **Description:** Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the standard Sudoku rules.
- **Reason:** Illustrates using HashSets (or arrays as frequency maps) to check for uniqueness within rows, columns, and 3x3 sub-boxes.
- **Focus:** Understand how to iterate through rows, columns, and sub-grids, using HashSets to ensure no number is repeated in any of these units. Pay attention to indexing for sub-grids.

#### **5. LRU Cache**

- **Difficulty:** Medium
- **Description:** Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement the `LRUCache` class.
- **Reason:** A classic design problem combining a HashMap (for O(1) key lookup) and a Doubly Linked List (for O(1) removal of LRU item and O(1) update of recently used item).
- **Focus:** Grasp the interplay between the HashMap (storing `key -> Node_in_DLL`) and the DLL (maintaining order of usage). Understand operations like `get` and `put` and how they affect both structures.

#### **6. Insert Delete GetRandom O(1)**

- **Difficulty:** Medium
- **Description:** Implement the `RandomizedSet` class: `RandomizedSet()` initializes the `RandomizedSet` object. `bool insert(int val)` inserts an item `val` into the set if not present. `bool remove(int val)` removes an item `val` from the set if present. `int getRandom()` returns a random element from the current set of elements. Each function should work in O(1) average time complexity.
- **Reason:** Demonstrates a clever use of a HashMap (to store `value -> index_in_list`) and a List/Array (to store elements) to achieve O(1) average time for all operations.
- **Focus:** Understand how `remove` works in O(1) by swapping the element to be removed with the last element in the list and then popping from the list, while updating the HashMap.

#### **7. Top K Frequent Elements**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.
- **Reason:** Combines HashMap for frequency counting with techniques like bucket sort or a min-heap to find the top K elements.
- **Focus:** First, use a HashMap to count frequencies. Then, explore how to efficiently extract the top K frequent elements (e.g., using a min-heap of size K or bucket sort based on frequencies).

#### **8. Subarray Sum Equals K**

- **Difficulty:** Medium
- **Description:** Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.
- **Reason:** Shows an advanced use of HashMaps to store prefix sums and their frequencies. If `current_sum - k` exists as a previous prefix sum, it means a subarray summing to `k` has been found.
- **Focus:** Understand the concept of prefix sums. The key insight is that if `sum[i] - sum[j] = k`, then the subarray `nums[j+1...i]` sums to `k`. The HashMap stores `sum[j]` and its count.

#### **9. Longest Consecutive Sequence**

- **Difficulty:** Medium
- **Description:** Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.
- **Reason:** Uses a HashSet to store all numbers for O(1) lookups. Then, for each number, it checks if it's the start of a sequence (i.e., `num-1` is not in the set) and extends the sequence.
- **Focus:** Learn how to iterate through numbers and, for each potential start of a sequence, count its length by checking for `num+1`, `num+2`, etc., in the HashSet. This avoids redundant checks.

#### **10. Find All Duplicates in an Array**

- **Difficulty:** Medium
- **Description:** Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears once or twice, return an array of all the integers that appears twice. You must write an algorithm that runs in O(n) time and uses only constant extra space.
- **Reason:** While the optimal solution uses in-place modification (array as hashmap), a HashSet approach is a valid first thought and good for understanding the trade-off. The optimal solution is a good contrast.
- **Focus:** For a HashSet solution, simply iterate and add to set; if add fails, it's a duplicate. For the O(1) space, understand how to use the sign of `nums[abs(nums[i])-1]` to mark visited numbers.

### Practice Questions (To Apply Patterns)

#### **1. Intersection of Two Arrays**

- **Difficulty:** Easy
- **Description:** Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

#### **2. Happy Number**

- **Difficulty:** Easy
- **Description:** Write an algorithm to determine if a number `n` is happy. A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy.

#### **3. Word Pattern**

- **Difficulty:** Easy
- **Description:** Given a `pattern` and a string `s`, find if `s` follows the same pattern. Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

#### **4. Isomorphic Strings**

- **Difficulty:** Easy
- **Description:** Given two strings `s` and `t`, determine if they are isomorphic. Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

#### **5. Minimum Index Sum of Two Lists**

- **Difficulty:** Easy
- **Description:** Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of their favorite restaurants represented by strings. You need to help them find out their common interest with the least list index sum.

#### **6. Unique Word Abbreviation**

- **Difficulty:** Medium
- **Description:** An abbreviation of a word follows the form `<first letter><number><last letter>`. Design a data structure that, given a dictionary of words, can quickly check if a given query word's abbreviation is unique in the dictionary.

#### **7. Logger Rate Limiter**

- **Difficulty:** Easy
- **Description:** Design a logger system that receives a stream of messages, each with a timestamp and a message string. It should print a message only if that same message has not been printed in the last 10 seconds.

#### **8. Design HashSet**

- **Difficulty:** Easy
- **Description:** Design a HashSet without using any built-in hash table libraries.

#### **9. Design HashMap**

- **Difficulty:** Easy
- **Description:** Design a HashMap without using any built-in hash table libraries.

#### **10. 4Sum II**

- **Difficulty:** Medium
- **Description:** Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of length `n`, return the number of tuples `(i, j, k, l)` such that `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`.

#### **11. Brick Wall**

- **Difficulty:** Medium
- **Description:** There is a rectangular brick wall in front of you with `n` rows of bricks. The `i`-th row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. For each row, a list of integers is given representing the width of each brick in this row from left to right. Your goal is to draw a vertical line from the top to the bottom and cross the least bricks.

#### **12. Longest Substring with At Most K Distinct Characters**

- **Difficulty:** Medium
- **Description:** Given a string `s` and an integer `k`, return the length of the longest substring of `s` that contains at most `k` distinct characters.

#### **13. Number of Boomerangs**

- **Difficulty:** Medium
- **Description:** You are given `n` points in the plane that are all distinct, where `points[i] = [x_i, y_i]`. A boomerang is a tuple of points `(i, j, k)` such that the distance between `i` and `j` equals the distance between `i` and `k` (the order of the tuple matters). Return the number of boomerangs.

#### **14. Palindrome Pairs**

- **Difficulty:** Hard
- **Description:** Given a list of unique words, return all pairs of distinct indices `(i, j)` in the given list, so that the concatenation of the two words `words[i] + words[j]` is a palindrome.

#### **15. Max Points on a Line**

- **Difficulty:** Hard
- **Description:** Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

#### **16. Design Twitter**

- **Difficulty:** Medium
- **Description:** Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

#### **17. Find Duplicate Subtrees**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

#### **18. Shortest Word Distance II**

- **Difficulty:** Medium
- **Description:** Design a data structure that takes a list of words `words` in the constructor and implements a method `shortest(word1, word2)` that returns the shortest distance between `word1` and `word2` in the list.

#### **19. Alert Using Same Key-Card Three or More Times in a One Hour Period**

- **Difficulty:** Medium
- **Description:** A company has a key-card system. Each employee has a key-card with a unique name. An employee can use their key-card to enter the company's building. The system records the name of the employee and the time they used the key-card. Given a list of key-card usage events, determine if any employee used their key-card three or more times in a one-hour period.

#### **20. Analyze User Website Visit Pattern**

- **Difficulty:** Medium
- **Description:** You are given two arrays of strings `username` and `website` and an integer array `timestamp`. All the arrays are of the same length. The `i`-th event means that the user `username[i]` visited the website `website[i]` at time `timestamp[i]`. A 3-sequence is a list of websites of length 3 sorted in ascending order of time of visit. Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such sequence.
