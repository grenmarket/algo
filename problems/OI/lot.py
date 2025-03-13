import sys
import heapq


def init():
    n = int(input())
    counts = []
    for i in range(n):
        # heapq only supports min
        counts.append((-int(input()), i + 1))
    return counts


def solve(counts):
    connections = []
    heap = counts.copy()
    heapq.heapify(heap)
    while len(heap) > 1:
        this_iteration = []
        current = heapq.heappop(heap)
        for _ in range(-current[0]):
            next = heapq.heappop(heap)
            connections.append((current[1], next[1]))
            if -next[0] > 1:
                this_iteration.append((next[0]+1, next[1]))
        for item in this_iteration:
            heapq.heappush(heap, item)
    return connections


c = init()
solution = solve(c)
for s in solution:
    sys.stdout.write(str(s[0]) + ' ' + str(s[1]) + '\n')
