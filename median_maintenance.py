from datastructures import heap

def init():
    with open('files/Median.txt', 'r') as file:
        return [int(line.strip()) for line in file]


numbers = init()
medians = []
left = heap.Heap(False)
right = heap.Heap(True)

medians.append(numbers[0])
left.insert(numbers[0])
for n in numbers[1:]:
    if n < left.min_peek():
        left.insert(n)
    else:
        right.insert(n)
    while left.size - right.size > 1:
        right.insert(left.min())
    while right.size - left.size > 0:
        left.insert(right.min())
    medians.append(left.min_peek())

sum_of_medians = sum(medians)
print(sum_of_medians % 10000)