from math import log

n = eval(input('enter the value of n '))
compute1 = 0 
for i in range(1,n+1):
    compute1 = (compute1 + (1/i))

    if i == n:
        compute = compute1 - log(n)

        
print(compute)         
