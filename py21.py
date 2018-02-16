a = input("how much wide = ")
tall = input("how much tall = ")

a =int(a)
tall = int(tall)
for k in range(0,1):
    print('*'*a)
for i in range(1,tall-1):
    
    print('*',end='')
    for j in range(a-1):
        print('',end='')
    print('*',end='')    
for j in range(tall,tall-1):
    print('*'*a)

