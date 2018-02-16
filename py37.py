s = input('What is the user name: ')

for i in range(len(s)):
    if s[i] == ' ':
        First_name = s[:i]

print('Dear' +' ' +s)
print('\n\n')
print('I am pleased to offer you our new Platinum Plus Rewards card at a special introductory APR of 47.99%.'+ First_name+', '+ 'an offer like this does not come along every day, so I urge you to call now toll-free at 1-800-314-1592. We cannot offer such a low rate for long, '+ First_name+', so call right away.')



