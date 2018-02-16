s = input('Enter the full name')

##a = s.index('')
string = ''
##a = s[0].upper()

for i in range(len(s)):
    
    if s[i] == ' ':
        z = s[i+1].upper()

        s = s.replace(s[i+1],z)

        

     
        



print(s)
        

        
        

