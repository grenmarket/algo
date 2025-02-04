import math
from typing import Dict
from datastructures import heap

correct = [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]

def shortest_path(graph, start):
    visited = {start}
    distances = {start: 0}
    not_visited = initialize_not_visited(graph, start)
    while len(visited) < len(graph):
        min_vertex = not_visited.min()
        v = min_vertex[0]
        distance = min_vertex[1]
        visited.add(v)
        not_visited.delete(v)
        distances[v] = distance
        for edge in graph[v]:
            dest = edge[0]
            cost = edge[1] + distance
            if dest not in visited:
                vertex_key = not_visited.get_value(dest)
                new_key = min(vertex_key, cost)
                not_visited.delete(dest)
                not_visited.insert((dest, new_key))
    return distances


def initialize_not_visited(graph, start):
    to_add = set()
    for v in graph:
        for e in graph[v]:
            to_add.add(e[0])
    to_add.remove(start)
    not_visited = heap.Heap(True, lambda obj: obj[1], lambda obj: obj[0])
    for edge in graph[start]:
        to_add.remove(edge[0])
        not_visited.insert((edge[0], edge[1]))
    for vertex in to_add:
        not_visited.insert((vertex, math.inf))
    return not_visited


def get_shortest_edge(visited, distances, graph: Dict):
    min = math.inf
    result = None
    for tail in graph.keys():
        if tail in visited:
            base_distance = distances[tail]
            for head in graph[tail]:
                if head[0] not in visited:
                    edge_length = head[1]
                    if edge_length + base_distance < min:
                        min = edge_length + base_distance
                        result = head[0]
    return result, min


def init():
    with open('files/dijkstra.txt', 'r') as file:
        graph = {}
        for line in file:
            split = line.strip().split()
            key = int(split[0])
            graph[key] = []
            for pair in split[1:]:
                coord = pair.split(',')
                graph[key].append((int(coord[0]), int(coord[1])))
        return graph

targets = [7,37,59,82,99,115,133,165,188,197]
graph = init()
result = shortest_path(graph, 1)
print([result[d] for d in targets])
