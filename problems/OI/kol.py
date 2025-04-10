import sys


def intersects(p1, k1, p2, k2):
    if k1 <= p2:
        return False
    if p1 >= k2:
        return False
    return True

def solve():
    n, m, z = map(int, input().split())
    remaining_capacity = m
    intervals = []
    answers = []
    for _ in range(z):
        p, k, l = map(int, input().split())
        if l < remaining_capacity:
            answers.append('T')
            intervals.append((p, k, l))
            remaining_capacity -= l
        else:
            capacity_on_interval = m
            # not very efficient
            for interval in intervals:
                if intersects(p, k, interval[0], interval[1]):
                    capacity_on_interval -= interval[2]
                if capacity_on_interval < l:
                    answers.append('N')
                    break
            if capacity_on_interval >= l:
                answers.append('T')
                intervals.append((p, k, l))
                remaining_capacity -= l
    sys.stdout.write('\n'.join(answers))

solve()