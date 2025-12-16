from utils import *
import queue
from collections import defaultdict


def day11():
	data = loadFileByLine(11, "")
	conn = dict()
	for l in data:
		name, to = l.split(": ")
		to = to.split(" ")
		conn[name] = to

	return testPath("dac", "fft", conn)

def day11t():
	data = loadFileByLine(11, "")
	conn = defaultdict(list)
	rev = defaultdict(list)
	for l in data:
		name, to = l.split(": ")
		to = to.split(" ")
		conn[name] = to
		for t in to:
			rev[t].append(name)
	if testPath("dac", "fft", conn):
		f, s = "dac", "fft"
	else:
		f, s = "fft", "dac"
	sumSecToEnd, ignore = sumPathDeux(s, "out", conn, set())
	sumFToS, ignoreSecond = sumPathDeux(f, s, conn, ignore)
	sumStartToF, _ = sumPathDeux("svr", f, conn, ignoreSecond)
	print(sumSecToEnd, sumFToS, sumStartToF)
	print(easy)
	return sumSecToEnd * sumFToS * sumStartToF

	

def sumPath(start, end, conn):
	tot = 0
	q = queue.Queue()
	q.put(start)
	while not q.empty():
		n = q.get()
		if n == end:
			tot += 1
			continue
		for to in conn[n]:
			q.put(to)
	return tot

def sumPathDeux(start, end, conn, ignore):
	seen = dict()
	tot = recPathDeux(start, end, conn, seen, ignore)
	return (tot, seen.keys())


def recPathDeux(start, end, conn, seen, ignore):
	if start == end:
		return 1
	elif start in ignore:
		return 0
	elif start in seen:
		return seen[start]
	else:
		tot = 0
		for n in conn[start]:
			tot += recPathDeux(n, end, conn, seen, ignore)
		seen[start] = tot
		return tot


def testPath(start, end, conn):
	q = queue.Queue()
	q.put(start)
	while not q.empty():
		n = q.get()
		if n == end:
			return True
		if n in conn:
			for to in conn[n]:
				q.put(to)
	return False

print(day11t())