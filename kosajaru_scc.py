import sys
from collections import defaultdict, Counter


class Execution:

    def __init__(self, max_v):
        self.max_v = max_v
        self.explored = [False for i in range(max_v + 1)]
        self.f_time = {}
        self.leaders = [None for i in range(max_v + 1)]
        self.t = 0
        self.s = None


    def init_from(self, execution):
        self.max_v = execution.max_v
        self.explored = [False for i in range(execution.max_v + 1)]
        self.f_time = execution.f_time
        self.leaders = [None for i in range(execution.max_v + 1)]
        self.t = 0
        self.s = None
        return self


def kosajaru(graph):
    max_v = max_node(graph)
    graph = normalize(graph)
    reversed = get_reversed_graph(graph, max_v)
    exec_1 = Execution(max_v)
    dfs_loop_rev(reversed, exec_1)
    exec_2 = exec_1.init_from(exec_1)
    dfs_loop(graph, exec_2)
    return exec_2.leaders


def dfs_loop_rev(graph, execution):
    for i in range(execution.max_v, 0, -1):
        if not execution.explored[i]:
            dfs_rev(graph, i, execution)


def dfs_loop(graph, execution):
    for i in sorted(execution.f_time, key=lambda x: execution.f_time[x], reverse=True):
        if not execution.explored[i]:
            execution.s = i
            dfs(graph, i, execution)


def dfs(graph, vertex, execution):
    execution.explored[vertex] = True
    execution.leaders[vertex] = execution.s
    for connection in list(graph[vertex]):
        if not execution.explored[connection]:
            dfs(graph, connection, execution)


def dfs_rev(graph, vertex, execution):
    execution.explored[vertex] = True
    for connection in list(graph[vertex]):
        if not execution.explored[connection]:
            dfs_rev(graph, connection, execution)
    execution.t += 1
    execution.f_time[vertex] = execution.t


def get_reversed_graph(graph, max):
    reversed = {}
    for u in graph:
        for v in graph[u]:
            if v not in reversed:
                reversed[v] = []
            reversed[v].append(u)
    for i in range(1, max + 1):
        if i not in reversed:
            reversed[i] = []
    return reversed


def init():
    with open('files/scc.txt', 'r') as file:
        graph = defaultdict(list)
        for line in file:
            key, value = map(int, line.split())
            graph[key].append(value)
        return graph


def normalize(graph):
    max_v = max_node(graph)
    for i in range(1, max_v + 1):
        if i not in graph:
            graph[i] = []
    return graph

def max_node(graph):
    max = 0
    for u in graph:
        if u > max:
            max = u
        for v in graph[u]:
            if v > max:
                max = v
    return max

# sys.setrecursionlimit(10**6)
# graph = init()
# leaders = kosajaru(graph)
# freq = Counter(leaders)
# print(dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]))
