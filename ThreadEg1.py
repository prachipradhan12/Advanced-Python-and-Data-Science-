'''
wapp for OOP threads
'''

import threading
import time
class Writing(threading.Thread):
	def run(self):
		print("Writing started")
		for i in range(1,10):
			print("writing",i,"assignment")
			time.sleep(0.5)
		print("writing completed")

class Music(threading.Thread):
	def run(self):
		print("Music started")
		for i in range(1,20):
			print("listen",i,"song")
			time.sleep(0.5)
		print("music over")
print("aaj ka kaam shuru")
w=Writing()
m=Music()
w.start()
m.start()
w.join()
m.join()
print("aaj ka kaam khaaataam")