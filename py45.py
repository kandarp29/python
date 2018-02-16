l = eval(input('Enter the list containing number between 1 to 12'))

for i in range(len(l)):
    if l[i] > 10:
        del(l[i])
        l.insert(i,10)

        




print(l)
