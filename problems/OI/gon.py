import sys
from typing import Set


class Node:

    def __init__(self, index, parent):
        self.index = index
        self.parent = parent
        self.level = 1 if parent is None else parent.level + 1
        self.visited = set() if parent is None else set(parent.visited)
        self.visited.add(index)


    def __str__(self):
        if self.parent == None:
            return 'root'
        return f'i:{self.index} p:{self.parent.index} l:{self.level} vis:{self.visited}'

def _init():
    v_size = int(input().strip())
    e_size = int(input().strip())
    graph = {}
    for i in range(e_size):
        edge = [int(s) for s in input().strip().split()]
        if edge[0] not in graph:
            graph[edge[0]] = set()
        graph[edge[0]].add(edge[1])
        if edge[1] not in graph:
            graph[edge[1]] = set()
        graph[edge[1]].add(edge[0])
    return graph


def _build_path_tree(graph, node: Node, reachable: Set, potential_solutions: Set):
    if node.level == len(graph):
        if node.index in graph[1]:
            potential_solutions.add(node)
        return
    else:
        for v in reachable:
            if v not in node.visited:
                new_reachable = set(reachable)
                new_reachable = new_reachable.union(graph[v])
                child = Node(v, node)
                _build_path_tree(graph, child, new_reachable, potential_solutions)
    return potential_solutions


def _recreate_solution(potential_solutions, graph):
    for ps in potential_solutions:
        current = ps
        reachable = set(graph[1])
        reachable = reachable.union(graph[current.index])
        while current.parent.index in reachable and current.parent.index != 1:
            current = current.parent
            reachable = reachable.union(graph[current.index])
        if current.parent.index == 1:
            return ps


def _format(solution):
    path = ['1']
    current = solution
    while current.index != 1:
        path.append(str(current.index))
        current = current.parent
    second_path = ['1'] + path[1:][::-1]
    return ' '.join(path), ' '.join(second_path)


graph = _init()
root = Node(1, None)
ps = _build_path_tree(graph, root, set(graph[1]), set())
solution = _recreate_solution(ps, graph)
p1, p2 = _format(solution)
sys.stdout.write(p1)
sys.stdout.write('\n')
sys.stdout.write(p2)




