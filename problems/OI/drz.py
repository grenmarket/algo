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

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def init():
    n_items = input()
    levels = [int(item) for item in input().strip().split()]
    return n_items, levels


def transform_into_tree(levels):
    if len(levels) == 1 and levels[0] == 0:
        return Node(0)
    stack = []
    start = Node(levels[0])
    stack.append(start)
    i = 1
    while i < len(levels):
        next = Node(levels[i])
        if next.level == stack[-1].level:
            stack[-1] = stack[-1].join(next)
        else:
            stack.append(next)
        i += 1
    if len(stack) == 1 and stack[0].level == 0:
        return stack[0]
    j = 1
    while j < len(stack) and len(stack) > 1:
        if stack[j].level == stack[j-1].level:
            parent = stack[j-1].join(stack[j])
            stack = stack[:j-1] + [parent] + stack[j+1:]
            j = 1
        else:
            j += 1
    if len(stack) == 1 and stack[0].level == 0:
        return stack[0]
    return None


i = 1
def label_nodes(root):
    global i
    root.key = i
    i += 1
    if root.left is not None:
        label_nodes(root.left)
    if root.right is not None:
        label_nodes(root.right)


levels = [3,3,2,3,3,3]
tree = transform_into_tree(levels)
if tree is None:
    print('none')
else:
    label_nodes(tree)
    tree.display()