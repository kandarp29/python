integer = eval(input("Enter the integer"))
l = []
for i in range(1,integer+1):
    if integer % i == 0:
        l.append(i)

print(l)

        
        
