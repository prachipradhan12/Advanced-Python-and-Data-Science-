class pcm:
	def __init__(self,phy,chem,math):
		self.phy=phy
		self.chem=chem
		self.math=math
	def show(self):
		print("Phy=",self.phy)
		print("Chem=",self.chem)
		print("Math=",self.math)
class nonpcm:
	def __init__(self,eng,bio):
		self.eng=eng
		self.bio=bio
	def show(self):
		print("Eng=",self.eng)
		print("Bio=",self.bio)
class marks(pcm,nonpcm):
	def __init__(self,phy,chem,math,eng,bio):
		pcm.__init__(self,phy,chem,math)
		nonpcm.__init__(self,eng,bio)
	def show(self):
		pcm.show(self)
		nonpcm.show(self)

m=marks(99,55,85,85,85)
m.show()