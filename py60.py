from random import shuffle
sent = input('Enter the sentence')
l = sent.split()
shuffle(l)

print(' '.join(l))

