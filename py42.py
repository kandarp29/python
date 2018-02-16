##list = []

L = eval(input("Enter the list of integer"))

length = len(L)-2

            
print(L)

print(L[len(L)-1])

print(L[: :-1])

if 5 in L:
    print('Yes')
    x = L.count(5)
    print(x)


del(L[0])
del(L[length])
L.sort()
print(L)

