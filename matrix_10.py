from random import randint
M=[]
for j in range(10):
    l=[]
    for i in range(10):
        a= randint(1,100)
        l.append(a)
    M.append(l)
        
    
print('largest value in third row= ',max(M[3]))
L=[]
for k in range(0,10):
    L.append(M[k][5])
    

print('Lowest value in a 6 column=',min(L))
