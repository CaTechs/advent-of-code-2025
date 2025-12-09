from utils import *
import queue
from collections import defaultdict


def day9():
	data = loadFileByLine(9, "")
	best = 0
	for p in rLen(data):
		p1 = data[p]
		for p2 in data[p + 1:]:
			area = calcArea(p1, p2)
			best = max(best, area)
	return best

def calcArea(p1, p2):
	x1, y1 = p1.split(",")
	x2, y2 = p2.split(",")
	return (abs(int(x1) - int(x2)) + 1) * (abs(int(y1) - int(y2)) + 1)

def calcAreaInt(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return (abs(int(x1) - int(x2)) + 1) * (abs(int(y1) - int(y2)) + 1)

def day9t():
	d = loadFileByLine(9, "")
	data = []
	for l in d:
		x, y = l.split(",")
		data.append((int(x), int(y)))
	vert, hori, bound  = doBoundary(data)
	bad = set()
	good = set()
	best = 0
	for p in rLen(data):
		p1 = data[p]
		for p2 in data[p + 1:]:
			area = calcAreaInt(p1, p2)
			if area > best and testZone(p1, p2, vert, hori, bound, good, bad):
				best = area
	return best


def doBoundary(data):
	vert = defaultdict(list) # Key : coordonnées en y, value : liste des coordoonées en x des contours verticaux
	hori = defaultdict(list) # Key : coordonnées en x, value : liste des coordoonées en y des contours horizontaux
	bound = set()
	for i in range(len(data) - 1):
		doLine(data[i], data[i+1], vert, hori, bound)
	doLine(data[-1], data[0], vert, hori, bound)
	for k in vert:
		vert[k].sort()
	for k in hori:
		hori[k].sort()
	return (vert, hori, bound)

def doLine(p1, p2, vert, hori, bound):
	x1, y1 = p1
	x2, y2 = p2
	if (x1 == x2):
		for y in range(min(y1, y2), max(y1, y2)):
			bound.add((x1, y))
			vert[y].append(x1)
	else:
		for x in range(min(x1, x2), max(x1, x2)):
			bound.add((x, y1))
			hori[x].append(y1)

def isPointInZone(p, vert, hori, bound, good, bad):
	if p in bound or p in good:
		return True
	if p in bad:
		return False
	x, y = p
	l = 0
	# Donc, on regarde combien de contours verticaux il existe à gauche sur la ligne de coordonnées y
	for v in vert[y]:
		if v < x:
			l += 1
		elif v > x:
			break
	# Pour qu'un point soit dans le cadre, il doit avoir un nombre impair de contour à gauche
	if (l % 2) == 0:
		bad.add(p)
		return False
	l = 0
	for h in hori[x]:
		if h < y:
			l += 1
		elif v > x:
			break
	if l % 2 == 0:
		bad.add(p)
		return False
	good.add((x, y))
	return True

def testZone(p1, p2, vert, hori, bound, good, bad):
	x1, y1 = p1
	x2, y2 = p2
	testNextOne = True
	testNextTwo = True
	for x in range(min(x1, x2), max(x1, x2)):
		if (testNextOne and not isPointInZone((x, y1), vert, hori, bound, good, bad)) or (testNextTwo and not isPointInZone((x, y2), vert, hori, bound, good, bad)):
			return False
		# Si on ne traverse pas une frontière et que le point actuel est bon, alors le suivant l'est aussi
		testNextOne = (x, y1) in bound 
		testNextTwo = (x, y2) in bound
	testNextOne = True
	testNextTwo = True	
	for y in range(min(y1, y2), max(y1, y2)):
		if (testNextOne and not isPointInZone((x1, y), vert, hori, bound, good, bad)) or (testNextTwo and not isPointInZone((x2, y), vert, hori, bound, good, bad)):
			return False
		testNextOne = (x1, y) in bound
		testNextTwo = (x2, y) in bound
	return True


print(day9t())