import socket
try:
	socket.create_connection(("www.google.com",80))
	print("u r connected")
except OSError as e:
	print("check network",e)