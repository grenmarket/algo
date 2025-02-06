import math


def shortest_path(graph, starting_vertex=1):
    A = {}
    edges_ending_at = {}
    for v in graph:
        A[(0, v)] = math.inf
        for edge in graph[v]:
            if edge[0] not in edges_ending_at:
                edges_ending_at[edge[0]] = set()
            edges_ending_at[edge[0]].add((v, edge[1]))
    A[(0, starting_vertex)] = 0
    for i in range(1, len(graph)+1):
        for v in graph:
            A[(i, v)] = min(A[(i-1, v)], min_with_one_less_edge(A, i, v, edges_ending_at))
        if is_already_optimal(A, i, graph):
            return [A[(i, vertex)] for vertex in graph]
    i_max = len(graph)
    for v in graph:
        if A[(i_max, v)] < A[(i_max - 1, v)]:
            # negative cycle
            return None
    return [A[(i_max, vertex)] for vertex in graph]


def is_already_optimal(A, i, graph):
    for v in graph:
        if A[(i, v)] != A[(i-1, v)]:
            return False
    return True


def min_with_one_less_edge(A, i, v, edge_map):
    candidates = []
    for edge in edge_map[v]:
        candidates.append(A[(i-1, edge[0])] + edge[1])
    return min(candidates)
