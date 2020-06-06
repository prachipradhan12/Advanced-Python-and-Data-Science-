'''
wapp for following :=class emp with IV(eid,ename,epds)
		     class attendence with IV(nodp)
			E=emp(1,'prachi',10000)
			a=attendence(25)        ==>sal=e*a
'''
'''unsupported operand type(s) for * between emp and attendence which means perform overriding in emp class'''

class emp:
	def __init__(self,eid,ename,epds):
		self.eid=eid
		self.ename=ename
		self.epds=epds

	def __mul__(self,other):    
		sal=self.epds*other.nodp
		return sal
class attendence:
	def __init__(self,nodp):
		self.nodp=nodp
e=emp(1,'Prachi',10000)
a=attendence(25)

sal=e*a
print("Salary=",sal)