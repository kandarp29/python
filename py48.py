L = eval(input("Enter 1st list"))
M  = eval(input("Enter 2nd list"))
N = []
if len(L) > len(M) or len(M) > len(L):
    print('List is not equal in size')
    
else:
    
    for i in range(len(L)):
        x = L[i] + M[i]
        N.append(x)

        
    print(N)
    
     
