import math


def count_inversions(nums):
    size = len(nums)
    if size == 1:
        return 0, nums
    count_left, l_arr = count_inversions(nums[:size//2])
    count_right, r_arr = count_inversions(nums[size//2:])
    intra, sorted = count_intra(l_arr, r_arr)
    return count_left + count_right + intra, sorted


def count_intra(left, right):
    res = []
    count = 0
    s_left = len(left)
    s_right = len(right)
    left.append(math.inf)
    right.append(math.inf)
    l_ind = 0
    r_ind = 0
    for i in range(s_right + s_left):
        if right[r_ind] < left[l_ind]:
            res.append(right[r_ind])
            count += (s_left - l_ind)
            r_ind += 1
        else:
            res.append(left[l_ind])
            l_ind += 1
    return count, res


with open('files/int_array.txt', 'r') as ints:
    nums = [int(line.strip()) for line in ints]
    print(count_inversions(nums)[0])