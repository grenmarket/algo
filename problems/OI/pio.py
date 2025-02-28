import sys


def indexes_affected(index):
    result = []
    if index % 8 > 0:
        result.append(index - 1)
        if index // 8 > 0:
            result.append(index - 9)
            result.append(index - 8)
        if index // 8 < 7:
            result.append(index + 7)
            result.append(index + 8)
    if index % 8 < 7:
        result.append(index + 1)
        if index // 8 > 0:
            result.append(index - 7)
            result.append(index - 8)
        if index // 8 < 7:
            result.append(index + 9)
            result.append(index + 8)
    return set(result)


def equation_row(index, target_value):
    one_indexes = indexes_affected(index)
    return [1 if i in one_indexes else 0 for i in range(64)] + [target_value]


def create_matrix(input, inverse):
    val = lambda x: other(x) if inverse else x
    return [equation_row(index, val(value)) for index, value in enumerate(input)]


def other(v):
    return 0 if v == 1 else 1


def add(row1, row2, matrix):
    result = [(matrix[row1][i] + matrix[row2][i]) % 2 for i in range(65)]
    matrix[row1] = result


def exchange(row_index_old, row_index_new, matrix):
    matrix[row_index_new], matrix[row_index_old] = matrix[row_index_old], matrix[row_index_new]


def find_rows_with_nonzero_values(col_index, matrix):
    result = []
    for i in range(col_index, 64):
        if matrix[i][col_index] != 0:
            result.append(i)
    return result


def solve(input):
    case1 = steps(create_matrix(input, False))
    case2 = steps(create_matrix(input, True))
    if len(case1) < len(case2):
        return case1
    else:
        return case2


def steps(m):
    for i in range(64):
        nz = find_rows_with_nonzero_values(i, m)
        if len(nz) > 0:
            adder = nz[-1]
            for row in nz[:-1]:
                add(row, adder, m)
            exchange(adder, i, m)
    return solution(m)


def solution(m):
    known = {}
    for i in range(63, -1, -1):
        sum = 0
        for j in range(63, i, -1):
            sum += known[j] * m[i][j]
            sum = sum % 2
        known[i] = (m[i][64] - sum) % 2
    result = []
    for k in known:
        if known[k] == 1:
            result.append(k)
    return result


a = []
for i in range(8):
    row = input().strip()
    for ch in row:
        if ch == 'C':
            a.append(1)
        else:
            a.append(0)

done = all(x == 1 for x in a) or all(x == 0 for x in a)
if done:
    sys.stdout.write('0')
else:
    s = solve(a)
    sys.stdout.write(str(len(s)) + '\n')
    sys.stdout.write(' '.join(str(x+1) for x in s))
