class Coord:
	def __init__(self, X, Y=None):
		if not (((type(X) == type([]) or type(X) == type((0, 0)) or \
				type(X) == type(self)) and Y == None) or \
				((type(X) != type([]) and type(X) != type((0, 0)) and \
				type(X) != type(self)) and Y != None)):
			raise ValueError("Bad initial params for Coord")
		if type(X) == type([]) or type(X) == type((0, 0)):
			if len(X) != 2:
				raise ValueError("Bad initial params for Coord")
			self.x = X[0]
			self.y = X[1]
		elif type(X) == type(self):
			self.x = X.x
			self.y = X.y
		else:
			self.x = X
			self.y = Y
	def __getitem__(self, ind):
		if ind == 0:
			return self.x
		elif ind == 1:
			return self.y
		else:
			raise ValueError("Index for Coord must be either 0 or 1")
	def __setitem__(self, ind, value):
		if ind == 0:
			self.x = value
		elif ind == 1:
			self.y = value
		else:
			raise ValueError("Index for Coord must be either 0 or 1")
	def __str__(self):
		return str((self.x, self.y))
	def __repr__(self):
		return str((self.x, self.y))
	def __cmp__(self, other):
		dx = self.x - other.x
		if dx < 0:
			return -1
		elif dx > 0:
			return 1
		else:
			dy = self.y - other.y
			if dy < 0:
				return -1
			elif dy > 0:
				return 1
			else:
				return 0
