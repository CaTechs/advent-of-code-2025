from utils import *


def day5():
	data = loadFileByLine(5, "")
	ranges, ing = init(data)
	ranges.sort()
	ing.sort()
	posR = 0
	tot = 0
	for i in ing:
		for r in ranges:
			a, b = r
			if a <= i and i <= b:
				tot += 1
				break
	return tot

def day5t():
	data = loadFileByLine(5, "")
	ranges, ing = init(data)
	ranges = merge(ranges)
	tot = 0
	for r in ranges:
		a, b = r
		tot += (b - a) + 1
	return tot

def merge(ranges):
	ranges.sort()
	newRanges = [ranges[0]]
	for r in ranges[1:]:
		a, b = r
		mergeR = newRanges[-1]
		ma, mb = mergeR
		if a <= mb:
			if b > mb:
				# Elles se croisent, donc on les rejoint
				newRanges.pop()
				newRanges.append((ma, b))
			#Sinon la range suivante est juste incluse dans l'actuelle, donc rien à faire
		else:
			newRanges.append((a, b))
	return newRanges

def init(data):
	listRanges = []
	for i in rLen(data):
		l = data[i]
		if l == "":
			return (listRanges, [int(k) for k in data[i + 1:]])
		else:
			a,b = l.split("-")
			listRanges.append((int(a), int(b)))

print(day5())
print(day5t())