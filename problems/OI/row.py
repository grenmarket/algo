import string
import sys
from typing import Dict

letters = list(string.ascii_lowercase)

class UnionFind:

    def __init__(self, size):
        self.components = [(i, 1, None) for i in range(size)]
        self.clusters = size


    def find(self, node):
        next = self.components[node][0]
        if next != node:
            return self.find(self.components[next][0])
        return next


    def merge(self, c1, c2):
        leader1 = self.find(c1)
        leader2 = self.find(c2)
        if leader1 != leader2:
            size1 = self.components[leader1][1]
            size2 = self.components[leader2][1]
            value1 = self.components[leader1][2]
            value2 = self.components[leader2][2]
            has_value = True if value1 is not None or value2 is not None else False
            if value1 is not None and value2 is not None:
                if value1 != value2:
                    self.clusters = -1
                    return
                else:
                    # cluster number has already been reduced for both so it should stay the same
                    self.clusters += 1
            new_value = None
            if has_value:
                if value1 is not None:
                    new_value = value1
                else:
                    new_value = value2
            if size1 > size2:
                self.components[leader2] = (leader1, size2, new_value)
                self.components[leader1] = (leader1, size1 + size2, new_value)
            else:
                self.components[leader1] = (leader2, size1, new_value)
                self.components[leader2] = (leader2, size1 + size2, new_value)
            self.clusters -= 1


    def assign(self, c1, value):
        leader = self.find(c1)
        size = self.components[leader][1]
        if self.components[leader][2] is None:
            self.components[leader] = (leader, size, value)
            self.clusters -= 1
        elif self.components[leader][2] != value:
                self.clusters = -1


def transform_word(word: str, length_map):
    result = []
    for ch in word:
        if ch == '0' or ch == '1':
            result.append(ch)
        else:
            n = length_map[ch]
            for i in range(n):
                result.append(ch + str(i))
    return result


def create_constraints(word1, word2, uf: UnionFind, variable_map: Dict):
    for i in range(len(word1)):
        ch1 = word1[i]
        ch2 = word2[i]
        if len(ch1) > 1 and len(ch2) > 1:
            uf.merge(variable_map[ch1], variable_map[ch2])
        else:
            if len(ch1) > 1 and len(ch2) == 1:
                uf.assign(variable_map[ch1], int(ch2))
            elif len(ch1) == 1 and len(ch2) > 1:
                uf.assign(variable_map[ch2], int(ch1))
            elif int(ch1) != int(ch2):
                uf.clusters = -1



def init():
    n_equations = int(input())
    for _ in range(n_equations):
        variable_map = {}
        length_map = {}
        main_index = 0
        n_variables = int(input())
        variables = [int(var) for var in input().split()]
        for i in range(n_variables):
            letter = letters[i]
            length_map[letter] = variables[i]
            for j in range(variables[i]):
                key = letter + str(j)
                variable_map[key] = main_index
                main_index += 1
        uf = UnionFind(main_index)
        input()
        word1 = input()
        input()
        word2 = input()
        w_arr_1 = transform_word(word1, length_map)
        w_arr_2 = transform_word(word2, length_map)
        create_constraints(w_arr_1, w_arr_2, uf, variable_map)
        n_clusters = uf.clusters
        if n_clusters < 0:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write(str(2**n_clusters)+'\n')

init()