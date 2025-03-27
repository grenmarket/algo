import sys


def init():
    lengths = [int(_) for _ in input().split()]
    n = int(input())
    totals = []
    for _ in range(n):
        totals.append(int(input()))
    return lengths, totals


def prepare_sums(lengths):
    l_set = set(lengths)
    global_min = min(l_set)
    sum_map = {}
    min_max = [(0,0),(global_min, max(l_set))]
    sum_map[0] = {0}
    sum_map[1] = set(lengths)
    while min_max[-1][1] - min_max[-2][0] < 1000:
        available = set()
        for el in sum_map[len(min_max) - 1]:
            for el2 in l_set:
                available.add(el + el2)
        sum_map[len(min_max)] = available
        curr_min = min(available)
        curr_max = max(available)
        min_max.append((curr_min, curr_max))
    step_map = {}
    curr_i = 1
    curr_steps = 1
    while curr_i <= 1000:
        if min_max[curr_steps][1] - min_max[curr_steps - 1][0] >= curr_i:
            step_map[curr_i] = curr_steps
            curr_i += 1
        else:
            curr_steps += 1
    return sum_map, step_map, global_min


def test(total, sum_map, step_map, global_min):
    step = step_map[total]
    available = sum_map[step].copy()
    for i in sum_map[step]:
        for j in range(global_min):
            available.add(i - j)
    has_winning = True
    for el in sum_map[step - 1]:
        complement = total - el
        if complement not in available:
            has_winning = False
            break
    return has_winning

lengths, totals = init()
sum_map, step_map, global_min = prepare_sums(lengths)
for t in totals:
    has_winning = test(t, sum_map, step_map, global_min)
    if has_winning:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('2\n')