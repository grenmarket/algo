g = {
    1: [2, 3],
    2: [1, 4, 5, 6],
    3: [1, 7],
    4: [2, 8],
    5: [2, 8],
    6: [2, 7],
    7: [3, 6],
    8: [4, 5]
}


def find_eulerian_path(graph, start_vertex):
    for v in graph:
        if len(graph[v]) % 2 != 0:
            return None
    stack = []
    result = []
    stack.append(start_vertex)
    while len(stack) > 0:
        current = stack[-1]
        if len(graph[current]) == 0:
            result.append(current)
            stack.pop()
        else:
            head = graph[current][0]
            graph[current].remove(head)
            graph[head].remove(current)
            stack.append(head)
    return result


print(find_eulerian_path(g, 1))
