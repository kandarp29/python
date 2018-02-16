num = input('Enter the number')
num = int(num)

divisor = []
for i in range(2,num):

    if num % i == 0:
        divisor.append(i)

        
print (divisor)
        
