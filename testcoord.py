from coord import Coord

c = Coord(3, 4)
if c.y == 4:
  print "PASS"

if c[1] == 4:
  print "PASS"

try:
  print c[2]
  print "FAIL"
except ValueError as e:
  print "PASS"

c = Coord([3, 4])
if c.y == 4:
  print "PASS"

c = Coord((3, 4))
if c.x == 3:
  print "PASS"

c[0] = 7
if c.x == 7:
  print "PASS"

if str(c) == "(7, 4)":
  print "PASS"
