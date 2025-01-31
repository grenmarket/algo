def init():
    with open('files/mwis.txt', 'r') as file:
        return [int(line) for line in file][1:]


def recreate_set(result, path_graph):
    vertices = []
    i = len(result) - 1
    while i > 0:
        if result[i-1] >= result[i-2] + path_graph[i-1]:
            i -= 1
        else:
            vertices.append(i-1)
            i -= 2
    return vertices[-1::-1]


def max_weight_independent_set(path_graph):
    result = [0, path_graph[0]]
    for i in range(1, len(path_graph)):
        result.append(max(result[i], result[i-1] + path_graph[i]))
    max_weight = result[-1]
    return max_weight, recreate_set(result, path_graph)

a = init()
res = set(max_weight_independent_set(a)[1])
indices = [0,1,2,3,16,116,516,996]
print(str(['0' if i not in res else '1' for i in indices]))