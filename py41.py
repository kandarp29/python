from random import randint

string1 = input("enter the string")

string = ''
for i in range(len(string1)):
    
    num = randint(0,len(string1))
    if num <= len(string1):
        
        string = string + string1[num-1]


print(string)

                

