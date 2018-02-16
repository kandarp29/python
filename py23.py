from random import randint

for i in range(1,10):
    x =randint(1,10)
    y = randint(1,10)

    z = x * y

    print('Question ',i, end= ' :')
    print(x ,'X',y ,' = ',end='')
    
    ans = eval(input())

    if ans == z:
        print('Right')

    else:
        print('wrong')
        
    
    
