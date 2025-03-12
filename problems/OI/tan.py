import bellman_ford_shortest_path

total_distance = 2000
distances = [0, 100, 120, 400, 700, 1000, 1200, 1440, 2000]
costs = [0, 54, 70, 17, 38, 25, 18, 40, 0]

def _build_graph():
    graph = {}
    for i in range(len(distances)):
        node_number = i+1
        graph[node_number] = []
        current_km = distances[i]
        j = i + 1
        while j < len(distances) and distances[j] - current_km <= 800:
            graph[node_number].append((j+1, costs[j]))
            j += 1
    print(graph)
    return graph

g = _build_graph()
print(bellman_ford_shortest_path.shortest_path(g))

# todo: use Bellman-Ford (with backtracking) to find minimum-cost journey (journey time ties resolvable)
# todo: use BFS with max-depth parameter to find minimum-time journey (journey cost ties resolvable)