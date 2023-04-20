from point import Point
from abc import ABC, abstractmethod


# ==================== Adajacency Base ======================================
class Adjacency2D(ABC):
    """Base class for 2D adjacencies."""

    @abstractmethod
    def neighbours(self, point):
        """Return a list of neighbours for the given point."""
        pass


# ===================== 4 Connected Adjacency ===============================
class Adjacency4(Adjacency2D):
    """4-connected adjacency: horizontal and vertical neighbours."""

    def __init__(self):
        self.offset_points = [
            Point(row=0, col=1),
            Point(row=1, col=0),
            Point(row=0, col=-1),
            Point(row=-1, col=0),
        ]

    def neighbours(self, point):
        """Return a list of 4-connected neighbours for the given point."""
        neighbours = []
        for offset in self.offset_points:
            neighbour = offset + point
            neighbours.append(neighbour)
        return neighbours


# ====================== 8 Connected Adjacency ===============================
class Adjacency8(Adjacency2D):
    """8-connected adjacency: horizontal, vertical, and diagonal neighbours."""

    def __init__(self, width, height):
        self.offset_points = [
            Point(row=-1, col=-1),
            Point(row=-1, col=0),
            Point(row=-1, col=1),
            Point(row=0, col=-1),
            Point(row=0, col=1),
            Point(row=1, col=-1),
            Point(row=1, col=0),
            Point(row=1, col=1),
        ]
        self.width = width
        self.height = height

    def neighbours(self, point):
        """Return a list of 8-connected neighbours for the given point."""
        neighbours = []
        for offset in self.offset_points:
            neighbour = offset + point
            if 0 <= neighbour.row < self.height and 0 <= neighbour.col < self.width:
                neighbours.append(neighbour)
        return neighbours
