integer = (input('Enter a large integer = '))

print(integer.count(''))
##string = ''
integer = integer[: :-1]
for i in range(len(integer)):

    if i%3 == 0:
        a = integer.index(i)
        integer = integer.replace(a+1,',')
        
        ##string = integer[:-i] + ',' + integer[-i:]
        ###string = string + string[i:-i] + ','
        
    
##print(string)

               
##for i in range(len(integer)):

##for c in integer:
    ##print(c)
    
    
