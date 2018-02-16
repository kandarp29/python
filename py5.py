a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list1 = len(a)
list2 = len(b)
c = []
for i in range(0,list1):
    num1 = a[i]
    for j in range(0,list2):
        num2 = b[j]

        if num1 == num2 and num1 not in c:
            c.append(num1)
            
print(c)            

            
    
