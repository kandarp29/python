string = input('Enter the string')
letter = 'a'
while letter in string:

    letter = input('Enter the letter to be indexed ')
    if letter in string:

        print(string.index(letter))

    else:
        print(letter,'letter is not in string')
        break





