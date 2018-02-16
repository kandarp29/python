
l=[2, 4, 5, 8, 1, 7, 9, 3, 6]
for i in range(len(l)-1,-1):
	
	if l[i] < l[i-1]:
		c = l[i]
		l[i]=l[i-1]
		l[i-1]=c
		
	else:
		continue
