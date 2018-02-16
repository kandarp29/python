

num  = eval(input('Enter the number '))
total = 0
for i in range(1,num):

    if (num%i == 0):
        total = total + i
        #print(i,end=',')
        
        
             
        

if(total == num):
    print('Perfect number = ',num)

if(total != num):
             
    print(num , 'is a not a perfect number')        

##print('total ',total)


    

            
