'''
wapp for POP threads
'''

import threading
import time
def writing():
	print("Writing started")
	for i in range(1,10):
		print("writing",i,"assignment")
		time.sleep(0.5)
	print("writing completed")

def music():
	print("Music started")
	for i in range(1,20):
		print("listen",i,"song")
		time.sleep(0.5)
	print("music over")
print("aaj ka kaam shuru")
w=threading.Thread(target=writing)
m=threading.Thread(target=music)
w.start()
m.start()
w.join()
m.join()
print("aaj ka kaam khaaataam")