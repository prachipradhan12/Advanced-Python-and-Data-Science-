'''
wapp to read into file if file does not exits filename wud be suppied by the user
'''

import os.path
filename=input("Enter filename ")
if os.path.exists(filename):     #isfile() also checks
	with open(filename,"r") as f:
		print(f.read())
		print("DONE......")
	
else:
	print(filename,"not found")	