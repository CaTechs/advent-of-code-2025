from utils import *


def day2():
	data = loadFile(2, "")
	data = data.split(",")
	tot = 0
	for l in data:
		l, r = l.split("-")
		tot += doZone(l, r)
	return tot

def day2t():
	data = loadFile(2, "")
	data = data.split(",")
	tot = 0
	for l in data:
		l, r = l.split("-")
		tot += doZoneTwo(l, r)
	return tot

def doZone(start, end):
	end = int(end)
	res = []
	s = len(start)
	l, r = start[:s//2], start[s//2:]
	if (len(l) < len(r)):
		l = "1" + ("0"*(len(r) - 1))
	l = int(l)
	start = int(start)
	while True:
		number = int(str(l) * 2)
		if number >= start and number <= end:
			res.append(number)
		elif number > end:
			break
		l += 1
	return sum(res)

def doZoneTwo(start, end):
	res = set()
	for i in range(1, len(end)//2 + 1):
		res = res | doPattern(i, start, end)
	return sum(res)

def doPattern(size, start, end):
	firstPatten = int("1" + ("0" * (size - 1)))
	muls = len(start) // size
	mule = len(end) // size
	res = set()
	if mule == 0:
		return res
	start, end = int(start), int(end)
	for mul in range(muls, mule + 1):
		if mul == 1:
			continue
		p = firstPatten
		while True:
			number = int(str(p) * mul)
			if number >= start and number <= end:
				res.add(number)
			if number > end:
				break
			p += 1
			if (len(str(p)) > len(str(firstPatten))):
				break
	return res

print(day2())
print(day2t()) #66500947346