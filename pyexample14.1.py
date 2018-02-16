class Investment:
	def _int_(self,principal,interest,n):
		self.principal = principal
		self.interest = interest
		self.n = n
	def value_after(self):
		self.value = self.principle((1 + self.interest) ** self.n)
		return self.value


p = Investment(2000,5,2)


print(p.Investment.value_after())
	    
