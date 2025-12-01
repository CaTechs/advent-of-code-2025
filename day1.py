from utils import *

def day1():
	pos = 50
	tot = 0
	data = loadFileByLine(1)
	for l in data:
		d, n = l[0],int(l[1:])
		if d == "L":
			n = -n
		pos += n
		pos = pos % 100
		if pos == 0:
			tot += 1
	return tot

def day1t():
	pos = 50
	tot = 0
	data = loadFileByLine(1, "")
	for l in data:
		d, n = l[0],int(l[1:])
		if d == "L":
			n = -n
		newPos = pos + n
		tot += abs((pos // 100) - (newPos // 100))
		if ((newPos % 100) == 0 and d == "L"):
			# On était à 650, on tombe à 600
			# Ca compte pour un 1 même si la division par 100 n'a pas changée
			tot += 1
		if ((pos % 100) == 0 and d == "L"):
			# On était à 600, on est retombé à moins
			# Le fait d'atteindre 600 était déjà compté comme un 0, donc 600 à 599 ne doit pas compter
			tot -= 1
		pos = newPos

	return tot

print(day1t())