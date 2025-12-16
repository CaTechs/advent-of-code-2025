from utils import *


def day12():
	data = loadFileByLine(12, "")
	forms, p = parseForms(data)
	tot = 0
	for l in data[p:]:
		if testZone(l, forms):
			tot += 1
	return tot



def testZone(l, forms):
	size, patterns = l.split(": ")
	patterns = [int(p) for p in patterns.split(" ")]
	a,b = [int(p) for p in size.split("x")]
	nbrSize3 = (a // 3)*(b // 3)
	if nbrSize3 >= sum(patterns):
		return True
	nbrTilesNeeded = sum([patterns[p]*forms[p][0] for p in rLen(patterns)])
	if nbrTilesNeeded >= a*b:
		return False
	assert False

def parseForms(data):
	forms=[]
	currForm = []
	currTot = 0
	for p in rLen(data):
		line = data[p]
		if "x" in line:
			return (forms, p)
		elif len(line) == 0:
			forms.append((currTot, currForm))
			currTot = 0
			currForm = []
		elif ":" in line:
			continue
		else:
			currForm.append(line)
			currTot += line.count("#")

print(day12())