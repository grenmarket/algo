import sys
from typing import List


class Labeler:
    def __init__(self, root):
        self.root = root
        self.index = 1

    def label(self):
        self._label(self.root)

    def _label(self, node):
        node.key = self.index
        self.index += 1
        if node.left is not None:
            self._label(node.left)
        if node.right is not None:
            self._label(node.right)


class Printer:
    def __init__(self, root):
        self.root = root

    def bracket_form(self):
        return self._bracket(self.root)

    def genealogical_form(self):
        root_array = [0]
        return self._genealogical(self.root, root_array)

    def _genealogical(self, node, array):
        if node.parent is not None:
            array.append(node.parent.key)
        if node.left is not None:
            self._genealogical(node.left, array)
        if node.right is not None:
            self._genealogical(node.right, array)
        return array

    def _bracket(self, node):
        if node.left is None and node.right is None:
            return '()'
        result = '(' + self._bracket(node.left) + self._bracket(node.right) + ')'
        return result


class Node:
    def __init__(self, level):
        self.parent = None
        self.left = None
        self.right = None
        self.level = level
        self.key = None

    def join(self, other):
        if self.level != other.level:
            raise Exception('levels not equal')
        parent = Node(self.level - 1)
        parent.left = self
        parent.right = other
        self.parent = parent
        other.parent = parent
        return parent


def init():
    input()
    return [int(item) for item in input().strip().split()]


def transform_into_tree(levels: List):
    if len(levels) == 1 and levels[0] == 0:
        return Node(0)

    nodes = [Node(level) for level in levels]
    max_level = max(levels)
    curr_level = max(levels)
    for i in range(max_level, 0, -1):
        for j in range(len(nodes) - 1):
            if j < len(nodes) - 1:
                if nodes[j].level == curr_level and nodes[j + 1].level == curr_level:
                    parent = nodes[j].join(nodes[j + 1])
                    nodes = nodes[:j] + [parent] + nodes[j + 2:]
        curr_level -= 1

    if len(nodes) == 1 and nodes[0].level == 0:
        return nodes[0]
    return None


levels = init()
tree = transform_into_tree(levels)
if tree is None:
    sys.stdout.write('NIE')
else:
    Labeler(tree).label()
    printer = Printer(tree)
    genealogical = printer.genealogical_form()
    sys.stdout.write(' '.join(str(i) for i in genealogical))
    sys.stdout.write('\n')
    sys.stdout.write(printer.bracket_form())
