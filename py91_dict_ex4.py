user_pass = {'abc':123,'cde':423,'drf':621}
print(user_pass)

user= input('Enter the user name')

for i in user_pass:

    if user == i:

        passw = eval(input('Enter the password'))
        
        if user_pass[user]== passw:
            print('Congo! You are successfully logged in')
        
        else:
            print('Wrong password')
            print('You are not a authorized user')


if user not in user_pass:
    print('You are not authorized user')
    
