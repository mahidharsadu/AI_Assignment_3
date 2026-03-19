V = 6
INF = 9999

def min_distance(dist, visited):
    minimum = INF
    index = -1

    for i in range(V):
        if not visited[i] and dist[i] <= minimum:
            minimum = dist[i]
            index = i

    return index


def dijkstra(graph, src):
    dist = [INF] * V
    visited = [False] * V

    dist[src] = 0

    for _ in range(V - 1):
        u = min_distance(dist, visited)
        visited[u] = True

        for v in range(V):
            if (not visited[v] and graph[u][v] != 0 and
                    dist[u] + graph[u][v] < dist[v]):
                dist[v] = dist[u] + graph[u][v]

    print("Shortest distances from source city:\n")

    for i in range(V):
        print(f"City {i} distance = {dist[i]}")


graph = [
    [0, 1400, 0, 1500, 0, 0],
    [1400, 0, 980, 0, 0, 0],
    [0, 980, 0, 0, 570, 350],
    [1500, 0, 0, 0, 0, 0],
    [0, 0, 570, 0, 0, 0],
    [0, 0, 350, 0, 0, 0]
]

dijkstra(graph, 0)
