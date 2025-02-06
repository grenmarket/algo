import math


def init():
    with open('files/nn.txt', 'r') as file:
        lines = [line.split() for line in file]
        vertices = [(int(e[0]), float(e[1]), float(e[2])) for e in lines[1:]]
        return vertices


def min_length_path(graph):
    visited = set()
    not_visited = set(graph)
    current = graph[0]
    visited.add(current)
    not_visited.remove(current)
    total_distance = 0
    while len(visited) < len(graph):
        next = get_nearest_not_visited(current, not_visited)
        distance = distance_between(current, next)
        total_distance += distance
        visited.add(next)
        not_visited.remove(next)
        current = next
    return total_distance + distance_between(current, graph[0])


def get_nearest_not_visited(v, vertices_around):
    x = v[1]
    y = v[2]
    return min(vertices_around, key=lambda neighbor: ((x - neighbor[1]) ** 2 + (y - neighbor[2]) ** 2, neighbor[0]))


def distance_between(v1, v2):
    return math.sqrt((v1[1] - v2[1]) ** 2 + (v1[2] - v2[2]) ** 2)


print(min_length_path(init()))
