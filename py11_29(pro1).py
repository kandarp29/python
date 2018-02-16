def solution(N,A):
    counter = [0 for i in range(0,N)]
    
    for k in range(len(A)):
        val = A[k]

        if val > len(counter):
            maxi = max(counter)
            for f in range(len(counter)):
                counter[f] = max(counter)
        else:
            
            counter[val] =counter[val] + 1
    print(counter)
