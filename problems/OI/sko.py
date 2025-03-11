import sys

filters = [
    (10000000,
     [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0,
      1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]),
    (1000000,
     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
      0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1]),
    (100000,
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
      0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0]),
    (10000,
     [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
      0, 1, 0]),
    (1000, [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]),
    (100, [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]),
    (10, [1, 0, 1, 0, 0, 0, 1, 0, 1])
]


def _jump_right(i, array):
    array[i] -= 1
    array[i + 1] -= 1
    array[i + 2] += 1


def _jump_left(i, array):
    array[i] -= 1
    array[i - 1] += 1
    array[i - 2] += 1


def _can_jump_right(i, array):
    if i < 0 or i + 1 >= len(array):
        return False
    return array[i] > 0 and array[i + 1] > 0


def _must_jump_left(i, array):
    if i < 2 or i >= len(array):
        return False
    return array[i - 1] == 0 and array[i] > 1 and array[i + 1] == 0


def _is_solved(array):
    gap = -1
    for i in range(len(array)):
        if array[i] > 1:
            return False
        if array[i] == 1:
            if gap == 0:
                return False
            else:
                gap = 0
        else:
            gap += 1
    return True


def _solve(array):
    while not _is_solved(array):
        _traverse_from_right(array)
        _traverse_from_left(array)
    return array


def _traverse_from_left(array):
    for i in range(2, len(array) - 1):
        if _must_jump_left(i, array):
            _jump_left(i, array)


def _traverse_from_right(array):
    for i in range(len(array) - 2, 0, -1):
        _apply_filter(i, array)
        if _can_jump_right(i - 1, array):
            _jump_right(i - 1, array)
            j = i
            while _can_jump_right(j, array):
                _jump_right(j, array)
                j += 1


def _apply_filter(i, array):
    if array[i] < 10:
        return
    f = None
    for filter in filters:
        if filter[0] <= array[i]:
            f = filter
    multiplier = array[i] // f[0]
    radius = len(f[1]) // 2
    if i < radius or i >= len(array) - radius:
        return
    temp = array[i] - multiplier * f[0] + f[1][radius]
    for j in range(-radius, radius + 1):
        array[i + j] += multiplier * f[1][j + radius]
    array[i] = temp


def init():
    n = int(input())
    radius = 60
    array = [0 for _ in range(n + 2 * radius)]
    for _ in range(n):
        line = [int(a) for a in input().split()]
        array[line[0] + radius] = line[1]
    solution = _solve(array)
    output = []
    for i in range(len(solution)):
        if solution[i] == 1:
            output.append(str(i - radius))
    sys.stdout.write(' '.join(output))


init()
