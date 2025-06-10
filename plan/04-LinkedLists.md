## Linked Lists

### Study Questions (To Learn Patterns)

#### **1. Reverse Linked List**

- **Difficulty:** Easy
- **Description:** Given the `head` of a singly linked list, reverse the list, and return the reversed list.
- **Reason:** Fundamental linked list manipulation. Introduces iterative (three pointers: prev, curr, next) and recursive approaches to reversing a list.
- **Focus:** Understand the pointer manipulations in the iterative solution. For the recursive solution, grasp the base case and how the "rest of the list" is reversed and then connected.

#### **2. Merge Two Sorted Lists**

- **Difficulty:** Easy
- **Description:** You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
- **Reason:** Classic problem demonstrating how to merge two sorted structures. Introduces the dummy head pattern for cleaner code.
- **Focus:** Learn to use a `dummy` head node to simplify edge cases (like an empty resulting list) and a `current` pointer to build the new list by comparing nodes from `list1` and `list2`.

#### **3. Linked List Cycle**

- **Difficulty:** Easy
- **Description:** Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
- **Reason:** Introduces Floyd's Tortoise and Hare (fast and slow pointer) algorithm for cycle detection.
- **Focus:** Understand why if there's a cycle, the fast pointer will eventually meet the slow pointer. Consider edge cases like an empty list or a list with one node.

#### **4. Remove Nth Node From End of List**

- **Difficulty:** Medium
- **Description:** Given the `head` of a linked list, remove the `n`-th node from the end of the list and return its head.
- **Reason:** Demonstrates the two-pointer technique where one pointer is advanced `n` steps ahead, and then both pointers move together until the first pointer reaches the end. The second pointer will then be at the node before the one to be removed.
- **Focus:** Pay attention to the use of a dummy head to handle cases where the head itself needs to be removed. Understand the relative positioning of the two pointers.

#### **5. Copy List with Random Pointer**

- **Difficulty:** Medium
- **Description:** A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`. Construct a deep copy of the list.
- **Reason:** Explores more complex list manipulation. Common solutions involve using a HashMap to map original nodes to copied nodes, or an O(1) space approach by interweaving copied nodes with original nodes.
- **Focus:** For the HashMap approach, understand the two-pass process: first create copies of all nodes and store mappings, then iterate again to set `next` and `random` pointers. For the interweaving approach, visualize the three steps: create copies, assign random pointers, separate lists.

#### **6. Add Two Numbers**

- **Difficulty:** Medium
- **Description:** You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
- **Reason:** Simulates arithmetic addition using linked lists, requiring handling of carry-overs and lists of different lengths.
- **Focus:** Learn to iterate through both lists simultaneously, calculate sum and carry at each step, and create new nodes for the result list. Use a dummy head for the result.

#### **7. Palindrome Linked List**

- **Difficulty:** Easy
- **Description:** Given the `head` of a singly linked list, return `true` if it is a palindrome.
- **Reason:** Combines several linked list techniques: find the middle, reverse the second half, and then compare the two halves.
- **Focus:** Understand each step: using fast/slow pointers to find the middle, reversing a portion of the list, and then comparing node values. Remember to restore the list if required (though not strictly necessary for just checking).

#### **8. Intersection of Two Linked Lists**

- **Difficulty:** Easy
- **Description:** Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.
- **Reason:** Presents a clever two-pointer approach where pointers traverse both lists. If they meet, it's the intersection. If one reaches the end, it jumps to the head of the other list.
- **Focus:** Understand why this pointer "resetting" strategy ensures that if an intersection exists, the pointers will meet at it after at most two traversals of each list combined.

#### **9. Reorder List**

- **Difficulty:** Medium
- **Description:** You are given the `head` of a singly linked-list. The list can be represented as: `L0 → L1 → … → Ln - 1 → Ln`. Reorder the list to be on the following form: `L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`. You may not modify the values in the list's nodes. Only nodes themselves may be changed.
- **Reason:** A multi-step problem: find the middle, reverse the second half, then merge the two halves in an alternating fashion.
- **Focus:** Break down the problem into sub-problems: finding the middle node, reversing a linked list, and then carefully interleaving nodes from two lists.

#### **10. Linked List Cycle II**

- **Difficulty:** Medium
- **Description:** Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.
- **Reason:** Extends Floyd's cycle detection algorithm. After finding the meeting point, one pointer is reset to the head, and both move one step at a time. Their next meeting point is the start of the cycle.
- **Focus:** Understand the mathematical proof or intuition behind why, after the first meeting, moving one pointer from the head and another from the meeting point at the same speed leads to the cycle's start.

### Practice Questions (To Apply Patterns)

#### **1. Delete Node in a Linked List**

- **Difficulty:** Easy
- **Description:** Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly. It is guaranteed that the node to be deleted is not a tail node.

#### **2. Remove Linked List Elements**

- **Difficulty:** Easy
- **Description:** Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return the new head.

#### **3. Middle of the Linked List**

- **Difficulty:** Easy
- **Description:** Given the `head` of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

#### **4. Convert Binary Number in a Linked List to Integer**

- **Difficulty:** Easy
- **Description:** Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number. Return the decimal value of the number in the linked list.

#### **5. Design Linked List**

- **Difficulty:** Medium
- **Description:** Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

#### **6. Odd Even Linked List**

- **Difficulty:** Medium
- -**Description:** Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list. The first node is considered odd, and the second node is even, and so on.

#### **7. Swap Nodes in Pairs**

- **Difficulty:** Medium
- **Description:** Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

#### **8. Rotate List**

- **Difficulty:** Medium
- **Description:** Given the `head` of a linked list, rotate the list to the right by `k` places.

#### **9. Partition List**

- **Difficulty:** Medium
- **Description:** Given the `head` of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`. You should preserve the original relative order of the nodes in each of the two partitions.

#### **10. Sort List**

- **Difficulty:** Medium
- **Description:** Given the `head` of a linked list, return the list after sorting it in ascending order. (Typically merge sort is used).

#### **11. Reverse Nodes in k-Group**

- **Difficulty:** Hard
- **Description:** Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list. `k` is a positive integer and is less than or equal to the length of the linked list.

#### **12. Flatten a Multilevel Doubly Linked List**

- **Difficulty:** Medium
- **Description:** You are given a doubly linked list, which also_nodes might have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on. Flatten the list so that all nodes appear in a single-level, doubly linked list.

#### **13. Split Linked List in Parts**

- **Difficulty:** Medium
- **Description:** Given the `head` of a singly linked list and an integer `k`, split the linked list into `k` consecutive linked list parts. The length of each part should be as equal as possible: no two parts should have a size differing by more than one.

#### **14. Next Greater Node In Linked List**

- **Difficulty:** Medium
- **Description:** You are given the `head` of a linked list with `n` nodes. For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is to the right of it and has a strictly larger value than it.

#### **15. Merge In Between Linked Lists**

- **Difficulty:** Medium
- **Description:** You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively. Remove `list1`'s nodes from the `a`-th node to the `b`-th node, and put `list2` in their place.

#### **16. Remove Duplicates from Sorted List**

- **Difficulty:** Easy
- **Description:** Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

#### **17. Remove Duplicates from Sorted List II**

- **Difficulty:** Medium
- **Description:** Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

#### **18. Add Two Numbers II**

- **Difficulty:** Medium
- **Description:** You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. (You are not allowed to modify the input lists directly, i.e., reversing the lists is not allowed unless you make copies).

#### **19. Plus One Linked List**

- **Difficulty:** Medium
- **Description:** Given a non-negative integer represented as a linked list of digits, plus one to the integer. The digits are stored such that the most significant digit is at the head of the list.

#### **20. Copy List with Random Pointer** (Practice applying the HashMap or interweaving method)

- **Difficulty:** Medium
- **Description:** A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`. Construct a deep copy of the list. (Re-listed for practice after studying the pattern).
