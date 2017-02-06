from gridmap import GridMap
from coord import Coord

grid = GridMap(16, 12)

grid[0, 0] = 1
if grid[0, 0] == 1:
	print "PASS"
grid[3, 4] = 7
grid[6, 2] = 5
if grid[3, 4] == 7:
	print "PASS"
if grid[6, 2] == 5:
	print "PASS"
grid[(0, 0)] = 2
if grid[0, 0] == 2:
	print "PASS"
grid[[0, 0]] = 3
if grid[0, 0] == 3:
	print "PASS"
grid[Coord(0, 0)] = 4
if grid[0, 0] == 4:
	print "PASS"
