#using semaphore

import threading
import time

balance=500
s=threading.Semaphore()
def deposit():
	global balance
	s.acquire()
	print("deposit started")
	amt1=balance
	amt1=amt1+100
	time.sleep(2)
	balance=amt1
	s.release()
	print("dep process started")

def withdraw():
	global balance
	
	s.acquire()
	print("withdraw started")
	amt2=balance
	amt2=amt2-100
	time.sleep(2)
	balance=amt2
	
	s.release()
	print("withdraw process started")
print("Initial balance",balance)
d=threading.Thread(target=deposit)
w=threading.Thread(target=withdraw)
d.start()
w.start()
d.join()
w.join()
print("Final balance",balance)