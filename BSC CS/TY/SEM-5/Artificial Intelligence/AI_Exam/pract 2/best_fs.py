import heapq

def bestfirstsearch_iterative(graph, heuristic_graph, start, destination):
    visited = set()
    priority_queue = [(heuristic_graph[start], start, 0)]
    total_distance = 0

    while priority_queue:
        _, current_node, dist = heapq.heappop(priority_queue)
        visited.add(current_node)
        print(current_node)
        total_distance += dist

        if current_node == destination:
            return total_distance

        for neighbor, distance in graph[current_node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(priority_queue, (heuristic_graph[neighbor], neighbor, distance))

    return total_distance

def bestfirstsearch_recursive(graph, heuristic_graph, visited, priority_queue, destination, total_distance):
    if not priority_queue:
        return total_distance

    _, current_node, dist = heapq.heappop(priority_queue)
    visited.add(current_node)
    print(current_node)
    total_distance += dist

    if current_node == destination:
        return total_distance

    for neighbor, distance in graph[current_node].items():
        if neighbor not in visited:
            visited.add(neighbor)
            heapq.heappush(priority_queue, (heuristic_graph[neighbor], neighbor, distance))

    return bestfirstsearch_recursive(graph, heuristic_graph, visited, priority_queue, destination, total_distance)

def bestfirstsearch_traverse(graph, heuristic_graph, start, destination, traverse):
    visited = set()
    priority_queue = [(heuristic_graph[start], start, 0)]
    total_distance = 0

    if traverse == "iterative":
        total_distance = bestfirstsearch_iterative(graph, heuristic_graph, start, destination)
    elif traverse == "recursive":
        total_distance = bestfirstsearch_recursive(graph, heuristic_graph, visited, priority_queue, destination, total_distance)

    print(f"The final distance from '{start}' to '{destination}' is: {total_distance}")


if __name__ == "__main__":
    Graph = {
        "S": {"A": 1, "G": 10},
        "A": {"B": 2, "C": 1},
        "B": {"D" : 5},
        "C": {"D": 3, "G": 4},
        "D": {"G": 2},
        "G": {}
    }

    heuristic_graph = {
        "S": 5,
        "A": 3,
        "B": 4,
        "C": 2,
        "D": 6,
        "G": 0
    }

    start = "S"
    destination = "G"

    bestfirstsearch_traverse(Graph, heuristic_graph, start, destination, traverse="recursive")
