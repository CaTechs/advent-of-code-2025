def loadFile(dayNumber, end = ""):
	dayNumber = str(dayNumber)
	path = "input/day" + dayNumber + end + ".txt"
	with open(path) as f:
		res = f.read()
	return res

def loadFileByLine(dayNumber, end = ""):
	content = loadFile(dayNumber, end)
	content = content.split("\n")
	if content[-1] == "":
		content.pop()

	return content

def loadAsIntList(dayNumber, end = ""):
	return [int(x) for x in loadFileByLine(dayNumber, end)]

def prettyPrint(t):
	for l in t:
		lStr = [str(k) for k in l]
		print("".join(lStr))


def rLen(l):
	return range(len(l))

def testInGrid(content, line, col):
    return line >= 0 and line < len(content) and col >= 0 and col < len(content[line])

def getAdja(x, y):
	return [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]

def getAdjaDiag(x, y):
	return getAdja(x,y) + [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]

def __main__():
	pass