l = [1,3,2,8,7,6]

indexedlist = []
f = eval(input('Enter the sum = '))

for j in l:
    for k in l:

        add = j + k

        if add == f:
            new_list= []
            a = l.index(j)
            b = l.index(k)
            new_list.append(a)
            new_list.append(b)
            indexedlist.append(new_list)

               
else:
    print('Invalid sum')


         
print(l)         
print('Indexed list = ',indexedlist)
