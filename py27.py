sum1  =0
sum2 = 0

for i in range(0,2000,2):

    sum1 = sum1 + i

for i in range(1,2000,2):
    sum2  = sum2 + i


total = sum2 - sum1
print(total)
