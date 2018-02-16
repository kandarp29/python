s1 = input('Enter a word with letter a = ')

s2 = input('Enter a word of same length a =')
string =''
if len(s1) == len(s2):
    for i in range(len(s1)):
        string = string+s2[i]+s1[i]
        
    

        
    
else:
    print('length of both words are not same')


print(string)
