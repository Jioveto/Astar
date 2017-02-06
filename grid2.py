# Jordan Lyon 	jjl242
# Cynthia Liu	cl844

import numpy as np
from random import randint
import heapq
#from heapq_showtree import show_tree
#from heapq_heapdata import data

x,y = 16, 12

grid = [[1 for i in range (x)] for j in range (y)]

randCell = []

#Hard To Traverse
for a in range(8):
	coorX = randint(1,12)-1
	coorY = randint(1,16)-1
	while [coorX,coorY] in randCell:			
		coorX = randint(1,12)-1
		coorY = randint(1,16)-1
	#center cell of 31x31
	#grid[coorX][coorY] = 4	
	randCell.append([coorX,coorY])

	for i in range(coorX-2,coorX+2):
		for j in range(coorY-2,coorY+2):
			if randint(0,10) > 4:
				if i >= 0 and i < 12 and j >= 0 and j < 16:
					grid[i][j] = 2


#Highways/Rivers
def makeRivers(start, direction):
	coordList = []
	coordList.append(start)
	x = start[0]
	y = start[1]
	

	#print 'starting direction: ' + direction

	#LOOP TO CREATE RIVER
	while (direction != 'null'):
		prob = randint(1,10)
		
		if direction == 'down':
			if len(coordList) == 1:
				#go 20 spaces down - initial
				for i in range(2):
					nextCoord = (x+1,y)
					if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
						coordList.append(nextCoord)
						x = x+1
						direction = 'down'
					else:
						#empty valid moves list
						print 'purged list: '
						print coordList
						coordList = []
						direction = 'null'
						break #failure
						
			if prob <= 6:
				#go 20 spaces down
				for i in range(2):
					nextCoord = (x+1,y)
					if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
						if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
							coordList.append(nextCoord)
							x = x+1
							direction = 'down'
						else:
							#empty valid moves list
							print 'purged list: '
							print coordList
							coordList = []
							direction = 'null'
							break #failure
					else:
						coordList.append(nextCoord)
						direction = 'null'
						break
			else:
				LorR = randint(1,2)
				if LorR == 1:
					#go left 20 spaces
					for i in range(2):
						#nextCoord = [x][y-1]
						nextCoord = (x,y-1)
						if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
							if nextCoord not in coordList and (grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2):
								coordList.append(nextCoord)
								y = y-1
								direction = 'left'
							else:
								print 'purged list: '
								print coordList
								coordList = []
								direction = 'null'
								break
						else:
							coordList.append(nextCoord)
							direction = 'null'
							break
				else:
					#go right 20 spaces
					for i in range(2):
						nextCoord = (x,y+1)
						if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
							if nextCoord not in coordList and (grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2):
								coordList.append(nextCoord)
								y = y+1
								direction = 'right'
							else:
								print 'purged list: '
								print coordList
								coordList = []
								direction = 'null'
								break
						else:
							coordList.append(nextCoord)
							direction = 'null'
							break
		
		if direction == 'left':
			if len(coordList) == 1:
				#go 20 spaces left - initial
				for i in range(2):
					nextCoord = (x,y-1)
					if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
						coordList.append(nextCoord)
						y = y-1
						direction = 'left'
					else:
						#empty valid moves list
						print 'purged list: '
						print coordList
						coordList = []
						direction = 'null'
						break #failure
			if prob <= 6:
				#go 20 spaces left
				for i in range(2):
					#nextCoord = [x][y-1]
					nextCoord = (x,y-1)
					if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
						if nextCoord not in coordList and (grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2):
							coordList.append(nextCoord)
							y = y-1
							direction = 'left'
						else:
							print 'purged list: '
							print coordList
							coordList = []
							direction = 'null'
							break
					else:
						coordList.append(nextCoord)
						direction = 'null'
						break
			else:
				UorD = randint(1,2)
				if UorD == 1:
					#go up 20 spaces
					for i in range(2):
						nextCoord = (x-1,y)
						if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
							if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
								coordList.append(nextCoord)
								x = x-1
								direction = 'up'
							else:
								#empty valid moves list
								print 'purged list: '
								print coordList
								coordList = []
								direction = 'null'
								break #failure
						else:
							coordList.append(nextCoord)
							direction = 'null'
							break
				else:
					#go down 20 spaces
					for i in range(2):
						nextCoord = (x+1,y)
						if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
							if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
								coordList.append(nextCoord)
								x = x+1
								direction = 'down'
							else:
								#empty valid moves list
								print 'purged list: '
								print coordList
								coordList = []
								direction = 'null'
								break #failure
						else:
							coordList.append(nextCoord)
							direction = 'null'
							break


		if direction == 'right':
			if len(coordList) == 1:
				#go 20 spaces right - initial
				for i in range(2):
					nextCoord = (x,y+1)
					if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
						coordList.append(nextCoord)
						y = y+1
						direction = 'right'
					else:
						#empty valid moves list
						print 'purged list: '
						print coordList
						coordList = []
						direction = 'null'
						break #failure
			if prob <= 6:
				#go 20 spaces right
				for i in range(2):
					nextCoord = (x,y+1)
					if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
						if nextCoord not in coordList and (grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2):
							coordList.append(nextCoord)
							y = y+1
							direction = 'right'
						else:
							print 'purged list: '
							print coordList
							coordList = []
							direction = 'null'
							break
					else:	
						coordList.append(nextCoord)	
						direction = 'null'
						break
			else:
				UorD = randint(1,2)
				if UorD == 1:
					#go up 20 spaces
					for i in range(2):
						nextCoord = (x-1,y)
						if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
							if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
								coordList.append(nextCoord)
								x = x-1
								direction = 'up'
							else:
								#empty valid moves list
								print 'purged list: '
								print coordList
								coordList = []
								direction = 'null'
								break #failure
						else:
							coordList.append(nextCoord)
							direction = 'null'
							break
				else:
					#go down 20 spaces
					for i in range(2):
						nextCoord = (x+1,y)
						if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
							if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
								coordList.append(nextCoord)
								x = x+1
								direction = 'down'
							else:
								#empty valid moves list
								print 'purged list: '
								print coordList
								coordList = []
								direction = 'null'
								break #failure
						else:
							coordList.append(nextCoord)
							direction = 'null'
							break

		if direction == 'up':
			if len(coordList) == 1:
				#go 20 spaces up - initial
				for i in range(2):
					nextCoord = (x-1,y)
					if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
						coordList.append(nextCoord)
						x = x-1
						direction = 'up'
					else:
						#empty valid moves list
						print 'purged list: '
						print coordList
						coordList = []
						direction = 'null'
						break #failure
			if prob <= 6:
				#go 20 spaces up
				for i in range(2):
					#nextCoord = [x+1][y]
					nextCoord = (x-1,y)
					if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
						if nextCoord not in coordList and grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2:
							coordList.append(nextCoord)
							x = x-1
							direction = 'up'
						else:
							#empty valid moves list
							print 'purged list: '
							print coordList
							coordList = []
							direction = 'null'
							break #failure
					else:
						coordList.append(nextCoord)
						direction = 'null'
						break
			else:
				LorR = randint(1,2)
				if LorR == 1:
					#go left 20 spaces
					for i in range(2):
						nextCoord = (x,y-1)
						if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
							if nextCoord not in coordList and (grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2):
								coordList.append(nextCoord)
								y = y-1
								direction = 'left'
							else:
								print 'purged list: '
								print coordList
								coordList = []
								direction = 'null'
								break
						else:
							coordList.append(nextCoord)
							direction = 'null'
							break
				else:
					#go right 20 spaces
					for i in range(2):
						nextCoord = (x,y+1)
						if (nextCoord[0] >= 1 and nextCoord[0] < 11) and (nextCoord[1] >= 1 and nextCoord[1] < 15):
							if nextCoord not in coordList and (grid[nextCoord[0]][nextCoord[1]] == 1 or grid[nextCoord[0]][nextCoord[1]] == 2):
								coordList.append(nextCoord)
								y = y+1
								direction = 'right'
							else:
								print 'purged list: '
								print coordList
								coordList = []
								direction = 'null'
								break
						else:
							coordList.append(nextCoord)
							direction = 'null'
							break
	
	print coordList
	return coordList


def gridReset(grid):
	for i in range(12):
		for j in range(16):
			if grid[i][j] == 'a':
				grid[i][j] = '1'
			elif grid[i][j] == 'b':
				grid[i][j] = '2'
			
	
	
riverCount = 0

for b in range(2):
#while riverCount != 4:
	restarts = 0
	randBorder = randint(1,4)
	direction = 'null'
	
	#Top
	if randBorder == 1:
		if direction == 'null':
			direction = 'down'
			#startCoord = [0][randint(1,14)]
			startCoord = (0, randint(1,14))
			river = makeRivers(startCoord, direction)
			while(len(river) < 10):
				print restarts
				river = makeRivers(startCoord, direction)
			#	if river == []:
			#		restarts = restarts + 1
			#		if restarts > 10:
			#			gridReset(grid)
			#			riverCount = 0
			#			restarts = 0
							
	#Left
	if randBorder == 2:
		if direction == 'null':
			direction = 'right'
			#startCoord = [randint(1,10)][0]
			startCoord = (randint(1,10), 0)
			river = makeRivers(startCoord, direction)
			while(len(river) < 10):
				print restarts
				river = makeRivers(startCoord, direction)
			#	if river == []:
			#		restarts = restarts + 1
			#		if restarts > 10:
			#			gridReset(grid)
			#			riverCount = 0
			#			restarts = 0
	
	#Right
	if randBorder == 3:
		if direction == 'null':
			direction = 'left'
			#startCoord = [randint(1,10)][15]
			startCoord = (randint(1,10),15)
			river = makeRivers(startCoord, direction)
			while(len(river) < 10):
				print restarts
				river = makeRivers(startCoord, direction)
			#	if river == []:
			#		restarts = restarts + 1
			#		if restarts > 10:
			#			gridReset(grid)
			#			riverCount = 0
			#			restarts = 0
	
	#Bottom
	if randBorder == 4:
		if direction == 'null':
			direction = 'up'
			#startCoord = [11][randint(1,14)]
			startCoord = (11, randint(1,14))
			river = makeRivers(startCoord, direction)
			while(len(river) < 10):
				print restarts
				river = makeRivers(startCoord, direction)
			#	if river == []:
			#		restarts = restarts + 1
			#		if restarts > 10:
			#			gridReset(grid)
			#			riverCount = 0
			#			restarts = 0
	
	while len(river) != 0:
		rivCoord = river[0]
		#print rivCoord[0]
		#print rivCoord[1]
		if grid[rivCoord[0]][rivCoord[1]] == 1:
			grid[rivCoord[0]][rivCoord[1]] = 'a'
		elif grid[rivCoord[0]][rivCoord[1]] == 2:
			grid[rivCoord[0]][rivCoord[1]] = 'b'
		river = river[1:]
		riverCount = riverCount + 1
	
	#bottom
 	#if randSide == 2:
	#	c = 11
	#	startHW = randint(2,15)-1
		#grid[c][startHW] = 4
	#	while c >=0: #(grid[c][startHW] != 'a' or 'b') and c >=0:
	#		if grid[c][startHW] == 1:
	#			grid[c][startHW] = 'a'
	#		elif grid[c][startHW] == 2:
	#			grid[c][startHW] = 'b'
	#		c = c - 1 
	#left
	#if randSide == 3:
	#	c = 0
	#	startHW = randint(2,11)-1
		#grid[startHW][c] = 4
	#	while c < 16: #(grid[startHW][c] != 'a' or 'b') and c < 16:
	#		if grid[startHW][c] == 1:
	#			grid[startHW][c] = 'a'
	#		elif grid[startHW][c] == 2:
	#			grid[startHW][c] = 'b'
	#		c = c + 1 
	#right	
	#if randSide == 4:
	#	c = 15
	#	startHW = randint(2,11)-1
		#grid[startHW][c] = 4
	#	while c >= 0:#(grid[startHW][c] != 'a' or 'b') and c >= 0:
	#		if grid[startHW][c] == 1:
	#			grid[startHW][c] = 'a'
	#		elif grid[startHW][c] == 2:
	#			grid[startHW][c] = 'b'
	#		c = c - 1 
	
	#Start to build highway/river

#Generate "blocked" cells
blocked = 0	 
while blocked != 38:
	coorX = randint(1,12)-1
	coorY = randint(1,16)-1
	if grid[coorX][coorY] == 1 or grid[coorX][coorY] == 2:
		grid[coorX][coorY] = 0
		blocked = blocked + 1

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

		if grid[xVal][yVal] == 1 or grid[xVal][yVal] == 2: 
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


