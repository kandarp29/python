l = input('Enter some text ')
count = 0
for c in l.split():
    if c == 'a' or c == 'an' or c == 'the':
        count = count + 1
        
    
print(count)


    

    
        
