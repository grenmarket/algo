import sys


def init():
    safe_heights = []
    n = int(input())
    for _ in range(n):
        safe_heights.append(int(input()))
    return safe_heights


def solve(safe_heights):
    min_set = []
    available = set()
    first = safe_heights[0]
    min_set.append(first)
    multiplied = first
    while multiplied <= 10000:
        available.add(multiplied)
        multiplied += first
    max_height = first
    for safe_height in safe_heights[1:]:
        for height in range(max_height + 1, safe_height):
            if height in available:
                return max_height, min_set
        if safe_height not in available:
            min_set.append(safe_height)
            available.add(safe_height)
            new_available = set()
            for h in available:
                new_available.add(safe_height + h)
            available = available.union(new_available)
        max_height = safe_height
    return max_height, min_set


sh = init()
mh, ms = solve(sh)
sys.stdout.write(str(mh) + "\n")
for el in ms:
    sys.stdout.write(str(el) + '\n')
