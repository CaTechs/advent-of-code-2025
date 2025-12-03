from utils import *

def day3():
	data = loadFileByLine(3)
	tot = 0
	for l in data:
		tot += doLine(l)
	return tot

def day3t():
	data = loadFileByLine(3)
	tot = 0
	for l in data:
		tot += int(doLineTwoRec(l, 12))
	return tot

def doLine(l):
	best, pos = findBest(l[:-1])
	secondBest, _ = findBest(l[pos + 1:])
	return 10*best + secondBest

def findBest(l):
	pos = 0
	best = 0
	for p in rLen(l):
		n = int(l[p])
		if n > best:
			best = n
			pos = p
	return (best, pos)

def doLineTwoRec(l, left):
	if left == -1:
		return ""
	if left == 0:
		# [:-0] rend une liste vide
		best, pos = findBest(l)
	else:
		best, pos = findBest(l[:-left])
	return str(best) + doLineTwoRec(l[pos+1:], left - 1)

print(day3())
print(day3t())