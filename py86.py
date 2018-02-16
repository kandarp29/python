from random import randint

l = [randint(0,1) for i in range(7)]

print(l)

i = 0 
while l[i] == 1:


    i= i + 1

else:
    l[i]  = 1


print('New list',l)
