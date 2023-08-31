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

    visited = []
    queue = []
    start = "versova"

    bfs_traverse(visited, Graph, start)