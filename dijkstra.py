import sys

def dijkstra(graph, V, src):
    dist = [sys.maxsize] * V
    dist[src] = 0

    visited = [False] * V
    parent = [-1] * V   # To store path

    for _ in range(V):
        min_dist = sys.maxsize
        u = -1

        # Find minimum distance vertex
        for i in range(V):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True

        # Update neighbors
        for v in range(V):
            if graph[u][v] > 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    parent[v] = u

    # ✅ Proper formatted output
    print("\n{:<10}{:<10}{}".format("Vertex", "Distance", "Path"))
    for i in range(V):
        print("{:<10}{:<10}".format(i, dist[i]), end="")
        print_path(parent, i)
        print()   # important for next line


# Function to print path
def print_path(parent, j):
    if parent[j] == -1:
        print(j, end="")
        return
    print_path(parent, parent[j])
    print(f" -> {j}", end="")


# ===== USER INPUT =====
V = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (0 if no edge):")
graph = []
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

# ✅ Safety check (prevents your earlier error)
if len(graph) != V or any(len(row) != V for row in graph):
    print("Error: Matrix must be V x V")
    exit()

src = int(input("Enter source vertex: "))

dijkstra(graph, V, src)
"""

Vertices = 4

Matrix:
0 5 0 10
5 0 3 0
0 3 0 1
10 0 1 0

Source = 0 """