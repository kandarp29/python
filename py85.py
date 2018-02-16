from random import randint

l= [[0]*5 for i in range(5)]

r =0
c =0
a = 1
b =1 

for i in range(10):
    
    
    
    r = randint(0,4)
    c = randint(0,4)
    a =r
    b =c
    l[r][c] = 1

    
