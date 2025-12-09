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
	vert, hori  = doBoundary(data)
	bad = set()
	good = set()
	best = 0
	for p in rLen(data):
		p1 = data[p]
		for p2 in data[p + 1:]:
			area = calcAreaInt(p1, p2)
			if area > best and testZone(p1, p2, vert, hori, good, bad):
				best = area
	return best


def doBoundary(data):
	vert = [] # Key : coordonnées en y, value : liste des coordoonées en x des contours verticaux
	hori = [] # Key : coordonnées en x, value : liste des coordoonées en y des contours horizontaux
	for i in range(len(data) - 1):
		doLine(data[i], data[i+1], vert, hori)
	doLine(data[-1], data[0], vert, hori)
	return (vert, hori)

def doLine(p1, p2, vert, hori):
	x1, y1 = p1
	x2, y2 = p2
	if (x1 == x2):
		vert.append((x1, min(y1, y2), max(y1, y2)))
	else:
		hori.append((y1, min(x1, x2), max(x1, x2)))

def isPointInZone(p, vert, hori, good, bad):
	if p in good:
		return True
	elif p in bad:
		return False
	x, y = p
	l = 0
	# Donc, on regarde combien de contours verticaux il existe à gauche sur la ligne de coordonnées y
	# On sait qu'on ne souffre pas du cas particulier d'être aligné avec un bord, car on s'est déplacé d'une demi case
	for v in vert:
		xv, y1, y2 = v
		if xv < x:
			if y1 <= y <= y2:
				l += 1
	# Pour qu'un point soit dans le cadre, il doit avoir un nombre impair de contour à gauche
	if (l % 2) == 0:
		bad.add(p)
		return False
	
	good.add((x, y))
	return True

def testZone(p1, p2, vert, hori, good, bad):
	x1, y1 = p1
	x2, y2 = p2
	testNextOne = True
	testNextTwo = True
	xm = min(x1, x2)
	ym = min(y1, y2)
	xmax, ymax = max(x1, x2), max(y1, y2)
	# On check si un point arbitraire du cadre est bien dans le polygone
	if not isPointInZone((xm + 0.5, ym + 0.5), vert, hori, good, bad):
		return False
	# Le point est dans le cadre, vérifions maintenant qu'aucun bord ne vient couper dans notre cadre
	for v in vert:
		xv, yv1, yv2 = v
		if xm < xv < xmax:
			# Ce contour vertical est aligné avec notre cadre
			if yv1 < ym:
				# La borne haute est au dessus du cadre
				if yv2 > ym:
					# La borne basse est strictement dans le cadre, on a donc perdu
					return False
				# Sinon, les deux sont au dessus, on est bon
			elif yv1 < ymax:
				# On sait que la borne haute n'est pas au dessus du cadre, donc si on est là elle est directement dans le cadre
				# On a donc perdu
				return False
			# Sinon, les deux sont en dessous du cadre, donc est bon
	for h in hori:
		yh, xh1, xh2 = h
		if ym < yh < ymax:
			if xh1 < xm:
				if xh2 > xm:
					return False
			elif xh1 < xmax:
				return False	

	return True


print(day9t())