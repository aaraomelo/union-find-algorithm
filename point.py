class Point:
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def __add__(self, q):
		return Point(self.row + q.row, self.col + q.col)

	def __sub__(self, q):
		return Point(self.row - q.row, self.col - q.col)

	def __eq__(self, q):
		return self.row == q.row and self.col == self.col

	def __ne__(self, q):
		return not (self == q)

	def __str__(self):
		return "(" + str(self.row) + ", " + str(self.col) + ")"
 
class Box:
	def __init__(self, top_left, bottom_right):
		assert (top_left.row < bottom_right.row), "bottom is above top in the plane"
		assert (top_left.col < bottom_right.col), "left is at right of 'right' in the plane"

		self.tl = top_left
		self.br = bottom_right

	def top(self):
		return self.tl.row

	def left(self):
		return self.tl.col

	def bottom(self):
		return self.br.row

	def right(self):
		return self.br.col

	def width(self):
		return self.br.col - self.tl.col

	def height(self):
		return self.br.row - self.tl.row

	def contains(self, point):
		return  self.left() <= point.col <= self.right() and self.top() <= point.row <= self.bottom()

class PixelIndexer:
	def __init__(self, domain):
		self.domain = domain

	def point_to_index(self, point):
		q = point - self.domain.tl
		return int(((self.domain.width()+1)*q.row) + q.col)

	def index_to_point(self, index):
		q = Point(int(index / (self.domain.width()+1)), int(index % (self.domain.width()+1)))
		return q + self.domain.tl 