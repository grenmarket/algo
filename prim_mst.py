import math
from typing import Dict, Set

def init():
    with open('files/edges.txt', 'r') as file:
        graph = {}
        edges = [line.strip() for line in file][1:]
        for e in edges:
            edge = e.split()
            source = int(edge[0])
            head = int(edge[1])
            weight = int(edge[2])
            if source not in graph:
                graph[source] = []
            graph[source].append((head, weight))
            if head not in graph:
                graph[head] = []
            graph[head].append((source, weight))
        return graph

def prim(graph: Dict):
    if len(graph) == 0:
        return None
    visited = set()
    mst = set()
    visited.add(list(graph.keys())[0])
    while len(visited) < len(graph):
        min = min_edge(graph, visited)
        mst.add(min)
        visited.add(min[1])
    return mst

def min_edge(graph: Dict, visited: Set):
    min = (None, None, math.inf)
    for source in graph:
        if source in visited:
            for edge in graph[source]:
                if edge[0] not in visited and edge[1] < min[2]:
                    min = (source, edge[0], edge[1])
    return min

mst = prim(init())
print(sum([edge[2] for edge in mst]))