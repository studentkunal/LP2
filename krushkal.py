class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        result = []
        total_weight = 0

        self.graph.sort(key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        i = 0
        e = 0

        # ✅ safer loop
        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                result.append((u, v, w))
                total_weight += w
                e += 1
                self.union(parent, rank, x, y)

        print("\nMinimum Spanning Tree:")
        print("Edge \tWeight")

        for u, v, weight in result:
            print(f"{u} - {v} \t{weight}")

        print("Total Weight:", total_weight)


# 🔽 MAIN PART (THIS WAS MISSING)

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

g = Graph(V)

print("Enter edges (u v weight):")
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

g.kruskal_mst()
"""
Enter number of vertices: 4
Enter number of edges: 5
Enter edges (u v weight):
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4 """