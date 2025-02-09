import bellman_ford_shortest_path
import dijksta_shortest_path

correct_results = [None, None, -19]
input = ['files/g1.txt', 'files/g2.txt', 'files/g3.txt']

def init(path):
    with open(path, 'r') as file:
        lines = [line.split() for line in file]
        num_of_vertices = int(lines[0][0])
        graph = {}
        for line in lines[1:]:
            u = int(line[0])
            v = int(line[1])
            weight = int(line[2])
            if u not in graph:
                graph[u] = []
            graph[u].append((v, weight))
        return graph, num_of_vertices

def shortest_paths(graph, num_of_vertices):
    virtual_vertex = num_of_vertices+1
    graph[virtual_vertex] = []
    for i in range(1, virtual_vertex):
        graph[virtual_vertex].append((i, 0))
    first_pass = bellman_ford_shortest_path.shortest_path(graph, virtual_vertex)
    if first_pass is None:
        return None
    new_graph = {}
    for u in graph:
        for v in graph[u]:
            if u != virtual_vertex:
                old_weight = v[1]
                pu = first_pass[u - 1]
                pv = first_pass[v[0] - 1]
                new_weight = old_weight + pu - pv
                if u not in new_graph:
                    new_graph[u] = []
                new_graph[u].append((v[0], new_weight))
    results = {}
    for vertex in range(1, virtual_vertex):
        results[vertex] = dijksta_shortest_path.shortest_path(new_graph, vertex)
    corrected_results = {}
    for u in results:
        for v in results[u]:
            weight = results[u][v]
            pu = first_pass[u-1]
            pv = first_pass[v-1]
            corrected_weight = weight + pv - pu
            corrected_results[(u, v)] = corrected_weight
    return corrected_results

res = []
for i in input:
    g, num = init(i)
    paths = shortest_paths(g, num)
    if paths is None:
        res.append(None)
    else:
        res.append(paths[min(paths, key=lambda p: paths[p])])
print(res)
