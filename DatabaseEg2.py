import cx_Oracle
con=None
try:
	con=cx_Oracle.connect("system/abc123")
	print("Connected")
	rno=int(input("Enter Roll no "))
	name=input("Enter name ")
	args=(rno,name)
	cursor=con.cursor()
	sql="insert into student values('%d','%s')"
	cursor.execute(sql % args)
	con.commit()
except cx_Oracle.DatabaseError as e:
	print("issue",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("disconnected")