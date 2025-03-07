import collections
import sys
from typing import Set


class Node:

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


class State:
    def __init__(self, containers=None):
        if containers is None:
            containers = []
        self.containers = containers.copy()

    def empty_container(self, index):
        self.containers[index] = 0

    def _states_from_filling_up(self, target_container, explored, moves, capacities):
        result = []
        difference = capacities[target_container] - self.containers[target_container]
        for index in range(len(self.containers)):
            if index != target_container and self.containers[index] > difference:
                move = (difference, capacities[index], target_container, capacities[target_container])
                if move not in moves:
                    copied = State(self.containers)
                    copied.containers[target_container] += difference
                    copied.containers[index] -= difference
                    if tuple(copied.containers) not in explored:
                        result.append(copied)
            elif index != target_container and self.containers[index] <= difference:
                move = (self.containers[index], capacities[index], target_container, capacities[target_container])
                if move not in moves:
                    copied = State(self.containers)
                    copied.containers[target_container] += self.containers[index]
                    copied.empty_container(index)
                    if tuple(copied.containers) not in explored:
                        result.append(copied)
        return result

    def possible_states(self, explored, capacities):
        result = []
        moves = set()
        for index in range(len(self.containers)):
            move = (self.containers[index], capacities[index], -1)
            if move not in moves:
                copied = State(self.containers)
                copied.empty_container(index)
                if tuple(copied.containers) not in explored:
                    result.append(copied)
            if self.containers[index] < capacities[index]:
                result.extend(self._states_from_filling_up(index, explored, moves, capacities))
        return result


def _create_decision_tree(target, node: Node, capacities):
    queue = collections.deque()
    explored = set()
    queue.append(node)
    while len(queue) > 0:
        current_node = queue.popleft()
        if current_node.state.containers == target.containers:
            return current_node
        explored.add(tuple(current_node.state.containers))
        options = current_node.state.possible_states(explored, capacities)
        for o in options:
            queue.append(Node(o, current_node))
    return None


def _solve_decision_tree(leaf):
    if leaf is None:
        return None
    count = 0
    current = leaf
    while current.parent is not None:
        current = current.parent
        count += 1
    return count


def init():
    num_of_containers = int(input().strip())
    containers = [int(i) for i in input().strip().split()]
    capacities = containers.copy()
    target = [int(i) for i in input().strip().split()]
    solution = _solve_decision_tree(_create_decision_tree(State(target), Node(State(capacities), None), capacities))
    if solution is None:
        sys.stdout.write('NIE')
    else:
        sys.stdout.write(str(solution))


init()
