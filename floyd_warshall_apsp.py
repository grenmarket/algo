import math


def init():
    with open('files/g3.txt', 'r') as file:
        lines = [line.split() for line in file]
        num_of_vertices = int(lines[0][0])
        graph = {}
        for line in lines[1:]:
            graph[(int(line[0]), int(line[1]))] = int(line[2])
        return graph, num_of_vertices


def all_pairs_shortest_path(graph, num_of_vertices):
    result = {}
    for i in range(1, 1 + num_of_vertices):
        for j in range(1, 1 + num_of_vertices):
            result[(i, j, 0)] = initial_distance(i, j, graph)

    for k in range(1, 1 + num_of_vertices):
        print(k)
        for i in range(1, 1 + num_of_vertices):
            for j in range(1, 1 + num_of_vertices):
                index = k % 2
                prev_index = (index + 1) % 2
                distance = min(result[(i, j, prev_index)],
                               result[(i, k, prev_index)] + result[(k, j, prev_index)])
                result[(i, j, index)] = distance
    distance_map = {}
    for i in range(1, 1 + num_of_vertices):
        for j in range(1, 1 + num_of_vertices):
            distance = result[(i, j, num_of_vertices % 2)]
            if i == j and distance < 0:
                # negative cycle
                return None
            distance_map[(i, j)] = distance
    return distance_map



def initial_distance(i, j, graph):
    if i == j:
        return 0
    elif (i, j) in graph:
        return graph[(i, j)]
    else:
        return math.inf

g, num = init()
result = all_pairs_shortest_path(g, num)
if result is not None:
    min_distance = min(result.values())
    print(min_distance)
else:
    print(None)