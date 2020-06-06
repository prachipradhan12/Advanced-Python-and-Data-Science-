import cx_Oracle
con=None
try:
	con=cx_Oracle.connect("system/abc123")
	print("Connected")
	sql="select * from student"
	cursor=con.cursor()
	cursor.execute(sql)
	data=cursor.fetchall()
	for d in data:
		print("Roll no=",d[0],"Name=",d[1])
	
except cx_Oracle.DatabaseError as e:
	print("issue",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("disconnected")