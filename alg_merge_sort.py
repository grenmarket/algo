import math


def mergesort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left_a = a[:mid]
        right_a = a[mid:]
        mergesort(left_a)
        mergesort(right_a)
        merge(a, left_a, right_a)


def merge(a, left, right):
    left.append(math.inf)
    right.append(math.inf)
    i = 0
    j = 0
    for n in range(len(a)):
        if left[i] <= right[j]:
            a[n] = left[i]
            i += 1
        else:
            a[n] = right[j]
            j += 1


array = [5, 3, 8, 11, 56, 2, 34, 77, 15, 23, 9, 10, 1, 44, 33, 14]
mergesort(array)
print(array)
