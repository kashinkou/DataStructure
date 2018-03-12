class UnionFind:
    """
    @param: n: An integer
    """

    def __init__(self, n):
        self.father = range(n + 1)

    """
    @param: x: An integer
    @return: An integer
    """

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])  # path compression
        return self.father[x]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
