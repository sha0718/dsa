class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

# Example: Detect cycle in undirected graph
def has_cycle(edges, n):
    uf = UnionFind(n)
    for u, v in edges:
        if uf.find(u) == uf.find(v):
            return True
        uf.union(u, v)
    return False

# Test
print(has_cycle([[0,1], [1,2], [2,3], [3,0]], 4))  # True
