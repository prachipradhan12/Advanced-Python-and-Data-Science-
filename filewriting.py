'''
wapp to write into file if file does not exits filename wud be suppied by the user
'''

import os.path
filename=input("Enter filename ")
if os.path.exists(filename):     #isfile() also checks
	print(filename," exists")
	f=None
	try:	
		f=open(filename,"a")
		data=input("Enter data to write ")
		f.write(data+"\n")
		print("DONE......")
	except Exception as e:
		print("Issue",e)
	finally:
		if f is not None:
			f.close()

else:
	print(filename,"not found")	