hour = eval(input('Enter hours= '))

zone = eval(input('am(1) or pm(2)? '))

time = eval(input('How many hours '))

new_hour = (hour + time)%12
if zone == 1:
    print('New hour:',new_hour,end = '  ')
    print('am')

else:
    print('New hour:',new_hour,end = '  ')
    print('pm')

            
