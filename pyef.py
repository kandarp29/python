from random import randint


l = []

for i in range(100):
	v = randint(100,200)
	if v % 2 == 0:
		l.append(v)
		if len(l)==5:
			break
