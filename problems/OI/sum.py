import sys


def is_possible(count, total):
    max_v = (count * (count - 1)) / 2
    min_v = 1 if count % 2 == 0 else 0
    return max_v >= abs(total) >= min_v


def next_v(base, count, total):
    new_total = total - base * count
    if new_total < 0:
        return base - 1
    return base + 1


def solve(count, total):
    if not is_possible(count, total):
        return None
    result = [0]
    curr_sum = 0
    for i in range(count - 1):
        next_value = next_v(result[-1], count - 1 - i, total - curr_sum)
        curr_sum += next_value
        result.append(next_value)
    if curr_sum != total:
        return None
    return result

n = int(input())
S = int(input())
solution = solve(n, S)
if solution is None:
    sys.stdout.write("NIE")
else:
    for item in solution:
        sys.stdout.write(str(item) + '\n')
