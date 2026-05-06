import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Shortest Path:", path)
            return

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    print("No path found")


# -------- USER INPUT --------
n = int(input("Enter number of nodes: "))

graph = {}

print("Enter node names:")
nodes = input().split()

for node in nodes:
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter edges (u v cost):")

for _ in range(e):
    u, v, cost = input().split()
    cost = int(cost)
    graph[u].append((v, cost))
    graph[v].append((u, cost))  # undirected graph

# Heuristic values
heuristic = {}
print("Enter heuristic values:")
for node in nodes:
    heuristic[node] = int(input(f"h({node}): "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# Run A*
a_star(graph, heuristic, start, goal)



"""Enter number of nodes: 4
Enter node names:
A B C D
Enter number of edges: 4
Enter edges (u v cost):
A B 1
A C 3
B D 2
C D 1
Enter heuristic values:
h(A): 4
h(B): 2
h(C): 1
h(D): 0
Enter start node: A
Enter goal node: D """
