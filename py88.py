e = 1
a = 10

l =[]

for i in range(100):
    e = e + a
    a = a**2

    l.append(e)

print(l)
