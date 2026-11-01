#1------BFS------

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("BFS Traversal:")
bfs(graph, 'A')

#2------DFS------


def dfs(graph, node, visited):

    if node not in visited:
        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS Traversal:")

visited = set()

dfs(graph, 'A', visited)

#3-------Kruskal Algorithm-------


edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]


edges.sort(key=lambda x: x[2])

parent = [0, 1, 2, 3]


def find(x):
    while parent[x] != x:
        x = parent[x]
    return x


result = []
total = 0

for u, v, weight in edges:

    a = find(u)
    b = find(v)

    if a != b:
        result.append((u, v, weight))
        total += weight
        parent[a] = b

    if len(result) == 3:
        break


print("Edges in Minimum Spanning Tree:")

for u, v, weight in result:
    print(u, "--", v, "=", weight)

print("Total Cost:", total)



#4--------Prim's-----------
graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

n = 4

visited = [False] * n
visited[0] = True

result = []
total = 0

for _ in range(n - 1):

    minimum = 999
    x = y = 0

    for i in range(n):
        if visited[i]:

            for j in range(n):

                if not visited[j] and graph[i][j] != 0:

                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    result.append((x, y, minimum))
    total += minimum

    visited[y] = True


print("Edges in Minimum Spanning Tree:")

for x, y, weight in result:
    print(x, "--", y, "=", weight)

print("Total Cost:", total)



#5---------Dijkstra's--------



graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

n = 4

distance = [999] * n
visited = [False] * n

distance[0] = 0

for _ in range(n):

    minimum = 999
    u = -1

    for i in range(n):
        if not visited[i] and distance[i] < minimum:
            minimum = distance[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    # Update distances
    for v in range(n):

        if graph[u][v] != 0 and not visited[v]:

            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:
                distance[v] = new_distance


print("Shortest distances from vertex 0:")

for i in range(n):
    print("0 ->", i, "=", distance[i])





