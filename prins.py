import sys

def prim_mst(graph, V):
    selected = [False] * V
    selected[0] = True   # Root vertex

    total_weight = 0     # 👉 NEW

    print("Root:", 0)    # 👉 NEW
    print("Edge \tWeight")
    
    for _ in range(V - 1):
        min_weight = sys.maxsize    
        x = 0
        y = 0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if (not selected[j]) and graph[i][j]:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            x = i
                            y = j
        
        print(f"{x} - {y} \t{graph[x][y]}")
        total_weight += graph[x][y]   # 👉 ADD THIS LINE
        selected[y] = True

    print("Total Weight:", total_weight)   # 👉 NEW


# --------- User Input ---------
V = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

prim_mst(graph, V)

"""Enter number of vertices: 4
Enter adjacency matrix:
0 2 0 6
2 0 3 8
0 3 0 0
6 8 0 0

Root: 0
Edge    Weight
0 - 1   2
1 - 2   3
0 - 3   6
Total Weight: 11 """
