import sys
from typing import Dict


def init():
    n, r = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = [int(item) for item in input().split()]
        matrix.append(row)
    return n, r, matrix

def calculate_sums(matrix):
    n = len(matrix)
    sums = {}
    curr_sum = 0
    for x in range(n):
        curr_sum += matrix[0][x]
        sums[(x, 0)] = curr_sum
    curr_sum = 0
    for x in range(n):
        curr_sum += matrix[x][0]
        sums[(0, x)] = curr_sum
    for i in range(1, n):
        for j in range(1, n):
            sums[(i, j)] = sums[(i-1, j)] + sums[(i, j-1)] - sums[(i-1, j-1)] + matrix[j][i]
    return sums

def solve(n, r, sums: Dict):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            left = i - r - 1
            right = min(n-1, i + r)
            top = j - r - 1
            bottom = min(n-1, j + r)
            base = sums[(right, bottom)]
            if left >= 0:
                base -= sums[(left, bottom)]
            if top >= 0:
                base -= sums[(right, top)]
            if left >= 0 and top >= 0:
                base += sums[(left, top)]
            result[j][i] = base
    return result

n, r, matrix = init()
sums = calculate_sums(matrix)
result = solve(n, r, sums)
for i in range(n):
    sys.stdout.write(' '.join([str(num) for num in result[i]]) + '\n')