import sys


def init():
    n = int(input())
    counts = []
    for i in range(n):
        counts.append((i+1, int(input())))
    return counts

def solve(counts):
    sorted_counts = sorted(counts, key=lambda c: c[1], reverse=True)
    remaining_capacity = [0 for _ in range(len(counts) + 1)]
    for count in sorted_counts:
        remaining_capacity[count[0]] = count[1]
    connections = []
    for i in range(len(sorted_counts)):
        curr_city = sorted_counts[i][0]
        index = i+1
        while remaining_capacity[curr_city] > 0:
            next_city = sorted_counts[index][0]
            if remaining_capacity[next_city] > 0:
                connections.append((curr_city, next_city))
                remaining_capacity[curr_city] -= 1
                remaining_capacity[next_city] -= 1
            index += 1
    return connections

c = init()
solution = solve(c)
for s in solution:
    sys.stdout.write(str(s[0]) + ' ' + str(s[1]) + '\n')
