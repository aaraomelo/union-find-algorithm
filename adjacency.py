from point import Point
from abc import ABC, abstractmethod


# ==================== Adajacency Base ======================================
class Adjacency2D(ABC):
	def __init__(self):
		pass 

	@abstractmethod
	def neighbours(self, point): 
		pass

# ===================== 4 Connected Adjacency ===============================
class Adjacency4(Adjacency2D):
	def __init__(self):
		super().__init__()
		self.offsets = [Point(row=0, col=1), Point(row=1, col=0), 
					    Point(row=0, col=-1),  Point(row=-1, col=0)]

	def neighbours(self, point):
		neighbours = []
		for offset in self.offsets:
			q = offset + point
			neighbours.append(offset + point)
		return neighbours
 
# ====================== 8 Connected Adjacency ===============================
class Adjacency8(Adjacency2D):
	def __init__(self, width, height):
		super().__init__(width, height)
		# TODO: 

	def neighbours(self, point):
		# TODO: 
		pass

