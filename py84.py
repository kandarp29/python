num1 = eval(input('Enter the first small number'))
num2 = eval(input('Enter the second large number'))

while num1 > 0:
    
    a = num2 % num1
    
    num2 = num1
    num1 = a

print('GCD of given numbers will be',num2)
