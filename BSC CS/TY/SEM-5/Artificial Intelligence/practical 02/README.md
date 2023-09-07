## Practical 02

## Problem Statement

**A * Search and Recursive Best-First Search**

1. Implement the A* Search algorithm for solving a pathfinding problem.
2. Implement the Recursive Best-First Search algorithm for the same problem.
3. Compare the performance and effectiveness of both algorithms.


### A * Search

1. A* search is a popular pathfinding algorithm that uses a combination of the cost to reach a node and the heuristic cost from the node to the goal to prioritize which nodes to explore. It operates by maintaining a priority queue of paths based on the cost function `f(n) = g(n) + h(n)`, where `g(n)` is the cost to reach the node and `h(n)` is the estimated cost from the node to the goal (the heuristic).

2. Here's a step-by-step run-through of A*:

3. We start at "versova" with `f(versova) = g(versova) + h(versova) = 0 + 1820 = 1820`. The neighbors are "kamdhenu signal", "juhu link rd (1)", and "dn nagar".

4. "kamdhenu signal": `f(kamdhenu signal) = g(kamdhenu signal) + h(kamdhenu signal) = 476 (cost from versova to kamdhenu signal) + 1560 = 2036`

5. "juhu link rd (1)": `f(juhu link rd (1)) = g(juhu link rd (1)) + h(juhu link rd (1)) = 106 + 1760 = 1866`

6. "dn nagar": `f(dn nagar) = g(dn nagar) + h(dn nagar) = 864 + 1390 = 2254`

7. Choose "juhu link rd (1)" as it has the smallest `f`.

8. From "juhu link rd (1)", there is only "orion sayi consultant pvt ltd": `f(orion sayi consultant pvt ltd) = g(orion sayi consultant pvt ltd) + h(orion sayi consultant pvt ltd) = 106 (cost from versova to juhu link rd (1)) + 1740 (cost from juhu link rd (1) to orion sayi consultant pvt ltd) + 146 = 1992`

9. Choose "orion sayi consultant pvt ltd".

10. From "orion sayi consultant pvt ltd", there is only "juhu circle": `f(juhu circle) = g(juhu circle) + h(juhu circle) = 106 (cost from versova to juhu link rd (1)) + 1740 (cost from juhu link rd (1) to orion sayi consultant pvt ltd) + 148 (cost from orion sayi consultant pvt ltd to juhu circle) + 0 = 1994`

11. So, the path found by A* is: "versova" -> "juhu link rd (1)" -> "orion sayi consultant pvt ltd" -> "juhu circle".

12. In this case, A* found the path with the least overall cost from "versova" to "juhu circle", even though it's not the path with the least heuristic cost at every step. The balance between the actual cost `g(n)` and heuristic cost `h(n)` helps A* to effectively find the shortest path to the goal.


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


## Algorithms

**A * Search algorithm**

1. start
2. 