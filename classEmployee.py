'''
wamdoopp for class employee:
	IV:eid,ename,esalary
	PI:for eid,ename,esalary
	IM:show() calc_bonus
	SV:ecount
	SM:show_ecount()

'''

class employee:
	ecount=0
	def __init__(self,eid,ename,esalary):
		self.eid=eid
		self.ename=ename
		self.esalary=esalary
		employee.ecount=employee.ecount+1
	def show(self):
		print("EID ",self.eid)
		print("ENAME ",self.ename)
		print("ESALARY ",self.esalary)
	def calc_bonus(self):
		ans=self.esalary*0.10
		print("bonus amt= ",round(ans,2))
	@staticmethod
	def show_ecount():
		print("Employee count ",employee.ecount)

list_of_emp=[]
while True:
	op=int(input("1.add 2.view 3.delete 4.exit "))
	if op==1:
		eid=int(input("Enter emp id "))
		ename=input("Enter emp name ")
		esalary=float(input("Enter emp salary "))
		e=employee(eid,ename,esalary)
		list_of_emp.append(e)
	elif op==2:
		employee.show_ecount()
		for e in list_of_emp:
			print("*"*40)
			e.show()
	elif op==3:
		id=int(input("Enter the id of employee to delete record "))
		for e in list_of_emp:
			if id==e.eid:
				list_of_emp.remove(e)
				employee.ecount=employee.ecount-1
			else:
				print("No such employee")					
	elif op==4:
		break
	else:
		print("Invalid Option ")
























		