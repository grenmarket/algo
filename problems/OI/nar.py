from collections import defaultdict, deque


def init():
    n = int(input())
    graph = {}
    rev_graph = {}
    for i in range(n-1):
        graph[i+1] = []
        nodes = [int(item) for item in input().split()][1:]
        for node in nodes:
            graph[i+1].append(node)
            if node not in rev_graph:
                rev_graph[node] = []
            rev_graph[node].append(i+1)
    graph[n] = []
    rev_graph[1] = []
    return graph, rev_graph, n

def modify_graph(graph, rev_graph):
    curr = len(graph) + 1
    for node in list(graph):
        if len(graph[node]) == len(rev_graph[node]):
            temp = graph[node].copy()
            graph[node] = [curr]
            graph[curr] = temp
            curr += 1
    return graph

def min_cut(graph, source, sink):
    residual_graph = defaultdict(dict)

    for u in graph:
        for v in graph[u]:
            residual_graph[u][v] = 1
            if v not in residual_graph:
                residual_graph[v] = {}
            residual_graph[v][u] = 0

    max_flow = 0
    while True:
        path, bottleneck = bfs_find_path(residual_graph, source, sink)

        if len(path) == 0:
            break

        max_flow += bottleneck
        current = sink
        for u in reversed(path[:-1]):
            residual_graph[u][current] -= bottleneck
            residual_graph[current][u] += bottleneck
            current = u
    return int(max_flow)

def bfs_find_path(residual_graph, source, sink):
    queue = deque([(source, [source], float('inf'))])
    visited = {source}

    while queue:
        node, path, bottleneck = queue.popleft()

        for neighbor, capacity in residual_graph[node].items():
            if neighbor not in visited and capacity > 0:
                visited.add(neighbor)
                new_bottleneck = min(bottleneck, capacity)

                if neighbor == sink:
                    return path + [neighbor], new_bottleneck

                queue.append((neighbor, path + [neighbor], new_bottleneck))

    return [], 0  # No augmenting path found

graph, rev, n = init()
graph = modify_graph(graph, rev)
print(min_cut(graph, 1, n))