import numpy as np
from coord import Coord
import numpy as np
from matplotlib import pyplot as plt

class GridMap: # embedding cost 
	def __init__(self, _width = 16, _height = 12, _grid = None):
		self.width = _width
		self.height = _height
		if _grid == None:
			self.grid = [["1" for i in range(self.width)] for j in range(self.height)]
		else:
			self.grid = _grid

		# display stuff
		self.figurecreated = False

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
		weight = (self.sym2weight(grid[pos1]) + self.sym2weight(grid[pos2])) / 2 # find the average weight
		if heuristic == "man":
			return weight * (abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y))
		elif heuristic == "euc":
			return weight * ((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2) ** 0.5

	def withinBounds(self, X, Y = None):
		"""
		Arguments:
			X: the position, or if this is a single number, then this is the X coordinate
			Y: only if X is a single number, then this is the Y coordinate
		Return:
			True if within bounds of the map, False otherwise
		"""
		pos = Coord(X, Y)
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
		if not self.withinBounds(pos1) or not self.withinBounds(pos2) or \
				self.grid[pos1.y][pos1.x] == "0" or self.grid[pos2.y][pos2.x] == "0":
			return False
		# note: if same position, considered a valid transition
		return (abs(pos1.x - pos2.x) <= 1 and abs(pos1.y - pos2.y) <= 1)

	def sym2weight(self, symbol):
		"""
		Arguments:
			symbol: either "0", "1", "2", "a", or "b"
		Return:
			the cost of the symbol, or None if invalid
		"""
		if symbol == "1":
			return 1.0
		elif symbol == "2":
			return 2.0
		elif symbol == "a":
			return 0.25
		elif symbol == "b":
			return 0.5
		elif symbol == "s":
			return 1.5
		elif symbol == "g":
			return 1.75 # careful! documentation does not indicate what this is
		else:
			return None

	def getSuccessors(self, X, Y = None):
		"""
		Arguments:
			X: the position, or if this is a single number, then this is the X coordinate
			Y: only if X is a single number, then this is the Y coordinate
		Return:
			a list of successor coordinates
		"""
		pos = Coord(X, Y)
		dx = [-1, -1, -1, 0, 1, 1, 1, 0]
		dy = [-1, 0, 1, 1, 1, 0, -1, -1]
		successors = []
		for i in range(8):
			newpos = Coord(pos.x + dx[i], pos.y + dy[i])
			if self.validTransition(self, pos, newpos):
				successors.append([newpos.x, newpos.y])
		return successors

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
		image = np.array([[[0.0, 0.0, 0.0] for x in range(self.width)] for y in range(self.height)])

		for x in range(self.width):
			for y in range(self.height):
				val = self.grid[y][x]
				if val == "1":
					val = [0.0, 0.5, 1.0]
				elif val == "2":
					val = [0.3, 0.1, 1.0]
				elif val == "a":
					val = [1.0, 1.0, 0.0]
				elif val == "b":
					val = [0.5, 1.0, 0.0]
				elif val == "s":
					val = [1.0, 0.0, 0.0]
				elif val == "g":
					val = [1.0, 1.0, 1.0]
				else:
					val = [0.0, 0.0, 0.0]
				image[y, x, :] = val

		if not self.figurecreated:
			self.figurecreated = True
			plt.figure(1)
			plt.title("AStar")

		plt.imshow(image, interpolation='nearest')
		plt.colorbar()
		plt.show()
