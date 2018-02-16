x= (input('Enter the lenth of A'))
x = int(x)
a = 1
div = x // 2
div = int(div)
for i in range(1):
    print(' '*((div*2)-i),'*')
    c=6
    
    i = 1
    for i in range(1,div):
        ##c =c+(div//2)
        print(' '*((div*2)-i),end='')
        print('*',' '*(i+i),'*')
        a =a+1
        a = div//2
    for j in range(a):
            
        c =c+1    
    b = c + div
    print(' '*(div-1),'*' * (b))    
    
    d = 2*div
    for k in range((div-1)):
        d =d+2
        print(' '*((div-1)-k),end='')
        print('*',' '*(d),'*')
        
           
