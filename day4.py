from utils import *

def day4():
	data = loadFileByLine(4, "")
	res = 0
	for y in rLen(data):
		for x in rLen(data[y]):
			if data[y][x] == "@" and testPost(data, x, y):
				res += 1
	return res

def day4t():
	data = loadFileByLine(4, "")
	removed = set()
	rolls = findAllRoll(data)
	startingRolls = len(rolls)
	while True:
		newRemoved = set()
		for r in rolls:
			x,y = r
			if testPostRemoved(rolls, x, y):
				newRemoved.add((x,y))
		if (len(newRemoved) == 0):
			break
		rolls = rolls - newRemoved
	return startingRolls - len(rolls)

def findAllRoll(data):
	res = set()
	for y in rLen(data):
		for x in rLen(data[y]):
			if data[y][x] == "@":
				res.add((x,y))
	return res

def testPost(grid, x, y):
	adja = getAdjaDiag(x, y)
	totAdja = 0
	for a in adja:
		l,c = a
		if testInGrid(grid, l, c) and grid[c][l] == "@":
			totAdja += 1
	return totAdja < 4

def testPostRemoved(rolls, x, y):
	adja = getAdjaDiag(x, y)
	totAdja = 0
	for a in adja:
		l,c = a
		if (l,c) in rolls:
			totAdja += 1
	return totAdja < 4

print(day4())
print(day4t())