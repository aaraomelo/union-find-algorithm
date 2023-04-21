import numpy as np
from point import Point, Box, PixelIndexer


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, id):
        self.parent[id] = id
        self.rank[id] = 0

    def find(self, id):
        if self.parent[id] != id:
            self.parent[id] = self.find(self.parent[id])
        return self.parent[id]

    def canonize(self):
        for key in self.parent.keys():
            self.find(key)

    def union(self, id1, id2):
        root1 = self.find(id1)
        root2 = self.find(id2)

        if root1 == root2:
            return

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1


def label(f, adj):
    uf = UnionFind()
    labels = {}
    current_label = 1
    for y in range(f.shape[0]):
        for x in range(f.shape[1]):
            if f[y, x] == 1:
                neighbors = [
                    f[n.row, n.col] for n in adj.neighbours(Point(row=y, col=x))
                ]
                neighbor_labels = [labels.get(n, None) for n in neighbors]
                neighbor_labels = [l for l in neighbor_labels if l is not None]
                if not neighbor_labels:
                    labels[(y, x)] = current_label
                    uf.make_set(current_label)
                    current_label += 1
                else:
                    min_label = min(neighbor_labels)
                    labels[(y, x)] = min_label
                    for l in neighbor_labels:
                        uf.union(min_label, l)

    uf.canonize()

    canonical_labels = {}
    for k, v in labels.items():
        canonical_labels[k] = uf.find(v)

    return canonical_labels
