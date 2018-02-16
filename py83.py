f = []
a = 1
b = 0

for i in range(10):
    f.append(a)
    for j in range(i):
        f.append(b)
        
    
print(f)
