import sys
from collections import defaultdict, Counter


def kosajaru():
    graph, rev_graph, max = init()
    initialize_global(max)
    dfs_loop_rev(rev_graph, max)
    global explored
    explored = [False for i in range(max+1)]
    dfs_loop(graph, max)
    print(frequency_map(leaders, 10))


def initialize_global(max):
    global explored
    explored = [False for i in range(max + 1)]
    global f_time
    f_time = {}
    global leaders
    leaders = [None for i in range(max + 1)]
    global t
    t = 0
    global s


def dfs_loop_rev(graph, max):
    for i in range(max, 0, -1):
        if not explored[i]:
            dfs_rev(graph, i)


def dfs_loop(graph, max):
    for i in sorted(f_time, key=lambda x: f_time[x], reverse=True):
        if not explored[i]:
            global s
            s = i
            dfs(graph, i)


def dfs(graph, vertex):
    explored[vertex] = True
    leaders[vertex] = s
    for connection in list(graph[vertex]):
        if not explored[connection]:
            dfs(graph, connection)


def dfs_rev(graph, vertex):
    global t
    explored[vertex] = True
    for connection in list(graph[vertex]):
        if not explored[connection]:
            dfs_rev(graph, connection)
    t += 1
    f_time[vertex] = t


def frequency_map(a, top):
    freq = Counter(a)
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top])


def init():
    with open('files/scc.txt', 'r') as file:
        max = -1
        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        for line in file:
            key, value = map(int, line.split())
            graph[key].append(value)
            rev_graph[value].append(key)
            if key > max:
                max = key
        g1 = dict(graph)
        g2 = dict(rev_graph)
        for i in range(1, max+1):
            if i not in g1:
                g1[i] = []
            if i not in g2:
                g2[i] = []
        return g1, g2, max

sys.setrecursionlimit(10**6)
kosajaru()

