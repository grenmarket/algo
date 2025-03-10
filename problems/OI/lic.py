def add(k, v, map):
    if k not in map:
        map[k] = set()
    map[k].add(v)

def init():
    n = int(input())
    text = ''
    lengths = [0]
    for _ in range(n):
        a = input()
        b = input()
        text += a
        text += b
        lengths.append(lengths[-1] + len(a))
        lengths.append(lengths[-1] + len(b))
    forward = {}
    backward = {}
    for i in range(len(lengths) - 1):
        add(lengths[i] - 1, lengths[i], forward)
        add(lengths[i] - 1, lengths[i + 1], forward)
        for j in range(lengths[i], lengths[i + 1]):
            add(j, j + 1, forward)
    for i in range(len(lengths) - 1, 0, -1):
        add(lengths[i], lengths[i] - 1, backward)
        add(lengths[i], lengths[i - 1] - 1, backward)
        for j in range(lengths[i] - 1, lengths[i - 1] - 1, -1):
            add(j, j - 1, backward)
    return text, forward, backward


def _create_tree(root, text, forward, backward, result):
    i = root[0]
    j = root[1]
    if j < i:
        return
    if i == j:
        result[0] += 1
        return
    possible_i = forward[i]
    possible_j = backward[j]
    if i < 0 or j >= len(text):
        for pos_i in possible_i:
            for pos_j in possible_j:
                _create_tree((pos_i, pos_j), text, forward, backward, result)
        return
    if text[i] == text[j]:
        for pos_i in possible_i:
            for pos_j in possible_j:
                _create_tree((pos_i, pos_j), text, forward, backward, result)


text, f, b = init()
print(f)
print(b)
result = [0]
_create_tree((-1, len(text)), text, f, b, result)
print(result[0])