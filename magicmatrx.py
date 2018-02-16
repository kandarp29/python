print('Pass only 4*4 matrix')
##M=[[1,15,14,4],[12,6,7,9],[8,10,11,5],[13,3,2,16]]

def Magicsquare(M):
    if sum(M[0])==sum(M[1])==sum(M[2])==sum(M[3]):
        a = sum(M[0])

        if M[0][0]+M[1][1]+M[2][2]+M[3][3] == a:
            if M[0][3]+M[1][2]+M[2][1]+M[3][0] == a:
                
                for i in range(4):
                    down = 0
                    count = 0
                    
                    for j in range(4):
                        
                        count+=M[j][i]
                        
                    if count == a:
                        down +=1
                        if down==4:
                            print('It is a magix matrix')

                    else:
                        print('Not a magic square')
                        break
            else:
                print('Not a magic square')
        else:
            print('Not a magic square')
    else:
        print('Not a magic square matrix')


##M=[[1,15,14,4],[12,6,7,9],[8,10,11,5],[13,3,2,16]]

##Magicsquare(M)
        
       
                    
                
                
                
            
                
        
