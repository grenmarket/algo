from datastructures import union_find

def init_small():
    with open('files/clustering1.txt', 'r') as file:
        lines = [line for line in file]
        result = []
        num_of_nodes = int(lines[0])
        for line in lines[1:]:
            parts = line.split()
            result.append([int(parts[0]), int(parts[1]), int(parts[2])])
        return result, num_of_nodes


def max_spacing(num_of_clusters):
    input = init_small()
    edges = input[0]
    num_of_nodes = input[1]
    sorted_edges = sorted(edges, key=lambda array: array[2])
    clusters = union_find.UnionFind(num_of_nodes)
    for edge in sorted_edges:
        head = edge[0]-1
        tail = edge[1]-1
        leader1 = clusters.find(head)
        leader2 = clusters.find(tail)
        if leader1 != leader2:
            clusters.merge(head, tail)
        if clusters.clusters == num_of_clusters:
            break
    spacings = set()
    for edge in sorted_edges[-1::-1]:
        if clusters.find(edge[0]-1) != clusters.find(edge[1]-1):
            spacings.add(edge[2])
    return min(spacings)

print(max_spacing(4))