L  = [i for i in range(100,1000)]
k=[]
for i in range(900):
    num = str(L[i])
    if num[:]==num[::-1]:
        k.append(num)
        num = int(num)



print(k)

        
        
