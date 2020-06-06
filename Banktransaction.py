from abc import *
class Rbi(ABC):
	def __init__(self,ano,balance):
		self.ano=ano
		self.balance=balance
	@abstractmethod
	def deposit(self,amt):		
		pass
	def withdraw(self,amt):
		pass
	def showbal(self):
		print("Remaining balance=",self.balance)
class Nayabank(Rbi):
	def deposit(self,amt):
		self.balance=self.balance+amt-10
	def withdraw(self,amt):
		if amt>self.balance:
			print("Insufficient balance ")
		else:		
			self.balance=self.balance-amt-20
			
n=Nayabank(10,1000)
while True:
	op=int(input("1.View balance 2.Withdraw Amount 3.Deposit Amount 4.Exit "))
	if op==1:
		n.showbal()
	elif op==2:
		amt=int(input("Enter the amount you want to withdraw "))
		n.withdraw(amt)
		n.showbal()		
	elif op==3:
		amt=int(input("Enter the amount you want to deposit "))
		n.deposit(amt)
		n.showbal()
	elif op==4:
		break
	else:
		print("Invalid Option")		









