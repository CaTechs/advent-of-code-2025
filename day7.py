from utils import *
from collections import defaultdict


def day7():
	grid = loadFileByLine(7, "")
	firstLaser = findStart(grid)
	laser = set()
	laser.add(firstLaser)
	total = 0
	while len(laser) > 0:
		nextLaser, totSplit = doIter(grid, laser)
		total += totSplit
		laser = nextLaser
	return total

def day7t():
	grid = loadFileByLine(7, "")
	x,y = findStart(grid)
	laser = set()
	laser.add((x, y, 1))
	nextLaser = laser
	while len(nextLaser) > 0:
		laser = nextLaser
		nextLaser = doIterDeux(grid, laser)
	total = 0
	for l in laser:
		x, y, w = l
		total += w
	return total

def findStart(grid):
	for x in rLen(grid[0]):
		if grid[0][x] == "S":
			return (x, 0)

def doIter(grid, laser):
	nextLaser = set()
	totSplit = 0
	for l in laser:
		x, y = l
		y += 1
		if testInGrid(grid, y, x):
			if grid[y][x] == "^":
				nextLaser.add((x-1, y))
				nextLaser.add((x+1, y))
				totSplit += 1
			else:
				nextLaser.add((x, y))
	return (nextLaser, totSplit)

def doIterDeux(grid, laser):
	nextLaser = defaultdict(int)
	totSplit = 0
	for l in laser:
		x, y, w = l
		y += 1
		if testInGrid(grid, y, x):
			if grid[y][x] == "^":
				nextLaser[(x-1, y)] += w
				nextLaser[(x+1, y)] += w
			else:
				nextLaser[(x, y)] += w
	res = []
	for l in nextLaser:
		x, y = l
		w = nextLaser[l]
		res.append((x, y, w))
	return res


print(day7())
print(day7t())