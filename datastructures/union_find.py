class UnionFind:

    def __init__(self, size):
        self.components = [(i, 1) for i in range(size)]
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
            if size1 > size2:
                self.components[leader2] = (leader1, size2)
                self.components[leader1] = (leader1, size1 + size2)
            else:
                self.components[leader1] = (leader2, size1)
                self.components[leader2] = (leader2, size1 + size2)
            self.clusters -= 1

