class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    # Add edge (Undirected)
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Recursive DFS function
    def dfs(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    # DFS Traversal
    def dfs_traversal(self, start):
        visited = [False] * self.V
        self.dfs(start, visited)


# -------- Main Program --------
V = int(input("Enter number of vertices: "))
g = Graph(V)

E = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting vertex: "))

print("DFS Traversal:", end=" ")
g.dfs_traversal(start)

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
