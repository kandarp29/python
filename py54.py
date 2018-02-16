l = eval(input('Enter the list'))
a = len(l)
for i in range(a-1):
    if (l[i]) in l:
        del (l[i])
        a = a - 1
        
print(l)




    
      
