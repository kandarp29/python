##Dictionay exercise 1
d = {'Sugar':50,'Coke':25,'Rice':82,'Wheat':29}

print(d)

price =eval(input('Enter the dollar amount to print product with less price than that'))

for key in d:

    if d[key] < price:
        print(key)

