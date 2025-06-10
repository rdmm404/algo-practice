## Graphs (including BFS, DFS, Adjacency List/Matrix representations, Connectivity, Basic Shortest Path Algorithms, Topological Sort)

### Study Questions (To Learn Patterns)

#### **1. Number of Islands**

- **Difficulty:** Medium
- **Description:** Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
- **Reason:** Fundamental graph traversal (DFS or BFS) on a grid. Each time an unvisited '1' is found, start a traversal to mark all connected land cells as visited and increment the island count.
- **Focus:** Understand how to represent the grid as a graph implicitly. Implement DFS (recursive or iterative with a stack) or BFS (with a queue) to explore connected components. Manage a `visited` set/matrix.

#### **2. Clone Graph**

- **Difficulty:** Medium
- **Description:** Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value and a list of its neighbors.
- **Reason:** Demonstrates graph traversal (DFS or BFS) while simultaneously building the cloned graph. A hash map is crucial to store `original_node -> cloned_node` mappings to avoid re-cloning and to connect neighbors correctly.
- **Focus:** Use a HashMap to keep track of visited/cloned nodes. When visiting a node, if not cloned, create a copy and store it in the map. Then, for each neighbor, recursively clone/retrieve its copy from the map and add it to the current cloned node's neighbors.

#### **3. Course Schedule**

- **Difficulty:** Medium
- **Description:** There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses. Otherwise, return `false`.
- **Reason:** Classic application of topological sort (detecting cycles in a directed graph). Can be solved using Kahn's algorithm (BFS-based with in-degrees) or DFS-based cycle detection.
- **Focus:** For Kahn's: build an adjacency list and an in-degree array. Start BFS with nodes having an in-degree of 0. When a node is processed, decrement the in-degree of its neighbors. If a neighbor's in-degree becomes 0, add it to the queue. If the count of visited nodes equals `numCourses`, it's possible. For DFS: use visited states (e.g., 0=unvisited, 1=visiting, 2=visited) to detect back-edges indicating a cycle.

#### **4. Pacific Atlantic Water Flow**

- **Difficulty:** Medium
- **Description:** You are given an `m x n` integer matrix `heights` representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges. Water can only flow in four directions (up, down, left, or right) from a cell to an adjacent cell with height equal or lower. Find a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
- **Reason:** Involves starting BFS/DFS from the ocean borders inwards. Maintain two `visited` sets/matrices, one for cells reachable from the Pacific and one for cells reachable from the Atlantic. The intersection is the answer.
- **Focus:** Perform two separate multi-source BFS/DFS traversals. One starts from all cells adjacent to the Pacific, marking reachable cells. The other starts from cells adjacent to the Atlantic. The condition for flow is `neighbor_height >= current_height`.

#### **5. Word Ladder**

- **Difficulty:** Hard
- **Description:** A transformation sequence from word `beginWord` to `word endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that every adjacent pair of words differs by a single letter, and every `si` is in `wordList`. `sk == endWord`. Given `beginWord`, `endWord`, and `wordList`, return the length of the shortest transformation sequence, or 0 if no such sequence exists.
- **Reason:** A shortest path problem on an implicit graph where nodes are words and an edge exists if two words differ by one letter. BFS is ideal for finding the shortest path in an unweighted graph.
- **Focus:** Understand how to generate neighbors (words differing by one letter). Use BFS to explore words level by level. Keep track of visited words to avoid cycles and redundant work. Pre-processing `wordList` for faster neighbor lookups (e.g., using wildcard patterns) can be beneficial.

#### **6. Rotting Oranges**

- **Difficulty:** Medium
- **Description:** You are given an `m x n` grid where each cell can have one of three values: `0` (empty), `1` (fresh), or `2` (rotten). Every minute, any fresh orange 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes until no cell has a fresh orange. If impossible, return -1.
- **Reason:** Multi-source BFS. Rotten oranges spread to fresh ones simultaneously. The levels in BFS correspond to minutes.
- **Focus:** Initialize the queue with all initially rotten oranges. Perform BFS. In each step (minute), rot all adjacent fresh oranges. Keep track of the number of fresh oranges. If after BFS, fresh oranges still exist, it's impossible.

#### **7. Network Delay Time**

- **Difficulty:** Medium
- **Description:** You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`. We will send a signal from a given node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. If it is impossible, return -1.
- **Reason:** A single-source shortest path problem on a weighted graph. Dijkstra's algorithm (using a min-priority queue) or Bellman-Ford (if negative weights were allowed, though not here) are suitable.
- **Focus:** For Dijkstra's: maintain an array of minimum distances to each node, initialized to infinity. Use a min-priority queue storing `(time_to_reach_node, node_id)`. Start with `(0, k)`. When extracting a node, relax its neighbors: if a shorter path to a neighbor is found, update its distance and add/update it in the priority queue. The answer is the maximum distance in the distances array (if all reachable).

#### **8. Course Schedule II**

- **Difficulty:** Medium
- **Description:** There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites`. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible, return an empty array.
- **Reason:** This is the problem of finding a topological sort order itself, not just detecting a cycle.
- **Focus:** Implement Kahn's algorithm (BFS with in-degrees) or DFS-based topological sort. For Kahn's, add nodes to the result list as they are dequeued. For DFS, add a node to the result list (or front of a list) after all its descendants have been visited.

#### **9. Is Graph Bipartite?**

- **Difficulty:** Medium
- **Description:** Given an undirected `graph`, return `true` if and only if it is bipartite. A graph is bipartite if we can partition its nodes into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
- **Reason:** Can be solved using BFS or DFS by trying to "color" the graph with two colors. If an edge connects two nodes of the same color, it's not bipartite.
- **Focus:** Maintain a `colors` array (e.g., 0=uncolored, 1=colorA, -1=colorB). Start traversal from an uncolored node, assign it a color. For its neighbors, assign the opposite color. If a neighbor is already colored and has the same color as the current node, return false. Process all connected components.

#### **10. Find if Path Exists in Graph**

- **Difficulty:** Easy
- **Description:** There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1`. The edges in the graph are represented as a 2D integer array `edges`. Given the `source` and `destination` vertices, return `true` if there is a valid path from `source` to `destination`, or `false` otherwise.
- **Reason:** Basic graph connectivity problem. Solvable with BFS or DFS starting from the `source` and checking if `destination` is visited.
- **Focus:** Build an adjacency list. Perform BFS or DFS. Maintain a `visited` set. If `destination` is reached, return true. If traversal completes without reaching `destination`, return false.

#### **11. Shortest Path in Binary Matrix**

- **Difficulty:** Medium
- **Description:** Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. A clear path is a path from the top-left cell `(0,0)` to the bottom-right cell `(n-1,n-1)` such that all visited cells are `0` and all adjacent cells are 8-directionally connected. If there is no clear path, return -1.
- **Reason:** BFS is ideal for finding the shortest path in an unweighted grid graph.
- **Focus:** Use BFS. Each state in the queue can be `(row, col, distance)`. Mark visited cells (e.g., by changing their value in the grid or using a separate visited matrix). Explore 8 directions.

#### **12. All Paths From Source to Target**

- **Difficulty:** Medium
- **Description:** Given a directed acyclic graph (DAG) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in any order.
- **Reason:** A classic DFS with backtracking problem. Explore paths, and when the target is reached, add the current path to the results.
- **Focus:** Implement DFS. Maintain the `current_path`. When moving to a neighbor, add it to `current_path`. Recursively call DFS. After the recursive call returns (backtracking), remove the neighbor from `current_path`.

### Practice Questions (To Apply Patterns)

#### **1. Find Center of Star Graph**

- **Difficulty:** Easy
- **Description:** There is an undirected star graph consisting of `n` nodes labeled from 1 to `n`. A star graph is a graph where there is one center node and exactly `n - 1` edges that connect the center node with every other node. You are given a 2D integer array `edges`. Return the center of the given star graph.

#### **2. Keys and Rooms**

- **Difficulty:** Medium
- **Description:** There are `N` rooms and you start in room `0`. Each room has a distinct number in `0, 1, ..., N-1`, and each room may have some keys to access the next room. Return `true` if and only if you can enter every room.

#### **3. Number of Connected Components in an Undirected Graph**

- **Difficulty:** Medium
- **Description:** You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph. Return the number of connected components in the graph. (Can use Union-Find or BFS/DFS).

#### **4. Graph Valid Tree**

- **Difficulty:** Medium
- **Description:** You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi`. Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise. (A tree is connected and has no cycles, or has n-1 edges and is connected/acyclic).

#### **5. Cheapest Flights Within K Stops**

- **Difficulty:** Medium
- **Description:** There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]`. You are also given three integers `src`, `dst`, and `k`. Return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return -1. (Variation of Bellman-Ford or modified Dijkstra).

#### **6. Reconstruct Itinerary**

- **Difficulty:** Hard
- **Description:** You are given a list of airline `tickets` where `tickets[i] = [from_i, to_i]`. Reconstruct the itinerary in order and return it. All of the tickets belong to a man who departs from "JFK". Thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. (Hierholzer's algorithm or DFS with backtracking).

#### **7. Minimum Height Trees**

- **Difficulty:** Medium
- **Description:** A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree. Given a tree with `n` nodes labeled from `0` to `n - 1`, and an array `edges`. Return a list of all minimum height trees' root labels.

#### **8. Alien Dictionary**

- **Difficulty:** Hard
- **Description:** There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are sorted lexicographically by the rules of this new language. Derive the order of letters in this language. If the order is invalid, return `""`. If there are multiple valid orders, return any of them.

#### **9. Redundant Connection**

- **Difficulty:** Medium
- **Description:** In this problem, a tree is an undirected graph that is connected and has no cycles. You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges`. Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input. (Union-Find is good here).

#### **10. Number of Provinces**

- **Difficulty:** Medium
- **Description:** There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`. A province is a group of directly or indirectly connected cities and no other cities outside of the group. You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i`-th city and the `j`-th city are directly connected, and `isConnected[i][j] = 0` otherwise. Return the total number of provinces.

#### **11. Satisfiability of Equality Equations**

- **Difficulty:** Medium
- **Description:** You are given an array of strings `equations` that represent relationships between variables. Each string `equations[i]` is of length 4 and has one of two different forms: `"a==b"` or `"a!=b"`. Here, `a` and `b` are lowercase letters (not necessarily different) that represent variable names. Return `true` if it is possible to assign integers to variable names so as to satisfy all the given equations, or `false` otherwise. (Union-Find).

#### **12. Evaluate Division**

- **Difficulty:** Medium
- **Description:** You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. You are also given some `queries`. For each `query[j] = [Cj, Dj]`, you need to find `Cj / Dj = ?`. Return the answers. If any single answer cannot be determined, return -1.0. (Graph traversal where edge weights are ratios).

#### **13. Flower Planting With No Adjacent**

- **Difficulty:** Easy
- **Description:** You have `n` gardens, labeled from `1` to `n`, and an array `paths` where `paths[i] = [xi, yi]` describes a bidirectional path between garden `xi` to garden `yi`. Each garden has at most 3 paths coming into or leaving it. Your task is to choose a flower type for each garden from 1, 2, 3, or 4 so that no two gardens connected by a path have the same type of flower. Return any valid assignment.

#### **14. Find the Town Judge**

- **Difficulty:** Easy
- **Description:** In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge. If the town judge exists, then: The town judge trusts nobody. Everybody (except for the town judge) trusts the town judge. There is exactly one person that satisfies properties 1 and 2. You are given an array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`. Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

#### **15. Path with Maximum Probability**

- **Difficulty:** Medium
- **Description:** You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a, b]` is an undirected edge between nodes `a` and `b` with success probability `succProb[i]`. Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability. If there is no path, return 0. (Dijkstra-like, maximizing product of probabilities).

#### **16. Connecting Cities With Minimum Cost**

- **Difficulty:** Medium
- **Description:** There are `n` cities labeled from `1` to `n`. You are given the integer `n` and an array `connections` where `connections[i] = [xi, yi, costi]` indicates the cost to connect city `xi` and city `yi` directly. Return the minimum cost to connect all the `n` cities such that there is at least one path between any two cities. If it is impossible to connect all the `n` cities, return -1. (Minimum Spanning Tree - Kruskal's or Prim's).

#### **17. Critical Connections in a Network**

- **Difficulty:** Hard
- **Description:** There are `n` servers numbered from `0` to `n - 1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [ai, bi]` represents a connection between servers `ai` and `bi`. Any server can reach any other server directly or indirectly through the network. A critical connection is a connection that, if removed, will make some server unable to reach some other server. Return all critical connections in the network in any order. (Tarjan's bridge-finding algorithm or similar).

#### **18. Shortest Path with Alternating Colors**

- **Difficulty:** Medium
- **Description:** You are given an integer `n`, the number of nodes in a directed graph where the nodes are labeled from `0` to `n - 1`. You are also given two 2D integer arrays `redEdges` and `blueEdges` where `redEdges[i] = [ui, vi]` indicates a directed red edge from node `ui` to node `vi`, and `blueEdges[j] = [uj, vj]` indicates a directed blue edge from node `uj` to node `vj`. Return an array `answer` of length `n`, where each `answer[x]` is the length of the shortest path from node `0` to node `x` such that the edge colors alternate along the path. If such a path does not exist, return -1.

#### **19. The Maze II**

- **Difficulty:** Medium
- **Description:** There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. Given the ball's `start` position, the `destination` and the `maze`, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

#### **20. Optimize Water Distribution in a Village**

- **Difficulty:** Hard
- **Description:** There are `n` houses in a village. We want to supply water for all the houses by building wells and laying pipes. For each house `i`, we can either build a well inside it directly with cost `wells[i - 1]` (note the 0-indexing for wells array), or pipe water from another well to it. The costs to lay pipes between houses are given by the array `pipes`, where each `pipes[j] = [house1_j, house2_j, cost_j]` represents the cost to connect `house1_j` and `house2_j` with a pipe. Return the minimum total cost to supply water to all houses. (MST problem with a virtual node for wells).
