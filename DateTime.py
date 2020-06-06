'''
wapp to wish the user GM/GA/GE
along that show display the date and time
'''

import datetime

dt=datetime.datetime.now()
print(dt)
date=dt.date()
print("date=",date)
time=dt.time()
print("time=",time)
print(dt.hour)
s1=time.strftime('%I:%M:%S %p')
print(s1)
if(dt.hour>6 and dt.hour<12):
	print("Guten Morgen")
elif(dt.hour>=12 and dt.hour<=17):
	print("Guten tag")
else:
	print("Guten abend")