import sys
 
import datetime
 
for line in sys.movie:
 
    line = line.strip()
 
    actor,movie,year = line.split('\t')
 
    actor_up = actor.upper()
 
print '\t'.join([str(actor_up),movie,year])
