
def count_div(A,B,K):
    count = 0
    for i in range(A,B):
        if i % 5 == 0:
            print(i)
            count = count + 1
    print('Number of integers that are divisible by',K,'in range',A,'to',B,'is',count)

count_div(5,50,5)


   
            
