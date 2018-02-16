l = eval(input('Enter the list'))
x = 0
for i in range(len(l)):
    l.sort()
    ##pop(i) = x
    if l[i] == l[i+1]:
        l=l.replace(l[i+1],'')
        
        
        
        
    

         
