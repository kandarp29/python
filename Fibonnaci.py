class Fibonacci:
    def __init__(self,start=0):
        self.start = start
    def fibo(self,n):
        first = 0
        second = 1
        if n==0:
            print(first)
        elif n==1:
            print(second)
        else:
            for i in range(n):
                if i==0 or i == 1:
                    print(i,end=' ')
                else:
                    result= first + second
                    first = second
                    second = result
                    print(result,end=' ')
                    
            
        
