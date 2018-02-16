l =[]
k = []
length = eval(input('Entet the length of list'))

for i in range(0,length):
    user = input('Enter the list ')
    l.append(user)
    if user not in k:
        k.append(user)



print(k)
        

