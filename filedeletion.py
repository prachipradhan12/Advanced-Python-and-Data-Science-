'''
wapp to delete a file if file does not exists filename wud be suppied by the user
'''

import os.path
filename=input("Enter filename to delete ")
if os.path.exists(filename):
	print(filename,"exists")
	os.remove(filename)
	print(filename,"Deleted")
else:
	print(filename,"not found")
	