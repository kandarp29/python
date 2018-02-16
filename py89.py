##Dictionay exercise 1
d = {}

print('Enter the product and its price once done type exit')
a = eval(input("enter the total number of product"))



for i in range(a):
    
    product = input('Enter the prduct name ')


    price = input('Enter the product price ')

    d[product] = price


print('Type product name to get its price')

for j in d:
    
    product_price = input('Enter the product name')



    if product_price in d:
        print(d[product_price])

    else:
        print('This product is not in dictionarie')

    


