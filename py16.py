import random
def pass_word():
    
    print("Generate password")

    aw=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    bw=random.choice('abcdefghijklmnopqrstuvwxyz')
    cw=random.randint(0,9)
    dw=random.choice('!@#$%&')
    dw = str(dw)
    cw=str(cw)
    print(aw+bw+cw+dw)









