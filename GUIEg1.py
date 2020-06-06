from tkinter import *
from datetime import *
from tkinter import messagebox
from webbrowser import *

root=Tk()
root.title("Da and Ti App")
root.geometry("400x300+300+100")
root.configure(background='light blue')

def f1():
	date=datetime.now().date()
	messagebox.showinfo("Date ",date)

def f2():
	time=datetime.now().time()
	messagebox.showwarning("Time ",time)

def f3():
	dt=datetime.now()
	messagebox.showerror("DateTime ",dt)

def f4():
	open("www.google.com")
btndate=Button(root,text="DATE",width=10,font=("arial",18,"bold"),command=f1)

btntime=Button(root,text="TIME",width=10,font=("arial",18,"bold"),command=f2)

btndt=Button(root,text="DA & TI",width=10,font=("arial",18,"bold"),command=f3)
btnvisit=Button(root,text="VISIT US",width=10,font=("arial",18,"bold"),command=f4)

btndate.pack(pady=10)
btntime.pack(pady=10)
btndt.pack(pady=10)
btnvisit.pack(pady=10)

root.mainloop()