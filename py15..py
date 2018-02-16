meal_price = input("Please enter your meal price ")
meal_price = int(meal_price)

tip = input("Percent of tip for host ")
tip = int(tip)

tip_price  = (meal_price * tip) / 100

print("tip price = ",tip_price)

total = meal_price +tip_price

print("Total bill = " ,total)

    

