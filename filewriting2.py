'''
wapp to write into file if file does not exits filename wud be suppied by the user
'''

import os.path
filename=input("Enter filename ")
if os.path.exists(filename):     #isfile() also checks
	with open(filename,"a") as f:
		data=input("Enter data to write ")
		f.write(data+"\n")
		print("DONE......")
	
else:
	print(filename,"not found")	