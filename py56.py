int_list = [0,1,0,1,2,2,3,4,5,7,9,8,10,1,1,3,4,5,6,7,8,9,10]

ints = []
for i in int_list:
    if i not in ints:
        ints.append(i)
ints.sort()
