from utils import *
import queue
from collections import defaultdict


def day8():
	data = loadFileByLine(8, "")
	data = parseData(data)
	q = makeQueue(data)
	n = doJunctions(q, 1000)
	res = listNetwork(n)
	return res[-1] * res[-2] * res[-3]

def day8t():
	data = loadFileByLine(8, "")
	data = parseData(data)
	q = makeQueue(data)
	return doJunctionsTotal(q, len(data))

def parseData(data):
	res = []
	for l in data:
		x,y,z = l.split(",")
		res.append((int(x), int(y), int(z)))
	return res

def calcDistance(a, b):
	xa, ya, za = a
	xb, yb, zb = b
	return ((xa - xb)**2 + (ya - yb)**2 + (za - zb)**2)**(1/2)

def makeQueue(data):
	q = queue.PriorityQueue()
	for p in rLen(data):
		x = data[p]
		for y in data[p + 1:]:
			d = calcDistance(x, y)
			q.put((d, x, y))
	return q


def doJunctions(q, nbr):
	res = defaultdict(set)
	for _ in range(nbr):
		d, x, y = q.get()
		newTotal = res[x] | res[y]
		newTotal.add(x)
		newTotal.add(y)
		for adj in newTotal:
			res[adj] = newTotal
	return res

def doJunctionsTotal(q, nbr):
	res = defaultdict(set)
	while True:
		d, x, y = q.get()
		newTotal = res[x] | res[y]
		newTotal.add(x)
		newTotal.add(y)
		if len(newTotal) == nbr:
			return x[0] * y[0]
		for adj in newTotal:
			res[adj] = newTotal

def listNetwork(n):
	seen = set()
	res = []
	for p in n:
		if p in seen:
			continue
		seen.add(p)
		seen |= n[p]
		res.append(len(n[p]))
	res.sort()
	return res


print(day8())
print(day8t())
# 2001048381 too low