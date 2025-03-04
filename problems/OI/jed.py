import sys
from typing import Set


class Node:

    def __init__(self, main, remainder, parent):
        self.main = main
        self.remainder = remainder
        self.parent = parent


def only_10s(number):
    if _is_satisfied(number):
        return number
    reduced, iterations = _reduce(number, 0)
    if _is_satisfied(reduced):
        return reduced * 10 ** iterations
    result = _divide(reduced)
    if result is not None and len(str(result)) - iterations <= 100:
        return result * 10 ** iterations
    return None


def _divide(number):
    used = set()
    used.add(number)
    root = Node(used, None, None)
    first = _ends_with_one(number)
    main = int(first // 10)
    first_child = Node(main, 1, root)
    last_node = _generate(number, first_child, used)
    return _unwind_solution(last_node)


def _unwind_solution(node):
    if node is None:
        return None
    curr = node
    result = str(node.main)
    while curr.remainder is not None:
        result += str(curr.remainder)
        curr = curr.parent
    return int(result)


def _generate(number, node, used: Set):
    if _is_satisfied(node.main):
        return node
    for i in range(1, 10):
        multiplied = number * i + node.main
        main = int(multiplied // 10)
        remainder = int(multiplied % 10)
        if (remainder == 0 or remainder == 1) and main not in used:
            child_node = Node(main, remainder, node)
            used.add(main)
            solution = _generate(number, child_node, used)
            if solution is not None:
                return solution
    return None


def _ends_with_one(number):
    for i in range(1, 10):
        multiplied = i * number
        if multiplied % 10 == 1:
            return multiplied


def _reduce(number, i):
    if number % 2 == 0:
        return _reduce(int(number / 2), i + 1)
    if number % 5 == 0:
        return _reduce(int(number / 5), i + 1)
    return number, i


def _is_satisfied(number):
    s = str(number)
    for i in range(len(s)):
        if s[i] != '1' and s[i] != '0':
            return False
    return True


n = int(input().strip())
for _ in range(n):
    number = int(input().strip())
    solution = only_10s(number)
    if solution is None:
        sys.stdout.write('BRAK\n')
    else:
        sys.stdout.write(str(solution) + '\n')
