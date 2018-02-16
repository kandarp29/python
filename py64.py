from random import randint
from random import sample
l=[]
count = 0
for i in range(6):
    user = eval(input('Enter the six digit lottery number one-by-one'))
    l.append(user)

k = [j for j in range(1,11)]



for f in range(100000000):
    comparative = sample(k,6)
    ##print(comparative)
    if comparative == l:
        count = count + 1




print(count)
    
