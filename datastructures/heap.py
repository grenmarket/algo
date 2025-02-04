from typing import Callable, TypeVar, Any


class Heap:
    T = TypeVar('T', bound=Any)
    C = TypeVar('C', bound=int)
    ExtractorType = Callable[[T], C]

    def __init__(self, isMin: bool, key_extractor: ExtractorType):
        self.array = []
        self.size = 0
        self.key_extractor = key_extractor
        self.compare = (lambda a, b: self.key_extractor(a) < self.key_extractor(b)) if isMin else (
            lambda a, b: self.key_extractor(a) > self.key_extractor(b))
        self.mapping = {}

    def insert(self, a):
        index = len(self.array)
        self.array.append(a)
        parent, parent_index = self.get_parent(index)
        while parent is not None and self.compare(a, parent):
            self.swap(index, parent_index)
            index = parent_index
            parent, parent_index = self.get_parent(index)
        self.size += 1
        self.mapping[a] = index

    def delete(self, a):
        index = self.mapping.get(a)
        if index is None:
            return
        last = len(self.array) - 1
        self.swap(last, index)
        del self.array[last]
        self.bubble_down(index)
        self.size -= 1
        self.mapping.pop(a)

    def swap(self, a, b):
        self.array[b], self.array[a] = self.array[a], self.array[b]

    def min_peek(self):
        if len(self.array) == 0:
            return None
        return self.array[0]

    def min(self):
        if len(self.array) == 0:
            return None
        result = self.array[0]
        last = len(self.array) - 1
        self.swap(last, 0)
        del self.array[last]
        self.bubble_down(0)
        self.size -= 1
        self.mapping.pop(result)
        return result

    def bubble_down(self, index):
        left = (index + 1) * 2 - 1
        right = left + 1
        if left >= len(self.array):
            return
        if right >= len(self.array):
            if self.compare(self.array[left], self.array[index]):
                self.swap(index, left)
                return
            else:
                return
        if self.compare(self.array[left], self.array[right]):
            if self.compare(self.array[left], self.array[index]):
                self.swap(left, index)
                self.bubble_down(left)
        else:
            if self.compare(self.array[right], self.array[index]):
                self.swap(right, index)
                self.bubble_down(right)

    def get_parent(self, index):
        if index == 0:
            return None, None
        parent_index = (index - 1) // 2
        return self.array[parent_index], parent_index
