def valid(x):
    l=[]
    lefty = '({['
    righty = ']})'

    for i in x:
        if i in lefty:
            l.append(i)
            
        elif i in righty:
            if len(l)==0:
                return True
            if righty.index(i)!=lefty.index(l.pop()):
                return False

            
    return True

