import sys


def solve():
    n = int(input())
    intervals = []
    for _ in range(n):
        a, b = map(int, input().split())
        intervals.append((a, b))
    intervals.sort(key=lambda i: i[0])
    result = []
    result.append(intervals[0])
    for i in range(1, len(intervals)):
        current = intervals[i]
        if current[0] <= result[-1][1]:
            result[-1] = (result[-1][0], max(current[1], result[-1][1]))
        else:
            result.append(current)
    for interval in result:
        sys.stdout.write(f'{interval[0]} {interval[1]}\n')

solve()