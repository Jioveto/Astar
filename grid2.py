# Jordan Lyon 	jjl242
# Cynthia Liu	cl844

import numpy as np
from random import randint
import heapq
#from heapq_showtree import show_tree
#from heapq_heapdata import data

x,y = 160, 120

##################################################### START GRID GENERATION
grid = GridMap(x, y)

########## Hard To Traverse ##########
def transformHarder():
	randCell = []
	for a in range(8):
		coord = Coord(randint(0, grid.width - 1), randint(0, grid.height - 1))
		while coord in randCell:
			coord = Coord(randint(0, grid.width - 1), randint(0, grid.height - 1))
		randCell.append(coord)

		for i in range(coord.y - 15, coord.y + 16):
			for j in range(coord.x - 15, coord.x + 16):
				if not grid.withinBounds(j, i): # make sure the coordinate is within bounds of the map
					continue
				if randint(0, 10) >= 5: # with 50% prob
					if 0 <= i and i < y and 0 <= j and j < x:
						grid[j, i] = "2" # make a hard to traverse cell

# Call transform harder
transformHarder()

########## Highways ##########
def generateHighways(numHighways = 4):
	""" Create highways for the gridmap

	Return:
		a list of lists of highway points
	"""
	coordsList = [[] for i in range(numHighways)] # make 4 highways
	allCoords = [] # just a list to store all highway points so that we can detect collisions

	while True:
		badTries = 0 # these are the number of tries before restarting the search for 4 new lists
		maxBadTries = 200
		listid = 0

		while badTries < maxBadTries:
			# try to now find good lists
			# start by choosing a random location and corresponding direction on the border of the gridmap
			direction = None
			randdomain = grid.width * 2 + grid.height * 2 - 4
			randloc = randint(0, randdomain)
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
			
			# now that we have a random location, let's try to get the highway
			isOnBoundary = lambda pt: pt.x == 0 or pt.x == grid.width - 1 or pt.y == 0 or pt.y == grid.height - 1
			loc = Coord(randloc)
			coordsList[listid].append(Coord(loc))
			allCoords.append(Coord(loc))
			highwayCollided = False
			while loc == randloc or (not isOnBoundary(loc) and not highwayCollided):
				# go for 20 spaces
				start = 1 if loc == randloc else 0
				for i in range(start, 20):
					if direction == "left":
						loc.x -= 1
					elif direction == "right":
						loc.x += 1
					elif direction == "up":
						loc.y -= 1 # its weird, cause y = 0 is at the top
					elif direction == "down":
						loc.y += 1
					# see if we need to break or if we can add to list
					coordsList[listid].append(Coord(loc))
					if loc in allCoords:
						highwayCollided = True
						break
					else:
						allCoords.append(Coord(loc))
					if isOnBoundary(loc):
						break
				if isOnBoundary(loc) or highwayCollided:
					break
				# now change the direction
				prob = randint(0, 10)
				next_direction = ["up", "left", "down", "right"]
				if prob < 2:
					ind = next_direction.index(direction)
					ind = (ind + 1) % 4
					direction = next_direction[ind]
				elif prob < 4:
					ind = next_direction.index(direction)
					ind = (ind - 1) % 4
					direction = next_direction[ind]
				else:
					# do nothing, just continue
					pass

			# detect if we need to restart trying to get another list or if we succeeded and can move on to the next one
			if highwayCollided or len(coordsList[listid]) < 100:
				badTries += 1
				coordsList[listid] = []
				allCoords = []
				for idx in range(0, listid): # all the way up to listid, not including listid
					allCoords += coordsList[idx]
			else:
				listid += 1
				if listid == len(coordsList): # yahoo! we've finished the last one
					break

		if badTries == maxBadTries:
			coordsList = [[] for i in range(4)] # make 4 highways
			allCoords = []
		else:
			break

	#return coordsList # we now have the coords list, just update the map
	for highway in coordsList:
		for pt in highway:
			grid[pt] = "a" if grid[pt] == "1" else "b"

# Call generate highways
generateHighways()

########## Blocked cells ##########
def blockedCells():
	totalCells = grid.width * grid.height
	blockedCellCount = totalCells / 5
	numCellsBlocked = 0
	while numCellsBlocked < blockedCellCount:
		randloc = Coord(randint(0, grid.width - 1), randint(0, grid.height - 1))
		if grid[randloc] == "a" or grid[randloc] == "b" or grid[randloc] == "0":
			continue
		grid[randloc] = "0"
		numCellsBlocked += 1

# Call blocked cells
blockedCells()

########## CONVERT BACK ##########
grid = grid.grid
##################################################### END GRID GENERATION

#Generate start/end cell
def startGoal(grid):
	placed = False

	xVal = randint(1,12)-1
	yVal = randint(1,16)-1
	while placed == False:

		random = randint(1,2)

		if xVal > 1 and xVal < 10:
			if random == 1:
				yVal = randint(1,2)-1
			else:
				yVal = randint(15,16)-1
		elif yVal > 1 and yVal < 14:
			if random == 1:
				xVal = randint(1,2)-1
			else:
				xVal = randint(11,12)-1

		#print xVal
		#print yVal

		if grid[xVal][yVal] == "1" or grid[xVal][yVal] == "2": 
			#grid[xVal][yVal] = 's'
			placed = True
	
	return (xVal,yVal)

#CREATE CONDITION TO DETERMINE DISTANCE
#Distance must be atleast 100 between goal and start
tup = startGoal(grid)
grid[tup[0]][tup[1]] = 's'
startPoint = grid[tup[0]][tup[1]]

tup2 = startGoal(grid)
temp = grid[tup2[0]][tup2[1]]
grid[tup2[0]][tup2[1]] = 'g'
goalPoint = grid[tup2[0]][tup2[1]]

while max(abs(tup2[1] - tup[1]),abs(tup2[0] - tup[0])) < 10:
	grid[tup2[0]][tup2[1]] = temp
	tup2 = startGoal(grid)
	temp = grid[tup2[0]][tup2[1]]
	grid[tup2[0]][tup2[1]] = 'g'
	goalPoint = grid[tup2[0]][tup2[1]]
	
print (np.matrix(grid))

#Begin A* navigation
heap = []


