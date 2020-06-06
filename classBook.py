class book:
	def __init__(self,nop):
		self.nop=nop
	def __add__(self,other):
		res=self.nop+other.nop
		return book(res)
	def __str__(self):
		msg="nop "+str(self.nop)
		return msg

b1=book(100)
b2=book(200)
b3=book(500)

r1=b1+b2+b3
print(r1) 