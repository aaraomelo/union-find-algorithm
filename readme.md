# Union-Find Algorithm

The Union-Find algorithm, also known as the Union-Find algorithm, is an algorithm that allows grouping elements into disjoint sets (or connected components) and efficiently querying to which set an element belongs.

The algorithm consists of three main operations:

- MakeSet: Creates a new set containing a single element.
- Find: Finds the set (or component) to which an element belongs.
- Union: Combines two distinct sets into a single set.

The data structure used to implement Union-Find is a tree. Each node in the tree represents an element and has a pointer to its parent node in the tree. The root of a tree is itself. When two sets are joined, the root of the smaller set is added as a child of the root of the larger set.

The rank array is a vector used in the Union-Find algorithm to keep track of the height of the tree. Each position in the array represents an element, and the value of the position indicates the height of the subtree rooted at the corresponding element.

When two sets are joined, the resulting tree can become unbalanced, with one branch much larger than the other. This can increase the execution time of operations such as Find, which traverse the tree.

The rank array is used to prevent this from happening, by keeping the height of the trees balanced. Whenever two sets of the same rank are joined, the height of the resulting tree is incremented by 1. When two sets with different heights are joined, the root of the smaller tree is added as a child of the root of the larger tree, keeping the height of the tree balanced.

This strategy of balancing the height of the trees ensures that the execution time of operations in Union-Find is O(log n), where n is the number of elements in the set.

To perform the Find operation, we traverse the tree from the element in question until we find the root, which represents the set to which it belongs. When traversing the tree, it is possible to optimize the search by "linking" the visited node directly to the root, reducing the height of the tree and improving performance.

```python
class UnionFind:
    def makeSet(x):
        parent[x] = x
        rank[x] = 0

    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
```
# Applying the Union-Find algorithm to a binary image

To apply the Union-Find algorithm to a binary image `f`, we can consider each pixel as an element to be inserted into a set. To do this, we can traverse the image and create a UnionFind object for each pixel with a value equal to 1. Then, for each created UnionFind object, we can call the `make_set()` method passing the pixel index as identifier.

After creating all UnionFind objects and inserting the elements into their respective sets, we can traverse the image again and, for each pair of adjacent pixels with a value equal to 1, we can merge the sets to which they belong using the `union()` method of the corresponding UnionFind object.

After merging all sets, we can call the `canonize()` method to update the root of each set and ensure that all pixels are associated with the correct set.

The final result will be a binary image where each set of pixels with a value equal to 1 will be represented by a single value. This process is useful, for example, for image segmentation, where objects in the image can be separated into different regions.

Code example:

```python
from PIL import Image
from union_find import UnionFind  # assuming that the implementation of UnionFind is in a separate module

# Load the binary image in grayscale
img = Image.open('binary_image.png').convert('L')

# Create an instance of UnionFind
uf = UnionFind()

# Traverse the image pixel by pixel
width, height = img.size
for y in range(height):
    for x in range(width):
        # If the pixel is white, create a new set and associate the pixel with it
        if img.getpixel((x, y)) == 255:
            p = (x, y)
            uf.make_set(p)

            # Check if neighboring pixels are also white and, if so, merge the sets
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                q = (x + dx, y + dy)
                if 0 <= q[0] < width and 0 <= q[1] < height and img.getpixel(q) == 255:
                    uf.union(p, q)

# Canonize the UnionFind (ensure that each element points directly to the root of its set)
uf.canonize()

# Create a dictionary that maps the roots of the sets to a label (integer number)
labels = {}
for p in uf.parent.keys():
    root = uf.find(p)
    if root not in labels:
        labels[root] = len(labels) + 1

# Traverse the image again, labeling each pixel with the corresponding label
for y in range(height):
    for x in range(width):
        if img.getpixel((x, y)) == 255:
            root = uf.find((x, y))
            img.putpixel((x, y), labels[root])

# Save the labeled image
img.save('labeled_image.png')
```
# Connected-Component Labeling Algorithm

To implement the `label` function using the `Adjacency8` and `UnionFind` classes, we can follow the steps of the connected-component labeling algorithm:

1. Create a `UnionFind` object.

```python
uf = UnionFind()
```

2. Initialize labels as `0`.

```python
labels = np.zeros(f.shape, dtype=np.int32)
```

3. Iterate through each pixel in the image `f`.

```python
for i in range(f.shape[0]):
    for j in range(f.shape[1]):
        if f[i,j] == 1:
            neighbours = adj.neighbours(Point(row=i, col=j))
            labels[i,j] = uf.make_set((i,j))
            for nb in neighbours:
                if labels[nb.row, nb.col]:
                    uf.union(labels[nb.row, nb.col], labels[i,j])
```

4. If the pixel is white (i.e., equal to `1`), find the labels of its 8-connected neighbors using the `UnionFind` object.
```python
if f[i,j] == 1:
    neighbours = adj.neighbours(Point(row=i, col=j))
    ...
```
5. If the pixel has no neighbors with labels, assign it a new label.
```python
if f[i,j] == 1:
    neighbours = adj.neighbours(Point(row=i, col=j))
    if not any(labels[nb.row, nb.col] for nb in neighbours):
        labels[i,j] = uf.make_set((i,j))
    ...
```

6. If the pixel has one neighbor with a label, assign it the same label.
```python
if f[i,j] == 1:
    neighbours = adj.neighbours(Point(row=i, col=j))
    neighbour_labels = set(labels[nb.row, nb.col] for nb in neighbours if labels[nb.row, nb.col])
    if len(neighbour_labels) == 1:
        labels[i,j] = neighbour_labels.pop()
    ...
```

7. If the pixel has multiple neighbors with labels, assign it the smallest label and union the other labels.
```python
if f[i,j] == 1:
    neighbours = adj.neighbours(Point(row=i, col=j))
    neighbour_labels = set(labels[nb.row, nb.col] for nb in neighbours if labels[nb.row, nb.col])
    if len(neighbour_labels) > 1:
        smallest_label = min(neighbour_labels)
        labels[i,j] = smallest_label
        for label in neighbour_labels:
            if label != smallest_label:
                uf.union(smallest_label, label)
    ...
```

8. After iterating through all pixels, canonize the `UnionFind` object to ensure that all labels are represented by their root label.
```python
uf.canonize()
```

9. Return a dictionary mapping the original labels to their canonical labels.
```python
canonical_labels = {label: uf.find(label) for label in np.unique(labels) if label != 0}
```
