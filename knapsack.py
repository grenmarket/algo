import sys


def max_value(objects, total_weigth):
    results = [[0] * (len(objects)+1) for _ in range(total_weigth + 1)]
    for w in range(total_weigth + 1):
        results[w][0] = 0
    for i in range(1, len(objects)+1):
        for w in range(0, total_weigth + 1):
            curr_value = objects[i-1][0]
            curr_weight = objects[i-1][1]
            if curr_weight > w:
                results[w][i] = results[w][i-1]
            else:
                results[w][i] = max(results[w][i-1], results[w-curr_weight][i-1] + curr_value)
    max_weight = results[total_weigth][len(objects)]
    max_objects = reconstruct_max(results, objects)
    return max_weight, max_objects


def max_value_recursive(objects, obj_index, total_weight, results):
    if obj_index == -1:
        return 0
    key = (obj_index, total_weight)
    if key in results:
        return results[key]
    repeat = max_value_recursive(objects, obj_index - 1, total_weight, results)
    results[(obj_index-1, total_weight)] = repeat
    curr_weight = objects[obj_index][1]
    curr_value = objects[obj_index][0]
    if curr_weight > total_weight:
        return repeat
    value_without = max_value_recursive(objects, obj_index-1, total_weight - curr_weight, results)
    results[(obj_index-1, total_weight - curr_weight)] = value_without
    alternative = curr_value + value_without
    return max(repeat, alternative)


def reconstruct_max(result, objects):
    i = -1
    w = -1
    chosen_objects = []
    value = result[w][i]
    while value > 0:
        if result[w][i] != result[w][i-1]:
            curr_value = objects[i][0]
            curr_weight = objects[i][1]
            chosen_objects.append(objects[i])
            w -= curr_weight
            value -= curr_value
        i -= 1
    return chosen_objects

def init():
    with open('files/knapsack_big.txt', 'r') as file:
        lines = [line.split() for line in file]
        knapsack_size = int(lines[0][0])
        objects = [(int(item[0]), int(item[1])) for item in lines[1:]]
        return objects, knapsack_size

sys.setrecursionlimit(10**6)
objects, size = init()
print(max_value_recursive(objects, len(objects) - 1, size, {}))
