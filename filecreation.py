'''
wapp to create a file if file does not exits filwname wud be suppied by the user
'''

import os.path
filename=input("Enter filename to create ")
if os.path.exists(filename):
	print(filename,"already exists")
else:
	f=None
	try:
		f=open(filename,"a")
		print(filename,"created")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()