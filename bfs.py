from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    # Add edge (Undirected Graph)
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Recursive BFS function
    def bfs_recursive(self, queue, visited):
        if not queue:
            return

        # Dequeue a vertex
        node = queue.popleft()
        print(node, end=" ")

        # Visit all adjacent vertices
        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

        # Recursive call
        self.bfs_recursive(queue, visited)

    # BFS driver function
    def bfs(self, start):
        visited = [False] * self.V
        queue = deque()

        visited[start] = True
        queue.append(start)

        print("BFS Traversal:")
        self.bfs_recursive(queue, visited)


# ----------- USER INPUT -----------

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

g = Graph(V)

print("Enter edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting vertex: "))

g.bfs(start)

"""
Enter number of vertices: 5
Enter number of edges: 4
Enter edges (u v):
0 1
0 2
1 3
1 4
Enter starting vertex: 0
"""
