from utils import *
import re


def day6():
	data = loadFileByLine(6, "")
	allList = getListOfNumbers(data)
	return getTotal(allList, data[-1])

def day6t():
	data = loadFileByLine(6, "")
	grid = data[:-1]
	grid = rotateGrid(grid)
	grid = groupRotated(grid)
	return getTotal(grid, data[-1])
	

def getListOfNumbers(data):
	firstLine = splitline(data[0])
	allList = [[int(a)] for a in firstLine]
	for l in data[1:-1]:
		l = splitline(l)
		for p in rLen(l):
			allList[p].append(int(l[p]))
	return allList

def rotateGrid(data):
	newGrid = [[] for k in range(len(data[0]))]
	for l in data:
		for p in rLen(l):
			newGrid[p].append(l[p])
	return newGrid

def groupRotated(data):
	res = []
	current = []
	for l in data:
		l = list(filter(lambda a: a != " ", l))
		l = "".join(l)
		if l == "":
			res.append(current)
			current = []
		else:
			current.append(int(l))
	if (len(current)) > 0:
		res.append(current)
	return res

def getTotal(listNumber, lineOperator):
	listOperator = splitline(lineOperator)
	tot = 0
	for p in rLen(listOperator):
		s = listOperator[p]
		if s == "+":
			tot += sum(listNumber[p])
		if s == "*":
			mul = 1
			for k in listNumber[p]:
				mul *= k
			tot += mul
	return tot



def splitline(line):
	while line[0] == " ":
		line = line[1:]
	sp = re.split(r' +', line)
	if sp[-1] == "":
		sp.pop()
	return sp

print(day6())
print(day6t())
