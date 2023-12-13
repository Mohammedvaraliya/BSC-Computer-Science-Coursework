def bfs_traverse(visited, graph, start):
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)




if __name__ == "__main__":

    Graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": []
    }

    visited = []
    queue = []
    start = "A"

    bfs_traverse(visited, Graph, start)