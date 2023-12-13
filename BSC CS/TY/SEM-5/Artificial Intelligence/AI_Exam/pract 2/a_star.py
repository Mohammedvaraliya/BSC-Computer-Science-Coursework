import heapq

def a_star_search(graph, heuristic_graph, start, destination):
    open_list = [(0, start)]
    closed_list = set()
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0
    parents = {}
    total_distance = 0

    while open_list:
        _, current_node = heapq.heappop(open_list)
        closed_list.add(current_node)

        if current_node == destination:
            path = []
            while current_node in parents:
                path.append(current_node)
                total_distance += graph[parents[current_node]][current_node]
                current_node = parents[current_node]
            path.append(start)
            path.reverse()
            return path, total_distance

        for neighbor, distance in graph[current_node].items():
            if neighbor in closed_list:
                continue

            tentative_g_score = g_scores[current_node] + distance
            if tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic_graph[neighbor] # f(n) = g(n) + h(n)
                heapq.heappush(open_list, (f_score, neighbor))
                parents[neighbor] = current_node

    return None


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

    path, total_distance = a_star_search(Graph, heuristic_graph, start, destination)
    if path:
        print(f"Shortest path from '{start}' to '{destination}': {path}")
        print(f"Total distance of the path: {total_distance}")
    else:
        print("No path found.")
