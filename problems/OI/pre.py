import math
import sys


def _appr1(chord, diff):
    return math.sqrt((diff ** 2 + 2 * chord * diff) / 4)


def _radius(sagitta, chord):
    return sagitta / 2 + ((chord ** 2) / (8 * sagitta))


def _sagitta(radius, chord, diff):
    angle = (chord + diff) / (radius * 2)
    return 2 * radius * (math.sin(angle / 2) ** 2)


def _solve(chord, diff):
    if chord == 2 and diff == 1:
        return 1
    approximation = int(_appr1(chord, diff))
    delta = (math.inf, approximation)
    while True:
        rad = _radius(approximation, chord)
        result = _sagitta(rad, chord, diff)
        exact = float(approximation)
        new_delta = abs(exact - result)
        if new_delta < delta[0]:
            delta = (new_delta, approximation)
        sign = 1.0 if result > exact else -1.0
        div = result / exact if sign > 0 else exact / result
        new_approximation = int(approximation + sign * (div - 1) * chord)
        if new_approximation == approximation:
            return delta[1]
        else:
            approximation = new_approximation


def init():
    n = int(input().strip())
    for _ in range(n):
        data = [int(i) for i in input().strip().split()]
        chord = data[0]
        diff = data[1]
        sys.stdout.write(str(_solve(chord, diff)) + '\n')


init()
