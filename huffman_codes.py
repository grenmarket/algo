from __future__ import annotations
from typing import Dict
from datastructures import heap

class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.left = None
        self.right = None
        self.frequency = frequency

    def merge(self, other: Node):
        metanode = Node(self.char + other.char, self.frequency + other.frequency)
        metanode.left = self
        metanode.right = other
        return metanode

def encode(frequency_map: Dict):
    h = heap.Heap(True, lambda node: node.frequency)
    for char in frequency_map:
        h.insert(Node(char, frequency_map.get(char)))
    while h.size > 1:
        min1 = h.min()
        min2 = h.min()
        parent = min1.merge(min2)
        h.insert(parent)
    root = h.min()
    result = sorted(traverse(root, [], ''), key=lambda e: len(e[1]))
    return result


def traverse(node, result, binary_string):
    if node.left is not None:
        traverse(node.left, result, binary_string + '0')
    if node.left is None and node.right is None:
        result.append((node.char, binary_string))
    if node.right is not None:
        traverse(node.right, result, binary_string + '1')
    return result


frequency_map = {
    'A': 51,
    'B': 21,
    'C': 11,
    'D': 8,
    'E': 5,
    'F': 3,
    'G': 1
}
print(encode(frequency_map))