# Python program showing a use 
# of get() and set() method in 
# normal function 

class Geek: 
	def __init__(self, age = 0): 
		self._age = age 
	
	# getter method 
	def get_age(self): 
		return self._age 
	
	# setter method 
	def set_age(self, x): 
		self._age = x 

anchal = Geek() 

# setting the age using setter 
anchal.set_age(21) 

# retrieving age using getter 
print(anchal.get_age()) 

print(anchal._age) 
