import math
from typing import Dict

correct = [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]

def shortest_path(graph, start):
    visited = {start}
    distances = {start: 0}
    while len(visited) < len(graph):
        shortest, distance = get_shortest_edge(visited, distances, graph)
        visited.add(shortest)
        distances[shortest] = distance
    return distances

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
