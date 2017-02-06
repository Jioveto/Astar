# Jordan Lyon 	jjl242
# Cynthia Liu	cl844

import numpy as np
from random import randint
import heapq
from coord import Coord
from gridmap import GridMap
#from heapq_showtree import show_tree
#from heapq_heapdata import data

x,y = 16, 12

#grid = [[1 for i in range (x)] for j in range (y)] # create grid, query format is (y, x)
grid = GridMap(x, y)

randCell = []

# Hard To Traverse
for a in range(8):
  coord = Coord(randint(0, x - 1), randint(0, y - 1))
	while coord in randCell:
    coord = Coord(randint(0, x - 1), randint(0, y - 1))
	randCell.append(coord)

  # fix to scale to 3x3, later change back to 31x31
	for i in range(coord.y - 1, coord.y + 2):
		for j in range(coord.x - 1, coord.x + 2):
      if not grid.withinBounds(j, i): # make sure the coordinate is within bounds of the map
        continue
			if randint(0, 10) >= 5: # with 50% prob
				if 0 <= i and i < y and 0 <= j and j < x:
					grid[j, i] = 2 # make a bad row


def generateHighways():
  """
  """
  coordsList = [[] for i in range(4)] # make 4 highways
  allCoords = []

  goodToGo = False
  while not goodToGo:
    goodToGo = True # temporarily set it to true
    badTries = 0 # this is the number of tries before restarting the search for 4 new lists

    while badTries < 10:
      # try to now find good lists
      for listid in range(len(coordsList)):
        # start by choosing a random location and corresponding direction on the border of the gridmap
        direction = None
        randdomain = grid.width * 2 + grid.height * 2 - 4
        randloc = randind(0, randdomain)
        if randloc < randdomain / 2:
          if randloc < grid.width:
            randloc = Coord(randloc, 0)
            direction = "down"
          else:
            randloc = Coord(0, randloc - grid.width + 1)
            direction = "right"
        else:
          randloc %= randdomain / 2
          if randloc < grid.width:
            randloc = Coord(randloc, grid.height - 1)
            direction = "up"
          else:
            randloc = Coord(grid.width - 1, randloc - grid.width + 1)
            direction = "left"
        
        # now that we have a random location, let's try to get the path
        isOnBoundary = lambda pt: pt.x == 0 or pt.x == grid.width - 1 or pt.y == 0 or pt.y == grid.height - 1
        loc = randloc
        coordsList[listid].append(loc)
        allCoords.append(loc)
        while loc == randloc or isOnBoundary(loc):
          start = 1 if loc == randloc else 0
          highwayIsGood = True
          for i in range(start, 20):
            if direction == "left":
              loc.x -= 1
            elif direction == "right":
              loc.x += 1
            elif direction == "up":
              loc.y -= 1 # its weird, cause y = 0 is at the top
            elif direction == "down":
              loc.y += 1
            if isOnBoundary(loc):
              break
            if loc in allCoords:
              highwayIsGood = False
#        return 

    if badTries == 10:
      goodToGo = False
      coordsList = [[] for i in range(4)] # make 4 highways
      allCoords = []


grid = GridMap(16, 12)

#Generate start/end cell
def startGoal(grid):
	placed = False

	xVal = randint(1,16)-1
	yVal = randint(1,12)-1
	while placed == False:

		random = randint(1,2)

		if xVal > 1 and xVal < 14:
			if random == 1:
				yVal = randint(1,2)-1
			else:
				yVal = randint(11,12)-1
		elif yVal > 1 and yVal < 10:
			if random == 1:
				xVal = randint(1,2)-1
			else:
				xVal = randint(15,16)-1

		#print xVal
		#print yVal

		if grid[xVal, yVal] == 1 or grid[xVal, yVal] == 2: 
			#grid[xVal][yVal] = 's'
			placed = True
	
	return (xVal,yVal)

#CREATE CONDITION TO DETERMINE DISTANCE
#Distance must be atleast 100 between goal and start
tup = startGoal(grid)
grid[tup[0],tup[1]] = 's'
startPoint = grid[tup[0],tup[1]]

tup2 = startGoal(grid)
temp = grid[tup2[0],tup2[1]]
grid[tup2[0],tup2[1]] = 'g'
goalPoint = grid[tup2[0],tup2[1]]

while max(abs(tup2[1] - tup[1]),abs(tup2[0] - tup[0])) < 10:
	grid[tup2[0],tup2[1]] = temp
	tup2 = startGoal(grid)
	temp = grid[tup2[0],tup2[1]]
	grid[tup2[0],tup2[1]] = 'g'
	goalPoint = grid[tup2[0],tup2[1]]
	
print (np.matrix(grid))

#Begin A* navigation
heap = []


