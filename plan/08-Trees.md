Okay, here's the continuation of the plan, focusing on Trees.

## Trees (including Binary Trees, Binary Search Trees, N-ary Trees, Traversals, Construction, and Common Tree Algorithms)

### Study Questions (To Learn Patterns)

#### **1. Maximum Depth of Binary Tree**

- **Difficulty:** Easy
- **Description:** Given the `root` of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
- **Reason:** Introduces basic tree recursion (DFS). The depth is `1 + max(depth(left_child), depth(right_child))`.
- **Focus:** Understand the base case (null node returns 0) and how recursive calls build up the depth information from leaves to the root.

#### **2. Same Tree**

- **Difficulty:** Easy
- **Description:** Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
- **Reason:** Demonstrates simultaneous recursion on two trees to compare structure and values.
- **Focus:** Grasp the conditions for two nodes/subtrees being identical: both null, one null and other not, values differ, or recursive calls on children return false.

#### **3. Invert Binary Tree**

- **Difficulty:** Easy
- **Description:** Given the `root` of a binary tree, invert the tree, and return its root.
- **Reason:** A simple yet illustrative recursive problem. The core idea is to swap the left and right children of each node.
- **Focus:** Understand that the inversion happens at each node: invert left subtree, invert right subtree, then swap the current node's left and right children.

#### **4. Binary Tree Inorder Traversal**

- **Difficulty:** Easy
- **Description:** Given the `root` of a binary tree, return the inorder traversal of its nodes' values. (Left, Root, Right)
- **Reason:** Fundamental tree traversal. Important to understand both recursive and iterative (using a stack) solutions.
- **Focus:** For recursion: `traverse(left)`, process `root`, `traverse(right)`. For iteration: use a stack to simulate recursion; go left as far as possible, then pop, process, and go right.

#### **5. Binary Tree Level Order Traversal**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
- **Reason:** Introduces Breadth-First Search (BFS) for trees using a queue.
- **Focus:** Understand how a queue is used to process nodes level by level. Keep track of the number of nodes at the current level to know when a level ends and a new one begins.

#### **6. Validate Binary Search Tree**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
- **Reason:** Highlights BST properties. Solutions involve recursive checks with min/max ranges or using an inorder traversal (which should be sorted for a BST).
- **Focus:** For the range method: each node's value must be within a `(min_val, max_val)` range, which gets updated for its children. For inorder traversal: check if the sequence of visited nodes is strictly increasing.

#### **7. Lowest Common Ancestor of a Binary Search Tree**

- **Difficulty:** Easy
- **Description:** Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
- **Reason:** Leverages BST properties for an efficient solution. The LCA is where the paths to the two nodes diverge.
- **Focus:** If both nodes are smaller than the current root, LCA is in the left subtree. If both are larger, LCA is in the right. Otherwise, the current root is the LCA.

#### **8. Lowest Common Ancestor of a Binary Tree**

- **Difficulty:** Medium
- **Description:** Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
- **Reason:** A more general LCA problem than for BSTs. Common solutions involve recursion: if a node is one of the targets or its children contain the targets, it contributes to the LCA path.
- **Focus:** Understand the recursive approach: a node is the LCA if it's one of the targets and the other is in its subtree, or if targets are in its left and right subtrees. If only one target is found in a subtree, return that target.

#### **9. Construct Binary Tree from Preorder and Inorder Traversal**

- **Difficulty:** Medium
- **Description:** Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.
- **Reason:** Classic tree construction problem. The preorder gives the root, and inorder helps find elements in the left and right subtrees.
- **Focus:** The first element of `preorder` is the root. Find this root in `inorder` to determine the elements in the left and right subtrees. Recursively build these subtrees. Using a map for inorder indices speeds up lookups.

#### **10. Convert Sorted Array to Binary Search Tree**

- **Difficulty:** Easy
- **Description:** Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
- **Reason:** Demonstrates constructing a balanced BST. The middle element of the array becomes the root.
- **Focus:** Recursively pick the middle element of the current subarray as the root, then build the left subtree from the left half and the right subtree from the right half.

#### **11. Path Sum**

- **Difficulty:** Easy
- **Description:** Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.
- **Reason:** Basic DFS application to explore paths and check sums.
- **Focus:** In the recursive function, subtract the current node's value from the `targetSum`. If it's a leaf node and the remaining sum is zero, a path is found.

#### **12. Binary Tree Right Side View**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
- **Reason:** Can be solved using BFS (take the last element at each level) or DFS (traverse right child first, add node if level is visited for the first time).
- **Focus:** For BFS: at each level, the last node added to the queue (or processed) for that level is part of the right side view. For DFS: pass the current level; if the result list's size equals the current level, it's the first node seen at this level from the right.

#### **13. Diameter of Binary Tree**

- **Difficulty:** Easy
- **Description:** Given the `root` of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
- **Reason:** Requires calculating the height of subtrees. The diameter at a node is `height(left) + height(right)`. The overall diameter is the maximum of these values across all nodes.
- **Focus:** The recursive function should return the height of the current subtree, but also update a global/member variable for the maximum diameter found so far.

#### **14. Subtree of Another Tree**

- **Difficulty:** Easy
- **Description:** Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.
- **Reason:** Combines tree traversal (on `root`) with a tree equality check (like "Same Tree") when a potential starting node for `subRoot` is found.
- **Focus:** Recursively traverse `root`. At each node, check if it's identical to `subRoot` using a helper function. If not, check in the left and right children of `root`.

#### **15. N-ary Tree Preorder Traversal**

- **Difficulty:** Easy
- **Description:** Given the `root` of an n-ary tree, return the preorder traversal of its nodes' values. N-ary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.
- **Reason:** Extends the concept of preorder traversal (Root, Children) to trees with multiple children per node.
- **Focus:** For recursion: process the root, then iterate through its children and recursively call traversal for each child. For iteration: use a stack; push root, then when popping a node, process it and push its children onto the stack in reverse order (rightmost to leftmost).

### Practice Questions (To Apply Patterns)

#### **1. Minimum Depth of Binary Tree**

- **Difficulty:** Easy
- **Description:** Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

#### **2. Symmetric Tree**

- **Difficulty:** Easy
- **Description:** Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

#### **3. Balanced Binary Tree**

- **Difficulty:** Easy
- **Description:** Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

#### **4. Merge Two Binary Trees**

- **Difficulty:** Easy
- **Description:** You are given two binary trees `root1` and `root2`. Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree.

#### **5. Path Sum II**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node values, not node references.

#### **6. Binary Tree Zigzag Level Order Traversal**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

#### **7. Kth Smallest Element in a BST**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary search tree, and an integer `k`, return the `k`-th smallest value (1-indexed) of all the values of the nodes in the tree.

#### **8. Binary Tree Maximum Path Sum**

- **Difficulty:** Hard
- **Description:** A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

#### **9. Count Good Nodes in Binary Tree**

- **Difficulty:** Medium
- **Description:** Given a binary tree `root`, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.

#### **10. Populating Next Right Pointers in Each Node**

- **Difficulty:** Medium
- **Description:** You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. Populate each `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `NULL`.

#### **11. Serialize and Deserialize Binary Tree**

- **Difficulty:** Hard
- **Description:** Design an algorithm to serialize a binary tree into a string and deserialize the string back to the original binary tree.

#### **12. Find Duplicate Subtrees**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

#### **13. Construct Binary Tree from Inorder and Postorder Traversal**

- **Difficulty:** Medium
- **Description:** Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

#### **14. All Nodes Distance K in Binary Tree**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

#### **15. N-ary Tree Level Order Traversal**

- **Difficulty:** Medium
- **Description:** Given an n-ary tree, return the level order traversal of its nodes' values.

#### **16. Binary Tree Pruning**

- **Difficulty:** Medium
- **Description:** Given the `root` of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

#### **17. Sum Root to Leaf Numbers**

- **Difficulty:** Medium
- **Description:** You are given the `root` of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree represents a number. Return the total sum of all root-to-leaf numbers.

#### **18. Binary Search Tree Iterator**

- **Difficulty:** Medium
- **Description:** Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST).

#### **19. Delete Node in a BST**

- **Difficulty:** Medium
- **Description:** Given a `root` node reference of a BST and a `key`, delete the node with the given `key` in the BST. Return the `root` node reference (possibly updated) of the BST.

#### **20. Vertical Order Traversal of a Binary Tree**

- **Difficulty:** Hard
- **Description:** Given the `root` of a binary tree, calculate the vertical order traversal of the binary tree. For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.
