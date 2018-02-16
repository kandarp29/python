from random import randint
print('Welcome to Guess Game')
player_amount = 100
while 0 < player_amount <= 200:
    coin = randint(0, 1)

    if coin == 1:
        coin_side = 'head'

    else:

        coin_side = 'tail'
    guess = input('Enter your guess')

    guess = guess.lower()

    if guess == coin_side:
        player_amount = player_amount + 9
        print(player_amount)
    else:
        player_amount = player_amount - 10
        print(player_amount)
else:
    if player_amount == 200:
        print('You won maximum prize')

    elif player_amount <= 0:
        print('You are out of money')



    

