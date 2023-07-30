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

    path, total_distance = a_star_search(Graph, heuristic_graph, start, destination)
    if path:
        print(f"Shortest path from '{start}' to '{destination}': {path}")
        print(f"Total distance of the path: {total_distance}")
    else:
        print("No path found.")
