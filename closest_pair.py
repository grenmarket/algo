# presorted
import math
import sys


def closest_pair(p_x, p_y):
    if len(p_x) == 1 or len(p_y) == 1:
        return best_pair(p_x, p_y)
    x_half = len(p_x) // 2
    x_mid = p_x[x_half][1]  # x-coordinate of middle point
    p_y_left = [p for p in p_y if p[1] <= x_mid]
    p_y_right = [p for p in p_y if p[1] > x_mid]
    p1, q1, d1 = closest_pair(p_x[:x_half], p_y_left)
    p2, q2, d2 = closest_pair(p_x[x_half:], p_y_right)
    result = sorted([(p1, q1, d1), (p2, q2, d2)], key=lambda r: r[2])
    delta = result[0][2]
    p3, q3, d3 = closest_split_pair(p_x, p_y, delta)
    if p3 is None:
        return result[0][0], result[0][1], result[0][2]
    result.append((p3, q3, d3))
    min_r = sorted(result, key=lambda r: r[2])[0]
    return min_r[0], min_r[1], min_r[2]


def closest_split_pair(p_x, p_y, delta):
    x_half = len(p_x) // 2
    x_max = p_x[x_half][1]
    s_y = [p for p in p_y if abs(p[1] - x_max) <= delta]
    best = delta
    best_p, best_q = None, None
    for i in range(0, len(s_y)):
        for j in range(min(7, len(s_y) - i)):
            p = s_y[i]
            q = s_y[i + j]
            if p[0] != q[0]:
                d = distance(p, q)
                if d < best:
                    best_p = p
                    best_q = q
                    best = d
    return best_p, best_q, best


def distance(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)


def best_pair(p1, p2):
    if len(p1) == 0 or len(p2) == 0:
        return None, None, math.inf
    p, q, d = p1[0], p2[0], math.inf
    for point_1 in p1:
        for point_2 in p2:
            dist = distance(point_1, point_2)
            if point_1[0] != point_2[0] and dist < d:
                d = dist
                p = point_1
                q = point_2
    return p, q, d


def init():
    with open('files/nn.txt', 'r') as file:
        lines = [line.split() for line in file]
        points = [(int(e[0]), float(e[1]), float(e[2])) for e in lines[1:]]
        p_x = sorted(points, key=lambda p: p[1])
        p_y = sorted(points, key=lambda p: p[2])
        return p_x, p_y


sys.setrecursionlimit(10**6)
x, y = init()
print(closest_pair(x, y))