class Product:
    def __init__(self,name,price):

        self.name = name
        #self.amount = amount
        self.price = price

    def get_price(self,num):

        if num < 10:
            value = (num * self.price)
            
        elif 10<=num<=99:
            value1 = (num * self.price)
            value = value1 - (0.10 * value1)
            
        else:
            value2 = (num * self.price)
            value = value2 -(0.20*value2)

        return value

    def make_purchase(self,num):

        Product.get_price(self,num)

        ##return value

        
        
e = Product('rice',25)

print(e.get_price(25))
