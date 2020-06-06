class student:
	def __init__(self,r,n,m):
		self.rno=r
		self.name=n
		self.marks=m
	def show(self):
		print("Roll no=",self.rno)
		print("Name=",self.name)
		print("Marks=",self.marks)
try:
	rno=int(input("Enter roll no "))
	if rno<1:
		raise Exception("Rno shud be more then or equal to 1") #throws the exception
	name=input("Enter name ")
	if len(name)<2:
		raise Exception("name shud be more than two chars ")
	marks=int(input("Enter marks "))
	if marks <0 or marks >100:
		raise Exception("Marks shud be between 0 to 100")
	
except Exception as e:				#catch the exception
	print("bad input",e)
else:
	s=student(rno,name,marks)
	s.show()