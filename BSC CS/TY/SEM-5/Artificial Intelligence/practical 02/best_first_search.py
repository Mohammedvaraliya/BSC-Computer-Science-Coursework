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
        "versova": {"kamdhenu signal": 476, "juhu link rd (1)": 106, "dn nagar": 864},
        "kamdhenu signal": {"jay maharashtra stationary": 436, "juhu link rd (2)": 628},
        "juhu link rd (1)": {"orion sayi consultant pvt ltd": 1740},
        "dn nagar": {"rossoneri pizza": 178, "ajay stationary": 728},
        "jay maharashtra stationary": {"n dutta marg": 463},
        "juhu link rd (2)": {"juhu circle": 1100},
        "orion sayi consultant pvt ltd": {"juhu circle": 148},
        "rossoneri pizza": {"indian oil nagar": 206},
        "ajay stationary": {"wonder kitchen corner": 222},
        "n dutta marg": {"wonder kitchen corner": 306},
        "indian oil nagar": {"juhu circle": 1180},
        "wonder kitchen corner": {"juhu circle": 620},
        "juhu circle": {}
    }

    heuristic_graph = {
        "versova": 1820,
        "kamdhenu signal": 1560,
        "juhu link rd (1)": 1760,
        "dn nagar": 1390,
        "jay maharashtra stationary": 1160,
        "juhu link rd (2)": 1080,
        "orion sayi consultant pvt ltd": 146,
        "rossoneri pizza": 1220,
        "ajay stationary": 708,
        "n dutta marg": 708,
        "indian oil nagar": 1180,
        "wonder kitchen corner": 622,
        "juhu circle": 0
    }

    start = "versova"
    destination = "juhu circle"

    bestfirstsearch_traverse(Graph, heuristic_graph, start, destination, traverse="recursive")
