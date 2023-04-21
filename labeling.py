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
    # TODO
    pass


"""
The Union-Find algorithm, also known as the Union-Find algorithm, is an algorithm that allows grouping elements into disjoint sets (or connected components) and efficiently querying to which set an element belongs.

The algorithm consists of three main operations:

MakeSet: Creates a new set containing a single element.
Find: Finds the set (or component) to which an element belongs.
Union: Combines two distinct sets into a single set.
The data structure used to implement Union-Find is a tree. Each node in the tree represents an element and has a pointer to its parent node in the tree. The root of a tree is itself. When two sets are joined, the root of the smaller set is added as a child of the root of the larger set.

The rank array is a vector used in the Union-Find algorithm to keep track of the height of the tree. Each position in the array represents an element, and the value of the position indicates the height of the subtree rooted at the corresponding element.

When two sets are joined, the resulting tree can become unbalanced, with one branch much larger than the other. This can increase the execution time of operations such as Find, which traverse the tree.

The rank array is used to prevent this from happening, by keeping the height of the trees balanced. Whenever two sets of the same rank are joined, the height of the resulting tree is incremented by 1. When two sets with different heights are joined, the root of the smaller tree is added as a child of the root of the larger tree, keeping the height of the tree balanced.

This strategy of balancing the height of the trees ensures that the execution time of operations in Union-Find is O(log n), where n is the number of elements in the set.

To perform the Find operation, we traverse the tree from the element in question until we find the root, which represents the set to which it belongs. When traversing the tree, it is possible to optimize the search by "linking" the visited node directly to the root, reducing the height of the tree and improving performance.

makeSet(x):
  parent[x] ← x
  rank[x] ← 0

find(x):
  if parent[x] = x, then
    return x
  else
    parent[x] ← find(parent[x])
    return parent[x]

union(x, y):
  rootX ← find(x)
  rootY ← find(y)
  if rootX ≠ rootY, then
    if rank[rootX] < rank[rootY], then
      parent[rootX] ← rootY
    else if rank[rootX] > rank[rootY], then
      parent[rootY] ← rootX
    else
      parent[rootY] ← rootX
      rank[rootX] ← rank[rootX] + 1
      
To apply the Union-Find algorithm to a binary image f, we can consider each pixel as an element to be inserted into a set. To do this, we can traverse the image and create a UnionFind object for each pixel with a value of 1. Then, for each created UnionFind object, we can call the make_set() method passing the pixel index as the identifier.

After creating all the UnionFind objects and inserting the elements into their respective sets, we can traverse the image again and for each pair of adjacent pixels with a value of 1, we can union the sets they belong to using the union() method of the corresponding UnionFind object.

After uniting all the sets, we can call the canonize() method to update the root of each set and ensure that all pixels are associated with the correct set.

The final result will be a binary image where each set of pixels with a value of 1 will be represented by a single value. This process is useful, for example, for image segmentation, where objects in the image can be separated into different regions.

Exemplo:

from PIL import Image
from union_find import UnionFind  # supondo que a implementação do UnionFind esteja em um módulo separado

# Carrega a imagem binária em escala de cinza
img = Image.open('imagem_binaria.png').convert('L')

# Cria uma instância do UnionFind
uf = UnionFind()

# Percorre a imagem pixel a pixel
width, height = img.size
for y in range(height):
    for x in range(width):
        # Se o pixel for branco, cria um novo conjunto e associa o pixel a ele
        if img.getpixel((x, y)) == 255:
            p = (x, y)
            uf.make_set(p)

            # Verifica se os pixels vizinhos também são brancos e, se sim, une os conjuntos
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                q = (x + dx, y + dy)
                if 0 <= q[0] < width and 0 <= q[1] < height and img.getpixel(q) == 255:
                    uf.union(p, q)

# Canoniza o UnionFind (garante que cada elemento aponte diretamente para a raiz de seu conjunto)
uf.canonize()

# Cria um dicionário que mapeia as raízes dos conjuntos a um rótulo (número inteiro)
labels = {}
for p in uf.parent.keys():
    root = uf.find(p)
    if root not in labels:
        labels[root] = len(labels) + 1

# Percorre a imagem novamente, rotulando cada pixel com o rótulo correspondente
for y in range(height):
    for x in range(width):
        if img.getpixel((x, y)) == 255:
            root = uf.find((x, y))
            img.putpixel((x, y), labels[root])

# Salva a imagem rotulada
img.save('imagem_rotulada.png')
      
"""
