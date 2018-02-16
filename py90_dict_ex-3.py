days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
month = input('Enter the month name')

b = list(days.keys())
##Modify the program from part (a) and the dictionary so that the user does not have to know how to spell the month name exactly. That is, all they have to do is spell the ﬁrst three letters of the month name correctly
for j in b:
    if month == j[:3]:
        

        print('Number of days in',j,'is',days[j])

a = []
a =list(days.keys())
a.sort()
for i in a:
    print(i)
    if days[i] == 31:
        print(i,'has a 31 days')



a = list(days.items())
a.sort()
print(a)

