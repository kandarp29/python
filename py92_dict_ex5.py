stats = {}
won_list=[]
for i in range(5):
    l = []
    team = input('Enter the team name')
    won = eval(input('How many games won?'))
    l.append(won)
    ##won_list.append(won)
    loss = eval(input('How many games lost?'))
    l.append(loss)

    stats[team] = l


que = input('Enter the team name to get winning percentage')        
val = stats[que]

perc = (val[0] * 100)/(val[0]+ val[1])



print('Winning percentage of ',que,'is',perc)

dass = list(stats.values())

for j in range(5):
    won_list.append(dass[j][0])


print(won_list)

