l = eval(input('Enter the list'))


for i in range(len(l)-1,0,-1):
    x = l.pop(l[i])
    l.insert(x,l[i-2])
    print(l)
    

    
    
