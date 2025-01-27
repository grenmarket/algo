from typing import Callable, TypeVar, Any


class Heap:

    T = TypeVar('T', bound=Any)
    C = TypeVar('C', bound=int)
    ExtractorType = Callable[[T], C]
    
    def __init__(self, isMin, key_extractor: ExtractorType):
        self.array = []
        self.isMin = isMin
        self.size = 0
        self.key_extractor = key_extractor


    def comp(self, a1, a2):
        if self.isMin:
            return self.key_extractor(a1) < self.key_extractor(a2)
        else:
            return self.key_extractor(a1) > self.key_extractor(a2)

    def insert(self, a):
        index = len(self.array)
        self.array.append(a)
        parent, parent_index = self.get_parent(index)
        while parent is not None and self.comp(a, parent):
            self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
            index = parent_index
            parent, parent_index = self.get_parent(index)
        self.size += 1

    def min_peek(self):
        if len(self.array) == 0:
            return None
        return self.array[0]

    def min(self):
        if len(self.array) == 0:
            return None
        result = self.array[0]
        last = len(self.array) - 1
        self.array[0], self.array[last] = self.array[last], self.array[0]
        del self.array[last]
        self.bubble_down(0)
        self.size -= 1
        return result

    def bubble_down(self, index):
        left = (index + 1) * 2 - 1
        right = left + 1
        if left >= len(self.array):
            return
        if right >= len(self.array):
            if self.comp(self.array[left], self.array[index]):
                self.array[left], self.array[index] = self.array[index], self.array[left]
                return
            else:
                return
        if self.comp(self.array[left], self.array[right]):
            self.array[index], self.array[left] = self.array[left], self.array[index]
            self.bubble_down(left)
        else:
            self.array[index], self.array[right] = self.array[right], self.array[index]
            self.bubble_down(right)

    def get_parent(self, index):
        if index == 0:
            return None, None
        parent_index = (index - 1) // 2
        return self.array[parent_index], parent_index
