l=['3 idiots','secret superstar','Tiger Zinda Hai']
def guess_game(i):
    guess = input('Guess the name:')
    

    if guess == i:
        return 'Your guess is correct'

        
    elif guess != i:
        print('Your guess is incorrect')
            
        guess_game(i)
        
print("Guess the name of movie")

for i in l:
    
    ##for j in range(len(i)):
    if len(i)<9:
            
        a = i[:1]+'_'+i[2:3]+'_'+i[4:6]+'_'+i[7:len(i)]
        print(a)
    else:
        
        a = (i[:1]+'_'+i[2:3]+'_'+i[4:6]+'_'+i[7:9]+'_'+i[11:13]+'_'+i[15:len(i)])
        print(a)
    
    
    guess_game(i)
    

    
        
