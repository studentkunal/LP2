def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(graph, m, color, v):
    if v == len(graph):
        return True
    
    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c
            
            if graph_coloring(graph, m, color, v + 1):
                return True
            
            color[v] = 0
    
    return False


# Driver
n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))

color = [0] * n

if graph_coloring(graph, m, color, 0):
    print("Solution exists:", color)
else:
    print("No solution")