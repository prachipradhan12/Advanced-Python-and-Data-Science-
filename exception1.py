#wapp to access command line arguement and receive two integers and perfrom ans n1/n2

import sys#can be anywhere by specify it before use

try:

	a=int(sys.argv[1])
	b=int(sys.argv[2])
	ans=a/b
except IndexError:
	print("Please enter the integers ")
except ValueError:
	print("Enter integers only ")
except ZeroDivisionError:
	print("Second number should not be 0")
except Exception as e:
	print("Some other issue ",e)

else:
	
	
	print("ans=",ans)