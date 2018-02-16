from random import randint

count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0


for i in range(10000):
    
    x = randint(1,6)
    y = randint(1,6)

    z = x+y

    if z == 2:
        count2 = count2 + 1
        a2 = count2 / 100

    elif z == 3:
        count3 = count3 + 1
        a3 = count3 / 100
        
    elif z == 4:
        count4 = count4 + 1
        a4 = count4 / 100
    elif z == 5:
        count5  = count5 + 1
        a5 = count5 / 100
    elif z == 6:
        count6 = count6 + 1
        a6 = count6 / 100
    elif z == 7:
        count7 = count7 + 1
        a7 = count7 / 100
    elif z == 8:
        count8 = count8 + 1
        a8 = count8 / 100
    elif z == 9:
        count9 = count9 + 1
        a9 = count9 / 100
    elif z == 10:
        count10 = count10 + 1
        a10 = count10 / 100
    elif z == 11:
        count11 = count11 + 1
        a11 = count11 / 100
    else:
        count12 = count12 + 1
        a12 = count12 / 100


##for j in range(2,13):
print('Probability of 2 = ',a2)
print('Probability of 3 = ',a3)
print('Probability of 4 = ',a4)
print('Probability of 5 = ',a5)
print('Probability of 6 = ',a6)
print('Probability of 7 = ',a7)
print('Probability of 8 = ',a8)
print('Probability of 9 = ',a9)
print('Probability of 10 = ',a10)
print('Probability of 11 = ',a11)
print('Probability of 12 = ',a12)
    #print('Probability of 13 = ' ,a13)
    
    
    

       
