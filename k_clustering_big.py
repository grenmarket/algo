from datastructures import union_find

def init_big():
    with open('files/clustering_big.txt', 'r') as file:
        lines = [line for line in file]
        num_of_nodes = int(lines[0].split()[0])
        return [line.replace(' ', '') for line in lines[1:]], num_of_nodes


def min_number_of_clusters(nodes):
    clusters = union_find.UnionFind(len(nodes))
    mask_mapping = {}
    for i in range(len(nodes)):
        if i % 10000 == 0:
            print('adding masks', i//10000)
        masks = masks_for_similar(nodes[i])
        for mask in masks:
            if mask not in mask_mapping:
                mask_mapping[mask] = set()
            mask_mapping[mask].add(i)
    for i in range(len(nodes)):
        if i % 10000 == 0:
            print('checking', i//10000)
        node_bits = nodes[i]
        if node_bits in mask_mapping:
            close_nodes = mask_mapping.get(node_bits)
            for node in close_nodes:
                if node != i:
                    clusters.merge(node, i)
    return clusters.clusters

def masks_for_similar(number: str):
    masks = set()
    masks.add(number)
    masks.add(replace_one(number, len(number) - 1))
    for i in range(len(number) - 1):
        masks.add(replace_one(number, i))
        for j in range(i+1, len(number)):
            masks.add(replace_two(number, i, j))
    return masks

def replace_two(binary, i, j):
    replaced = replace_one(binary, i)
    return replace_one(replaced, j)

def replace_one(binary, i):
    return binary[:i] + reverse(binary[i]) + binary[i+1:]

def reverse(char):
    return '0' if char == '1' else '1'


print(min_number_of_clusters(init_big()[0]))