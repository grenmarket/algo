import sys
from typing import List
def max_decrease(results: List):
    lengths = {}
    decreasing = [(float(value), index) for index, value in enumerate(results)]
    decreasing.sort(key=lambda r: r[0], reverse=True)
    for i in range(len(decreasing)-1, -1, -1):
        lengths[i] = count_decrease(decreasing, i, lengths)
    return max(lengths.values())

def count_decrease(decreasing, index, lengths):
    if index == len(decreasing) - 1:
        return 1
    curr_max = 1
    for i in range(index + 1, len(decreasing)):
        if decreasing[i][1] > decreasing[index][1] and decreasing[i][0] < decreasing[index][0]:
            curr = 1 + lengths[i]
            if curr > curr_max:
                curr_max = curr
    return curr_max

n = input()
results = input().strip().split()
max_d = max_decrease(results)
sys.stdout.write(str(100*max_d))