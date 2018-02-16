##Program to enter the right password

password_try = 0
passcode = 2358

while password_try < 5:
    password_try = password_try + 1
    guess = eval(input('Enter the 4 digit password you have 5 try'))
    if guess == passcode:
        print('You logged in to the system')
        break

    else:
        print('You entered a wrong password,you used',password_try,'guesses')

else:

    print('You are kicked out of the system')

