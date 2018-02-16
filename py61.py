from random import shuffle
sent = input('Enter the sentence')
sent = sent.lower()

l = sent.split()


shuffle(l)



a = ' '.join(l)

cap = a[0].upper()

print(cap+a[1:])




