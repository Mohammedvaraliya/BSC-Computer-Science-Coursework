from collections import deque

def iterativeDFS(graph, start):
    stack = deque()
    visited = []
    stack.appendleft(start)

    while stack:
        node = stack.popleft()

        if node in visited:
            continue

        visited.append(node)
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.appendleft(neighbor)





if __name__ == "__main__":

    Graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": []
    }

    start = "A"

    iterativeDFS(Graph, start)