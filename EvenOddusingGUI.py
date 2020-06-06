from tkinter import *
from tkinter import messagebox

def f1():
	try:
		s=entno.get()
		num=int(s)
		msg=""
		if num%2==0:
			msg="Even"
		else:
			msg="Odd"
		message.showinfo("Javab")

root=Tk()
root.title("EVEN ODD CALC")
root.geometry("400x300+200+100")
lblno=Label(root,text="enter number ",font=("Comic Sans MS",30,"bold"))
lblno.pack(pady=10)
entno=Entry(root,bd=10,font=("Comic Sans MS",30,"bold"))
entno.pack(pady=20)

btnfind=Button(root,text="enter number ",font=("Comic Sans MS",30,"bold"),command=f1)
btnfind.pack(pack=10)

root.mainloop()