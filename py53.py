from random import randint
count = 0
l = []
count1 = 0
for i in range(100):
    x = randint(0,1)
    
    if x == 0:
        count = count + 1

        if count >= count1:
            count1 = count
    if x==1:
        count = 0
            
    
    l.append(x)
    
print(l)
print(count1)



    
    

    
