## Practical 1

## Problem Statement

**Breadth First Search & Iterative Depth First Search**

1. Implement the Breadth First Search algorithm to solve a given problem.
2. Implement the Iterative Depth First Search algorithm to solve the same problem.
3. Compare the performance and efficiency of both algorithms.

---

## Algorithms

**Breadth First Search algorithm**

1. Start
1. Initialize an empty `visited` list to keep track of visited nodes.
2. Initialize an empty `queue` to store nodes that need to be explored.
3. Enqueue the `start` node into the `queue`.
1. Initialize a `m` variable.
4. While the `queue` is not empty:
   - Deque a node from the left of the `queue` and assign it to `m`.
   - Print node `m`.
   - If node `m` is equal to the `destination`, stop the traversal.
   - For each neighbor `neighbour` of node `m`:
     - If `neighbour` is not in the `visited` list:
       - Mark `neighbour` as visited by adding it to the `visited` list.
       - Enqueue `neighbour` into the `queue`.
5. End.

---

**Time and Space Complexity**

1. Time complexity - $O(|V| + |E|)$ where $|V|$ is the number of vertices in the graph and $|E|$ is the number of edges in the graph.
2.  Space complexity - $O(|V|)$ where $|V|$ is the number of nodes in the graph.

---

**Iterative Depth First Search algorithm**

1. Start
1. Import the `deque` class from the `collections` module.
3. Create an empty `stack` using the `deque` class and an empty `visited` list.
4. Append the `start` node to the `stack`.
1. Initialize a `node` variable.
5. While the `stack` is not empty:
   - Pop a node from the left of the `stack` and assign it to `node`.
   - If `node` is already in the `visited` list, skip to the next iteration.
   - Add `node` to the `visited` list and print it.
   - For each neighbor `neighbor` of `node`:
      - If `neighbor` is not in the `visited` list, appendleft it to the `stack`.
6. End

---

**Time and Space Complexity**

1. Time complexity - $O(|V| + |E|)$ where $|V|$ is the number of vertices in the graph and $|E|$ is the number of edges in the graph.
2.  Space complexity - $O(|V|)$ where $|V|$ is the number of nodes in the graph.

---

## Comparison of the algorithms

1. While Breadth First Search and Iterative Depth First Search have similar time and space complexity, however the differences lies in completeness.
2. Completeness is guarantee that a given algorithm will eventually reach goal state.
3. Breadth First Search algorithm is complete, depth first search on the other hand is not complete i.e there is a possibility that the algorithm would not end up in a goal state eventually running an infinite loop.

---