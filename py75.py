num =1
count = 0
l= 0
total  = 0
ave = 0
while num > 0:

    num = eval(input('Enter the numbers'))
    if num > 0:
        total = (total + num)
        l = l + 1
        if num >= 90:

            count= count + 1


else:
    print('You are done with entering numbers')




ave = total / l

print('total students got A grade = ',count)
print('Average of the numbers',ave)
