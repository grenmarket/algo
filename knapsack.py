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

objects = [(3,4),(2,3),(4,2),(4,3)]
print(max_value(objects, 6))
