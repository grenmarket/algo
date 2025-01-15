from typing import Dict
from typing import List
import random

def min_cut_lowest(graph):
    min = len(graph.keys())**2
    for i in range(min):
        # random.seed(i)
        current = min_cut(graph)
        if current < min:
            min = current
    return min
def min_cut(graph: Dict[int, List]):
    while len(graph.keys()) > 2:
        pick_and_contract(graph)
    return len(graph[list(graph.keys())[0]])


def pick_and_contract(graph):
    #     pick edge at random
    tail = random.choice(list(graph.keys()))
    head = random.choice(graph[tail])
    #     contract edge
    if head > tail:
        contract(graph, tail, head)
    else:
        contract(graph, head, tail)


def contract(graph: [int, List], smaller: int, larger: int):
    # always leave the smaller key
    graph[smaller].extend(graph[larger])
    while larger in list(graph[smaller]):
        graph[smaller].remove(larger)
    # remove self-loops
    while smaller in list(graph[smaller]):
        graph[smaller].remove(smaller)
    graph.pop(larger)
    for key in list(graph[smaller]):
        while larger in list(graph[key]):
            graph[key].remove(larger)
            graph[key].append(smaller)


def init():
    with open('files/random_contraction.txt', 'r') as file:
        graph = {}
        for line in file:
            vertices = [int(el) for el in line.strip().split()]
            graph[vertices[0]] = vertices[1:]
        return graph

graph = init()
print(min_cut_lowest(graph))