L = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
count = 0
K=[i for i in range(51) if i not in L]
J=[]
for i in range(2,51):
    if i not in L:
        count = count+ 1
    if i in  L:
        J.append(count)
        count = 0

        
   
        
    
       
        
        

print('Given list',L)
print('Mssing elements of list',K)
print('Number of gaps in a list',J)

print('Maximum gap in a list',max(J))




