from collections import deque

def iterativeDFS(graph, start, destination):
    stack = deque()
    visited = []
    stack.append(start)

    while stack:
        node = stack.popleft()

        if node in visited:
            continue

        visited.append(node)
        print(node)

        if node == destination:
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.appendleft(neighbor)




if __name__ == "__main__":

    Graph = {
        "versova" : ["kamdhenu signal", "juhu link rd (1)", "dn nagar"],
        "kamdhenu signal" : ["jay maharashtra stationary", "juhu link rd (2)"],
        "juhu link rd (1)" : ["orion sayi consultant pvt ltd"],
        "dn nagar" : ["rossoneri pizza", "ajay stationary"],
        "jay maharashtra stationary" : ["n dutta marg"],
        "juhu link rd (2)" : ["juhu circle"],
        "orion sayi consultant pvt ltd" : ["juhu circle"],
        "rossoneri pizza" : ["indian oil nagar"],
        "ajay stationary" : ["wonder kitchen corner"],
        "n dutta marg" : ["wonder kitchen corner"],
        "indian oil nagar" : ["juhu circle"],
        "wonder kitchen corner" : ["juhu circle"],
        "juhu circle" : []
    }

    start = "versova"
    destination = "juhu circle"

    iterativeDFS(Graph, start, destination)