class Coord:
  def __init__(self, X, Y=None):
    if not ((type(X) == type([]) and Y == None) or Y != None):
      raise ValueError("Bad initial params for Coord")
    if type(X) == type([]):
      if (len(X) != 2):
        raise ValueError("Bad initial params for Coord")
      self.x = X[0]
      self.y = X[1]
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
