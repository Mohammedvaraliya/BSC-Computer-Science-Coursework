## Practical 02

## Problem Statement

**A* Search and Recursive Best-First Search**
1. Implement the A* Search algorithm for solving a pathfinding problem.
2. Implement the Recursive Best-First Search algorithm for the same problem.
3. Compare the performance and effectiveness of both algorithms.

### Best First Search


1. Best-First Search algorithm uses an evaluation function f(n) for each node and the evaluation function is construed as a cost estimate. So the node with the smallest evaluation is chosen. The evaluation function f(n) is typically a heuristic function h(n) that estimates the cost to reach the goal from the node n.

2. Given the problem you've provided, we are going to apply the Greedy Best-First Search algorithm which is a version of best-first search that uses only the heuristic function to decide which path to follow. The algorithm does not take into account the cost of reaching the current node when deciding on the path, it uses only the estimated cost to reach the goal from the current node.

3. To illustrate, the algorithm starts from "versova" and aims to reach "juhu circle". It will expand the node with the smallest heuristic value at each step. If multiple nodes have the same smallest heuristic value, it will choose one arbitrarily.

4. Here is the step-by-step illustration of the algorithm:

5. Start at "versova". The neighbours are "kamdhenu signal" (heuristic: 1560), "juhu link rd (1)" (heuristic: 1760), "dn nagar" (heuristic: 1390). Choose "dn nagar" as it has the smallest heuristic value.

6. From "dn nagar", the neighbours are "rossoneri pizza" (heuristic: 1220), "ajay stationary" (heuristic: 708). Choose "ajay stationary".

7. From "ajay stationary", the neighbour is "wonder kitchen corner" (heuristic: 622). Choose "wonder kitchen corner".

8. From "wonder kitchen corner", the neighbour is "juhu circle" (heuristic: 0). Choose "juhu circle".

9. So, the path found by the algorithm is "versova" -> "dn nagar" -> "ajay stationary" -> "wonder kitchen corner" -> "juhu circle".

10. Please note that this path is not necessarily the optimal path. The Greedy Best-First Search algorithm does not guarantee finding the shortest path. It aims to find a path as quickly as possible by always choosing the path that appears to be the best at each step, but this path may not be the shortest overall. In other words, it prioritizes speed over accuracy.
