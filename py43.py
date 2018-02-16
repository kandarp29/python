from random import randint


l = []
a = 0
count = 0
for i in range(20):
    x = randint(1,100)
    l.append(x)
    a= a + x

    if x%2 == 0:
        count = count+1
        
print(l)

ave = a/20

print(ave)

l.sort()

print('Smallest Value =',l[0])
print('Largest value = ',l[19])

print('Second smallest in list',l[1])

print('Second largest in list',l[18])

print('Number of even numbers ',count)






    
    
