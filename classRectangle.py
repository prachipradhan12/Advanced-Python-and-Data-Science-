'''
waoopp for class rectangle:
	IV:length and width
	Im:show() for showing length and width
	Im:area() for area of rect
	IM:perimeter of rectangle
'''

class rectangle:
	def __init__(self,l,w):
		self.length=l
		self.width=w
	def show(self):
		print("Length=",self.length)
		print("Width=",self.width)
	def area(self):
		area=self.length*self.width
		print("Area=",area)
	def peri(self):
		perimeter=2*self.length*self.width
		print("Perimeter=",perimeter)

length=int(input("Enter the length "))
width=int(input("Enter the width "))
r=rectangle(length,width)
r.show()
r.area()
r.peri()