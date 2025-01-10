import math
from typing import List

total = 0
def quicksort(arr: List[int], start: int, end: int):
    if end - start < 2:
        return 0
    pivot, index = get_pivot(arr, start, end)
    pivot_index = sort(arr, index, start, end)
    left = quicksort(arr, start, pivot_index)
    right = quicksort(arr, pivot_index + 1, end)
    return left + right + (end - start - 1)


def get_pivot(arr, start, end):
    z_index = math.ceil((end + start) / 2.0) - 1
    indexes = [start, end - 1, z_index]
    middle = sorted(indexes, key=lambda x: arr[x])[1]

    return arr[middle], middle


def sort(arr, pivot_index, start, end):
    pivot = arr[pivot_index]
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    i, j, n = 1, 1, 1
    while n < end - start:
        if arr[n + start] > pivot:
            j += 1
        else:
            arr[i + start], arr[j + start] = arr[j + start], arr[i + start]
            i += 1
            j += 1
        n += 1
    arr[start], arr[i + start - 1] = arr[i + start - 1], arr[start]
    return i + start - 1

with open('files/quicksort.txt', 'r') as file:
    nums = [int(line.strip()) for line in file]
    print(quicksort(nums, 0, len(nums)))