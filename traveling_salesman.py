import math
from itertools import combinations


def init():
    with open('files/tsp.txt', 'r') as file:
        lines = [line.split() for line in file][1:]
        num_of_vertices = len(lines)
        graph = {}
        for i in range(0, num_of_vertices):
            coord_i = lines[i]
            # vertices indexed 1-n
            graph[i+1] = {}
            # points have a certain structure, otherwise all-to-all connection
            for j in range(max(0, i - num_of_vertices//2), min(num_of_vertices, i + num_of_vertices//2)):
                coord_j = lines[j]
                if i != j:
                    graph[i+1][j+1] = edge_length(coord_i, coord_j)
        return graph


def min_length_path(graph, num_of_vertices, starting_vertex):
    subsets = []
    A = {}
    for i in range(1, num_of_vertices+1):
        subsets.extend(all_subsets_of_size(i, num_of_vertices, starting_vertex))
    for subset in subsets:
        A[subset] = [math.inf] * num_of_vertices
    A[frozenset({1})][0] = 0
    for m in range(2, num_of_vertices+1):
        print(m)
        current_subsets = all_subsets_of_size(m, num_of_vertices, starting_vertex)
        for s in current_subsets:
            for j in s:
                if j != starting_vertex:
                    A[s][j-1] = min(get_all_subproblems(A, s, graph, j))
    results = []
    superset = frozenset([i for i in range(1, num_of_vertices+1)])
    for j in range(2, num_of_vertices+1):
        result = A[superset][j-1] + get_edge_cost(graph, j, starting_vertex)
        results.append(result)
    return min(results)

def get_all_subproblems(A, subset: frozenset, graph, j):
    subproblems = []
    for k in subset:
        if k != j:
            edge_cost = get_edge_cost(graph, j, k)
            subset_without_j = set(subset)
            subset_without_j.remove(j)
            subproblems.append(A[frozenset(subset_without_j)][k-1] + edge_cost)
    return subproblems


def get_edge_cost(graph, j, k):
    edge_cost = graph[k].get(j)
    if edge_cost is None:
        edge_cost = math.inf
    return edge_cost


def all_subsets_of_size(size, superset_size, starting_point):
    S = range(1, superset_size+1)
    combs = list(combinations(S, size))
    sets = [frozenset(c) for c in combs]
    result = []
    for s in sets:
        if starting_point in s:
            result.append(s)
    return frozenset(result)

def edge_length(coord1, coord2):
    x1 = float(coord1[0])
    x2 = float(coord2[0])
    y1 = float(coord1[1])
    y2 = float(coord2[1])
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

graph = init()
print(min_length_path(graph, 25, 1))