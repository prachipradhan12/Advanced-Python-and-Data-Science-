'''
waoopp for class circle:
	IV:radius
	Im:display() for showing length and width
	Im:area() for area of rect
	IM:circumference of rectangle
'''

class circle:
	def __init__(self,r):
		self.radius=r
		
	def show(self):
		print("Radius=",self.radius)
		
	def area(self):
		area=3.14*self.radius**2
		print("Area=",area)
	def cir(self):
		circumference=2*3.14*self.radius
		print("Circumference=",circumference)

radius=int(input("Enter the radius "))
c=circle(radius)
c.show()
c.area()
c.cir()