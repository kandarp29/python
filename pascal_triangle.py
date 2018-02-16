def pascal(x):
    l = []


    for line in range(1,x-1):

        for i in range(1,line):

            if (line == i or i == 0):

                l[line][i] = 1
            else:
                l[line][i] = l[line-1][i-1] + l[line-1][i]

                print(l[line][i])



            
pascal(4)
