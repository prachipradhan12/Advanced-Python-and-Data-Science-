'''
wapp to class mech with IV price
	class Bee with IV amount
m=mech(750)	r1=m+b
b=Bee(650)	r2=b-m
		r3=m*b
'''

class Mech:
	def __init__(self,price):
		self.price=price

	def __add__(self,other):
		res=self.price+other.amount
		return res

	def __mul__(self,other):
		res=self.price*other.amount
		return res

class Bee:	
	def __init__(self,amount):
		self.amount=amount

	def __sub__(self,other):
		res=self.amount-other.price
		return res


m=Mech(750)
b=Bee(350)

r1=m+b
print(r1)
r2=b-m
print(r2)
r3=m*b
print(r3)

