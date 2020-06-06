import os.path
import pickle
class student:
	def __init__(self,rno,name):
		self.rno=rno
		self.name=name
	def show(self):
		print("RNO ",self.rno)
		print("NAME ",self.name)
list_of_students=[]
filename="student_ka_data.ser"
if os.path.isfile(filename):
	with open(filename,"rb") as f:
		list_of_students=pickle.load(f)
while True:
	op=int(input("1.add 2.view 3.delete 4.exit "))
	if op==1:
		rno=int(input("Enter the rno "))
		name=input("Enter name ")
		s=student(rno,name)
		list_of_students.append(s)
		print("Record saved")
	elif op==2:
		for d in list_of_students:
			d.show()
	elif op==3:
		ye=int(input("Enter the rno which uh want to delete "))
		for e in list_of_students:
			if ye==e.rno:
				list_of_students.remove(e)
				print(list_of_students[e],"deleted from the record")
			else:
				print("No such person")
	elif op==4:
		with open(filename,"wb") as f:
			pickle.dump(list_of_students,f)
		break
		
	else:
		print("Invalid Option ")


