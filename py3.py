
num = input( 'Enter number smaller than 100:')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = len(a)
new_list = []
for i in range(b):
    
    if a[i] <= int(num):
        
        new_list.append(a[i])
        

    
    
print (new_list)
        
      
