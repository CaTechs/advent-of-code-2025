from utils import *
import queue
from collections import defaultdict


def day10():
	data = loadFileByLine(10, "")
	tot = 0
	for line in data:
		tot += doProblem(line)
	return tot

def day10t():
	data = loadFileByLine(10, "")
	tot = 0
	for line in data:
		print("new Line")
		tot += doProblemDeux(line)
	return tot

def parseProblem(line):
	line = line.split(" ")
	target = parseTarget(line[0])
	buttons = [parseButton(b) for b in line[1:-1]]
	return (target, buttons)
	

def parseTarget(t):
	tar = ""
	t = t[1:-1]
	tot = 0
	for p in rLen(t):
		l = t[p]
		if l == "#":
			tot += 2**p
	return tot

def parseButton(b):
	b = b[1:-1].split(",")
	tot = 0
	for c in b:
		c = int(c)
		tot += 2**c
	return tot


def doProblem(line):
	target, buttons = parseProblem(line)
	seen = set()
	q = queue.Queue()
	q.put((0, 0))
	while not q.empty():
		n, p = q.get()
		if n in seen:
			continue
		seen.add(n)
		p += 1
		for b in buttons:
			newN = n ^ b
			if newN == target:
				return p
			else:
				q.put((newN, p))
	return 0

def parseProblemDeux(line):
	line = line.split(" ")
	joltage = parseJoltage(line[-1])
	m = defaultdict(list)
	buttons = [parseButtonDeux(b, m) for b in line[1:-1]]
	return (joltage, m)

def parseButtonDeux(b, m):
	b = b[1:-1].split(",")
	b = [int(k) for k in b]
	for c in b:
		m[c].append(b)

def parseJoltage(j):
	j = j[1:-1].split(",")
	j = [int(k) for k in j]
	return j

print(day10())
