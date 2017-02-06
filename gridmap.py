import numpy as np
from coord import Coord
import pygame

# initialize the displayer
pygame.init()

class GridMap: # embedding cost 
	def __init__(self, _width = 16, _height = 12, _grid = None):
		self.width = _width
		self.height = _height
		if _grid == None:
			self.grid = [["1" for i in range(self.width)] for j in range(self.height)]
		else:
			self.grid = _grid

		# display stuff
		self.screen = None
		self.clock = None

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
		weight = (sym2weight(grid[pos1]) + sym2weight(grid[pos2])) / 2 # find the average weight
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
			return 0
		elif symbol == "g":
			return 1 # careful! documentation does not indicate what this is
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
		idealsize = (640, 480)
		ratio = (idealsize[0] / self.width, idealsize[0] / self.width)
		w = int(ratio[0]) * self.width
		h = int(ratio[1]) * self.height

		if self.screen == None:
			self.screen = pygame.display.set_mode((w, h))
		if self.clock == None:
			self.clock = pygame.time.Clock()
		if self.handleEvents() == False: # handle any events, such as closing the window
			return False
		self.screen.fill((255, 255, 255))

		color_regular = (0, 255, 255)
		color_regular_slow = (0, 0, 255)
		color_highway = (0, 255, 0)
		color_highway_slow = (0, 128, 0)
		color_start = (255, 0, 0)
		color_goal = (255, 0, 255)
		color_block = (0, 0, 0)

		# draw the grid
		for x in range(self.width):
			for y in range(self.height):
				region = pygame.Rect(x * ratio[0], y * ratio[1], ratio[0], ratio[1])
				color = color_block
				if self.grid[y][x] == "1":
					color = color_regular
				elif self.grid[y][x] == "2":
					color = color_regular_slow
				elif self.grid[y][x] == "a":
					color = color_highway
				elif self.grid[y][x] == "b":
					color = color_highway_slow
				elif self.grid[y][x] == "s":
					color = color_start
				elif self.grid[y][x] == "g":
					color = color_goal
				pygame.draw.rect(self.screen, color, region)

		# display the grid
		pygame.display.flip()
		self.clock.tick(40) # 40 fps
		return True

	def handleEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				self.screen = None
				self.clock = None
				return False
		return True
	def close(self):
		pygame.quit()
		self.screen = None
		self.clock = None
