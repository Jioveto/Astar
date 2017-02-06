import numpy as np
from coord import Coord

class GridMap: # embedding cost 
	def __init__(self, _width = 16, _height = 12):
		self.width = _width
		self.height = _height
		self.grid = [[1 for i in range(self.width)] for j in range(self.height)]

	def getCost(self, pos1, pos2, heuristic = "euc"):
		"""
		Arguments:
			pos1: the first position
			pos2: the second position
			heuristic: either "man" for manhattan or "euc" for euclidean (default)
		Return:
			the cost if pos1 and pos2 are valid position, else None if they are not valid positions
		"""
		if not self.withinBounds(pos1) or not self.withinBounds(pos2) or \
				not self.validTransition(pos1, pos2):
			return None
		weight = (grid[pos1] + grid[pos2]) / 2 # find the average weight
		if heuristic == "man":
			return weight * (abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y))
		elif heuristic == "euc":
			return weight * ((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2) ** 0.5

	def withinBounds(self, pos):
		"""
		Arguments:
			pos: the position
		Return:
			True if within bounds of the map, False otherwise
		"""
		pos = Coord(pos)
		return (0 <= pos.x and pos.x < self.width and 0 <= pos.y and pos.y < self.height)

	def validTransition(self, pos1, pos2):
		"""
		Arguments:
			pos1: the first position
			pos2: the second position
		Return:
			True if a valid transition, False otherwise (according to specifications)
		"""
		pos1 = Coord(pos1)
		pos2 = Coord(pos2)
		if not self.withinBounds(pos1) or not self.withinBounds(pos2):
			return False
		# note: if same position, considered a valid transition
		return (abs(pos1.x - pos2.x) <= 1 and abs(pos1.y - pos2.y) <= 1)

	def __getitem__(self, ind):
		assert((type(ind) == type([]) or type(ind) == type((0, 0))) and len(ind) == 2 or \
				type(ind) == type(Coord(0, 0)))
		return self.grid[ind[1]][ind[0]]
	def __setitem__(self, ind, value):
		assert((type(ind) == type([]) or type(ind) == type((0, 0))) and len(ind) == 2 or \
				type(ind) == type(Coord(0, 0)))
		self.grid[ind[1]][ind[0]] = value
	def __str__(self):
		return str(np.matrix(self.grid)) + "\n"
	def display(self):
		# fill in later
		pass
	def close(self):
		# fill in later, closes display()
		pass
