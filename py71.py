from random import randint
l = []

for i in range(10):
    k=[]
    for j in range(10):
        a= randint(1,100)
        k.append(a)

    l.append(k)

    
        
        
print(l)
print(max(l[2]))

b = []
for i in range(10):
    a = l[i][5]
    b.append(a)

print(min(b))


    
