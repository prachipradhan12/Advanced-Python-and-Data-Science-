'''
find area and circumference
'''

import math
radius=float(input("Enter radius "))
area=math.pi*math.pow(radius,2)
cir=2*math.pi*radius
print("Area=",round(area,2))
print("Circumference=",round(cir,2))