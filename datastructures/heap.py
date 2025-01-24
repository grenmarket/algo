array = []

def insert(a):
    index = len(array)
    array.append(a)
    parent, parent_index = get_parent(index)
    while parent is not None and parent > a:
        array[parent_index], array[index] = array[index], array[parent_index]
        index = parent_index
        parent, parent_index = get_parent(index)

def min():
    if len(array) == 0:
        return None
    result = array[0]
    last = len(array) - 1
    array[0], array[last] = array[last], array[0]
    del array[last]
    bubble_down(0)
    return result

def bubble_down(index):
    left = (index+1)*2 - 1
    right = left+1
    if left >= len(array):
        return
    if right >= len(array):
        if array[left] < array[index]:
            array[left], array[index] = array[index], array[left]
            return
        else:
            return
    if array[left] < array[right]:
        array[index], array[left] = array[left], array[index]
        bubble_down(left)
    else:
        array[index], array[right] = array[right], array[index]
        bubble_down(right)


def get_parent(index):
    if index == 0:
        return None, None
    parent_index = (index-1) // 2
    return array[parent_index], parent_index

# todo: turn into a class, min/max parameter
