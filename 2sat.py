import sys
from collections import Counter

import kosajaru_scc

def is_satisfiable(clauses):
    sys.setrecursionlimit(10**6)
    graph = convert_to_implication_graph(clauses)
    leaders = kosajaru_scc.kosajaru(graph)
    return not contains_contradiction(leaders)

def convert_to_implication_graph(clauses):
    graph = {}
    for clause in clauses:
        v1 = clause[0]
        v2 = clause[1]
        neg_v1 = -v1
        neg_v2 = -v2
        v1 = normalize(v1)
        v2 = normalize(v2)
        neg_v1 = normalize(neg_v1)
        neg_v2 = normalize(neg_v2)
        if neg_v1 not in graph:
            graph[neg_v1] = []
        graph[neg_v1].append(v2)
        if neg_v2 not in graph:
            graph[neg_v2] = []
        graph[neg_v2].append(v1)
    return graph


def contains_contradiction(leaders):
    leader_map = {}
    for i in range(len(leaders)):
        literal_index = i // 2 if i % 2 == 0 else (i + 1) // -2
        if leaders[i] not in leader_map:
            leader_map[leaders[i]] = set()
        if -literal_index in leader_map[leaders[i]]:
            return True
        leader_map[leaders[i]].add(literal_index)
    return False



def normalize(v):
    if v < 0:
        return -2 * v - 1
    else:
        return 2 * v


def file_to_clauses(path):
    with open(path, 'r') as file:
        lines = [line.split() for line in file]
        return [(int(c[0]), int(c[1])) for c in lines[1:]]

for i in range(1, 7):
    file_name = f'files/2sat{i}.txt'
    clauses = file_to_clauses(file_name)
    print(is_satisfiable(clauses))