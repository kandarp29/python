print('Program to find the GCD')

num1 = eval(input('Enter the first small number'))
num2 = eval(input('Enter the second large number'))
rem = 1
while rem == 0:

    rem = num2 % num1
    num2 = num1
    num1 = rem

print('GCD is ', num2)
