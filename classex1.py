#!/usr/bin/python

class Investment:
    
    def __init__(self, p, i):
      self.p = p
      self.i = i
      
    def __str__(self):

        return('Principal- '+ str(self.p)+ '  Interest rate - '+str(self.i)+'%')
        
    def value_after(self, n):
        
        
        value=(self.p * ((1 + self.i) ** n))
        return(value)
        
        
e = Investment(1000,5.63)
print(e)
print(e.value_after(2))
